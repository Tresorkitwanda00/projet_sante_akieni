
"""
Projet : AKIENI Scientific Calculator (ASC)
Description : Calculatrice scientifique, intelligente et pédagogique.
              Structure globale et gestion des menus interactive.
"""
# ==============================================================================
#  SECTION 1 : IMPORTS ET INITIALISATIONS DE L'ENVIRONNEMENT
# Chargement des modules natifs, dépendances externes et moteur de rendu Rich.
# =============================================================================
import math
import random
from rich import print
from rich.console import Console

# Initialisation globale du composant d'affichage de l'Académie
console = Console()
# ==============================================================================
#  SECTION 2 : CONFIGURATIONS ET VARIABLES D'ÉTAT GLOBALES
# Gestion de la mémoire vive de la session (Historique, Décimales, Mode Pédago).
# ==============================================================================
MODE_PEDAGOGIQUE = True
DECIMALES = 2
MEMOIRE = 0.0
HISTORIQUE = []

# ---  Utilisation dans une fonction ---
def modifier_precision():
    global DECIMALES  # Indique à Python qu'on veut MODIFIER la variable globale
    nouvelle_precision = int(lire_nombre("Entrez le nombre de décimales souhaité (0-9) : "))
    if 0 <= nouvelle_precision <= 9:
        DECIMALES = nouvelle_precision
        console.print(f"[bold green]Précision mise à jour à {DECIMALES} décimales ![/bold green]")
# ==============================================================================
#  SECTION 3 : LOGIQUE INTERACTIVE ET UTILITAIRES DE CONTROLE UI/UX
# Fonctions de capture sécurisée des données et formatage visuel du terminal.
# ==============================================================================

def afficher_titre(titre):
    """Affiche un titre de section stylisé et centré avec Rich."""
    console.print() 
    console.rule(f"[bold cyan] {titre} [/bold cyan]", style="cyan")
    console.print()

def afficher_resultat(operation, detail, resultat):
    """Affiche le résultat d'un calcul de manière très visuelle."""
    console.print(f"\n[bold green]✔ Calcul réussi ![/bold green]")
    console.print(f"[dim]Opération : {operation}[/dim]")
    console.print("┌" + "─" * 45 + "┐", style="bold green")
    console.print(f"│  [bold white]{detail:<41}[/bold white]  │", style="bold green")
    console.print(f"│  [bold yellow]Résultat : {resultat:<30}[/bold yellow]  │", style="bold green")
    console.print("└" + "─" * 45 + "┘", style="bold green")

def lire_nombre(prompt="Saisissez un nombre : "):
    """Lit un nombre de manière sécurisée avec une UX colorée."""
    while True:
        try:
            # On utilise console.input pour garder le style coloré sur l'invite de saisie
            saisie = console.input(f"[bold white]{prompt}[/bold white]").strip()
            saisie = saisie.replace(",", ".")
            return float(saisie)
        except ValueError:
            console.print("[bold red]Erreur de saisie :[/bold red] Ce n'est pas un nombre valide. "
                          "[dim](Exemple attendu : 12 ou 5.5)[/dim]")
            console.print()

def lire_choix(nb_options):
    """Force l'utilisateur à choisir une option valide dans le menu."""
    while True:
        try:
            choix = int(console.input(f"\n[bold cyan]Votre choix (1-{nb_options}) : [/bold cyan]"))
            if 1 <= choix <= nb_options:
                return choix
            else:
                console.print(f"[bold orange3]Option hors limites ![/bold orange3] Veuillez choisir un nombre entre [bold]1 et {nb_options}[/bold].")
        except ValueError:
            console.print("[bold red]Saisie incorrecte ![/bold red] Veuillez entrer un numéro de menu valide.")


# ==============================================================================
#  SECTION 4 : MOTEUR D'EXPLICATIONS PÉDAGOGIQUES ET DISPATCHER
# Routage dynamique des analyses conceptuelles et vulgarisation des mathématiques.
# ==============================================================================

def exp_modulo(*args, resultat):
    a, b = args[0], args[1]
    console.print(f"Le [bold yellow]Modulo (%)[/bold yellow] correspond au [bold green]RESTANT[/bold green] d'une division entière.")
    console.print(f"Imaginons que nous partagions [bold]{int(a)}[/bold] serveurs équitablement entre [bold]{int(b)}[/bold] équipes :")
    console.print(f"  Chaque équipe reçoit d'abord [bold cyan]{int(a // b)}[/bold cyan] serveur(s).")
    console.print(f"  Il reste [bold green]{int(a % b)}[/bold green] serveur(s) qui ne peuvent pas être distribués.")
    console.print(f"\n[bold yellow]Formule mathématique :[/bold yellow] {int(a)} = ({int(b)} x {int(a // b)}) + [bold green]{int(a % b)}[/bold green]")

def exp_factorielle(*args, resultat):
    n = int(args[0])
    console.print(f"La [bold yellow]Factorielle (!)[/bold yellow] consiste à multiplier un entier par tous ses antécédents non nuls.")
    etapes = " x ".join(f"[bold cyan]{i}[/bold cyan]" for i in range(n, 0, -1))
    console.print(f"Pour [bold]{n}![/bold], le déploiement complet est : {etapes}")
    console.print(f" [bold green]Résultat final = {resultat}[/bold green]")

def exp_puissance(*args, resultat):
    a, b = args[0], args[1]
    console.print(f"La [bold yellow]Puissance (^)[/bold yellow] est une croissance accélérée par multiplication répétée.")
    console.print(f"Calculer [bold]{a}^{int(b)}[/bold], c'est multiplier le nombre [bold]{a}[/bold], [bold cyan]{int(b)} fois[/bold cyan] de suite :")
    etapes = " x ".join(f"[bold cyan]{a}[/bold cyan]" for _ in range(int(b)))
    console.print(f"  {etapes} = [bold green]{resultat}[/bold green]")

def exp_racine_carree(*args, resultat):
    a = args[0]
    console.print(f"Extraire la [bold yellow]Racine Carrée (√)[/bold yellow] de {a} revient à identifier le nombre unique")
    console.print(f"qui, multiplié par lui-même, restitue la valeur de base.")
    console.print(f"  [bold cyan]{resultat}[/bold cyan] x [bold cyan]{resultat}[/bold cyan] = [bold green]{a}[/bold green]")

def exp_trigo(*args, resultat):
    angle, fonction, res_val = args[0], args[1], args[2]
    console.print(f"La fonction [bold yellow]{fonction.upper()}[/bold yellow] interagit sur un angle géométrique de [bold]{angle}°[/bold].")
    console.print("Visualisons un triangle rectangle (comme une rampe d'accès inclinée) :")
    console.print(" - L'Hypoténuse représente la longueur physique de la rampe.")
    
    if fonction == "sin":
        console.print(" - Le [bold cyan]Sinus[/bold cyan] détermine la [bold green]HAUTEUR[/bold green] d'élévation verticale.")
        console.print(f"Pour une rampe de 10 mètres, le gain de hauteur est de :")
        console.print(f"   10 x {fonction.upper()}({angle}°) = [bold green]{round(10 * res_val, 2)}[/bold green] mètres.")
    elif fonction == "cos":
        console.print(" - Le [bold cyan]Cosinus[/bold cyan] détermine l'empreinte au sol (distance horizontale).")
        console.print(f"Pour une rampe de 10 mètres, la projection au sol est de :")
        console.print(f"   10 x {fonction.upper()}({angle}°) = [bold green]{round(10 * res_val, 2)}[/bold green] mètres.")
    elif fonction == "tan":
        console.print(" - La [bold cyan]Tangente[/bold cyan] mesure la pente (le ratio Hauteur / Distance horizontale).")
        console.print(f"Pour chaque mètre horizontal, la déclivité verticale est de [bold green]{round(res_val, 2)}[/bold green] mètre(s).")
EXPLICATIONS = {
    "modulo": exp_modulo,
    "factorielle": exp_factorielle,
    "puissance": exp_puissance,
    "racine_carree": exp_racine_carree,
    "trigo": exp_trigo
}

def expliquer_operation(nom_op, *args, resultat=None):
    """Explique de manière interactive et dynamique n'importe quelle opération."""
    if nom_op not in EXPLICATIONS:
        return # Si l'opération n'a pas besoin d'explications, on passe
        
    console.print()
    console.rule("[bold gold3] ASSISTANT PÉDAGOGIQUE[/bold gold3]", style="gold3")
    console.print()
    
    # Appel dynamique de la fonction correspondante stockée dans le dictionnaire
    fonction_explicative = EXPLICATIONS[nom_op]
    fonction_explicative(*args, resultat=resultat)
    
    console.print()
    console.rule(style="gold3")
# ==============================================================================
#  MÉMOIRE : MODULE DE STOCKAGE ET DE MANIPULATION DES REGISTRES (M+/M-/MR/MC)
# Persistance temporaire, cumul, soustraction et restitution des valeurs de calcul.
# ==============================================================================
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

# ==============================================================================
#  SECTION 5 : MODULES MÉTIERS MATHÉMATIQUES (First-Class Citizens)
# Moteurs de calculs purs via fonctions Lambda et algorithmes scientifiques sécurisés.
# ==============================================================================
# ==========================================
# PHASE 1 : CALCUL DE BASE
# ==========================================
OPERATIONS_BASE = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: None if b == 0 else a / b,
    "%": lambda a, b: None if b == 0 else a % b,
    "^": lambda a, b: a ** b
}

# Rappel de notre structure de données "First-Class Citizens" pour les calculs
OPERATIONS_BASE = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: None if b == 0 else a / b,
    "%": lambda a, b: None if b == 0 else a % b,
    "^": lambda a, b: a ** b
}

# Table de correspondance pour les métadonnées de l'interface
MAPPING_OPERATIONS = {
    1: {"symbole": "+", "nom_op": "addition"},
    2: {"symbole": "-", "nom_op": "soustraction"},
    3: {"symbole": "*", "nom_op": "multiplication"},
    4: {"symbole": "/", "nom_op": "division"},
    5: {"symbole": "%", "nom_op": "modulo"},
    6: {"symbole": "^", "nom_op": "puissance"}
}

# ==========================================
# PHASE 2 : FONCTIONS SCIENTIFIQUES AVANCÉES
# ==========================================

def racine_carree(a):
    """Calcule la racine carrée d'un nombre positif."""
    if a < 0:
        console.print("\n [bold red]Erreur de calcul :[/bold red] Impossible de calculer la racine carrée d'un nombre négatif.")
        return None
    return math.sqrt(a)


def factoriel(n):
    """Calcule la factorielle d'un entier positif."""
    if n < 0 or not n.is_integer():
        console.print("\n [bold red]Erreur de calcul :[/bold red] La factorielle exige un nombre entier positif.")
        return None
    return math.factorial(int(n))


def calcul_trigo(angle, function):
    """Calcule les rapports trigonométriques à partir d'un angle en degrés."""
    radians = math.radians(angle)
    if function == "sin":
        return math.sin(radians)
    elif function == "cos":
        return math.cos(radians)
    elif function == "tan":
        # Cas critique : tangente non définie pour les asymptotes verticales (90°, 270°, etc.)
        if abs(angle % 180) == 90:
            console.print("\n [bold red]Erreur de calcul :[/bold red] La tangente n'est pas définie pour un angle de 90° ou ses multiples.")
            return None
        return math.tan(radians)


def calculer_log(a, type_log):
    """Calcule les logarithmes ou l'exponentielle."""
    if type_log != "exp" and a <= 0:
        console.print("\n [bold red]Erreur de calcul :[/bold red] Le logarithme exige une valeur strictement supérieure à 0.")
        return None
    
    if type_log == "ln":
        return math.log(a)
    elif type_log == "log":
        return math.log10(a)
    elif type_log == "exp":
        return math.exp(a)


# ==========================================
#  2. CONFIGURATION ET ROUTAGE DYNAMIQUE (First-Class Citizens)
# ==========================================

CONFIG_AVANCEE = {
    1: {
        "nom_op": "racine_carree",
        "prompt": "Entrez le nombre pour la racine carrée : ",
        "calcul": lambda num: racine_carree(num),
        "formateur": lambda num, res: (f"√({num})", "racine_carree", (num,))
    },
    2: {
        "nom_op": "factorielle",
        "prompt": "Entrez un nombre entier pour la factorielle : ",
        "calcul": lambda num: factoriel(num),
        "formateur": lambda num, res: (f"{int(num)}!", "factorielle", (num,))
    }
}

# ==============================================================================
#  SECTION 6 : LA BASE DE CONNAISSANCES DE L'ACADÉMIE
# ==============================================================================
LEXIQUE_ACADEMIE = {
    1: {
        "titre": "À quoi sert la Trigonométrie (Sin, Cos, Tan) ?",
        "categorie": "TRIGONOMETRIE",
        "description": (
            "La trigonométrie étudie les relations entre les angles et les distances dans les triangles.\n\n"
            "[bold cyan]Applications concrètes :[/bold cyan]\n"
            " • [bold yellow]Jeux Vidéo & Animation 3D :[/bold yellow] Utilisée pour calculer les trajectoires de sauts "
            "des personnages, gérer les rotations de caméra et simuler des mouvements ondulatoires (comme les vagues ou le vent).\n"
            " • [bold yellow]Géolocalisation & GPS :[/bold yellow] Permet de déterminer ta position exacte sur Terre par triangulation "
            "en mesurant les angles de signal avec plusieurs satellites."
        )
    },
    2: {
        "titre": "C'est quoi un Logarithme ?",
        "categorie": "LOGARITHMES",
        "description": (
            "Le logarithme est l'opération inverse de l'exponentielle. Il permet de ramener des échelles de croissance explosives "
            "à des proportions faciles à lire.\n\n"
            "[bold cyan]Applications concrètes :[/bold cyan]\n"
            " • [bold yellow]Sismologie (Échelle de Richter) :[/bold yellow] Un séisme de magnitude 6 n'est pas 'un point' plus fort qu'un "
            "séisme de magnitude 5. Il libère environ [bold red]32 fois plus d'énergie[/bold red] ! L'échelle logarithmique permet de "
            "représenter des écarts colossaux sur une échelle simple de 1 à 10.\n"
            " • [bold yellow]Acoustique (Décibels) :[/bold yellow] L'oreille humaine perçoit le son de manière logarithmique. "
            "Deux aspirateurs en marche ne font pas deux fois plus de bruit dans tes oreilles qu'un seul, le volume sonore global n'augmente que de 3 décibels."
        )
    }
}

# ==========================================
#. L'INTERFACE DE LECTURE DU LEXIQUE
# ==========================================
def dictionnaire_pedagogique():
    """Lexique vulgarisé géré par dictionnaire pour un code évolutif."""
    continuer_dict = True
    while continuer_dict:
        afficher_titre("Le Savoir de l'Académie (Lexique)")
        
        # Génération dynamique du menu à partir de notre dictionnaire de connaissances
        for option, concept in LEXIQUE_ACADEMIE.items():
            print(f"{option}. {concept['titre']}")
        print(f"{len(LEXIQUE_ACADEMIE) + 1}. Retour au menu principal")
        
        # Attente du choix (le nombre d'options s'adapte automatiquement)
        nb_choix_possible = len(LEXIQUE_ACADEMIE) + 1
        choix = lire_choix(nb_choix_possible)
        
        if choix == nb_choix_possible:
            continuer_dict = False
            continue
            
        # Affichage stylisé de la fiche sélectionnée
        fiche = LEXIQUE_ACADEMIE[choix]
        
        console.print()
        console.rule(f"[bold gold3] FOCUS : {fiche['categorie']}[/bold gold3]", style="gold3")
        console.print()
        console.print(fiche['description'])
        console.print()
        console.rule(style="gold3")
        
        input("\nAppuyez sur Entrée pour continuer...")

# ==============================================================================
#  SECTION 7 : INTERFACES APPLICATIVES ET SOUS-MENUS DE ROUTAGE
# Contrôleurs d'écrans liant la navigation aux moteurs métiers et au Super Quiz.
# ==============================================================================
#MENU DE CALCUL DE BASE

def sous_menu_calculs_base():
    """Interface de routage et d'exécution pour les calculs arithmétiques basiques."""
    global HISTORIQUE, DECIMALES, MODE_PEDAGOGIQUE
    dans_sous_menu = True
    
    while dans_sous_menu:
        afficher_titre("Calculs de Base")
        console.print("1. Addition (+)")
        console.print("2. Soustraction (-)")
        console.print("3. Multiplication (*)")
        console.print("4. Division (/)")
        console.print("5. Modulo (%)")
        console.print("6. Puissance (^)")
        console.print("7. Retour au menu principal")

        choix = lire_choix(7)
        if choix == 7:
            dans_sous_menu = False
            continue
            
        console.print("\n[bold cyan] Saisie des opérandes :[/bold cyan]")
        num1 = lire_nombre("Entrez le premier nombre : ")
        num2 = lire_nombre("Entrez le second nombre : ")
        
        # Récupération dynamique des propriétés de l'opération
        metadonnees = MAPPING_OPERATIONS[choix]
        symbole = metadonnees["symbole"]
        nom_op = metadonnees["nom_op"]

        # Récupération et exécution de la fonction Lambda associée (First-Class Citizen)
        fonction_calcul = OPERATIONS_BASE[symbole]
        resultat = fonction_calcul(num1, num2)

        # Gestion des erreurs de calcul (comme la division par zéro)
        if resultat is None:
            console.print(f"\n [bold red]Erreur :[/bold red] L'opération [bold yellow]{nom_op}[/bold yellow] par zéro est mathématiquement impossible !")
        else:
            # Formatage de l'arrondi dynamique selon la configuration de session
            res_arrondi = round(resultat, DECIMALES)
            ligne_calcul = f"{num1} {symbole} {num2} = {res_arrondi}"
            
            # Affichage stylisé du résultat
            afficher_resultat(f"Opération ({nom_op.capitalize()})", f"{num1} {symbole} {num2}", res_arrondi)
            
            # Journalisation dans le registre d'historique global de la session
            HISTORIQUE.append(f"[cyan]{num1} {symbole} {num2}[/cyan] = [bold green]{res_arrondi}[/bold green]")
            
            # Déclenchement automatique et dynamique de l'assistant pédagogique s'il est activé
            if MODE_PEDAGOGIQUE:
                expliquer_operation(nom_op, num1, num2, resultat=res_arrondi)
                
        input("\nAppuyez sur Entrée pour continuer...")
#MENU DE CALCUL AVANCE
def sous_menu_calculs_avances():
    """Interface de routage pour l'exécution analytique et trigonométrique."""
    global HISTORIQUE, DECIMALES, MODE_PEDAGOGIQUE
    dans_sous_menu = True
    
    while dans_sous_menu:
        afficher_titre("Fonctions Avancées & Trigonométrie")
        console.print("1. Racine carrée (√)")
        console.print("2. Factorielle (!)")
        console.print("3. Trigonométrie (Sin, Cos, Tan)")
        console.print("4. Logarithmes & Exponentielle (Ln, Log10, Exp)")
        console.print("5. Retour au menu principal")
        
        choix = lire_choix(5)
        if choix == 5:
            dans_sous_menu = False
            continue
            
        resultat = None
        ligne_calcul = ""
        nom_explication = ""
        arguments_explication = ()

        # --- CAS 1 & 2 : ROUTAGE ULTRA-SIMPLIFIÉ GRÂCE À CONFIG_AVANCEE ---
        if choix in CONFIG_AVANCEE:
            config = CONFIG_AVANCEE[choix]
            num = lire_nombre(config["prompt"])
            resultat = config["calcul"](num)
            
            if resultat is not None:
                # Arrondi sans toucher aux factorielles géantes qui doivent rester entières
                res_arrondi = int(resultat) if choix == 2 else round(resultat, DECIMALES)
                expression, nom_explication, arguments_explication = config["formateur"](num, res_arrondi)
                ligne_calcul = f"{expression} = {res_arrondi}"

        # --- CAS 3 : SOUS-MENU TRIGONOMÉTRIE ---
        elif choix == 3:
            console.print("\n[bold cyan] Options Trigonométriques :[/bold cyan]")
            console.print("1. Sinus (Sin)")
            console.print("2. Cosinus (Cos)")
            console.print("3. Tangente (Tan)")
            choix_trigo = lire_choix(3)
            
            angle = lire_nombre("Entrez l'angle en degrés : ")
            func_map = {1: "sin", 2: "cos", 3: "tan"}
            nom_fonc = func_map[choix_trigo]
            
            resultat = calcul_trigo(angle, nom_fonc)
            if resultat is not None:
                res_arrondi = round(resultat, DECIMALES)
                ligne_calcul = f"{nom_fonc.capitalize()}({angle}°) = {res_arrondi}"
                nom_explication = "trigo"
                arguments_explication = (angle, nom_fonc, resultat)

        # --- CAS 4 : SOUS-MENU LOGARITHMES & EXPONENTIELLE ---
        elif choix == 4:
            console.print("\n[bold cyan] Options Logarithmiques :[/bold cyan]")
            console.print("1. Logarithme Népérien (Ln)")
            console.print("2. Logarithme Décimal (Log10)")
            console.print("3. Exponentielle (Exp)")
            choix_log = lire_choix(3)
            
            num = lire_nombre("Entrez le nombre : ")
            log_map = {1: ("ln", "Ln"), 2: ("log", "Log10"), 3: ("exp", "Exp")}
            cle_log, label_log = log_map[choix_log]
            
            resultat = calculer_log(num, cle_log)
            if resultat is not None:
                res_arrondi = round(resultat, DECIMALES)
                ligne_calcul = f"{label_log}({num}) = {res_arrondi}"
                nom_explication = "exponentielle" if cle_log == "exp" else "logarithme"
                arguments_explication = (num, cle_log)

        # --- ENREGISTREMENT ET AFFICHAGE PÉDAGOGIQUE ---
        if resultat is not None:
            # Affichage de notre magnifique encadré vert de résultat
            afficher_resultat("Calcul Scientifique", ligne_calcul.split(" = ")[0], res_arrondi)
            
            # Sauvegarde dans l'historique global stylisé
            HISTORIQUE.append(f"[cyan]{ligne_calcul.split(' = ')[0]}[/cyan] = [bold green]{res_arrondi}[/bold green]")
            
            # Déclenchement de l'explication si activée
            if MODE_PEDAGOGIQUE and nom_explication != "":
                expliquer_operation(nom_explication, *arguments_explication, resultat=res_arrondi)
                
        input("\nAppuyez sur Entrée pour continuer...")

#MENU QUIZ 

def lancer_quiz_capacites():
    """
    Génère un examen de passage couvrant l'ensemble des fonctionnalités de la calculatrice.
    Fournit un score final, un diagnostic précis et des corrections dynamiques adaptatives.
    """
    global DECIMALES
    afficher_titre("Examen de Capacités - ASC")
    
    console.print("[bold yellow]Préparez-vous ![/bold yellow] Vous allez être testé sur [bold cyan]5 notions mathématiques[/bold cyan] de la calculatrice.")
    console.print("[dim]En cas d'erreur, le tuteur de l'Académie vous expliquera votre faute théorique.[/dim]\n")
    
    score = 0
    total_questions = 5
    
    # Notre pool complet de catégories d'opérations
    categories = ["arithmetique", "modulo", "puissance", "racine", "factorielle", "trigo", "logarithme"]
    # Sélection aléatoire de 5 catégories uniques pour ce quiz
    selection_questions = random.sample(categories, k=total_questions)
    
    for i, cat in enumerate(selection_questions, 1):
        console.print(f"\n[bold cyan] Question {i}/{total_questions} : Catégorie [{cat.upper()}][/bold cyan]")
        console.print("─" * 50)
        
        reponse_correcte = None
        instruction = ""
        
        # --- GÉNÉRATION DYNAMIQUE DES QUESTIONS ---
        if cat == "arithmetique":
            a = random.randint(15, 45)
            b = random.randint(5, 15)
            op = random.choice(["+", "-", "*"])
            if op == "+":
                reponse_correcte = a + b
            elif op == "-":
                reponse_correcte = a - b
            else:
                reponse_correcte = a * b
            instruction = f"Résolvez de tête : [bold white]{a} {op} {b}[/bold white]"
            
        elif cat == "modulo":
            a = random.randint(13, 25)
            b = random.randint(3, 5)
            reponse_correcte = a % b
            instruction = f"Quel est le reste de la division (modulo) de {a} par {b} ? [dim](Noté {a} % {b})[/dim]"
            
        elif cat == "puissance":
            a = random.choice([2, 3, 5])
            b = random.choice([2, 3])
            reponse_correcte = a ** b
            instruction = f"Calculez [bold white]{a}[/bold white] élevé à la puissance [bold white]{b}[/bold white] [dim](Noté {a}^{b})[/dim]"
            
        elif cat == "racine":
            a = random.choice([16, 25, 36, 64, 81, 100])
            reponse_correcte = int(math.sqrt(a))
            instruction = f"Trouvez la racine carrée exacte de [bold white]{a}[/bold white] [dim](√{a})[/dim]"
            
        elif cat == "factorielle":
            a = random.randint(3, 5)
            reponse_correcte = math.factorial(a)
            instruction = f"Calculez la factorielle de [bold white]{a}[/bold white] [dim](Noté {a}!)[/dim]"
            
        elif cat == "trigo":
            console.print("Quelle fonction trigonométrique mesure le rapport géométrique entre la [bold cyan]Hauteur d'élévation opposée[/bold cyan] et l'Hypoténuse d'un triangle rectangle ?")
            console.print("1. Le Sinus (Sin)")
            console.print("2. Le Cosinus (Cos)")
            console.print("3. La Tangente (Tan)")
            reponse_correcte = 1
            
        elif cat == "logarithme":
            console.print("Sur une échelle logarithmique de base 10 (comme l'échelle de Richter pour les séismes), si une intensité augmente de [bold cyan]+1 point[/bold cyan], l'énergie physique réelle est multipliée par :")
            console.print("1. 2 fois plus")
            console.print("2. 10 fois plus")
            console.print("3. 100 fois plus")
            reponse_correcte = 2

        # --- SAISIE ET VALIDATION ---
        if cat in ["trigo", "logarithme"]:
            choix_user = lire_choix(3)
            reponse_user = choix_user
        else:
            console.print(instruction)
            reponse_user = lire_nombre("Votre réponse : ")
            
        # --- DIAGNOSTIC ET CORRECTION AUTOMATIQUE ---
        if reponse_user == reponse_correcte:
            console.print("\n [bold green]Excellent ! C'est une réponse parfaite.[/bold green]")
            score += 1
        else:
            console.print(f"\n [bold red]Ce n'est pas tout à fait ça.[/bold red] La bonne réponse était [bold green]{reponse_correcte}[/bold green].")
            
            # Diagnostic intelligent de l'erreur
            if cat == "puissance" and reponse_user == a * b:
                console.print("\n [bold orange3]Alerte Diagnostic :[/bold orange3] Vous avez multiplié la base par l'exposant (a x b).")
            elif cat == "modulo":
                console.print("\n [bold orange3]Alerte Diagnostic :[/bold orange3] Rappelez-vous que le modulo cherche ce qu'il RESTE, pas le résultat de la division.")
                
            # Appel dynamique de l'assistant pédagogique via notre dictionnaire d'explications !
            if cat == "modulo":
                expliquer_operation("modulo", a, b, resultat=reponse_correcte)
            elif cat == "puissance":
                expliquer_operation("puissance", a, b, resultat=reponse_correcte)
            elif cat == "racine":
                expliquer_operation("racine_carree", a, resultat=reponse_correcte)
            elif cat == "factorielle":
                expliquer_operation("factorielle", a, resultat=reponse_correcte)
            elif cat == "trigo":
                expliquer_operation("trigo", 45, "sin", 0.707)  # Exemple pédagogique pour illustrer le sinus
            elif cat == "logarithme":
                console.print("\n [bold gold3]Règle des Logarithmes :[/bold gold3] Une échelle logarithmique transforme les multiplications en additions. Chaque pas linéaire de +1 représente en réalité une multiplication par la base (ici, x10).")

        console.print("\n" + "═" * 50)
        input("Appuyez sur Entrée pour passer à la suite...")

    # ==========================================
    #  BILAN ET NOTATION DE L'ACADÉMIE
    # ==========================================
    afficher_titre("Résultat de l'Évaluation")
    pourcentage = (score / total_questions) * 100
    
    # Détermination du statut de capacité
    if score == 5:
        statut = "[bold gold3] EXPERT SCIENTIFIQUE (100%)[/bold gold3]"
        message = "Impressionnant ! Vous avez démontré une maîtrise absolue de toutes les opérations mathématiques de la console."
    elif score >= 3:
        statut = "[bold green] PRATICIEN AVANCÉ[/bold green]"
        message = "Très bonne performance. Vos compétences de calcul sont solides, continuez ainsi !"
    else:
        statut = "[bold red] APPRENTI[/bold red]"
        message = "Certains concepts méritent d'être revus. Activez le 'Mode Pédagogique' lors de vos prochains calculs pour vous entraîner."

    console.print(f"Votre Score Final : [bold cyan]{score}/{total_questions}[/bold cyan] ({pourcentage}%)")
    console.print(f"Votre Niveau : {statut}")
    console.print(f"\n[dim]{message}[/dim]")
    
    input("\nAppuyez sur Entrée pour retourner au menu principal...")

# ==============================================================================
# SEXTION : 8 PARAMÈTRES : INTERFACE DE MISE À JOUR DYNAMIQUE DES CONFIGURATIONS
# Gestion des bascules d'état de la session (Précision d'affichage et Mode Pédagogique).
# ==============================================================================


def gerer_parametres():
    """
    Interface de mise à jour dynamique des configurations de l'application.
    
    LOGIQUE DU CODE :
    1. Lecture en boucle pour maintenir l'utilisateur dans l'écran des paramètres.
    2. Injection des variables globales (DECIMALES, MODE_PEDAGOGIQUE) via le mot-clé 'global'.
    3. Rendu visuel adaptatif (Vert si activé, Rouge si désactivé) avec Rich.
    4. Saisie sécurisée et contrôle des limites de la précision (chiffre entier de 0 à 9).
    """
    global DECIMALES, MODE_PEDAGOGIQUE
    dans_parametres = True
    
    while dans_parametres:
        afficher_titre("Paramètres de Session")
        
        # Affichage des statuts actuels avec du style et des couleurs
        statut_pedago = "[bold green]ACTIVÉ[/bold green]" if MODE_PEDAGOGIQUE else "[bold red]DÉSACTIVÉ[/bold red]"
        
        console.print(f"1. Modifier la précision d'affichage [dim](Actuel : {DECIMALES} décimales)[/dim]")
        console.print(f"2. Mode Pédagogique [dim](Actuel : {statut_pedago})[/dim]")
        console.print("3. Retour au menu principal")
        
        choix = lire_choix(3)
        
        if choix == 1:
            console.print("\n[bold cyan]🔧 Configuration de la précision[/bold cyan]")
            # Nous utilisons une saisie sécurisée directe de 0 à 9 sans décalage d'index (-1)
            while True:
                nb = lire_nombre("Combien de décimales souhaitez-vous afficher (0-9) ? : ")
                if nb.is_integer() and 0 <= int(nb) <= 9:
                    DECIMALES = int(nb)
                    break
                else:
                    console.print(" [bold orange3]Saisie invalide ![/bold orange3] Veuillez entrer un nombre entier entre [bold]0 et 9[/bold].")
            
            console.print(f"\n✔ [bold green]Configuration modifiée :[/bold green] Les résultats seront arrondis à [bold yellow]{DECIMALES}[/bold yellow] décimales.")
            input("\nAppuyez sur Entrée pour continuer...")
            
        elif choix == 2:
            # Inversion simple du booléen
            MODE_PEDAGOGIQUE = not MODE_PEDAGOGIQUE
            nouveau_statut = "[bold green]Activé[/bold green]" if MODE_PEDAGOGIQUE else "[bold red]Désactivé[/bold red]"
            
            console.print(f"\n[bold green]Configuration modifiée :[/bold green] Mode d'explication théorique {nouveau_statut}.")
            input("\nAppuyez sur Entrée pour continuer...")
            
        elif choix == 3:
            dans_parametres = False
# ==============================================================================
# SECTION 9 : POINT D'ENTRÉE ET HUB PRINCIPAL DE L'APPLICATION
# Orchestration de la boucle maîtresse continue et gestion de sortie sécurisée.
# ==============================================================================

def afficher_menu_principal():
    """Génère l'affichage textuel stylisé du hub principal avec Rich."""
    # Titre général du programme
    afficher_titre("AKIENI Scientific Calculator (ASC)")
    
    # Présentation du menu sous forme de liste élégante et colorée
    console.print("[bold cyan]🔹 MENU PRINCIPAL 🔹[/bold cyan]\n", justify="center")
    console.print("  [bold yellow]1.[/bold yellow] Calculs de Base [dim](Arithmétique)[/dim]")
    console.print("  [bold yellow]2.[/bold yellow] Fonctions Avancées & Scientifiques [dim](Analyse & Trigo)[/dim]")
    console.print("  [bold yellow]3.[/bold yellow] Gestion de la Mémoire [dim](M+, M-, MR, MC)[/dim]")
    console.print("  [bold yellow]4.[/bold yellow] Afficher l'Historique de Session")
    console.print("  [bold yellow]5.[/bold yellow] Paramètres de l'Application [dim](Précision & Pédagogie)[/dim]")
    console.print("  [bold yellow]6.[/bold yellow] Le Savoir de l'Académie [dim](Lexique vulgarisé)[/dim]")
    console.print("  [bold yellow]7.[/bold yellow] Test de Capacités [bold green](Quiz Interactif)[/bold green]")
    console.print("  [bold yellow]8.[/bold yellow] Quitter le programme")
    console.print()

def main():
    """Boucle maîtresse appliquant la logique d'exécution continue de la session."""
    continuer = True
    
    # Message de bienvenue de l'Académie
    console.print("\n[bold green] Initialisation du moteur ASC réussie ![/bold green]")
    console.print("[dim]Bienvenue dans l'environnement d'apprentissage de l'Akieni Academy.[/dim]\n")
    
    while continuer:
        afficher_menu_principal()
        
        # Prise en charge des 8 options désormais disponibles
        choix = lire_choix(8)
        
        if choix == 1:
            sous_menu_calculs_base()
        elif choix == 2:
            sous_menu_calculs_avances()
        elif choix == 3:
            gerer_memoire()  # La fonction qui modifie ou consulte la variable globale MEMOIRE
        elif choix == 4:
            afficher_historique()  # Affiche la liste HISTORIQUE sous forme de journal
        elif choix == 5:
            gerer_parametres()  # Modifie DECIMALES ou MODE_PEDAGOGIQUE
        elif choix == 6:
            dictionnaire_pedagogique()  # Ouvre le Lexique
        elif choix == 7:
            lancer_quiz_capacites()  # Lance le grand examen à 5 questions !
        elif choix == 8:
            console.print("\n[bold orange3] Confirmation :[/bold orange3] Êtes-vous sûr de vouloir quitter ?")
            console.print(" 1. [bold green]Oui[/bold green], fermer la session")
            console.print(" 2. [bold red]Non[/bold red], rester sur la console")
            
            confirmation = lire_choix(2)
            if confirmation == 1:
                continuer = False
                
    # Message de sortie propre et chaleureux
    console.print("\n[bold cyan] Au revoir et merci d'avoir utilisé ASC ! À bientôt à l'Académie ![/bold cyan]\n")

if __name__ == "__main__":
    main()