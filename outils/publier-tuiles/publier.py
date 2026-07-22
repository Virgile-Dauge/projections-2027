"""Upload multipart du PMTiles via le worker local (binding R2 distant).

Parts de 32 Mio, 5 tentatives par part — résiste aux coupures du tunnel.
"""

import http.client
import json
import sys
import time
from pathlib import Path

TAILLE_PART = 32 * 1024 * 1024
ESSAIS = 5

fichier = Path(sys.argv[1])
taille = fichier.stat().st_size
n_parts = (taille + TAILLE_PART - 1) // TAILLE_PART
print(f"upload {fichier.name} : {taille} octets en {n_parts} parts de ≤{TAILLE_PART} o", flush=True)


def requete(methode, chemin, corps=None, entetes=None):
    conn = http.client.HTTPConnection("localhost", 8790, timeout=600)
    try:
        conn.request(methode, chemin, body=corps, headers=entetes or {})
        rep = conn.getresponse()
        donnees = rep.read().decode("utf-8", errors="replace")
        if rep.status != 200:
            raise RuntimeError(f"HTTP {rep.status}: {donnees[:200]}")
        return json.loads(donnees)
    finally:
        conn.close()


upload_id = requete("POST", "/create")["uploadId"]
print(f"uploadId = {upload_id[:20]}…", flush=True)

parts = []
with fichier.open("rb") as f:
    for n in range(1, n_parts + 1):
        bloc = f.read(TAILLE_PART)
        for essai in range(1, ESSAIS + 1):
            try:
                debut = time.time()
                part = requete(
                    "PUT",
                    f"/part?uploadId={upload_id}&n={n}",
                    corps=bloc,
                    entetes={"Content-Length": str(len(bloc))},
                )
                parts.append(part)
                print(f"part {n}/{n_parts} ok ({len(bloc)} o, {time.time() - debut:.0f}s)", flush=True)
                break
            except Exception as exc:  # retry: le tunnel du binding distant est fragile
                print(f"part {n} essai {essai}/{ESSAIS} échoué : {exc}", flush=True)
                if essai == ESSAIS:
                    sys.exit(1)
                time.sleep(3 * essai)

resultat = requete("POST", "/complete", corps=json.dumps({"uploadId": upload_id, "parts": parts}))
print(f"terminé : {resultat}")
