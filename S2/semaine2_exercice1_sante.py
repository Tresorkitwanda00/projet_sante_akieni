# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville
# Votre nom : KITWANDA NYEMBO TRESOR
# Date : Le 20/06/2026
# ============================================================

# --- SECTION 1 : VARIABLES PATIENT ---

# TODO : Declarer toutes les variables patient ci-dessous

nom_patient = "MAVOUNGOU Celestion"  # Nom complet du patient (chaîne de caractères)
age_patient = 42                     # Âge du patient (entier)
sexe_patient = 'M'                   # Sexe du patient (M ou F)
departement_patient = 'Brazzaville'  # Lieu de résidence du patient
couverture_sociale = 'CNSS'          # Type de couverture sociale du patient

# --- SECTION 2 : VARIABLES CONSULTATION ---

# TODO : Declarer les variables consultation

type_consultation = 'Urgence'            # Type de consultation réalisée
cout_consultation_fcfa = 15000.0         # Coût unitaire de la consultation (FCFA)
nb_consultations = 1                     # Nombre de consultations effectuées
remise_cnss_pct = 30.0                   # Taux de remise appliqué par la CNSS (%)
diagnostic_principal = 'Paludisme grave' # Diagnostic médical principal (CIM-10)

# --- SECTION 3 : VARIABLES HOPITAL ---

# TODO : Declarer les variables hopital

nom_hospital = "CHU de Brazzaville"  # Nom officiel de l’établissement hospitalier
ville_hospital = 'Brazzaville'       # Ville d’implantation de l’hôpital
nb_lits_total = 320                  # Capacité totale en lits de l’hôpital
nb_lits_occupes = 284                # Nombre de lits actuellement occupés
nb_medecins_actifs = 47              # Nombre de médecins en activité

# --- SECTION 4 : CALCULS ---

# TODO : Calculer le cout total apres remise CNSS

cout_total_fcfa = float(
    cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
)

# TODO : Calculer le taux d'occupation (en pourcentage, arrondi a 1 decimale)

taux_occupation_pct = round(nb_lits_occupes / nb_lits_total * 100, 1)

# TODO : Calculer le ratio consultations par medecin (ce jour)

# Hypothese : 120 consultations ont eu lieu ce matin dans tout l'hopital

nb_consultations_hopital = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)

# --- SECTION 5 : AFFICHAGE ---

# TODO : Afficher une fiche complete avec f-strings

print('='*60)  # Affichage d’un séparateur visuel pour structurer la sortie
print(f' \t FICHE PATIENT — {nom_patient}')
print('='*60)

#==================================== debut affichage section patient =========================================================

# Construction de la section "informations patient" sous forme de texte structuré
info_patient = "\n \t Age         :"+" "+ str(age_patient)+" ans"
info_patient += " \n \t Sexe        : " + sexe_patient
info_patient += " \n \t Departement : " + departement_patient
info_patient += " \n \t Couverture  : " + couverture_sociale

print(f'\t Information du Patient \n \t{"-"*24}  {info_patient} ')

#==================================== Fin d'affichage des donnees patient =========================================================

print('='*60)

#==================================== debut affichage section consultation  =========================================================

# Construction de la section "consultation" pour l'affichage structuré
info_consultaion = " \n \t Type          : " + type_consultation
info_consultaion += " \n \t Diagnostic    : " + diagnostic_principal
info_consultaion += "\n \t Cout unitaire :"+" "+ str(cout_consultation_fcfa)+" FCFA"
info_consultaion += "\n \t Remise CNSS   :"+" "+ str(remise_cnss_pct)+" %"
info_consultaion += "\n \t COUT TOTAL    :"+" "+ str(cout_total_fcfa)+" FCFA"

print(f'\t Information de la consultation \n \t{"-"*32}  {info_consultaion} ')

#==================================== Fin d'affichage des donnees lies a la consultation =========================================================

print('='*60)

#==================================== debut affichage section etablissement  =========================================================

# Construction de la section "hôpital" pour synthèse des données
info_hospital = " \n \t Hospital        : " + nom_hospital
info_hospital += " \n \t Ville           : " + ville_hospital
info_hospital += "\n \t Lits occupes    : " + str(nb_lits_occupes) + " / " + str(nb_lits_total) + " (" + str(taux_occupation_pct) + "%)"
info_hospital += "\n \t Medecins actifs :"+" "+ str(nb_medecins_actifs)
info_hospital += "\n \t Ratio consult.  :"+" "+ str(ratio_consultations_medecin)+" consultations / medecin ce matin"

print(f'\t Information de l\'etablissement \n \t{"-"*32}  {info_hospital} ')

#==================================== Fin d'affichage des donnees lies de l'etablissement =========================================================

print('='*60)