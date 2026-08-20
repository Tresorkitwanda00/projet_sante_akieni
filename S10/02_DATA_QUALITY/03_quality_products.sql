-- =============================================================================
-- SCRIPT DE CONTRÔLE DE QUALITÉ DES DONNÉES : OLIST PRODUCTS
-- Table source : staging_products
-- =============================================================================


-- =============================================================================
-- TEST 1 : Vérification de l'unicité de la clé primaire (Uniqueness)
-- Objectif : Vérifier qu'aucun product_id n'est dupliqué.
-- Attendu  : Le résultat doit être vide (0 ligne).
-- =============================================================================
SELECT
    product_id,
    COUNT(*) AS occurences
FROM staging_products
GROUP BY product_id
HAVING COUNT(*) > 1;


-- =============================================================================
-- TEST 2 : Vérification de la complétude (Completeness)
-- Objectif : Identifier le nombre et le pourcentage de valeurs manquantes
--            (NULL, chaînes vides ou espaces) par colonne.
-- =============================================================================
SELECT
    COUNT(*) AS total_lignes,
    
    -- Nulls ou vides sur product_id
    SUM(CASE WHEN product_id IS NULL OR LEN(TRIM(product_id)) = 0 THEN 1 ELSE 0 END) AS product_id_missing,
    
    -- Nulls ou vides sur la catégorie
    SUM(CASE WHEN product_category_name IS NULL OR LEN(TRIM(product_category_name)) = 0 THEN 1 ELSE 0 END) AS category_missing,
    
    -- Nulls ou invalides sur le nombre de photos
    SUM(CASE WHEN product_photos_qty IS NULL OR TRY_CAST(TRIM(product_photos_qty) AS INT) IS NULL THEN 1 ELSE 0 END) AS photos_qty_missing_or_invalid,
    
    -- Nulls ou invalides sur la longueur du nom
    SUM(CASE WHEN product_name_lenght IS NULL OR TRY_CAST(TRIM(product_name_lenght) AS INT) IS NULL THEN 1 ELSE 0 END) AS name_lenght_missing_or_invalid,
    
    -- Nulls ou invalides sur les dimensions et le poids
    SUM(CASE WHEN product_weight_g IS NULL OR TRY_CAST(TRIM(product_weight_g) AS FLOAT) IS NULL THEN 1 ELSE 0 END) AS weight_missing_or_invalid,
    SUM(CASE WHEN product_length_cm IS NULL OR TRY_CAST(TRIM(product_length_cm) AS FLOAT) IS NULL THEN 1 ELSE 0 END) AS length_missing_or_invalid,
    SUM(CASE WHEN product_height_cm IS NULL OR TRY_CAST(TRIM(product_height_cm) AS FLOAT) IS NULL THEN 1 ELSE 0 END) AS height_missing_or_invalid,
    SUM(CASE WHEN product_width_cm IS NULL OR TRY_CAST(TRIM(product_width_cm) AS FLOAT) IS NULL THEN 1 ELSE 0 END) AS width_missing_or_invalid
FROM staging_products;


-- =============================================================================
-- TEST 3 : Conformation des types de données (Type Validity)
-- Objectif : Détecter les valeurs non convertibles dans les types cibles.
-- Attendu  : Le résultat doit être vide (0 ligne).
-- =============================================================================
SELECT *
FROM staging_products
WHERE (product_photos_qty IS NOT NULL AND TRY_CAST(TRIM(product_photos_qty) AS INT) IS NULL)
   OR (product_name_lenght IS NOT NULL AND TRY_CAST(TRIM(product_name_lenght) AS INT) IS NULL)
   OR (product_description_lenght IS NOT NULL AND TRY_CAST(TRIM(product_description_lenght) AS INT) IS NULL)
   OR (product_weight_g IS NOT NULL AND TRY_CAST(TRIM(product_weight_g) AS FLOAT) IS NULL)
   OR (product_length_cm IS NOT NULL AND TRY_CAST(TRIM(product_length_cm) AS FLOAT) IS NULL)
   OR (product_height_cm IS NOT NULL AND TRY_CAST(TRIM(product_height_cm) AS FLOAT) IS NULL)
   OR (product_width_cm IS NOT NULL AND TRY_CAST(TRIM(product_width_cm) AS FLOAT) IS NULL);


-- =============================================================================
-- TEST 4 : Validité des plages de valeurs Métier (Value Range Validity)
-- Objectif : Détecter les dimensions/poids négatifs, nuls ou irréalistes.
-- Attendu  : Le résultat doit être vide (0 ligne).
-- =============================================================================
SELECT *
FROM staging_products
WHERE TRY_CAST(TRIM(product_photos_qty) AS INT) < 0 OR TRY_CAST(TRIM(product_photos_qty) AS INT) > 30
   OR TRY_CAST(TRIM(product_name_lenght) AS INT) <= 0
   OR TRY_CAST(TRIM(product_description_lenght) AS INT) <= 0
   OR TRY_CAST(TRIM(product_weight_g) AS FLOAT) <= 0
   OR TRY_CAST(TRIM(product_length_cm) AS FLOAT) <= 0
   OR TRY_CAST(TRIM(product_height_cm) AS FLOAT) <= 0
   OR TRY_CAST(TRIM(product_width_cm) AS FLOAT) <= 0;


-- =============================================================================
-- TEST 5 : Cohérence globale des données (Data Consistency)
-- Objectif : Vérifier qu'un produit n'a pas des dimensions valides tout en ayant un poids nul.
-- Attendu  : Le résultat doit être vide (0 ligne).
-- =============================================================================
SELECT *
FROM staging_products
WHERE TRY_CAST(TRIM(product_length_cm) AS FLOAT) > 0
  AND TRY_CAST(TRIM(product_height_cm) AS FLOAT) > 0
  AND TRY_CAST(TRIM(product_width_cm) AS FLOAT) > 0
  AND (TRY_CAST(TRIM(product_weight_g) AS FLOAT) IS NULL OR TRY_CAST(TRIM(product_weight_g) AS FLOAT) = 0);


-- =============================================================================
-- TEST 6 : Analyse des catégories de produits (Categorical Validity)
-- Objectif : Détecter les catégories non renseignées ou les anomalies de saisie.
-- =============================================================================
SELECT
    COALESCE(LOWER(TRIM(product_category_name)), '[NON SPÉCIFIÉ]') AS categorie_nettoyee,
    COUNT(*) AS nombre_produits
FROM staging_products
GROUP BY LOWER(TRIM(product_category_name))
ORDER BY nombre_produits DESC;

/*--------------------------------------------------------------------
    ÉTAPE 1 : NETTOYAGE DES COLONNES TEXTE
----------------------------------------------------------------------
    Règle :
    - Suppression des espaces inutiles avec TRIM().
    - Conversion des chaînes vides en 'NON_SPECIFIE'.
    - Normalisation de la catégorie en minuscules.

    Cette transformation est effectuée dans la table de staging
    avant le chargement dans la table finale.
--------------------------------------------------------------------*/

UPDATE staging_products
SET product_category_name =
    COALESCE(
        NULLIF(LOWER(TRIM(product_category_name)), ''),
        'NON_SPECIFIE'
    );

    /*--------------------------------------------------------------------
    ÉTAPE 2 : NETTOYAGE DES COLONNES ENTIÈRES
----------------------------------------------------------------------
    Règle :
    Les valeurs NULL, vides ou non numériques sont remplacées
    par 0.

    Colonnes concernées :
        - product_name_lenght
        - product_description_lenght
        - product_photos_qty
--------------------------------------------------------------------*/

UPDATE staging_products
SET
    product_name_lenght =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_name_lenght), '') AS INT),
            0
        ),

    product_description_lenght =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_description_lenght), '') AS INT),
            0
        ),

    product_photos_qty =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_photos_qty), '') AS INT),
            0
        );
GO
/*--------------------------------------------------------------------
    ÉTAPE 3 : NETTOYAGE DES COLONNES DÉCIMALES
----------------------------------------------------------------------
    Règle :
    Les valeurs NULL, vides ou non numériques sont remplacées
    par 0.

    Colonnes concernées :
        - product_weight_g
        - product_length_cm
        - product_height_cm
        - product_width_cm
--------------------------------------------------------------------*/

UPDATE staging_products
SET
    product_weight_g =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_weight_g), '') AS DECIMAL(10,2)),
            0
        ),

    product_length_cm =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_length_cm), '') AS DECIMAL(10,2)),
            0
        ),

    product_height_cm =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_height_cm), '') AS DECIMAL(10,2)),
            0
        ),

    product_width_cm =
        COALESCE(
            TRY_CAST(NULLIF(TRIM(product_width_cm), '') AS DECIMAL(10,2)),
            0
        );
GO

/*--------------------------------------------------------------------
    ÉTAPE 5 : SUPPRESSION DES PRODUITS SANS MÉTADONNÉES
----------------------------------------------------------------------
    Règle de qualité :
    Un produit possédant uniquement son product_id et aucune autre
    information exploitable est considéré comme inutilisable.

    Ces lignes sont supprimées du staging avant le chargement
    dans la table finale.
--------------------------------------------------------------------*/

DELETE FROM staging_products
WHERE
    product_id IS NOT NULL
    AND TRIM(product_id) <> ''
    AND product_category_name = 'NON_SPECIFIE'
    AND product_name_lenght = '0'
    AND product_description_lenght = '0'
    AND product_photos_qty = '0'
    AND product_weight_g = '0'
    AND product_length_cm = '0'
    AND product_height_cm = '0'
    AND product_width_cm = '0';
GO
SELECT *
FROM staging_products
WHERE
    product_category_name = 'NON_SPECIFIE'
    AND product_name_lenght = '0'
    AND product_description_lenght = '0'
    AND product_photos_qty = '0'
    AND product_weight_g = '0'
    AND product_length_cm = '0'
    AND product_height_cm = '0'
    AND product_width_cm = '0';