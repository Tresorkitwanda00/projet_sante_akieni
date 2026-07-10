
"""
Projet : AKIENI Scientific Calculator (ASC)
Description : Calculatrice scientifique, intelligente et pédagogique.
              Structure globale et gestion des menus interactive.
"""

import math

# ==========================================
# CONFIGURATIONS ET CONTEXTES GLOBAUX
# ==========================================

MODE_PEDAGOGIQUE = True  # Active l'affichage des explications mathématiques pas-à-pas
DECIMALES = 2           # Nombre de chiffres affichés après la virgule
MEMOIRE = 0.0           # Stockage de la mémoire utilisateur (MR, MC, M+, M-)
HISTORIQUE = []         # Registre de session stockant les chaînes de calculs réussis


# ==========================================
# PHASE 1 : GESTION DES SAISIES & INTERFACE
# ==========================================

def afficher_titre(titre):
    """Affiche un bandeau de titre visuellement standardisé pour la console."""
    print("\n" + "=" * 40)
    print(f"{titre.upper()}".center(40, "-"))
    print("=" * 40)


def lire_choix(max_options):
    """
    Sécurise la saisie d'une option de menu.
    Garantit le retour d'un entier valide compris entre 1 et max_options.
    """
    while True:
        try:
            saisie = input(f"Votre choix (1-{max_options}) : ").strip()
            choix = int(saisie)
            if 1 <= choix <= max_options:
                return choix
            else:
                print(f"Erreur : Veuillez choisir un nombre entre 1 et {max_options}.")
        except ValueError:
            print("Erreur : Saisie invalide. Veuillez entrer un nombre entier.")


def lire_nombre(message="Entrez un nombre : "):
    """
    Sécurise la saisie d'un opérande numérique réel.
    Prend en charge l'usage de la virgule et intercepte les ruptures de type (ValueError).
    """
    while True:
        try:
            saisie = input(message).strip()
            saisie = saisie.replace(",", ".")  # Flexibilité pour l'utilisateur francophone
            return float(saisie)
        except ValueError:
            print(" Erreur : Ce n'est pas un nombre valide. Réessayez.")


# ==========================================
# PHASE 2 : MÉMOIRE & HISTORIQUE
# ==========================================

def ajouter_a_l_historique(operation):
    """Insère un enregistrement textuel de l'opération dans le registre global."""
    global HISTORIQUE
    HISTORIQUE.append(operation)


def gerer_memoire():
    """Pilote l'état de la mémoire accumulée et gère son sous-menu dédié."""
    global MEMOIRE
    dans_memoire = True
    
    while dans_memoire:
        afficher_titre("Gestion de la Mémoire")
        print(f"Valeur actuelle en mémoire [M] : {MEMOIRE}")
        print("----------------------------------------")
        print("1. Rappeler la mémoire (MR) -> Afficher la valeur")
        print("2. Effacer la mémoire (MC) -> Remettre à 0")
        print("3. Ajouter un nombre à la mémoire (M+)")
        print("4. Soustraire un nombre de la mémoire (M-)")
        print("5. Retour au menu principal")
        
        choix = lire_choix(5)
        
        if choix == 1:
            print(f"\n Valeur en mémoire : {MEMOIRE}")
        elif choix == 2:
            MEMOIRE = 0.0
            print("\n Mémoire remise à zéro.")
        elif choix == 3:
            valeur = lire_nombre("Entrez la valeur à ajouter à la mémoire : ")
            MEMOIRE += valeur
            print(f"\n {valeur} ajouté à la mémoire.")
        elif choix == 4:
            valeur = lire_nombre("Entrez la valeur à soustraire de la mémoire : ")
            MEMOIRE -= valeur
            print(f"\n {valeur} soustrait de la mémoire.")
        elif choix == 5:
            dans_memoire = False
            
        if choix != 5:
            input("\nAppuyez sur Entrée pour continuer...")


def afficher_historique():
    """Affiche de manière indexée les logs de calculs et propose sa purge complète."""
    global HISTORIQUE
    afficher_titre("Historique des calculs")
    
    if not HISTORIQUE:
        print("L'historique est vide pour le moment.")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    for i, calcul in enumerate(HISTORIQUE, 1):
        print(f"{i}. {calcul}")
        
    print("\n----------------------------------------")
    print("1. Effacer tout l'historique")
    print("2. Retour au menu principal")
    
    choix = lire_choix(2)
    if choix == 1:
        HISTORIQUE.clear()
        print("Historique vidé avec succès.")
        input("\nAppuyez sur Entrée pour continuer...")


# ==========================================
# PHASE 3 : LOGIQUE DES CALCULS ARITHMÉTIQUES
# ==========================================

def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        print(" Erreur : Division par zéro impossible !")
        return None
    return a / b


def modulo(a, b):
    if b == 0:
        print(" Erreur : Le modulo par zéro est impossible !")
        return None
    return a % b 


def puissance(a, b):
    return a ** b


def sous_menu_calculs_base():
    """Interface de routage et d'exécution pour les calculs arithmétiques basiques."""
    dans_sous_menu = True
    while dans_sous_menu:
        afficher_titre("Calculs de Base")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Puissance (^)")
        print("7. Retour au menu principal")

        choix = lire_choix(7)
        if choix == 7:
            dans_sous_menu = False
            continue
            
        print("\n--- Saisie des opérations ---")
        num1 = lire_nombre("Entrez le premier nombre : ")
        num2 = lire_nombre("Entrez le second nombre : ")
        resultat = None
        symbole = ""
        nom_op = ""

        if choix == 1:
            resultat = addition(num1, num2)
            symbole = "+"
        elif choix == 2:
            resultat = substraction(num1, num2)
            symbole = "-"
        elif choix == 3:
            resultat = multiplication(num1, num2)
            symbole = "*"
        elif choix == 4:
            resultat = division(num1, num2)
            symbole = "/"
        elif choix == 5:
            resultat = modulo(num1, num2)
            symbole = "%"
            nom_op = "modulo"
        elif choix == 6:
            resultat = puissance(num1, num2)
            symbole = "^"
            nom_op = "puissance"

        if resultat is not None:
            res_arrondi = round(resultat, DECIMALES)
            ligne_calcul = f"{num1} {symbole} {num2} = {res_arrondi}"
            print(f"\n Résultat : {ligne_calcul}")
            ajouter_a_l_historique(ligne_calcul)
            
            # Déclenchement de l'assistant pédagogique si l'option est supportée
            if MODE_PEDAGOGIQUE and nom_op in ["modulo", "puissance"]:
                expliquer_operation(nom_op, num1, num2, resultat=res_arrondi)
                
        input("\nAppuyez sur Entrée pour continuer...")


# ==========================================
# PHASE 4 : FONCTIONS SCIENTIFIQUES AVANCÉES
# ==========================================

def racine_carree(a):
    if a < 0:
        print(" Erreur : Impossible de calculer la racine carrée d'un nombre négatif.")
        return None
    return math.sqrt(a)


def factoriel(n):
    if n < 0 or not n.is_integer():
        print(" Erreur : La factorielle exige un nombre entier positif.")
        return None
    return math.factorial(int(n))


def calcul_trigo(angle, function):
    """Exécute les opérations trigonométriques en convertissant les degrés d'entrée."""
    radians = math.radians(angle)
    if function == "sin":
        return math.sin(radians)
    elif function == "cos":
        return math.cos(radians)
    elif function == "tan":
        if abs(angle % 180) == 90:
            print(" Erreur : La tangente n'est pas définie pour cet angle !")
            return None
        return math.tan(radians)


def calculer_log(a, type_log):
    if a <= 0:
        print(" Erreur : Le logarithme exige un nombre strictement supérieur à 0.")
        return None
    if type_log == "ln":
        return math.log(a)
    elif type_log == "log":
        return math.log10(a)
    elif type_log == "exp":
        return math.exp(a)


def sous_menu_calculs_avances():
    """Interface de routage pour l'exécution analytique et trigonométrique."""
    dans_sous_menu = True
    
    while dans_sous_menu:
        afficher_titre("Fonctions Avancées & Trigonométrie")
        print("1. Racine carrée (√)")
        print("2. Factorielle (!)")
        print("3. Trigonométrie (Sin, Cos, Tan)")
        print("4. Logarithmes & Exponentielle (Ln, Log10, Exp)")
        print("5. Retour au menu principal")
        
        choix = lire_choix(5)
        if choix == 5:
            dans_sous_menu = False
            continue
            
        resultat = None
        
        if choix == 1:
            num = lire_nombre("Entrez le nombre pour la racine carrée : ")
            resultat = racine_carree(num)
            if resultat is not None:
                res_arrondi = round(resultat, DECIMALES)
                ligne_calcul = f"√({num}) = {res_arrondi}"
                print(f"\n Résultat : {ligne_calcul}")
                ajouter_a_l_historique(ligne_calcul)
                if MODE_PEDAGOGIQUE:
                    expliquer_operation("racine_carree", num, resultat=res_arrondi)
                
        elif choix == 2:
            num = lire_nombre("Entrez un nombre entier pour la factorielle : ")
            resultat = factoriel(num)
            if resultat is not None:
                ligne_calcul = f"{int(num)}! = {resultat}"
                print(f"\n Résultat : {ligne_calcul}")
                ajouter_a_l_historique(ligne_calcul)
                if MODE_PEDAGOGIQUE:
                    expliquer_operation("factorielle", num, resultat=resultat)

        elif choix == 3:
            print("\n--- Options Trigonométriques ---")
            print("1. Sinus (Sin)")
            print("2. Cosinus (Cos)")
            print("3. Tangente (Tan)")
            choix_trigo = lire_choix(3)
            angle = lire_nombre("Entrez l'angle en degrés : ")
            
            func_map = {1: "sin", 2: "cos", 3: "tan"}
            nom_fonc = func_map[choix_trigo]
            resultat = calcul_trigo(angle, nom_fonc)
            
            if resultat is not None:
                res_arrondi = round(resultat, DECIMALES)
                ligne_calcul = f"{nom_fonc.capitalize()}({angle}°) = {res_arrondi}"
                print(f"\n Résultat : {ligne_calcul}")
                ajouter_a_l_historique(ligne_calcul)
                if MODE_PEDAGOGIQUE:
                    expliquer_operation("trigo", angle, nom_fonc, resultat, resultat=res_arrondi)

        elif choix == 4:
            print("\n--- Options Logarithmiques ---")
            print("1. Logarithme Népérien (Ln)")
            print("2. Logarithme Décimal (Log10)")
            print("3. Exponentielle (Exp)")
            choix_log = lire_choix(3)
            num = lire_nombre("Entrez le nombre : ")
            
            log_map = {1: ("ln", "Ln"), 2: ("log", "Log10"), 3: ("exp", "Exp")}
            cle_log, label_log = log_map[choix_log]
            resultat = calculer_log(num, cle_log)
            
            if resultat is not None:
                res_arrondi = round(resultat, DECIMALES)
                ligne_calcul = f"{label_log}({num}) = {res_arrondi}"
                print(f"\n Résultat : {ligne_calcul}")
                ajouter_a_l_historique(ligne_calcul)
                
        input("\nAppuyez sur Entrée pour continuer...")


# ==========================================
# PHASE 5 : MODULES ENSEIGNEMENT & PEDAGOGIE
# ==========================================

def expliquer_operation(nom_op, *args, resultat=None):
    """Détaille analytiquement la mécanique conceptuelle de l'opération effectuée."""
    print("\n" + " COIN EXPLICATION ".center(50, "═"))
    
    if nom_op == "modulo":
        a, b = args[0], args[1]
        print(f"Le Modulo (%), c'est le RESTANT d'une division entière.")
        print(f"Si on partage {int(a)} billes équitablement entre {int(b)} personnes :")
        print(f" -> Chacun reçoit {int(a // b)} bille(s).")
        print(f" -> Il reste {int(a % b)} bille(s) qu'on ne peut plus distribuer.")
        print(f"Voilà pourquoi {int(a)} % {int(b)} = {resultat}")
        
    elif nom_op == "factorielle":
        n = int(args[0])
        print(f"La Factorielle (!), consiste à multiplier l'entier par ses antécédents non nuls.")
        etapes = " x ".join(str(i) for i in range(n, 0, -1))
        print(f"Pour {n}!, le déploiement est : {etapes}")
        print(f"Résultat final = {resultat}")
        
    elif nom_op == "puissance":
        a, b = args[0], args[1]
        print(f"La Puissance (^), est une itération de multiplications auto-référencées.")
        print(f"Ici, on multiplie le nombre {a}, {int(b)} fois de suite :")
        etapes = " x ".join(str(a) for _ in range(int(b)))
        print(f" -> {etapes} = {resultat}")

    elif nom_op == "racine_carree":
        a = args[0]
        print(f"Extraire la racine carrée (√) de {a}, revient à identifier la valeur")
        print(f"qui, élevée au carré, restitue l'opérande d'origine.")
        print(f" -> {resultat} x {resultat} = {a}")

    elif nom_op == "trigo":
        angle, fonction, res_val = args[0], args[1], args[2]
        print(f"La fonction {fonction.upper()} interagit sur un angle géométrique de {angle}°.")
        print("Visualisons un triangle rectangle (à l'image d'une rampe inclinée) :")
        print(" - L'Hypoténuse représente la longueur physique de la pente.")
        if fonction == "sin":
            print(" - Le Sinus détermine la HAUTEUR d'élévation verticale.")
            print(f"Pour une trajectoire de 10 mètres, le gain d'altitude est de :")
            print(f"   10 x {fonction.upper()}({angle}°) = {round(10 * res_val, 2)} mètres.")
        elif fonction == "cos":
            print(" - Le Cosinus comptabilise la distance d'ancrage horizontale (au sol).")
            print(f"Pour une trajectoire de 10 mètres, l'avancée au sol est de :")
            print(f"   10 x {fonction.upper()}({angle}°) = {round(10 * res_val, 2)} mètres.")
        elif fonction == "tan":
            print(" - La Tangente est l'indicateur de déclivité (Pente = Hauteur / Base).")
            print(f"Pour chaque mètre parcouru horizontalement, le dénivelé est de {round(res_val, 2)} mètre(s).")

    print("═" * 50)


def dictionnaire_pedagogique():
    """Lexique vulgarisé expliquant les cas d'application concrets dans le monde réel."""
    continuer_dict = True
    while continuer_dict:
        afficher_titre("Le Savoir de l'Académie (Lexique)")
        print("1. À quoi sert la Trigonométrie (Sin, Cos, Tan) ?")
        print("2. C'est quoi un Logarithme ?")
        print("3. Retour au menu principal")
        
        choix = lire_choix(3)
        if choix == 3:
            continuer_dict = False
            continue
            
        print("\n" + " APPRENDRE ENSEMBLE ".center(50, "═"))
        if choix == 1:
            print("Utilité concrète de la Trigonométrie :")
            print(" - En Ingénierie : Permet de calculer l'altitude et la portée de forces")
            print("   sans déploiement d'instruments physiques complexes.")
            print(" - En Jeu Vidéo : Modélise les ondulations physiques, trajectoires de sauts")
            print("   et rotations spatiales d'éléments de décors.")
        elif choix == 2:
            print("Utilité concrète du Logarithme :")
            print(" - Linéarisation d'échelles : Ramène des dynamiques exponentielles à taille humaine.")
            print(" - Sismologie & Acoustique : L'échelle de Richter ou les Décibels s'appuient")
            print("   sur cette logique : une augmentation linéaire cache une multiplication par 10.")
        print("═" * 50)
        input("\nAppuyez sur Entrée pour continuer...")


# ==========================================
# PHASE 6 : PARAMÈTRES & CONFIGURATIONS
# ==========================================

def gerer_parametres():
    """Interface de mise à jour dynamique des configurations de l'application."""
    global DECIMALES, MODE_PEDAGOGIQUE
    dans_parametres = True
    
    while dans_parametres:
        afficher_titre("Paramètres")
        print(f"1. Modifier le nombre de décimales (Actuel : {DECIMALES})")
        print(f"2. Mode Pédagogique (Actuel : {'ACTIVÉ' if MODE_PEDAGOGIQUE else 'DÉSACTIVÉ'})")
        print("3. Retour au menu principal")
        
        choix = lire_choix(3)
        
        if choix == 1:
            print("\nCombien de décimales souhaitez-vous afficher (0-9) ?")
            nb = lire_choix(10) - 1
            DECIMALES = nb
            print(f" Configuration modifiée : Résultats fixés à {DECIMALES} décimales.")
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == 2:
            MODE_PEDAGOGIQUE = not MODE_PEDAGOGIQUE
            print(f" Configuration modifiée : Mode d'explication {'Activé' if MODE_PEDAGOGIQUE else 'Désactivé'}.")
            input("\nAppuyez sur Entrée pour continuer...")
        elif choix == 3:
            dans_parametres = False


# ==========================================
# ORCHESTRATION DU FLUX PRINCIPAL
# ==========================================

def afficher_menu_principal():
    """Génère l'affichage textuel du hub principal."""
    afficher_titre("AKIENI Scientific Calculator (ASC)")
    print("1. Calculs de Base")
    print("2. Fonctions Avancées & Scientifiques")
    print("3. Gestion de la Mémoire")
    print("4. Afficher l'Historique")
    print("5. Paramètres de l'application")
    print("6. Le Savoir de l'Académie (Lexique)")
    print("7. Quitter le programme")


def main():
    """Boucle maîtresse appliquant la logique d'exécution continue."""
    continuer = True
    while continuer:
        afficher_menu_principal()
        choix = lire_choix(7)  # Prise en charge des 7 options du menu principal
        
        if choix == 1:
            sous_menu_calculs_base()
        elif choix == 2:
            sous_menu_calculs_avances()
        elif choix == 3:
            gerer_memoire()
        elif choix == 4:
            afficher_historique()
        elif choix == 5:
            gerer_parametres()
        elif choix == 6:
            dictionnaire_pedagogique()
        elif choix == 7:
            print("\n Êtes-vous sûr de vouloir quitter ?")
            print("1. Oui")
            print("2. Non")
            confirmation = lire_choix(2)
            if confirmation == 1:
                continuer = False
                
    print("\n Au revoir et merci d'avoir utilisé ASC !")

if __name__ == "__main__":
    main()