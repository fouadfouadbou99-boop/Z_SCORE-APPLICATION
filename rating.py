"""
Module de mapping Score Quantitatif -> Rating
"""

from config import RATING_SCALE


def get_rating(score: float) -> str:
    """
    Retourne la notation associée au score.
    """

    for grade in RATING_SCALE:
        if score >= grade["min_score"]:
            return grade["rating"]

    return "CCC"


def get_rating_details(score: float) -> dict:
    """
    Retourne les informations complètes relatives à la note.
    """

    rating = get_rating(score)

    rating_info = {
        "AAA": {
            "description": "Qualité de crédit exceptionnelle",
            "risk_level": "Très Faible"
        },
        "AA": {
            "description": "Qualité de crédit très élevée",
            "risk_level": "Faible"
        },
        "A": {
            "description": "Qualité de crédit élevée",
            "risk_level": "Modéré Faible"
        },
        "BBB": {
            "description": "Qualité de crédit satisfaisante",
            "risk_level": "Modéré"
        },
        "BB": {
            "description": "Profil spéculatif modéré",
            "risk_level": "Modéré Élevé"
        },
        "B": {
            "description": "Profil spéculatif élevé",
            "risk_level": "Élevé"
        },
        "CCC": {
            "description": "Risque de crédit très élevé",
            "risk_level": "Très Élevé"
        }
    }

    return {
        "score": round(score, 2),
        "rating": rating,
        "description": rating_info[rating]["description"],
        "risk_level": rating_info[rating]["risk_level"]
    }


def get_rating_color(rating: str) -> str:

    colors = {
        "AAA": "#006400",
        "AA": "#228B22",
        "A": "#32CD32",
        "BBB": "#FFD700",
        "BB": "#FFA500",
        "B": "#FF4500",
        "CCC": "#B22222"
    }

    return colors.get(rating, "#808080")
def get_trend(current_score, previous_score):

    delta = current_score - previous_score

    if delta >= 0.20:
        return "Amélioration"

    if delta <= -0.20:
        return "Dégradation"

    return "Stable"
