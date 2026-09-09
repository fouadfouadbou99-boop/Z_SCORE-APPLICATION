# Z-Score Quantitative Scoring Application

Application de scoring quantitatif destinée à l'analyse du risque de crédit des émetteurs obligataires à partir d'indicateurs financiers normalisés par la méthode Z-Score.

## Fonctionnalités

- Import de fichiers Excel
- Calcul automatique des moyennes historiques
- Calcul des écarts-types
- Calcul des Z-Scores
- Prise en compte du sens des indicateurs (Haut / Bas)
- Calcul des scores pondérés
- Calcul du score quantitatif global
- Export des résultats au format Excel
- Interface Web Streamlit
- Compatible avec les modèles internes de notation crédit

---

## Structure du projet

```text
zscore-app/
│
├── app.py
├── scoring.py
├── excel_io.py
├── report_generator.py
├── config.py
│
├── data/
│
├── outputs/
│
├── templates/
│   └── template.xlsx
│
├── requirements.txt
├── README.md
└── .gitignore
