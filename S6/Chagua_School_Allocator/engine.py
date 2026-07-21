# engine.py
from config import STRUCTURES_CLASSES_INITIALES, SEUIL_MAX_ELEVES_PAR_CLASSE

def repartir_eleves(liste_n_eleves: list) -> dict:
    """
    Moteur principal de Chagua School Allocator.
    """
    # 1. Copie propre des classes
    classes_finales = {classe: list(eleves) for classe, eleves in STRUCTURES_CLASSES_INITIALES.items()}
    noms_classes = list(classes_finales.keys()) # ['1ère SEC A', '1ère SEC B', '1ère SEC C', '1ère SEC D']

    # 2. Séparation : Inclusifs vs Standards
    eleves_prioritaires = [e for e in liste_n_eleves if e["besoin_particulier"] == True]
    eleves_standards = [e for e in liste_n_eleves if e["besoin_particulier"] == False]

    # 3. Tri par le mérite ENAFEP
    eleves_standards_tries = sorted(eleves_standards, key=lambda x: x["score_enafep"], reverse=True)

    index_classe = 0

    # 4. Distribution des élèves à besoins spécifiques
    for eleve in eleves_prioritaires:
        classe_cible = noms_classes[index_classe]
        classes_finales[classe_cible].append(eleve)
        index_classe = (index_classe + 1) % len(noms_classes)

    # 5. Distribution du reste de la population (Round-Robin sécurisé)
    for eleve in eleves_standards_tries:
        placé = False
        # On teste les classes une par une en partant de index_classe
        for _ in range(len(noms_classes)):
            classe_cible = noms_classes[index_classe]
            
            # Si la classe a encore de la place
            if len(classes_finales[classe_cible]) < SEUIL_MAX_ELEVES_PAR_CLASSE:
                classes_finales[classe_cible].append(eleve)
                index_classe = (index_classe + 1) % len(noms_classes)
                placé = True
                break # Élève placé, on passe au suivant dans eleves_standards_tries
            
            # Si pleine, on pointe vers la classe suivante pour le test
            index_classe = (index_classe + 1) % len(noms_classes)
            
        if not placé:
            # Si toutes les classes sont pleines à 55 (55 x 4 = 220 places max)
            # Les élèves restants ne dépasseront plus le seuil EPST
            pass

    return classes_finales