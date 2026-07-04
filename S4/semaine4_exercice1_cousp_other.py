from rich import print
from rich.console import Console

console = Console()

# ==========================================================
# VARIABLES D'ACCUMULATEURS
# ==========================================================
total_suspects = 0
total_confirmes = 0
total_deces = 0
total_actifs = 0

zones_vertes = 0
zones_jaunes = 0
zones_oranges = 0
zones_rouges = 0

nb_districts = 9

console.print("\n[bold cyan]===== SURVEILLANCE NATIONALE MPOX =====[/bold cyan]\n")

# ==========================================================
# BOUCLE SUR LES DISTRICTS
# ==========================================================
for i in range(1, nb_districts + 1):

    console.print(f"\n[bold blue]---------- DISTRICT {i} ----------[/bold blue]")

    nom_district = input("Nom du district : ")
    suspects = int(input("Cas suspects : "))
    confirmes = int(input("Cas confirmés : "))
    deces = int(input("Décès : "))

    # ======================================================
    # CALCUL DES CAS ACTIFS
    # ======================================================
    cas_actifs = confirmes - deces

    # ======================================================
    # CALCUL DE LA LÉTALITÉ
    # ======================================================
    if confirmes > 0:
        letalite = (deces / confirmes) * 100
    else:
        letalite = 0

    # ======================================================
    # CLASSIFICATION DU NIVEAU D'ALERTE
    # ======================================================
    if confirmes >= 10:
        alerte = "ROUGE"
        couleur = "bold red"
        zones_rouges += 1

    elif confirmes >= 5:
        alerte = "ORANGE"
        couleur = "bold dark_orange"

        zones_oranges += 1

    elif confirmes >= 2:
        alerte = "JAUNE"
        couleur = "bold yellow"
        zones_jaunes += 1

    else:
        alerte = "VERT"
        couleur = "bold green"
        zones_vertes += 1

    # ======================================================
    # MISE À JOUR DES CUMULATIFS
    # ======================================================
    total_suspects += suspects
    total_confirmes += confirmes
    total_deces += deces
    total_actifs += cas_actifs

    # ======================================================
    # AFFICHAGE PAR DISTRICT
    # ======================================================
    console.print(f"[bold]District :[/bold] {nom_district}")

    console.print(f"[bold]Alerte :[/bold] [{couleur}]{alerte}[/{couleur}]")

    console.print(f"[cyan]Cas actifs :[/cyan] {cas_actifs}")

    console.print(f"[magenta]Létalité :[/magenta] {letalite:.1f}%")

console.print("\n")
console.print("[bold cyan]========================================[/bold cyan]")
console.print("[bold white on blue] RAPPORT NATIONAL MPOX 2025 [/bold white on blue]")
console.print("[bold cyan]========================================[/bold cyan]")

console.print(f"[green]Districts analysés :[/green] {nb_districts}")

console.print(f"[yellow]Total suspects :[/yellow] {total_suspects}")

console.print(f"[red]Total confirmés :[/red] {total_confirmes}")

console.print(f"[bold red]Total décès :[/bold red] {total_deces}")

console.print(f"[cyan]Total cas actifs :[/cyan] {total_actifs}")

console.print()

console.print(f"[bold green]Zones VERTES :[/bold green] {zones_vertes}")

console.print(f"[bold yellow]Zones JAUNES :[/bold yellow] {zones_jaunes}")

console.print(f"[bold dark_orange]Zones ORANGES :[/bold dark_orange] {zones_oranges}")

console.print(f"[bold red]Zones ROUGES :[/bold red] {zones_rouges}")

console.print("[bold cyan]========================================[/bold cyan]")