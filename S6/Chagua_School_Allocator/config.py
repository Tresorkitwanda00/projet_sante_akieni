# config.py

# ==========================================
# CONFIGURATION ADMINISTRATIVE & PÉDAGOGIQUE
# ==========================================

# Nombre maximum d'élèves par classe (Norme EPST pour éviter le surpeuplement)
SEUIL_MAX_ELEVES_PAR_CLASSE = 55

# Pourcentage maximal de redoublants autorisé par classe pour garantir l'équilibre
QUOTA_MAX_REDOUBLANTS_POURCENTAGE = 0.20  # Max 20% de redoublants par classe

# Écoles de provenance cibles prioritaires à diversifier

ECOLES_PROVENANCE_CONNUES = [ 
    "CS MAMA YETU", 
    "CS LES VOLCANS", 
    "EP MAUA", 
    "EP CIPUKO", 
    "CS LA FONTAINE", 
    "CS LA CONCORDE",
    "EP KATINDO",
    "CS METANOIA",
    "EP KESHERO",
    "EP KARISIMBI"
]

# ==========================================
# STRUCTURES DE DONNÉES COMPLEXES INITIALES
# ==========================================

# Dictionnaire des classes vides. Les clés sont les sections officielles.
# Chaque clé contient une liste vide qui accueillera les dictionnaires des élèves.
STRUCTURES_CLASSES_INITIALES = {
    "1ère SEC A": [],
    "1ère SEC B": [],
    "1ère SEC C": [],
    "1ère SEC D": []
}

# Modèle de structure pour un élève (Donné à titre indicatif pour le développement)
# Chaque élève injecté dans le système devra suivre ce format exact de dictionnaire :
# {
#     "id": str,
#     "nom": str,
#     "sexe": str ( 'M' ou 'F' ),
#     "score_enafep": float ( en % ),
#     "ecole_provenance": str,
#     "statut": str ( 'Nouveau' ou 'Redoublant' ),
#     "besoin_particulier": bool ( True ou False )
# }