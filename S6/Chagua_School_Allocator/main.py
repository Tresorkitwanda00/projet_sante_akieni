from generator import generer_population
from engine import repartir_eleves
from utils import afficher_dashboard_diagnostic

def afficher_menu():
    print("\n=== CHAGUA SCHOOL ALLOCATOR (EPST - RDC) ===")
    print("1. Générer l'effectif des n élèves (Simulateur)")
    print("2. Lancer la répartition automatique des classes")
    print("3. Afficher le Dashboard de Diagnostic Pédagogique")
    print("4. Quitter")
    print("============================================")
def main():
    population_n = []
    classes_reparties = {}

    while True:
        afficher_menu()
        choix = input("Faites votre choix (1-4) : ").strip()

        if choix == "1":
            print("\n Génération des n élèves de Goma en cours...")
            population_n = generer_population(taille=89)
            print(f" {len(population_n)} élèves inscrits avec succès dans la base temporaire !")

        elif choix == "2":
            if not population_n:
                print("\n Erreur : Veuillez d'abord générer les élèves (Option 1).")
            else:
                print("\n Exécution de l'algorithme de tri & répartition...")
                classes_reparties = repartir_eleves(population_n)
                print("Répartition terminée avec succès !")

        elif choix == "3":
            if not classes_reparties:
                print("\n Erreur : Lancez d'abord la répartition (Option 2).")
            else:
                afficher_dashboard_diagnostic(classes_reparties)

        elif choix == "4":
            print("\nMerci d'avoir utilisé Chagua School Allocator. À bientôt !")
            break
        else:
            print("\n Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()