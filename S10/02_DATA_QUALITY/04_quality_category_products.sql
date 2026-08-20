/*--------------------------------------------------------------------
    TEST DE QUALITÉ N°1 : UNICITÉ DE PRODUCT_CATEGORY_NAME

    Hypothèse :
    Chaque catégorie doit apparaître une seule fois dans la table
    de traduction.
--------------------------------------------------------------------*/

SELECT
    product_category_name,
    COUNT(*) AS nombre_occurrences
FROM staging_product_category_name_translation
GROUP BY product_category_name
HAVING COUNT(*) > 1;

/*--------------------------------------------------------------------
    TEST DE QUALITÉ N°2 : VALEURS NULL OU VIDES
--------------------------------------------------------------------*/

SELECT
    SUM(
        CASE
            WHEN product_category_name IS NULL
              OR TRIM(product_category_name) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_category,

    SUM(
        CASE
            WHEN product_category_name_english IS NULL
              OR TRIM(product_category_name_english) = ''
            THEN 1
            ELSE 0
        END
    ) AS null_category_english

FROM staging_product_category_name_translation;