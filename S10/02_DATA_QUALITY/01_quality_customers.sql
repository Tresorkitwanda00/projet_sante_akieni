
/*--------------------------------------------------------------------
    4. TEST DE QUALITÉ N°1 : UNICITÉ DE CUSTOMER_ID
----------------------------------------------------------------------
    Hypothèse :
    Chaque customer_id doit être unique dans la table de staging.

    Pourquoi ?
    Le customer_id représente l'identifiant d'un client.
    Deux lignes possédant le même customer_id peuvent indiquer
    un doublon ou une anomalie dans les données sources.

    Méthode :
    - Regrouper les lignes par customer_id.
    - Compter le nombre d'occurrences de chaque identifiant.
    - Conserver uniquement les identifiants apparaissant plus d'une fois.

    Interprétation :
    - Aucun résultat retourné :
      L'hypothèse d'unicité est respectée.
    - Une ou plusieurs lignes retournées :
      Des doublons existent et doivent être analysés.
--------------------------------------------------------------------*/

SELECT
    customer_id,
    COUNT(*) AS nombre_occurrences
FROM staging_customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


/*--------------------------------------------------------------------
    5. TEST DE QUALITÉ N°2 : VALEURS NULL OU VIDES
----------------------------------------------------------------------
    Hypothèse :
    Les colonnes obligatoires suivantes ne doivent contenir
    ni valeur NULL ni chaîne vide :

        - customer_id
        - customer_unique_id
        - customer_zip_code_prefix
        - customer_city
        - customer_state

    Pourquoi ?
    Une valeur manquante dans ces colonnes peut empêcher
    l'identification correcte du client ou compromettre
    les analyses et les jointures futures.

    Méthode :
    Pour chaque colonne, compter les lignes dont la valeur est :
        - NULL
        - vide ('')
        - composée uniquement d'espaces

    Interprétation :
    - Résultat = 0 :
      Aucune valeur manquante détectée pour la colonne.
    - Résultat > 0 :
      Des valeurs manquantes doivent être analysées et éventuellement
      corrigées ou traitées avant l'intégration finale.
--------------------------------------------------------------------*/

SELECT
    SUM(
        CASE
            WHEN customer_id IS NULL
              OR TRIM(customer_id) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_customer_id,

    SUM(
        CASE
            WHEN customer_unique_id IS NULL
              OR TRIM(customer_unique_id) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_unique_id,

    SUM(
        CASE
            WHEN customer_zip_code_prefix IS NULL
              OR TRIM(customer_zip_code_prefix) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_zip,

    SUM(
        CASE
            WHEN customer_city IS NULL
              OR TRIM(customer_city) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_city,

    SUM(
        CASE
            WHEN customer_state IS NULL
              OR TRIM(customer_state) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_state

FROM staging_customers;


/*--------------------------------------------------------------------
    6. TEST DE QUALITÉ N°3 : FORMAT DU CODE D'ÉTAT
----------------------------------------------------------------------
    Hypothèse :
    Tous les codes d'état brésiliens stockés dans customer_state
    doivent comporter exactement 2 caractères.

    Exemples valides :
        SP
        RJ
        MG

    Pourquoi ?
    Le code d'état brésilien est représenté par une abréviation
    standardisée composée de deux caractères.

    Méthode :
    - Supprimer les espaces éventuels avec TRIM().
    - Calculer la longueur avec LEN().
    - Identifier les valeurs dont la longueur est différente de 2.

    Interprétation :
    - Aucun résultat :
      Tous les codes respectent le format attendu.
    - Une ou plusieurs lignes :
      Les valeurs concernées doivent être examinées.
--------------------------------------------------------------------*/

SELECT DISTINCT
    customer_state,
    LEN(TRIM(customer_state)) AS longueur
FROM staging_customers
WHERE LEN(TRIM(customer_state)) <> 2;

