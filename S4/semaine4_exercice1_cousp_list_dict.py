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

nb_districts = 2
liste_departements = []

# ==========================================================
# BOUCLE SUR LES DISTRICTS
# ==========================================================
for i in range(0, nb_districts):
    print('--- District', i+1, '---')
    #creation et validation des donnees 

    while True:
        nom_district = input('Nom du district : ')
        nom_district = nom_district.strip()
        if  len(nom_district) <= 2 and not(nom_district.isdigit()):
            print("Le nom du district doit avoir au moins 3 caracteres")
        else:
            break
    while True:
        departement = input('Nom du departement : ')
        departement = departement.strip()
        if  len(departement) <= 2 and not(departement.isdigit()):
            print("Le nom du departement doit avoir au moins 3 caracteres et ne doit pas etre ex:123")
        else:
            break
    while True:
        suspect = input('cas suspect')
        if not suspect.isdigit():
            print("Seul les nombres entiers sont prises en charge")
        else:
            suspect = int(suspect)
            break
    while True:
        confirmes = input('Cas confirmes : ')
        if not confirmes.isdigit():
            print("Seul les nombres entiers sont prises en charge")
        else:
            confirmes = int(confirmes)
            break
    while True:
        deces = input('Deces : ')
        if not deces.isdigit():
            print("Seul les nombres entiers sont prises en charge")
        else:
            deces = int(deces)
            break
    #   Creation d'une dictionnaire des infos
    dict_informations = {
        'nom_district':nom_district,
        'cas_suspects':suspects,
        'departement':departement,
        'cas_confirmes':confirmes,
        'deces':deces
    }
    liste_departements.append(dict_informations)

    # ======================================================
    # CALCUL DES CAS ACTIFS
    # ======================================================

#     # ======================================================
#     # CALCUL DE LA LETALITE
#     # ======================================================
#     if confirmes > 0:
#         letalite = (deces / confirmes) * 100
#     else:
#         letalite = 0

#     # ======================================================
#     # CLASSIFICATION DU NIVEAU D'ALERTE
#     # ======================================================
#     if confirmes >= 10:
#         alerte = 'ROUGE'
#         zones_rouges = zones_rouges + 1

#     elif confirmes >= 5:
#         alerte = 'ORANGE'
#         zones_oranges = zones_oranges + 1

#     elif confirmes >= 2:
#         alerte = 'JAUNE'
#         zones_jaunes = zones_jaunes + 1


#     else:
#         alerte = 'VERT'
#         zones_vertes = zones_vertes + 1

#     # ======================================================
#     # MISE A JOUR DES CUMULATIFS
#     # ======================================================
#     total_suspects = total_suspects + suspects
#     total_confirmes = total_confirmes + confirmes
#     total_deces = total_deces + deces
#     total_actifs = total_actifs + cas_actifs

#     # ======================================================
#     # AFFICHAGE PAR DISTRICT
#     # ======================================================
#     print(' Alerte :', alerte)
#     print(' Actifs :', cas_actifs)
#     print(' Letalite :', round(letalite, 1), '%')
#     print()
# #============ fin =========================
# # ==========================================================
# # RAPPORT NATIONAL
# # ==========================================================
# print('=======================================')
# print(' RAPPORT NATIONAL MPOX 2025 ')
# print('=======================================')

# print('Districts analyses :', nb_districts)
# print('Total suspects :', total_suspects)
# print('Total confirmes :', total_confirmes)
# print('Total deces :', total_deces)
# print('Total cas actifs :', total_actifs)

# print('Zones VERTES :', zones_vertes)
# print('Zones JAUNES :', zones_jaunes)
# print('Zones ORANGES :', zones_oranges)
# print('Zones ROUGES :', zones_rouges)

# print('=======================================')
