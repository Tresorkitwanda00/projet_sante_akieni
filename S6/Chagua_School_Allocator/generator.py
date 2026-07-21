# generator.py
import random 
from config import ECOLES_PROVENANCE_CONNUES

def generer_eleve(index:int)->dict:
    """
    Génère un dictionnaire représentant un élève unique de Goma 
    avec des données aléatoires mais pédagogiquement cohérentes.
    """
    # Liste de prénoms pour simuler des données réelles
    prenoms_f = ["Amani", "Dorcas", "Kabibi", "Furaha", "Neema", "Sifa", "Merveille"]
    prenoms_m = ["Musa", "Baraka", "Bahati", "Akili", "Shukuru", "Tumaini", "Jean"]
    noms_famille = ["Kabila", "Tshibanda", "Kasongo", "Kambale", "Kavira", "Mbuyi", "Ilunga"]
    # Détermination du sexe et du nom complet
    sexe = random.choice(['F','M'])
    prenom = random.choice(prenoms_f) if sexe == 'F' else random.choice([prenoms_m])
    nom_complet = f"{prenom} {random.choice(noms_famille)}"
    # Critère ENAFEP : Note réaliste en pourcentage (entre 50.0% et 98.5%)
    score_enafep = round(random.uniform(50.0, 98.5), 1)
    # Critère EPST : Statut (85% de nouveaux, 15% de redoublants)
    statut = "Redoublant" if random.random() < 0.15 else "Nouveau"
    # Critère Inclusion : Besoins spécifiques (environ 2% des élèves)
    besoin_particulier = True if random.random() < 0.02 else False
    # Assemblage de la structure complexe (Dictionnaire)
    return {
        "id": f"ELV_2026_{index:03d}",
        "nom": nom_complet,
        "sexe": sexe,
        "score_enafep": score_enafep,
        "ecole_provenance": random.choice(ECOLES_PROVENANCE_CONNUES),
        "statut": statut,
        "besoin_particulier": besoin_particulier
    }
def generer_population(taille:int = 700)->list:
    """
    Boucle pour créer la liste principale contenant les 700 dictionnaires d'élèves.
    """
    population = []

    for i in range(1,taille+1):
        un_eleve = generer_eleve(i)
        population.append(un_eleve)
    return population
