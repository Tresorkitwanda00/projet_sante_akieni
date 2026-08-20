/*====================================================================
    SCRIPT FINAL : SELLERS
----------------------------------------------------------------------
    Objectif :
    Effectuer les contrôles finaux sur la table sellers après
    transformation et chargement des données.

    À ce stade du processus ETL :
        - Les données brutes ont été importées dans staging_sellers.
        - Les contrôles de qualité ont été réalisés.
        - Les transformations ont été appliquées.
        - Les données nettoyées ont été chargées dans sellers.

    La table sellers représente maintenant la version finale,
    standardisée et exploitable des données relatives aux vendeurs.

    Contrôles finaux :
        1. Vérifier le nombre total de vendeurs.
        2. Vérifier l'unicité de seller_id.
        3. Vérifier l'absence de valeurs NULL ou vides.
        4. Vérifier le format des codes d'État.
        5. Vérifier un échantillon des données finales.
====================================================================*/


/*--------------------------------------------------------------------
    1. VÉRIFICATION DU NOMBRE TOTAL DE VENDEURS
----------------------------------------------------------------------
    Objectif :
    Vérifier que les données ont été correctement chargées dans
    la table finale sellers.

    Le nombre obtenu peut être comparé au nombre de lignes de la
    table staging après exclusion des éventuelles lignes invalides.
--------------------------------------------------------------------*/

SELECT COUNT(*) AS nombre_total_vendeurs
FROM sellers;


/*--------------------------------------------------------------------
    2. VÉRIFICATION DE L'UNICITÉ DE SELLER_ID
----------------------------------------------------------------------
    Hypothèse :
    Chaque seller_id doit identifier un seul vendeur.

    Interprétation :
        - Aucun résultat :
          Aucun doublon détecté.
        - Une ou plusieurs lignes :
          Des doublons existent dans la table finale et doivent
          être analysés.
--------------------------------------------------------------------*/

SELECT
    seller_id,
    COUNT(*) AS nombre_occurrences
FROM sellers
GROUP BY seller_id
HAVING COUNT(*) > 1;


/*--------------------------------------------------------------------
    3. VÉRIFICATION DES VALEURS NULL OU VIDES
----------------------------------------------------------------------
    Objectif :
    Vérifier qu'aucune donnée obligatoire n'est manquante après
    transformation et chargement.

    Les colonnes contrôlées sont :
        - seller_id
        - seller_zip_code_prefix
        - seller_city
        - seller_state

    Interprétation :
        Une valeur égale à 0 indique qu'aucune valeur NULL ou vide
        n'a été détectée dans la colonne concernée.
--------------------------------------------------------------------*/

SELECT
    SUM(CASE
            WHEN seller_id IS NULL
              OR TRIM(seller_id) = ''
            THEN 1 ELSE 0
        END) AS null_seller_id,

    SUM(CASE
            WHEN seller_zip_code_prefix IS NULL
            THEN 1 ELSE 0
        END) AS null_zip,

    SUM(CASE
            WHEN seller_city IS NULL
              OR TRIM(seller_city) = ''
            THEN 1 ELSE 0
        END) AS null_city,

    SUM(CASE
            WHEN seller_state IS NULL
              OR TRIM(seller_state) = ''
            THEN 1 ELSE 0
        END) AS null_state

FROM sellers;


/*--------------------------------------------------------------------
    4. VÉRIFICATION DU FORMAT DE SELLER_STATE
----------------------------------------------------------------------
    Hypothèse :
    Chaque code d'État doit comporter exactement deux caractères.

    Les valeurs ont normalement déjà été normalisées en majuscules
    lors de la transformation.

    Interprétation :
        - Aucun résultat :
          Tous les codes respectent le format attendu.
        - Une ou plusieurs lignes :
          Des anomalies de format doivent être analysées.
--------------------------------------------------------------------*/

SELECT DISTINCT
    seller_state,
    LEN(TRIM(seller_state)) AS longueur
FROM sellers
WHERE LEN(TRIM(seller_state)) <> 2;


/*--------------------------------------------------------------------
    5. VÉRIFICATION VISUELLE DES DONNÉES FINALES
----------------------------------------------------------------------
    Objectif :
    Afficher un échantillon de la table finale afin de vérifier
    visuellement que les transformations ont correctement été
    appliquées.

    Contrôles visuels :
        - seller_id correctement nettoyé ;
        - code postal correctement converti ;
        - ville standardisée en minuscules ;
        - code d'État standardisé en majuscules.
--------------------------------------------------------------------*/

SELECT TOP 20
    seller_id,
    seller_zip_code_prefix,
    seller_city,
    seller_state
FROM sellers;


