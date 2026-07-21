def calculer_statistiques_classe(liste_eleves: list) -> dict:
    """
    Calcule les métriques clés d'une classe donnée.
    """
    total = len(liste_eleves)
    if total == 0:
        return {}
    # 1. Calcul de la moyenne ENAFEP
    somme_notes = sum(e['score_enafep'] for e in liste_eleves)
    moyenne_enafep = round(somme_notes / total,2)

    # 2. Ratio Sexe (Filles / Garçons)
    filles = sum(1 for e in liste_eleves if e['sexe']=='F')
    garcons = total - filles
    pct_filles = round((filles / total) * 100, 1)

    # 3. Proportion de redoublants
    redoublants = sum(1 for e in liste_eleves if e["statut"]=="Redoublant")
    pct_redoublants = round((redoublants / total) * 100, 1)
    # 4. Élèves à besoins particuliers
    besoins_speciaux = sum(1 for e in liste_eleves if e["besoin_particulier"])
    
    return {
        "total": total,
        "moyenne_enafep": moyenne_enafep,
        "pct_filles": pct_filles,
        "pct_garcons": round(100 - pct_filles, 1),
        "pct_redoublants": pct_redoublants,
        "besoins_speciaux": besoins_speciaux
    }
def afficher_dashboard_diagnostic(classes_reparties: dict):
    """
    Affiche un rapport clair et lisible dans la console pour valider l'équilibre.
    """
    print("\n" + "=" * 70)
    print(" DASHBOARD DE DIAGNOSTIC PÉDAGOGIQUE - CHAGUA SCHOOL ALLOCATOR")
    print("=" * 70)

    for nom_classe, liste_eleves in classes_reparties.items():
        stats = calculer_statistiques_classe(liste_eleves)
        print(f"\n [{nom_classe}] - Effectif: {stats['total']} élèves")
        print(f"   ├─ Moyenne ENAFEP   : {stats['moyenne_enafep']} %")
        print(f"   ├─ Parité F/M       : {stats['pct_filles']}% Filles | {stats['pct_garcons']}% Garçons")
        print(f"   ├─ Redoublants      : {stats['pct_redoublants']}%")
        print(f"   └─ Besoins Spéciaux : {stats['besoins_speciaux']} élève(s)")

    print("\n" + "=" * 70)

