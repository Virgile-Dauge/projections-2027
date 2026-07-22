# Publier une nouvelle version des tuiles

Le `france.pmtiles` (338 Mo) est hébergé sur Cloudflare R2 (bucket
`projections-2027-tiles`, URL publique r2.dev — voir `site/config.js`).
Ni `wrangler r2 object put` ni le dashboard n'acceptent un fichier > ~300 Mo :
on passe par l'API Workers (binding R2, limite ~5 Gio) via un worker local
jetable + un upload multipart résumable (parts de 32 Mio, 5 essais).

## Publier

```bash
uv run build-tiles                       # reconstruit data/tiles/france.pmtiles (gate vert requis)
cd outils/publier-tuiles
npx wrangler dev --port 8790 --no-bundle # binding distant vers le bucket (auth : wrangler login)
# dans un autre terminal :
python publier.py ../../data/tiles/france.pmtiles
```

`--no-bundle` est requis (aucun import dans le worker, et esbuild s'étouffe
sur un `~/package.json` parasite). L'URL publique ne change pas d'une
publication à l'autre : `site/config.js` n'est à toucher que si le bucket change.

## Refaire la config du bucket (une fois, déjà faite)

```bash
npx wrangler r2 bucket create projections-2027-tiles
npx wrangler r2 bucket cors set projections-2027-tiles --file cors.json -y
npx wrangler r2 bucket dev-url enable projections-2027-tiles -y
```

Pourquoi R2 : un PMTiles se consomme en range requests cross-origin — il faut
CORS + Range. Les assets de Release GitHub renvoient un 302 sans
`Access-Control-Allow-Origin` : carte silencieusement vide.
