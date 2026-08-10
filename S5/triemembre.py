import random

# Nombre de membres
nombre_membres = int(input("Combien y a-t-il de membres ? "))

# Liste des membres
membres = []

for i in range(nombre_membres):
    nom = input(f"Nom du membre {i + 1} : ")
    membres.append(nom)


def organiser_vote(candidats, nombre_votes):
    """Organise un vote aléatoire et retourne les résultats."""
    votes = {}

    # Initialiser les votes
    for candidat in candidats:
        votes[candidat] = 0

    print("\n--- Début du vote ---")

    # Générer les votes
    for i in range(nombre_votes):
        vote = random.choice(candidats)
        votes[vote] += 1
        print(f"Vote {i + 1} : {vote}")

    print("\n--- Résultat ---")
    for candidat, nb_votes in votes.items():
        print(f"{candidat} : {nb_votes} vote(s)")

    return votes


# Premier tour
votes = organiser_vote(membres, nombre_membres)

# Vérification des égalités
while True:

    max_votes = max(votes.values())

    # Liste des candidats ayant le plus de votes
    egalites = []

    for candidat, nb_votes in votes.items():
        if nb_votes == max_votes:
            egalites.append(candidat)

    # Un seul gagnant
    if len(egalites) == 1:
        chef = egalites[0]
        print(f"\n Le chef du groupe est : {chef} avec {max_votes} vote(s).")
        break

    # Égalité : second tour
    print("\n⚠ Égalité détectée entre :", ", ".join(egalites))
    print("➡ Organisation d'un second tour...\n")

    votes = organiser_vote(egalites, nombre_membres)