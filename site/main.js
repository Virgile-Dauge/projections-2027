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

// Couches mobilisation (issue #26, ADR 0002/0003) : réserve de voix par bloc
// (#25) + rapport de force projeté (#5), jointes par IDENTIFIANTS aux mêmes
// contours que ci-dessus (voir projections.build_tiles.joindre_mobilisation_*).
// Nombre de tranches (quantiles larges) : doit rester cohérent avec les
// défauts de projections.mobilisation (n_quantiles_reserve=5, n_quantiles_force=4).
const N_QUANTILES_RESERVE = 5;
const N_QUANTILES_FORCE = 4;

const protocole = new pmtiles.Protocol();
maplibregl.addProtocol("pmtiles", protocole.tile);

function expressionOpaciteQuantile(colonneQuantile, nMax) {
  // Tranche ordinale 1..nMax -> intensité visuelle croissante. AUCUN pourcentage
  // à intervalle de confiance affiché (ADR 0001) : l'opacité code un RANG de
  // tranche, jamais une valeur continue. Une unité sans estimation pour ce bloc
  // (quantile null) reste visible, quasi transparente -- jamais masquée à 0.
  const opaciteMin = 0.15;
  const opaciteMax = 0.9;
  return [
    "case",
    ["==", ["get", colonneQuantile], null],
    0.05,
    [
      "+",
      opaciteMin,
      ["*", (opaciteMax - opaciteMin) / (nMax - 1), ["-", ["to-number", ["get", colonneQuantile]], 1]],
    ],
  ];
}

function expressionCouleurRapportForce() {
  // Même convention de couleurs que expressionCouleurBloc, lue sur la propriété
  // `rapport_force_bloc_tete` (préfixée pour ne pas se confondre avec `bloc_tete`,
  // la couche descriptive résultats 2024 réels -- voir build_tiles.py).
  return [
    "match",
    ["get", "rapport_force_bloc_tete"],
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
    COULEURS_BLOC.Divers,
  ];
}

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

    // --- Couches mobilisation (issue #26) -- masquées par défaut, bandeau
    // "Résultats 2024" étant la couche active au chargement. Le sélecteur de
    // couche (index.html) bascule leur visibilité. Réserve : bloc Gauche
    // uniquement (décision mainteneur, PR #33) -- pas de sélecteur de bloc.

    {
      id: "mob-reserve-communes-fill",
      type: "fill",
      source: "france",
      "source-layer": "communes",
      layout: { visibility: "none" },
      paint: {
        "fill-color": COULEURS_BLOC.Gauche,
        "fill-opacity": expressionOpaciteQuantile("quantile_reserve_gauche", N_QUANTILES_RESERVE),
      },
    },
    {
      id: "mob-reserve-bureaux-fill",
      type: "fill",
      source: "france",
      "source-layer": "bureaux",
      minzoom: ZOOM_BASCULE,
      layout: { visibility: "none" },
      paint: {
        "fill-color": COULEURS_BLOC.Gauche,
        "fill-opacity": expressionOpaciteQuantile("quantile_reserve_gauche", N_QUANTILES_RESERVE),
      },
    },
    {
      id: "mob-force-communes-fill",
      type: "fill",
      source: "france",
      "source-layer": "communes",
      layout: { visibility: "none" },
      paint: {
        "fill-color": expressionCouleurRapportForce(),
        "fill-opacity": expressionOpaciteQuantile("quantile_rapport_force", N_QUANTILES_FORCE),
      },
    },
    {
      id: "mob-force-bureaux-fill",
      type: "fill",
      source: "france",
      "source-layer": "bureaux",
      minzoom: ZOOM_BASCULE,
      layout: { visibility: "none" },
      paint: {
        "fill-color": expressionCouleurRapportForce(),
        "fill-opacity": expressionOpaciteQuantile("quantile_rapport_force", N_QUANTILES_FORCE),
      },
    },
    {
      // Communes en repli : dégradation TOUJOURS visible (jamais silencieuse,
      // CONTEXT.md « Repli »), à tout zoom où une couche mobilisation est active
      // -- y compris au zoom bureau, là où la couche bureaux n'a aucune
      // donnée fiable pour elles (maxzoom par feature, cf. joindre_communes).
      id: "mob-repli-ligne",
      type: "line",
      source: "france",
      "source-layer": "communes",
      filter: ["==", ["get", "degrade"], true],
      layout: { visibility: "none" },
      paint: {
        "line-color": "#222222",
        "line-width": 1.5,
        "line-dasharray": [2, 2],
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

function formatNombre(valeur) {
  return valeur === null || valeur === undefined ? "n/d" : Math.round(Number(valeur)).toLocaleString("fr-FR");
}

function libelleQuantile(quantile, nMax) {
  return quantile === null || quantile === undefined ? "n/d" : `tranche ${quantile}/${nMax}`;
}

function libelleStatut(proprietes) {
  // Dégradation jamais silencieuse (CONTEXT.md « Repli ») : le statut de
  // réconciliation est toujours affiché, jamais seulement encodé visuellement.
  // `degrade` n'existe QUE sur les features de la couche communes (jamais
  // sur la couche bureaux, où la maille est toujours "bureau") : `true` ->
  // repli, `false` -> agrégat de dézoom d'une commune stable, absent -> bureau.
  if (proprietes.degrade === true) {
    return "⚠ commune en repli — statut agrégé, pas de détail fiable par bureau (voir la méthode)";
  }
  if (proprietes.degrade === false) {
    return "vue agrégée (dézoom) — somme des bureaux de la commune, jamais une moyenne";
  }
  return `statut : ${proprietes.statut || "n/d"}`;
}

function fermerBouton() {
  return `<button id="fermer-panneau" aria-label="Fermer le panneau">×</button>`;
}

function ouvrirPanneau(html) {
  panneau.innerHTML = html;
  panneau.hidden = false;
  document.getElementById("fermer-panneau").addEventListener("click", () => {
    panneau.hidden = true;
  });
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

  ouvrirPanneau(`
    ${fermerBouton()}
    <h2>${titre}</h2>
    <p class="tete">Bloc en tête : <strong>${proprietes.bloc_tete}</strong></p>
    <table>${lignes}</table>
    <p class="participation">Participation : ${formatPct(proprietes.participation)}</p>
  `);
}

function afficherPanneauReserve(proprietes, estCommune) {
  // Décision mainteneur (PR #33) : seule la réserve du bloc Gauche est
  // affichée (et embarquée dans les tuiles) — les autres blocs restent
  // publiés dans reserve-2027.md, lié depuis la page méthode.
  const titre = estCommune
    ? proprietes.commune || proprietes.code_commune
    : `${proprietes.commune || ""} — bureau ${proprietes.bureau || ""}`;

  ouvrirPanneau(`
    ${fermerBouton()}
    <h2>${titre}</h2>
    <p class="tete">Réserve de voix — <a href="methode.html">estimateur v1</a></p>
    <p>
      <span class="pastille" style="background:${COULEURS_BLOC.Gauche}"></span>Gauche :
      <strong>${formatNombre(proprietes.reserve_gauche)}</strong> inscrits mobilisables
      (${libelleQuantile(proprietes.quantile_reserve_gauche, N_QUANTILES_RESERVE)})
    </p>
    <p class="participation">${libelleStatut(proprietes)}</p>
  `);
}

function afficherPanneauForce(proprietes, estCommune) {
  const titre = estCommune
    ? proprietes.commune || proprietes.code_commune
    : `${proprietes.commune || ""} — bureau ${proprietes.bureau || ""}`;
  const bloc = proprietes.rapport_force_bloc_tete;

  ouvrirPanneau(`
    ${fermerBouton()}
    <h2>${titre}</h2>
    <p class="tete">
      Bloc en tête (projeté) : <span class="pastille" style="background:${COULEURS_BLOC[bloc] || COULEURS_BLOC.Divers}"></span>
      <strong>${bloc || "n/d"}</strong>
    </p>
    <p>Intensité : ${libelleQuantile(proprietes.quantile_rapport_force, N_QUANTILES_FORCE)} (quantile large — l'ordre fin n'est pas fiable, <a href="methode.html">voir la méthode</a>)</p>
    <p class="participation">${libelleStatut(proprietes)}</p>
  `);
}

// Couches par mode -- une seule visible à la fois (le sélecteur de couche
// bascule leur `visibility`), plus la ligne de repli active pour les 2 modes
// mobilisation (jamais pour "resultats2024", qui n'a pas de notion de repli).
const COUCHES_PAR_MODE = {
  resultats2024: ["communes-fill", "communes-ligne", "bureaux-fill", "bureaux-ligne"],
  reserve: ["mob-reserve-communes-fill", "mob-reserve-bureaux-fill", "mob-repli-ligne"],
  force: ["mob-force-communes-fill", "mob-force-bureaux-fill", "mob-repli-ligne"],
};

const BANDEAU_PAR_MODE = {
  resultats2024: { titre: "Carte descriptive", texte: "— résultats 2024 réels, pas une projection." },
  reserve: {
    titre: "Réserve mobilisable",
    texte: "— estimateur v1, assumé grossier (ADR 0002) : voir la méthode.",
  },
  force: {
    titre: "Rapport de force projeté",
    texte: "— quantiles larges uniquement, l'ordre fin n'est pas fiable (voir la méthode).",
  },
};

let modeCouche = "resultats2024";

function appliquerMode() {
  for (const [mode, ids] of Object.entries(COUCHES_PAR_MODE)) {
    const visible = mode === modeCouche;
    for (const id of ids) {
      // "mob-repli-ligne" appartient à 2 modes : ne la cache que si NI l'un
      // ni l'autre n'est actif (pas à chaque itération de la boucle).
      if (id === "mob-repli-ligne") continue;
      map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
    }
  }
  map.setLayoutProperty(
    "mob-repli-ligne",
    "visibility",
    modeCouche === "reserve" || modeCouche === "force" ? "visible" : "none"
  );

  document.getElementById("legende-quantile").hidden = modeCouche === "resultats2024";

  const bandeau = BANDEAU_PAR_MODE[modeCouche];
  document.getElementById("bandeau-titre").textContent = bandeau.titre;
  document.getElementById("bandeau-texte").textContent = bandeau.texte;
}

map.on("load", () => {
  const couchesInteractives = [
    "communes-fill",
    "bureaux-fill",
    "mob-reserve-communes-fill",
    "mob-reserve-bureaux-fill",
    "mob-force-communes-fill",
    "mob-force-bureaux-fill",
  ];
  couchesInteractives.forEach((id) => {
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
  map.on("click", "mob-reserve-communes-fill", (e) => {
    if (e.features.length) afficherPanneauReserve(e.features[0].properties, true);
  });
  map.on("click", "mob-reserve-bureaux-fill", (e) => {
    if (e.features.length) afficherPanneauReserve(e.features[0].properties, false);
  });
  map.on("click", "mob-force-communes-fill", (e) => {
    if (e.features.length) afficherPanneauForce(e.features[0].properties, true);
  });
  map.on("click", "mob-force-bureaux-fill", (e) => {
    if (e.features.length) afficherPanneauForce(e.features[0].properties, false);
  });

  appliquerMode();

  document.querySelectorAll('input[name="couche"]').forEach((input) => {
    input.addEventListener("change", (e) => {
      modeCouche = e.target.value;
      appliquerMode();
    });
  });
});
