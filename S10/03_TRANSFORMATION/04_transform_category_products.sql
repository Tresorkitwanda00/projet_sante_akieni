/*====================================================================
    CHARGEMENT FINAL
----------------------------------------------------------------------
    Les données ont été :
        - importées ;
        - contrôlées ;
        - nettoyées.

    Elles sont maintenant chargées dans la table finale.
====================================================================*/

INSERT INTO product_category_name_translation (
    product_category_name,
    product_category_name_english
)
SELECT
    TRIM(product_category_name),
    TRIM(product_category_name_english)
FROM staging_product_category_name_translation;
GO