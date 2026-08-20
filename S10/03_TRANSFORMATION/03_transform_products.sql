/*====================================================================
    CHARGEMENT FINAL : PRODUCTS
====================================================================*/

INSERT INTO products (
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm,
    product_brand,
    is_active
)
SELECT
    TRIM(product_id),

    LOWER(TRIM(product_category_name)),

    CAST(product_name_lenght AS INT),

    CAST(product_description_lenght AS INT),

    CAST(product_photos_qty AS INT),

    -- Conversion '225.00' → 225
    CAST(
        TRY_CAST(product_weight_g AS DECIMAL(10,2))
        AS INT
    ),

    CAST(product_length_cm AS DECIMAL(10,2)),

    CAST(product_height_cm AS DECIMAL(10,2)),

    CAST(product_width_cm AS DECIMAL(10,2)),

    'NON_SPECIFIE',

    CAST(1 AS BIT)

FROM staging_products;
GO