# ============================================================

# MODULE FONDATEUR — Projet Santé Publique / Akieni Academy

# Ce fichier centralise toutes les constantes et variables métier.

# Il sera enrichi chaque semaine jusqu'à la S24.

# ============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========

TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3

# Seuil OMS : nombre de médecins pour 1 000 habitants

SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # Pourcentage minimum recommandé par l'OMS
SEUIL_MORTALITE_ALERTE = 2.0        # Taux d'alerte : % de décès par rapport aux hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30      # Nombre de jours minimum de stock de sécurité à maintenir
DEPARTEMENTS_CONGO = [              # Les 12 départements officiels de la République du Congo
'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
'Niari', 'Plateaux', 'Pool', 'Sangha'
]
#============================================================

# DONNÉES DE COUVERTURE VACCINALE PAR DÉPARTEMENT

#===========================================================
#============ Département de Brazzaville ==================
departement_1 = 'Brazzaville'
population_cible_1 = 450_000
personnes_vaccinees_1 = 418_500

#============ Département de Pointe-Noire ==================
departement_2 = 'Pointe-Noire'
population_cible_2 = 280_000
personnes_vaccinees_2 = 229_600

#============ Département de Pool ====================
departement_3 = 'Pool'
population_cible_3 = 120_000
personnes_vaccinees_3 = 54_000

#============ Département de Sangha ===================
departement_4 = 'Sangha'
population_cible_4 = 85_000
personnes_vaccinees_4 = 35_700

#================== FIN DES DONNÉES DE VACCINATION ==========

# === SECTION B : VARIABLES DES 5 HÔPITAUX ===================

# ==========================================

# DÉCLARATION DES 5 HÔPITAUX

# ==========================================

# Hôpital 1 — CHU de Brazzaville

h1_nom              = 'CHU de Brazzaville'
h1_ville            = 'Brazzaville'
h1_departement      = 'Brazzaville'
h1_type             = 'CHU'
h1_nb_lits          = 320
h1_nb_lits_occupes  = 284
h1_nb_medecins      = 47
h1_nb_infirmiers    = 123
h1_population_zone  = 1_800_000

# Hôpital 2 - Hôpital Général Pointe-Noire

h2_nom              = 'Hopital General Pointe-Noire'
h2_ville            = 'Pointe-Noire'
h2_departement      = 'Pointe-Noire'
h2_type             = 'Hopital General'
h2_nb_lits          = 220
h2_nb_lits_occupes  = 175
h2_nb_medecins      = 32
h2_nb_infirmiers    = 85
h2_population_zone  = 1_200_000

# Hôpital 3 - Hôpital de Dolisie

h3_nom              = 'Hopital de Dolisie'
h3_ville            = 'Dolisie'
h3_departement      = 'Niari'
h3_type             = 'Hopital de reference'
h3_nb_lits          = 110
h3_nb_lits_occupes  = 65
h3_nb_medecins      = 12
h3_nb_infirmiers    = 42
h3_population_zone  = 180_000

# Hôpital 4 - Hôpital de district Owando

h4_nom              = 'Hopital de district Owando'
h4_ville            = 'Owando'
h4_departement      = 'Cuvette'
h4_type             = 'Hopital de district'
h4_nb_lits          = 75
h4_nb_lits_occupes  = 40
h4_nb_medecins      = 6
h4_nb_infirmiers    = 28
h4_population_zone  = 90_000

# Hôpital 5 - Centre de santé d'Impfondo

h5_nom              = 'Centre de sante de Impfondo'
h5_ville            = 'Impfondo'
h5_departement      = 'Likouala'
h5_type             = 'CSI'
h5_nb_lits          = 30
h5_nb_lits_occupes  = 18
h5_nb_medecins      = 2
h5_nb_infirmiers    = 14
h5_population_zone  = 45_000

# === SECTION C : VARIABLES DES 5 MÉDICAMENTS ================

# TODO : Déclarer les 5 médicaments essentiels

# ==========================================

# DÉCLARATION DES 5 MÉDICAMENTS ESSENTIELS

# ==========================================

# Médicament 1 : Artéméther-luméfantrine (Antipaludique)

m1_nom            = 'Artemether-Lumefantrine'
m1_stock          = 3200
m1_seuil_rupture  = 2000
m1_cout_unitaire  = 3500.0   # En FCFA

# Médicament 2 : Amoxicilline (Antibiotique)

m2_nom            = 'Amoxicilline 500mg'
m2_stock          = 950
m2_seuil_rupture  = 800
m2_cout_unitaire  = 850.0

# Médicament 3 : Paracétamol (Analgésique / Antipyrétique)

m3_nom            = 'Paracetamol 500mg'
m3_stock          = 12400
m3_seuil_rupture  = 3000
m3_cout_unitaire  = 120.0

# Médicament 4 : SRO (Sels de Réhydratation Orale)

m4_nom            = 'SRO (sachets)'
m4_stock          = 4200
m4_seuil_rupture  = 5000
m4_cout_unitaire  = 125.0

# Médicament 5 : Vaccin antipaludique

m5_nom            = 'Vaccin DTP-HepB-Hib'
m5_stock          = 820
m5_seuil_rupture  = 1000
m5_cout_unitaire  = 8500.0

# === SECTION D : CALCULS D'INITIALISATION ===================

# 1. Agrégation des données des hôpitaux

total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

# 2. Calcul des indicateurs clés (KPI) hospitaliers

taux_occupation_global = (total_lits_occupes / total_lits) * 100
densite_medicale_globale = (total_medecins / total_population) * 1000

# 3. Calcul des indicateurs clés (KPI) des médicaments

valeur_stock_usd = (
(m1_stock * m1_cout_unitaire) +
(m2_stock * m2_cout_unitaire) +
(m3_stock * m3_cout_unitaire) +
(m4_stock * m4_cout_unitaire) +
(m5_stock * m5_cout_unitaire)
)
valeur_stock_fcfa = valeur_stock_usd * TAUX_USD_FCFA # Attention à la petite faute de frappe dans votre variable 'TAUX_USD_FCFA'

# Compteur d'alertes pour les ruptures de stock

alertes_rupture = 0
if m1_stock <= m1_seuil_rupture: alertes_rupture += 1
if m2_stock <= m2_seuil_rupture: alertes_rupture += 1
if m3_stock <= m3_seuil_rupture: alertes_rupture += 1
if m4_stock <= m4_seuil_rupture: alertes_rupture += 1
if m5_stock <= m5_seuil_rupture: alertes_rupture += 1

# === SECTION E : RAPPORT D'INVENTAIRE =======================

#===SECTION F : CLASSIFICATION STATUT STOCKS (NEW S3) (if/elif/else)

# RÈGLES DE GESTION — STOCK DES MÉDICAMENTS :

# Si stock <= seuil_rupture => STATUT : RUPTURE CRITIQUE (alerte immédiate PNA)

# Si stock <= seuil_rupture * 1.5 => STATUT : ALERTE STOCK (commande urgente à déclencher)

# Si stock <= seuil_rupture * 2 => STATUT : STOCK LIMITE (surveillance renforcée)

# Sinon => STATUT : STOCK NORMAL

# Médicament 1

if m1_stock <= m1_seuil_rupture:
     m1_statut, m1_couleur, m1_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immédiate PNA — commande express sous 24h'
elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut, m1_couleur, m1_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente à déclencher sous 72h'
elif m1_stock <= m1_seuil_rupture * 2.0:
     m1_statut, m1_couleur, m1_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcée — planifier une commande'
else:
     m1_statut, m1_couleur, m1_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 2

if m2_stock <= m2_seuil_rupture:
    m2_statut, m2_couleur, m2_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immédiate PNA — commande express sous 24h'
elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut,m2_couleur , m2_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente à déclencher sous 72h'
elif m2_stock <= m2_seuil_rupture * 2.0:
    m2_statut, m2_couleur, m2_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcée — planifier une commande'
else:
    m2_statut, m2_couleur, m2_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 3

if m3_stock <= m3_seuil_rupture:
    m3_statut, m3_couleur, m3_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immédiate PNA — commande express sous 24h'
elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut,m3_couleur , m3_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente à déclencher sous 72h'
elif m3_stock <= m3_seuil_rupture * 2.0:
    m3_statut, m3_couleur, m3_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcée — planifier une commande'
else:
    m3_statut, m3_couleur, m3_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 4

if m4_stock <= m4_seuil_rupture:
    m4_statut, m4_couleur, m4_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immédiate PNA — commande express sous 24h'
elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut,m4_couleur , m4_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente à déclencher sous 72h'
elif m4_stock <= m4_seuil_rupture * 2.0:
    m4_statut, m4_couleur, m4_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcée — planifier une commande'
else:
    m4_stock, m4_couleur, m4_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# Médicament 5

if m5_stock <= m5_seuil_rupture:
    m5_statut, m5_couleur, m5_action = 'RUPTURE CRITIQUE', '[ROUGE]', 'Alerte immédiate PNA — commande express sous 24h'
elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut,m5_couleur , m5_action = 'ALERTE STOCK', '[ORANGE]', 'Commande urgente à déclencher sous 72h'
elif m5_stock <= m5_seuil_rupture * 2.0:
    m5_statut, m5_couleur, m5_action = 'STOCK LIMITE', '[JAUNE]', 'Surveillance renforcée — planifier une commande'
else:
    m5_statut, m5_couleur, m5_action = 'STOCK NORMAL', '[VERT]', 'Situation normale — suivi standard'

# 1. Initialisation des compteurs et des chaînes de caractères de résumé

nb_ruptures_critiques = 0
nb_alertes_stock     = 0
nb_stock_limites      = 0
nb_stock_normaux      = 0

nom_med_critique      = ""
nom_med_alerte_stock  = ""
nom_med_stock_limite  = ""
nom_med_stock_normaux= ""

# Comptage et agrégation pour le Médicament 1

if m1_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques += 1; nom_med_critique += m1_nom + ", "
elif m1_statut == 'ALERTE STOCK': nb_alertes_stock += 1; nom_med_alerte_stock += m1_nom + ", "
elif m1_statut == 'STOCK LIMITE': nb_stock_limites += 1; nom_med_stock_limite += m1_nom + ", "
elif m1_statut == 'STOCK NORMAL': nb_stock_normaux += 1; nom_med_stock_normaux += m1_nom + ", "

# Comptage et agrégation pour le Médicament 2

if m2_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques += 1; nom_med_critique += m2_nom + ", "
elif m2_statut == 'ALERTE STOCK': nb_alertes_stock += 1; nom_med_alerte_stock += m2_nom + ", "
elif m2_statut == 'STOCK LIMITE': nb_stock_limites += 1; nom_med_stock_limite += m2_nom + ", "
elif m2_statut == 'STOCK NORMAL': nb_stock_normaux += 1; nom_med_stock_normaux += m2_nom + ", "

# Comptage et agrégation pour le Médicament 3

if m3_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques += 1; nom_med_critique += m3_nom + ", "
elif m3_statut == 'ALERTE STOCK': nb_alertes_stock += 1; nom_med_alerte_stock += m3_nom + ", "
elif m3_statut == 'STOCK LIMITE': nb_stock_limites += 1; nom_med_stock_limite += m3_nom + ", "
elif m3_statut == 'STOCK NORMAL': nb_stock_normaux += 1; nom_med_stock_normaux += m3_nom + ", "

# Comptage et agrégation pour le Médicament 4

if m4_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques += 1; nom_med_critique += m4_nom + ", "
elif m4_statut == 'ALERTE STOCK': nb_alertes_stock += 1; nom_med_alerte_stock += m4_nom + ", "
elif m4_statut == 'STOCK LIMITE': nb_stock_limites += 1; nom_med_stock_limite += m4_nom + ", "
elif m4_statut == 'STOCK NORMAL': nb_stock_normaux += 1; nom_med_stock_normaux += m4_nom + ", "

# Comptage et agrégation pour le Médicament 5

if m5_statut == 'RUPTURE CRITIQUE': nb_ruptures_critiques += 1; nom_med_critique += m5_nom + ", "
elif m5_statut == 'ALERTE STOCK': nb_alertes_stock += 1; nom_med_alerte_stock += m5_nom + ", "
elif m5_statut == 'STOCK LIMITE': nb_stock_limites += 1; nom_med_stock_limite += m5_nom + ", "
elif m5_statut == 'STOCK NORMAL': nb_stock_normaux += 1; nom_med_stock_normaux += m5_nom + ", "

#====SECTION G : CLASSIFICATION OCCUPATION HOPITAUX (NEW S3) (if/elif/else) =========

# 1. CALCUL DES INDICATEURS CLÉS (KPI) POUR CHAQUE ÉTABLISSEMENT

# Hôpital 1 — CHU de Brazzaville

taux_occupation_h1 = (h1_nb_lits_occupes / h1_nb_lits) * 100
densite_medicale_h1 = (h1_nb_medecins / h1_population_zone) * 1000

# Hôpital 2 — Hôpital Général Pointe-Noire

taux_occupation_h2 = round(((h2_nb_lits_occupes / h2_nb_lits) * 100),2)
densite_medicale_h2 = (h2_nb_medecins / h2_population_zone) * 1000

# Hôpital 3 — Hôpital de Dolisie

taux_occupation_h3 = round(((h3_nb_lits_occupes / h3_nb_lits) * 100),2)
densite_medicale_h3 = (h3_nb_medecins / h3_population_zone) * 1000

# Hôpital 4 — Hôpital de district Owando

taux_occupation_h4 = round(((h4_nb_lits_occupes / h4_nb_lits) * 100),2)
densite_medicale_h4 = (h4_nb_medecins / h4_population_zone) * 1000

# Hôpital 5 — CMS Impfondo

taux_occupation_h5 = (h5_nb_lits_occupes / h5_nb_lits) * 100
densite_medicale_h5 = (h5_nb_medecins / h5_population_zone) * 1000

# ===============================================================================================

# 2. CLASSIFICATION PRÉALABLE DES STATUTS D'OCCUPATION EN FONCTION DU TAUX D'OCCUPATION

# ================================================================================================

# RÈGLES DE GESTION — TAUX D'OCCUPATION DES LITS :

# Si taux > 95% => ALERTE CRITIQUE (saturation — transferts à organiser)

# Si taux > 85% => ALERTE ÉLEVÉE (capacité limite — renforcement prévu)

# Si taux > 70% => SITUATION OPTIMALE

# Sinon => SOUS-UTILISATION (ressources sous-exploitées)

# Hôpital 1 — CHU Brazzaville

if taux_occupation_h1 > 95:
    status_occ_h1,action_1 = '[ALERTE CRITIQUE]','saturation — transferts a organiser'
elif taux_occupation_h1 > 85:
    status_occ_h1,action_1 = '[ALERTE ELEVEE]','capacite limite — renforcement prevu'
elif taux_occupation_h1 > 70:
    status_occ_h1,action_1 = '[SITUATION OPTIMALE]','capacite optimale — stabilite'
else:
    status_occ_h1,action_1 = '[SOUS-UTILISATION]','ressources sous-exploitees'

# Hôpital 2 — Hôpital Pointe-Noire

if taux_occupation_h2 > 95:
    status_occ_h2,action_2 = '[ALERTE CRITIQUE]','saturation — transferts a organiser'
elif taux_occupation_h2 > 85:
    status_occ_h2,action_2 = '[ALERTE ELEVEE]','capacite limite — renforcement prevu'
elif taux_occupation_h2 > 70:
    status_occ_h2,action_2 = '[SITUATION OPTIMALE]','capacite optimale — stabilite'
else:
    status_occ_h2,action_2 = '[SOUS-UTILISATION]','ressources sous-exploitees'

# Hôpital 3 — Hôpital Dolisie

if taux_occupation_h3 > 95:
    status_occ_h3,action_3 = '[ALERTE CRITIQUE]','saturation — transferts a organiser'
elif taux_occupation_h3 > 85:
    status_occ_h3,action_3 = '[ALERTE ELEVEE]','capacite limite — renforcement prevu'
elif taux_occupation_h3 > 70:
    status_occ_h3,action_3 = '[SITUATION OPTIMALE]','capacite optimale — stabilite'
else:
    status_occ_h3,action_3 = '[SOUS-UTILISATION]','ressources sous-exploitees'

# Hôpital 4 — Hôpital Owando4

if taux_occupation_h4 > 95:
    status_occ_h4,action_4 = '[ALERTE CRITIQUE]','saturation — transferts a organiser'
elif taux_occupation_h4 > 85:
    status_occ_h4,action_4 = '[ALERTE ELEVEE]','capacite limite — renforcement prevu'
elif taux_occupation_h4 > 70:
    status_occ_h4,action_4 = '[SITUATION OPTIMALE]','capacite optimale — stabilite'
else:
    status_occ_h4,action_4 = '[SOUS-UTILISATION]','ressources sous-exploitees'

# Hôpital 5 — CMS Impfondo

if taux_occupation_h5 > 95:
    status_occ_h5,action_5 = '[ALERTE CRITIQUE]','saturation — transferts a organiser'
elif taux_occupation_h5 > 85:
    status_occ_h5,action_5 = '[ALERTE ELEVEE]','capacite limite — renforcement prevu'
elif taux_occupation_h5 > 70:
    status_occ_h5,action_5 = '[SITUATION OPTIMALE]','capacite optimale — stabilite'
else:
    status_occ_h5,action_5 = '[SOUS-UTILISATION]','ressources sous-exploitees'
#===SECTION H : CLASSIFICATION COUVERTURE VACCINALE (NEW S3) (if/elif/else)============================================

# 1. CALCUL DES TAUX DE VACCINATION POUR CHAQUE DÉPARTEMENT

# Département 1 — Brazzaville

taux_vaccination_d1 = (personnes_vaccinees_1 / population_cible_1) * 100

# Département 2 — Pointe-Noire

taux_vaccination_d2 = (personnes_vaccinees_2 / population_cible_2) * 100

# Département 3 — Pool

taux_vaccination_d3 = (personnes_vaccinees_3 / population_cible_3) * 100

# Département 4 — Sangha

taux_vaccination_d4 = (personnes_vaccinees_4 / population_cible_4) * 100

# ===========================================================================================

# 2. CLASSIFICATION PRÉALABLE DES STATUTS DE VACCINATION EN FONCTION DU TAUX DE VACCINATION

# ============================================================================================

# RÈGLE 4 — COUVERTURE VACCINALE PAR DÉPARTEMENT :

# Si taux < 50% => ZONE CRITIQUE (campagne d'urgence obligatoire)

# Si taux < 80% => ZONE À RISQUE (campagne renforcée requise)

# Si taux < 95% => ZONE INSUFFISANTE (objectif OMS non atteint)

# Sinon => ZONE OMS CONFORME

# Département 1 — Brazzaville

if taux_vaccination_d1 < 50:
    status_vac_h1,action_vac_1 = '[ZONE CRITIQUE]','campagne d\'urgence obligatoire'
elif taux_vaccination_d1 < 80:
    status_vac_h1,action_vac_1 = '[ZONE A RISQUE]','campagne renforcee requise'
elif taux_vaccination_d1 < 95:
    status_vac_h1,action_vac_1 = '[ZONE INSUFFISANTE]','objectif OMS non atteint'
else:
    status_vac_h1,action_vac_1 = '[ZONE OMS CONFORME]','zone sous controle conforme'

# Département 2 — Pointe-Noire

if taux_vaccination_d2 < 50:
    status_vac_h2,action_vac_2 = '[ZONE CRITIQUE]','campagne d\'urgence obligatoire'
elif not taux_vaccination_d2 < 80:
    status_vac_h2,action_vac_2 = '[ZONE A RISQUE]','campagne renforcee requise'
elif taux_vaccination_d2 < 95:  
    status_vac_h2,action_vac_2 = '[ZONE INSUFFISANTE]','objectif OMS non atteint'
else:
    status_vac_h2,action_vac_2 = '[ZONE OMS CONFORME]','zone sous controle conforme'

# Département 3 — Pool

if taux_vaccination_d3 < 50:
    status_vac_h3,action_vac_3 = '[ZONE CRITIQUE]','campagne d\'urgence obligatoire'
elif taux_vaccination_d3 < 80:
    status_vac_h3,action_vac_3 = '[ZONE A RISQUE]','campagne renforcee requise'
elif taux_vaccination_d3 < 95:
    status_vac_h3,action_vac_3 = '[ZONE INSUFFISANTE]','objectif OMS non atteint'
else:
    status_vac_h3,action_vac_3 = '[ZONE OMS CONFORME]','zone sous controle conforme'

# Département 4 — Sangha

if taux_vaccination_d4 < 50:
    status_vac_h4,action_vac_4 = '[ZONE CRITIQUE]','campagne d\'urgence obligatoire'
elif taux_vaccination_d4 < 80:
    status_vac_h4,action_vac_4 = '[ZONE A RISQUE]','campagne renforcee requise'
elif taux_vaccination_d4 < 95:
    status_vac_h4,action_vac_4 = '[ZONE INSUFFISANTE]','objectif OMS non atteint'
else:
    status_vac_h4,action_vac_4 = '[ZONE OMS CONFORME]','zone sous controle conforme'

#==== SECTION I : Rapport d'état global avec alertes (NEW S3) (compteurs + f-strings)

# S3 (Nouveau) : Les statuts et les indicateurs colorés sont déterminés par les conditions ci-dessus.

# TODO 1 : Rapport de la pharmacie

print('=' * 163)
print(f"{'':<44}\t{'TABLEAU DE BORD DU STOCK DE LA PHARMACIE NATIONALE D’APPROVISIONNEMENT (PNA)'}")
print('=' * 163)

# Les en-têtes du tableau de suivi des stocks de médicaments

print(f"{'Nom du médicament':<30}\t| {'Stock actuel':<5}\t| {'Seuil d’alerte':<5}\t| {'Statut du stock':<0}\t| {'Couleur':<5}\t| {'Action requise':<0}")
print('-' * 163)

# Affichage pour le Médicament 1

print(f"{m1_nom:<30}\t| {m1_stock:<10}unites\t| {m1_seuil_rupture:<7}unites\t| {m1_statut:<15}\t| {m1_couleur:<5}\t| {m1_action:<15}")
print('-' * 163)

# Affichage pour le Médicament 2

print(f"{m2_nom:<30}\t| {m2_stock:<10}unites\t| {m2_seuil_rupture:<7}unites\t| {m2_statut:<15}\t| {m2_couleur:<5}\t| {m2_action:<15}")
print('-' * 163)

print(f"{m3_nom:<30}\t| {m3_stock:<10}unites\t| {m3_seuil_rupture:<7}unites\t| {m3_statut:<15}\t| {m3_couleur:<5}\t| {m3_action:<15}")
print('-' * 163)

print(f"{m4_nom:<30}\t| {m4_stock:<10}unites\t| {m4_seuil_rupture:<7}unites\t| {m4_statut:<15}\t| {m4_couleur:<5}\t| {m4_action:<15}")
print('-' * 163)

print(f"{m5_nom:<30}\t| {m5_stock:<10}unites\t| {m5_seuil_rupture:<7}unites\t| {m5_statut:<15}\t| {m5_couleur:<5}\t| {m5_action:<15}")
print('=' * 163)

# --- BILAN FINAL ---

print('  SYNTHÈSE DE L’INVENTAIRE DES STOCKS — PNA CONGO')
print(f'  Médicaments en rupture critique : {nb_ruptures_critiques} ({nom_med_critique})')
print(f'  Médicaments en alerte stock     : {nb_alertes_stock} ({nom_med_alerte_stock})')
print(f'  Médicaments en stock limité     : {nb_stock_limites} ({nom_med_stock_limite})')
print(f'  Médicaments en stock normal     : {nb_stock_normaux} ({nom_med_stock_normaux})')

print('=' * 65)

# Alerte prioritaire conditionnelle (affichée uniquement en cas de rupture critique)

if nb_ruptures_critiques > 0:
    print(f'  !! ALERTE PRIORITAIRE : {nb_ruptures_critiques} médicament(s) en RUPTURE CRITIQUE !!')
print('=' * 65)

# TODO 2 : Affichage du rapport sur les niveaux d'occupation des hôpitaux

print('=' * 142)
print(f"{'':<44}\t{'ANALYSE DES ÉTABLISSEMENTS SELON LEUR TAUX D’OCCUPATION DES LITS'}")
print('=' * 142)

# Les en-têtes du tableau de suivi de la capacité hospitalière

print(f"{'Nom de l’établissement':<30}\t| {'Total lits':<5}\t| {'Lits occupés':<5}\t| {'Taux d’occupation':<0}\t| {'Statut (Normes OMS)':<5}\t| {'Action requise':<0}")
print('-' * 142)
print(f"{h1_nom:<30}\t| {h1_nb_lits:<10}\t| {h1_nb_lits_occupes:<10}\t| {taux_occupation_h1:<14}%\t| {status_occ_h1:<5}\t| {action_1:<0}")
print('-' * 142)

print(f"{h2_nom:<30}\t| {h2_nb_lits:<10}\t| {h2_nb_lits_occupes:<10}\t| {taux_occupation_h2:<14}%\t| {status_occ_h2:<5}\t| {action_2:<0}")
print('-' * 142)

print(f"{h3_nom:<30}\t| {h3_nb_lits:<10}\t| {h3_nb_lits_occupes:<10}\t| {taux_occupation_h3:<14}%\t| {status_occ_h3:<5}\t| {action_3:<0}")
print('-' * 142)

print(f"{h4_nom:<30}\t| {h4_nb_lits:<10}\t| {h4_nb_lits_occupes:<10}\t| {taux_occupation_h4:<14}%\t| {status_occ_h4:<5}\t| {action_4:<0}")
print('-' * 142)

print(f"{h5_nom:<30}\t| {h5_nb_lits:<10}\t| {h5_nb_lits_occupes:<10}\t| {taux_occupation_h5:<14}%\t| {status_occ_h5:<5}\t| {action_5:<0}")
print('=' * 142)
#======================== Compteurs triés selon le statut OMS attendu ========================================================

nb_hopitaux_saturation = 0
if status_occ_h1 == '[ALERTE CRITIQUE]': nb_hopitaux_saturation += 1
if status_occ_h2 == '[ALERTE CRITIQUE]': nb_hopitaux_saturation += 1
if status_occ_h3 == '[ALERTE CRITIQUE]': nb_hopitaux_saturation += 1
if status_occ_h4 == '[ALERTE CRITIQUE]': nb_hopitaux_saturation += 1
if status_occ_h5 == '[ALERTE CRITIQUE]': nb_hopitaux_saturation += 1

nb_hopitaux_capacite_limite = 0
if status_occ_h1 == '[ALERTE ELEVEE]' : nb_hopitaux_capacite_limite += 1
if status_occ_h2 == '[ALERTE ELEVEE]' : nb_hopitaux_capacite_limite += 1
if status_occ_h3 == '[ALERTE ELEVEE]' : nb_hopitaux_capacite_limite += 1
if status_occ_h4 == '[ALERTE ELEVEE]' : nb_hopitaux_capacite_limite += 1
if status_occ_h5 == '[ALERTE ELEVEE]' : nb_hopitaux_capacite_limite += 1

nb_hopitaux_capacite_optimale = 0
if status_occ_h1 == '[SITUATION OPTIMALE]' : nb_hopitaux_capacite_optimale += 1
if status_occ_h2 == '[SITUATION OPTIMALE]' : nb_hopitaux_capacite_optimale += 1
if status_occ_h3 == '[SITUATION OPTIMALE]' : nb_hopitaux_capacite_optimale += 1
if status_occ_h4 == '[SITUATION OPTIMALE]' : nb_hopitaux_capacite_optimale += 1
if status_occ_h5 == '[SITUATION OPTIMALE]' : nb_hopitaux_capacite_optimale += 1

nb_hopitaux_sous_utilisation = 0
if status_occ_h1 == '[SOUS-UTILISATION]' : nb_hopitaux_sous_utilisation += 1
if status_occ_h2 == '[SOUS-UTILISATION]' : nb_hopitaux_sous_utilisation += 1
if status_occ_h3 == '[SOUS-UTILISATION]' : nb_hopitaux_sous_utilisation += 1
if status_occ_h4 == '[SOUS-UTILISATION]' : nb_hopitaux_sous_utilisation += 1
if status_occ_h5 == '[SOUS-UTILISATION]' : nb_hopitaux_sous_utilisation += 1

# --- BILAN FINAL ---

print('SYNTHÈSE DE LA CAPACITÉ HOSPITALIÈRE — CONFORMITÉ OMS')
print(f'  Hôpitaux en état de saturation       : {nb_hopitaux_saturation} / 5 établissement(s)')
print(f'  Hôpitaux à capacité limite           : {nb_hopitaux_capacite_limite} / 5 établissement(s)')
print(f'  Hôpitaux à capacité optimale         : {nb_hopitaux_capacite_optimale} / 5 établissement(s)')
print(f'  Hôpitaux en sous-utilisation active  : {nb_hopitaux_sous_utilisation} / 5 établissement(s)')
print('=' * 65)

# Alerte prioritaire conditionnelle

if nb_hopitaux_saturation > 0:
    print(f'  !! ALERTE PRIORITAIRE : {nb_hopitaux_saturation} structure(s) saturée(s) — transferts à organiser d’urgence !!')
    print('=' * 65)
else :
    print('  Félicitations : Aucune saturation n’est à déplorer dans les 5 établissements suivis.')
#================= Fin d'affichage du rapport de niveau d'occupation

# TODO : Affichage des données sur la couverture vaccinale

print('=' * 160)
print(f"{'':<44}\t{'ÉVALUATION DE LA COUVERTURE VACCINALE PAR DÉPARTEMENT'}")
print('=' * 160)

# Les en-têtes du tableau de suivi des campagnes de vaccination

print(f"{'Département cible':<10}\t| {'Population cible':<5}\t| {'Personnes vaccinées':<5}\t| {'Taux de vaccination':<26}\t| {'Statut (Normes OMS)':<5}\t| {'Objectif d’action':<0}")
print('-' * 160)
print(f"{departement_1:<20}\t| {population_cible_1:<15}\t| {personnes_vaccinees_1:<15}\t| {taux_vaccination_d1:<26}%\t| {status_vac_h1:<5}\t| {action_vac_1:<0}")
print('-' * 160)
print(f"{departement_2:<20}\t| {population_cible_2:<15}\t| {personnes_vaccinees_2:<15}\t| {taux_vaccination_d2:<26}%\t| {status_vac_h2:<5}\t| {action_vac_2:<0}")
print('-' * 160)
print(f"{departement_3:<20}\t| {population_cible_3:<15}\t| {personnes_vaccinees_3:<15}\t| {taux_vaccination_d3:<26}%\t| {status_vac_h3:<5}\t| {action_vac_3:<0}")
print('-' * 160)
print(f"{departement_4:<20}\t| {population_cible_4:<15}\t| {personnes_vaccinees_4:<15}\t| {taux_vaccination_d4:<26}%\t| {status_vac_h4:<5}\t| {action_vac_4:<0}")
print('-' * 160)

# #======================== Compteurs triés selon le statut OMS attendu ========================================================

nb_departement_camp_urg = 0
if status_vac_h1 == '[ZONE CRITIQUE]': nb_departement_camp_urg += 1
if status_vac_h2 == '[ZONE CRITIQUE]': nb_departement_camp_urg += 1
if status_vac_h3 == '[ZONE CRITIQUE]': nb_departement_camp_urg += 1
if status_vac_h4 == '[ZONE CRITIQUE]': nb_departement_camp_urg += 1

nb_departement_camp_renforce = 0
if status_vac_h1 == '[ZONE A RISQUE]': nb_departement_camp_renforce += 1
if status_vac_h2 == '[ZONE A RISQUE]': nb_departement_camp_renforce += 1
if status_vac_h3 == '[ZONE A RISQUE]': nb_departement_camp_renforce += 1
if status_vac_h4 == '[ZONE A RISQUE]': nb_departement_camp_renforce += 1

nb_departement_camp_zone_insuf = 0
if status_vac_h1 == '[ZONE INSUFFISANTE]': nb_departement_camp_zone_insuf += 1
if status_vac_h2 == '[ZONE INSUFFISANTE]': nb_departement_camp_zone_insuf += 1
if status_vac_h3 == '[ZONE INSUFFISANTE]': nb_departement_camp_zone_insuf += 1
if status_vac_h4 == '[ZONE INSUFFISANTE]': nb_departement_camp_zone_insuf += 1

nb_departement_camp_zone_conforme = 0
if status_vac_h1 == '[ZONE OMS CONFORME]': nb_departement_camp_zone_conforme += 1
if status_vac_h2 == '[ZONE OMS CONFORME]': nb_departement_camp_zone_conforme += 1
if status_vac_h3 == '[ZONE OMS CONFORME]': nb_departement_camp_zone_conforme += 1
if status_vac_h4 == '[ZONE OMS CONFORME]': nb_departement_camp_zone_conforme += 1

# --- BILAN FINAL ---

print('SYNTHÈSE DE LA COUVERTURE VACCINALE PAR DÉPARTEMENT — OBJECTIFS OMS')
print(f'  Départements requérant une campagne d’urgence obligatoire : {nb_departement_camp_urg} / 4 département(s)')
print(f'  Départements requérant une campagne renforcée de suivi     : {nb_departement_camp_renforce} / 4 département(s)')
print(f'  Départements sous le seuil attendu (objectif OMS non atteint) : {nb_departement_camp_zone_insuf} / 4 département(s)')
print(f'  Départements parfaitement conformes aux normes de l’OMS     : {nb_departement_camp_zone_conforme} / 4 département(s)')
print('=' * 65)

# Alerte prioritaire conditionnelle

if nb_departement_camp_zone_insuf > 0:
    print(f'  !! ALERTE PRIORITAIRE : {nb_departement_camp_zone_insuf} département(s) nécessite(nt) un renforcement immédiat pour atteindre les seuils recommandés !!')
    print('=' * 65)
else :
    print('  Félicitations : Tous les départements atteignent une couverture vaccinale optimale.')
#================= Fin d'affichage du rapport de vaccination =====================================================================================
#======================================== Fin du module S3 ===============================================================================================================