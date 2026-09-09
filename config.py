"""
config.py
Configuration centrale de l'application Z-Score
"""

# =====================================================
# COLONNES HISTORIQUES
# =====================================================

HISTORICAL_COLUMNS = [
    "N-5",
    "N-4",
    "N-3",
    "N-2",
    "N-1"
]

CURRENT_COLUMN = "N"

# =====================================================
# PARAMETRES DE CALCUL
# =====================================================

MIN_HISTORY = 3

EPSILON = 1e-10

MAX_ZSCORE = 5

MIN_ZSCORE = -5

# =====================================================
# FICHIERS DE SORTIE
# =====================================================

OUTPUT_FILE = "outputs/rapport_zscore.xlsx"

PDF_OUTPUT_FILE = "outputs/rapport_zscore.pdf"

CHART_OUTPUT_FILE = "outputs/evolution_score.png"

# =====================================================
# MAPPING RATING
# =====================================================

RATING_SCALE = [

    {
        "rating": "AAA",
        "min_score": 3.00
    },

    {
        "rating": "AA",
        "min_score": 2.00
    },

    {
        "rating": "A",
        "min_score": 1.00
    },

    {
        "rating": "BBB",
        "min_score": 0.50
    },

    {
        "rating": "BB",
        "min_score": 0.00
    },

    {
        "rating": "B",
        "min_score": -1.00
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
# DESCRIPTIONS DES RATINGS
# =====================================================

RATING_DESCRIPTIONS = {

    "AAA": {
        "description": "Qualité de crédit exceptionnelle",
        "risk_level": "Très faible"
    },

    "AA": {
        "description": "Qualité de crédit très élevée",
        "risk_level": "Faible"
    },

    "A": {
        "description": "Qualité de crédit élevée",
        "risk_level": "Modéré faible"
    },

    "BBB": {
        "description": "Qualité de crédit satisfaisante",
        "risk_level": "Modéré"
    },

    "BB": {
        "description": "Qualité de crédit spéculative",
        "risk_level": "Modéré élevé"
    },

    "B": {
        "description": "Risque de crédit élevé",
        "risk_level": "Elevé"
    },

    "CCC": {
        "description": "Risque de crédit très élevé",
        "risk_level": "Très élevé"
    }
}

# =====================================================
# SENS PAR DEFAUT DES KPI
# =====================================================

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
# ALERTES CREDIT
# =====================================================

ALERT_THRESHOLDS = {

    "Dette nette/EBITDA": 5.00,

    "Dette nette/Fonds propres": 2.00,

    "Gearing": 1.50,

    "Dette/Actif total": 0.70,

    "Couverture interets": 1.50,

    "FFO/Dette": 0.10,

    "CFO/Dette": 0.10,

    "Liquidité générale": 1.00,

    "Quick Ratio": 0.80
}
