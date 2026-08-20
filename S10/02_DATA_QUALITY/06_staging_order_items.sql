/*====================================================================
    ÉTAPE 3 : DATA QUALITY — STAGING_ORDER_ITEMS
----------------------------------------------------------------------
    Objectif :
    Contrôler la qualité des données brutes avant leur transformation
    et leur chargement dans la table finale order_items.

    Aucun UPDATE ni DELETE n'est effectué à cette étape.

    Contrôles :
        1. Nombre total de lignes
        2. Doublons de la clé métier
        3. Valeurs NULL ou vides
        4. Validité de order_item_id
        5. Validité des prix
        6. Validité des frais de transport
        7. Validité des dates
        8. Intégrité référentielle
====================================================================*/


/*--------------------------------------------------------------------
    TEST 1 — NOMBRE TOTAL DE LIGNES
--------------------------------------------------------------------*/

SELECT 
    COUNT(*) AS total_lignes
FROM staging_order_items;
GO


/*--------------------------------------------------------------------
    TEST 2 — DOUBLONS DE LA CLÉ COMPOSÉE

    Une ligne est normalement identifiée par :
        order_id + order_item_id

    On recherche donc les couples présents plusieurs fois.
--------------------------------------------------------------------*/

SELECT
    TRIM(order_id) AS order_id,
    TRIM(order_item_id) AS order_item_id,
    COUNT(*) AS nombre_occurrences
FROM staging_order_items
GROUP BY
    TRIM(order_id),
    TRIM(order_item_id)
HAVING COUNT(*) > 1;
GO


/*--------------------------------------------------------------------
    TEST 3 — VALEURS NULL OU VIDES
--------------------------------------------------------------------*/

SELECT
    SUM(CASE 
            WHEN order_id IS NULL OR TRIM(order_id) = '' 
            THEN 1 ELSE 0 
        END) AS null_order_id,

    SUM(CASE 
            WHEN order_item_id IS NULL OR TRIM(order_item_id) = '' 
            THEN 1 ELSE 0 
        END) AS null_order_item_id,

    SUM(CASE 
            WHEN product_id IS NULL OR TRIM(product_id) = '' 
            THEN 1 ELSE 0 
        END) AS null_product_id,

    SUM(CASE 
            WHEN seller_id IS NULL OR TRIM(seller_id) = '' 
            THEN 1 ELSE 0 
        END) AS null_seller_id,

    SUM(CASE 
            WHEN shipping_limit_date IS NULL 
                 OR TRIM(shipping_limit_date) = ''
            THEN 1 ELSE 0 
        END) AS null_shipping_date,

    SUM(CASE 
            WHEN price IS NULL OR TRIM(price) = '' 
            THEN 1 ELSE 0 
        END) AS null_price,

    SUM(CASE 
            WHEN freight_value IS NULL OR TRIM(freight_value) = '' 
            THEN 1 ELSE 0 
        END) AS null_freight_value

FROM staging_order_items;
GO


/*--------------------------------------------------------------------
    TEST 4 — VALIDITÉ DE order_item_id

    La valeur doit pouvoir être convertie en entier.
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_item_id,
    CASE
        WHEN order_item_id IS NULL 
            THEN 'NULL'

        WHEN TRIM(order_item_id) = ''
            THEN 'VIDE'

        WHEN TRY_CAST(TRIM(order_item_id) AS INT) IS NULL
            THEN 'NON NUMERIQUE'

        ELSE 'VALIDE'
    END AS diagnostic
FROM staging_order_items
WHERE
       order_item_id IS NULL
    OR TRIM(order_item_id) = ''
    OR TRY_CAST(TRIM(order_item_id) AS INT) IS NULL;
GO


/*--------------------------------------------------------------------
    TEST 5 — VALIDITÉ DU PRIX
--------------------------------------------------------------------*/

SELECT
    order_id,
    price,
    CASE
        WHEN price IS NULL 
            THEN 'NULL'

        WHEN TRIM(price) = ''
            THEN 'VIDE'

        WHEN TRY_CAST(TRIM(price) AS DECIMAL(10,2)) IS NULL
            THEN 'NON NUMERIQUE'

        WHEN TRY_CAST(TRIM(price) AS DECIMAL(10,2)) < 0
            THEN 'NEGATIF'

        ELSE 'VALIDE'
    END AS diagnostic
FROM staging_order_items
WHERE
       price IS NULL
    OR TRIM(price) = ''
    OR TRY_CAST(TRIM(price) AS DECIMAL(10,2)) IS NULL
    OR TRY_CAST(TRIM(price) AS DECIMAL(10,2)) < 0;
GO


/*--------------------------------------------------------------------
    TEST 6 — VALIDITÉ DU FREIGHT_VALUE
--------------------------------------------------------------------*/

SELECT
    order_id,
    freight_value,
    CASE
        WHEN freight_value IS NULL 
            THEN 'NULL'

        WHEN TRIM(freight_value) = ''
            THEN 'VIDE'

        WHEN TRY_CAST(TRIM(freight_value) AS DECIMAL(10,2)) IS NULL
            THEN 'NON NUMERIQUE'

        WHEN TRY_CAST(TRIM(freight_value) AS DECIMAL(10,2)) < 0
            THEN 'NEGATIF'

        ELSE 'VALIDE'
    END AS diagnostic
FROM staging_order_items
WHERE
       freight_value IS NULL
    OR TRIM(freight_value) = ''
    OR TRY_CAST(TRIM(freight_value) AS DECIMAL(10,2)) IS NULL
    OR TRY_CAST(TRIM(freight_value) AS DECIMAL(10,2)) < 0;
GO


/*--------------------------------------------------------------------
    TEST 7 — VALIDITÉ DE LA DATE D'EXPÉDITION
--------------------------------------------------------------------*/

SELECT
    order_id,
    shipping_limit_date,
    CASE
        WHEN shipping_limit_date IS NULL
            THEN 'NULL'

        WHEN TRIM(shipping_limit_date) = ''
            THEN 'VIDE'

        WHEN TRY_CAST(TRIM(shipping_limit_date) AS DATETIME) IS NULL
            THEN 'DATE INVALIDE'

        ELSE 'VALIDE'
    END AS diagnostic
FROM staging_order_items
WHERE
       shipping_limit_date IS NULL
    OR TRIM(shipping_limit_date) = ''
    OR TRY_CAST(TRIM(shipping_limit_date) AS DATETIME) IS NULL;
GO


/*--------------------------------------------------------------------
    TEST 8 — INTÉGRITÉ AVEC ORDERS

    Chaque order_id de order_items doit exister dans orders.
--------------------------------------------------------------------*/

SELECT
    s.order_id
FROM staging_order_items s
LEFT JOIN orders o
    ON TRIM(s.order_id) = o.order_id
WHERE o.order_id IS NULL;
GO


/*--------------------------------------------------------------------
    TEST 9 — INTÉGRITÉ AVEC PRODUCTS

    Chaque product_id doit exister dans products.
--------------------------------------------------------------------*/

SELECT
    s.product_id
FROM staging_order_items s
LEFT JOIN products p
    ON TRIM(s.product_id) = p.product_id
WHERE p.product_id IS NULL;
GO


/*--------------------------------------------------------------------
    TEST 10 — INTÉGRITÉ AVEC SELLERS

    Chaque seller_id doit exister dans sellers.
--------------------------------------------------------------------*/

SELECT
    s.seller_id
FROM staging_order_items s
LEFT JOIN sellers se
    ON TRIM(s.seller_id) = se.seller_id
WHERE se.seller_id IS NULL;
GO