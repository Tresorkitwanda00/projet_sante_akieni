/*--------------------------------------------------------------------
    ÉTAPE : TRANSFORMATION ET CHARGEMENT DES DONNÉES SELLERS
----------------------------------------------------------------------
    Objectif :
    Nettoyer et standardiser les données présentes dans la table
    staging_sellers, puis les charger dans la table finale sellers.

    Source :
        staging_sellers

    Destination :
        sellers

    Transformations appliquées :

    1. seller_id
       - Suppression des espaces superflus avec TRIM().
       - Conservation uniquement des identifiants non NULL et non vides.
       - L'identifiant est utilisé pour identifier chaque vendeur.

    2. seller_zip_code_prefix
       - Conversion de la valeur en type entier avec CAST(... AS INT).
       - Cette conversion permet d'obtenir un type numérique dans
         la table finale.

    3. seller_city
       - Suppression des espaces superflus avec TRIM().
       - Conversion en minuscules avec LOWER() afin de standardiser
         la représentation des noms de villes.

    4. seller_state
       - Suppression des espaces superflus avec TRIM().
       - Conversion en majuscules avec UPPER() afin de normaliser
         les codes d'État (ex. : "sp" → "SP").

    5. DISTINCT
       - Élimine les lignes strictement identiques issues de la table
         de staging afin d'éviter l'insertion de doublons identiques.

    Filtre appliqué :
       Les lignes dont seller_id est NULL ou vide sont exclues,
       car un vendeur doit obligatoirement être identifiable.

    Résultat attendu :
       La table finale sellers contient des données nettoyées,
       standardisées et prêtes pour les analyses, les jointures
       et les traitements ultérieurs.
--------------------------------------------------------------------*/

INSERT INTO sellers (
    seller_id,
    seller_zip_code_prefix,
    seller_city,
    seller_state
)
SELECT DISTINCT
    TRIM(seller_id) AS seller_id,
    CAST(seller_zip_code_prefix AS INT) AS seller_zip_code_prefix,
    LOWER(TRIM(seller_city)) AS seller_city,
    UPPER(TRIM(seller_state)) AS seller_state
FROM staging_sellers
WHERE seller_id IS NOT NULL
  AND TRIM(seller_id) <> '';