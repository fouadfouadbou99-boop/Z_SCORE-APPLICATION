"""
Configuration centrale du modèle Z-Score
"""

# =====================================================
# HISTORIQUE
# =====================================================

HISTORICAL_COLUMNS = [
    "N-5",
    "N-4",
    "N-3",
    "N-2",
    "N-1"
]

CURRENT_YEAR_COLUMN = "N"

# =====================================================
# SENS DES INDICATEURS
# =====================================================

# Haut = plus élevé est meilleur
# Bas = plus faible est meilleur

KPI_DIRECTIONS = {

    "Dette nette/EBITDA": "Bas",
    "Dette nette/Fonds propres": "Bas",
    "Gearing": "Bas",
    "Dette/Actif total": "Bas",
    "Dette/CFO": "Bas",

    "Fonds propres/Actif": "Haut",
    "Couverture interets": "Haut",
    "FFO/Dette": "Haut",
    "CFO/Dette": "Haut",
    "FCF/Dette": "Haut",

    "Marge EBITDA %": "Haut",
    "Marge EBIT %": "Haut",
    "ROA %": "Haut",
    "ROE %": "Haut",

    "Liquidité générale": "Haut",
    "Quick Ratio": "Haut",
    "Trésorerie/Dette CT": "Haut",

    "Croissance CA %": "Haut"
}

# =====================================================
# POIDS DE REFERENCE
# =====================================================

DEFAULT_WEIGHTS = {

    "Dette nette/EBITDA": 8,
    "Dette nette/Fonds propres": 6,
    "Gearing": 6,
    "Dette/Actif total": 5,
    "Fonds propres/Actif": 5,

    "Couverture interets": 8,

    "FFO/Dette": 6,
    "CFO/Dette": 6,
    "FCF/Dette": 5,
    "Dette/CFO": 5,

    "Marge EBITDA %": 6,
    "Marge EBIT %": 4,
    "ROA %": 4,
    "ROE %": 4,

    "Liquidité générale": 4,
    "Quick Ratio": 3,
    "Trésorerie/Dette CT": 3,

    "Croissance CA %": 2
}

# =====================================================
# PARAMETRES STATISTIQUES
# =====================================================

MIN_HISTORICAL_YEARS = 3

EPSILON = 1e-10

MAX_ZSCORE = 5

MIN_ZSCORE = -5

# =====================================================
# MAPPING SCORE -> RATING
# =====================================================

RATING_SCALE = [

    {
        "rating": "AAA",
        "min_score": 2.50
    },

    {
        "rating": "AA",
        "min_score": 2.00
    },

    {
        "rating": "A",
        "min_score": 1.50
    },

    {
        "rating": "BBB",
        "min_score": 1.00
    },

    {
        "rating": "BB",
        "min_score": 0.50
    },

    {
        "rating": "B",
        "min_score": 0.00
    },

    {
        "rating": "CCC",
        "min_score": -999
    }
]

# =====================================================
# COULEURS DASHBOARD
# =====================================================

COLOR_POSITIVE = "#2E8B57"
COLOR_NEGATIVE = "#DC143C"
COLOR_NEUTRAL = "#808080"

# =====================================================
# EXPORT
# =====================================================

OUTPUT_EXCEL_FILE = "rapport_zscore.xlsx"

OUTPUT_SHEET_NAME = "Scoring"

# =====================================================
# COLONNES RESULTAT
# =====================================================

OUTPUT_COLUMNS = [

    "KPI",
    "Poids %",
    "Moyenne",
    "Ecart-Type",
    "Z-Score",
    "Sens",
    "Z Ajusté",
    "Score Pondéré"
]

# =====================================================
# ALERTES CREDIT
# =====================================================

ALERT_THRESHOLDS = {

    "Dette nette/EBITDA": 5.0,

    "Gearing": 1.50,

    "Dette/Actif total": 0.70,

    "Couverture interets": 1.50,

    "FFO/Dette": 0.10,

    "CFO/Dette": 0.10,

    "Liquidité générale": 1.00,

    "Quick Ratio": 0.80
}
