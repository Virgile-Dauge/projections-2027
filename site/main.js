// Carte descriptive 2024 par bloc, bureau de vote — MapLibre GL JS + PMTiles.
//
// Une seule source vectorielle (le PMTiles France entière, deux couches :
// `bureaux` haute zoom, `communes` basse zoom pour le dézoom — voir
// projections.build_tiles). Pas de fond de carte externe : la choroplèthe EST
// la carte, les contours communaux servent de repère en filigrane à tout zoom.

// Couleurs de blocs — convention du projet (docs/heritage-2024.md). Garder en
// synchro avec BLOC_SLUG de src/projections/carte.py.
const COULEURS_BLOC = {
  Gauche: "#e60000",
  Centre: "#ffcc00",
  Droite: "#542788",
  "Extrême droite": "#996633",
  Divers: "#bababa",
};

const BLOCS_AFFICHAGE = [
  { slug: "gauche", label: "Gauche" },
  { slug: "centre", label: "Centre" },
  { slug: "droite", label: "Droite" },
  { slug: "extreme_droite", label: "Extrême droite" },
  { slug: "divers", label: "Divers" },
];

// Zoom de bascule bureaux <-> communes : doit rester cohérent avec
// BUREAUX_MINZOOM / COMMUNES_MAXZOOM de src/projections/build_tiles.py.
const ZOOM_BASCULE = 9;

const protocole = new pmtiles.Protocol();
maplibregl.addProtocol("pmtiles", protocole.tile);

function expressionCouleurBloc() {
  return [
    "match",
    ["get", "bloc_tete"],
    "Gauche",
    COULEURS_BLOC.Gauche,
    "Centre",
    COULEURS_BLOC.Centre,
    "Droite",
    COULEURS_BLOC.Droite,
    "Extrême droite",
    COULEURS_BLOC["Extrême droite"],
    "Divers",
    COULEURS_BLOC.Divers,
    COULEURS_BLOC.Divers, // repli si bloc_tete absent/inconnu
  ];
}

const style = {
  version: 8,
  sources: {
    france: {
      type: "vector",
      url: "pmtiles://" + PMTILES_URL,
    },
  },
  layers: [
    {
      id: "fond",
      type: "background",
      paint: { "background-color": "#eef0ef" },
    },
    {
      id: "communes-fill",
      type: "fill",
      source: "france",
      "source-layer": "communes",
      maxzoom: ZOOM_BASCULE,
      paint: {
        "fill-color": expressionCouleurBloc(),
        "fill-opacity": 0.85,
      },
    },
    {
      // Filigrane des limites communales, repère géographique sans fond de
      // carte externe. La géométrie communes n'existe dans les tuiles que
      // jusqu'à ZOOM_BASCULE (voir COMMUNES_MAXZOOM côté build_tiles.py) :
      // au-delà, bureaux-ligne prend le relais comme repère visuel.
      id: "communes-ligne",
      type: "line",
      source: "france",
      "source-layer": "communes",
      maxzoom: ZOOM_BASCULE,
      paint: {
        "line-color": "#8a8a8a",
        "line-width": 0.5,
        "line-opacity": 0.4,
      },
    },
    {
      id: "bureaux-fill",
      type: "fill",
      source: "france",
      "source-layer": "bureaux",
      minzoom: ZOOM_BASCULE,
      paint: {
        "fill-color": expressionCouleurBloc(),
        "fill-opacity": 0.85,
      },
    },
    {
      id: "bureaux-ligne",
      type: "line",
      source: "france",
      "source-layer": "bureaux",
      minzoom: ZOOM_BASCULE,
      paint: {
        "line-color": "#ffffff",
        "line-width": 0.3,
        "line-opacity": 0.5,
      },
    },
  ],
};

const map = new maplibregl.Map({
  container: "carte",
  style,
  center: [2.5, 46.6], // France métropolitaine ; les DROM restent accessibles en dézoomant/déplaçant la vue.
  zoom: 5,
  minZoom: 2,
  maxZoom: 16,
});

map.addControl(new maplibregl.NavigationControl({ showCompass: false }), "top-right");

const panneau = document.getElementById("panneau");

function formatPct(valeur) {
  return Number(valeur).toLocaleString("fr-FR", { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + " %";
}

function afficherPanneau(proprietes, estCommune) {
  const titre = estCommune
    ? proprietes.commune || proprietes.code_commune
    : `${proprietes.commune || ""} — bureau ${proprietes.bureau || ""}`;
  const lignes = BLOCS_AFFICHAGE.map(
    (bloc) => `
      <tr>
        <td><span class="pastille" style="background:${COULEURS_BLOC[bloc.label]}"></span>${bloc.label}</td>
        <td>${formatPct(proprietes["pct_" + bloc.slug])}</td>
      </tr>`
  ).join("");

  panneau.innerHTML = `
    <button id="fermer-panneau" aria-label="Fermer le panneau">×</button>
    <h2>${titre}</h2>
    <p class="tete">Bloc en tête : <strong>${proprietes.bloc_tete}</strong></p>
    <table>${lignes}</table>
    <p class="participation">Participation : ${formatPct(proprietes.participation)}</p>
  `;
  panneau.hidden = false;
  document.getElementById("fermer-panneau").addEventListener("click", () => {
    panneau.hidden = true;
  });
}

map.on("load", () => {
  ["communes-fill", "bureaux-fill"].forEach((id) => {
    map.on("mouseenter", id, () => {
      map.getCanvas().style.cursor = "pointer";
    });
    map.on("mouseleave", id, () => {
      map.getCanvas().style.cursor = "";
    });
  });

  map.on("click", "communes-fill", (e) => {
    if (e.features.length) afficherPanneau(e.features[0].properties, true);
  });
  map.on("click", "bureaux-fill", (e) => {
    if (e.features.length) afficherPanneau(e.features[0].properties, false);
  });
});
