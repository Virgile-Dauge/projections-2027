// URL du fichier PMTiles France entière (bureaux + communes, résultats 2024).
//
// Placeholder pour le développement local : sert `site/` avec
// `python -m http.server` depuis ce dossier, avec `data/tiles/france.pmtiles`
// copié ou symlinké vers `site/tiles/france.pmtiles`.
//
// L'orchestrateur remplace cette constante par l'URL définitive une fois le
// PMTiles hébergé (voir README, section "Site carto" : si le fichier dépasse
// 100 Mo, il est servi en asset de Release GitHub plutôt que commité dans
// site/tiles/ — l'URL pointe alors vers cette release).
const PMTILES_URL =
  "https://github.com/Virgile-Dauge/projections-2027/releases/download/tuiles-2024-legi-t1/france.pmtiles";
// Développement local : commenter la constante ci-dessus et utiliser
// const PMTILES_URL = "./tiles/france.pmtiles";
