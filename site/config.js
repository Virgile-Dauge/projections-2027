// URL du fichier PMTiles France entière (4 couches : bureaux + communes
// résultats 2024, mobilisation_bureaux + mobilisation_communes).
//
// Hébergé sur Cloudflare R2 (bucket `projections-2027-tiles`, URL publique
// r2.dev) : un PMTiles se consomme en range requests cross-origin, il faut un
// hôte qui parle CORS + Range — les assets de Release GitHub ne le font PAS
// (302 sans Access-Control-Allow-Origin, carte silencieusement vide).
// Publication d'une nouvelle version : voir outils/publier-tuiles/.
// ponytail: URL r2.dev rate-limitée (non-production) — passer sur un domaine
// custom Cloudflare si le trafic le justifie.
const PMTILES_URL =
  "https://pub-3b5e818f176f45a3a7e52042b7629ee3.r2.dev/france.pmtiles";
// Développement local : commenter la constante ci-dessus et utiliser
// const PMTILES_URL = "./tiles/france.pmtiles";
