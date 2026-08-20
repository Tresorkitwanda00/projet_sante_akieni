/*--------------------------------------------------------------------
    CONTRÔLES DE QUALITÉ DES DONNÉES : SELLERS
----------------------------------------------------------------------
    Objectif général :
    Vérifier la qualité, la complétude et la conformité des données
    présentes dans la table de staging_sellers avant leur transformation
    et leur chargement dans la table finale sellers.

    Les contrôles portent principalement sur :
        1. L'unicité de seller_id.
        2. La présence de valeurs NULL ou vides.
        3. Le format du code d'État seller_state.
--------------------------------------------------------------------*/


/*--------------------------------------------------------------------
    TEST DE QUALITÉ N°1 : UNICITÉ DE SELLER_ID
----------------------------------------------------------------------
    Hypothèse :
    Chaque seller_id doit être unique dans la table de staging.

    Pourquoi ?
    seller_id représente l'identifiant d'un vendeur. Un même identifiant
    apparaissant plusieurs fois peut indiquer la présence de doublons
    ou une anomalie dans les données sources.

    Méthode :
        - Regrouper les données selon seller_id.
        - Compter le nombre d'occurrences de chaque identifiant.
        - Afficher uniquement les identifiants apparaissant plus d'une fois.

    Interprétation :
        - Aucun résultat :
          L'hypothèse d'unicité est respectée.

        - Une ou plusieurs lignes :
          Des doublons ont été détectés et doivent être analysés
          avant le chargement dans la table finale.
--------------------------------------------------------------------*/

SELECT
    seller_id,
    COUNT(*) AS nombre_occurrences
FROM staging_sellers
GROUP BY seller_id
HAVING COUNT(*) > 1;


/*--------------------------------------------------------------------
    TEST DE QUALITÉ N°2 : VALEURS NULL OU VIDES
----------------------------------------------------------------------
    Hypothèse :
    Les colonnes importantes de la table sellers ne doivent contenir
    ni valeur NULL ni chaîne vide.

    Colonnes contrôlées :
        - seller_id
        - seller_zip_code_prefix
        - seller_city
        - seller_state

    Méthode :
    Pour chaque colonne, compter les lignes dont la valeur est :
        - NULL ;
        - vide ;
        - composée uniquement d'espaces.

    Interprétation :
        - Résultat = 0 :
          Aucune valeur manquante détectée dans la colonne.

        - Résultat > 0 :
          Des valeurs manquantes sont présentes et doivent être
          analysées avant l'intégration dans la table finale.
--------------------------------------------------------------------*/

SELECT
    SUM(
        CASE
            WHEN seller_id IS NULL
              OR TRIM(seller_id) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_seller_id,

    SUM(
        CASE
            WHEN seller_zip_code_prefix IS NULL
              OR TRIM(seller_zip_code_prefix) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_zip,

    SUM(
        CASE
            WHEN seller_city IS NULL
              OR TRIM(seller_city) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_city,

    SUM(
        CASE
            WHEN seller_state IS NULL
              OR TRIM(seller_state) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_state

FROM staging_sellers;


/*--------------------------------------------------------------------
    TEST DE QUALITÉ N°3 : FORMAT DE SELLER_STATE
----------------------------------------------------------------------
    Hypothèse :
    Chaque code d'État brésilien présent dans seller_state doit
    comporter exactement deux caractères.

    Exemples de formats attendus :
        SP
        RJ
        MG
        BA

    Particularité :
    REPLACE() est utilisé pour supprimer les guillemets doubles
    éventuellement présents dans les données importées.

    TRIM() permet ensuite de supprimer les espaces superflus.

    Méthode :
        - Supprimer les guillemets avec REPLACE().
        - Supprimer les espaces avec TRIM().
        - Vérifier que la longueur obtenue est égale à 2 caractères.

    Interprétation :
        - Aucun résultat :
          Tous les codes respectent la longueur attendue.

        - Une ou plusieurs lignes :
          Des valeurs présentent un format incorrect et doivent être
          examinées avant la transformation finale.
--------------------------------------------------------------------*/

SELECT DISTINCT
    seller_state
FROM staging_sellers
WHERE LEN(
          TRIM(
              REPLACE(seller_state, '"', '')
          )
      ) <> 2;