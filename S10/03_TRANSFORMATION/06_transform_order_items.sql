/*====================================================================
    ÉTAPE 4 : TRANSFORMATION ET CHARGEMENT — ORDER_ITEMS
----------------------------------------------------------------------
    Objectif :
    Transformer les données de staging_order_items afin de respecter
    les types et contraintes définis dans la table finale order_items.

    Transformations appliquées :

        - order_id
            Suppression des espaces inutiles.

        - order_item_id
            Conversion de VARCHAR vers INT.

        - product_id
            Suppression des espaces inutiles.

        - seller_id
            Suppression des espaces inutiles.

        - shipping_limit_date
            Conversion de VARCHAR vers DATETIME.

        - price
            Conversion de VARCHAR vers DECIMAL(10,2).

        - freight_value
            Conversion de VARCHAR vers DECIMAL(10,2).

    Les données ayant déjà passé les contrôles DATA QUALITY,
    elles peuvent maintenant être chargées dans la table finale.
====================================================================*/


INSERT INTO order_items (
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
)
SELECT
    TRIM(order_id) AS order_id,

    TRY_CAST(TRIM(order_item_id) AS INT) AS order_item_id,

    TRIM(product_id) AS product_id,

    TRIM(seller_id) AS seller_id,

    TRY_CAST(TRIM(shipping_limit_date) AS DATETIME) 
        AS shipping_limit_date,

    TRY_CAST(TRIM(price) AS DECIMAL(10,2)) 
        AS price,

    TRY_CAST(TRIM(freight_value) AS DECIMAL(10,2)) 
        AS freight_value

FROM staging_order_items;
GO