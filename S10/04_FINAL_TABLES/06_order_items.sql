/*====================================================================
    SCRIPT FINAL : ORDER_ITEMS
----------------------------------------------------------------------
    Objectif :
    Effectuer les contrôles finaux de qualité et d'intégrité après
    le chargement des données transformées dans la table order_items.

    Les données ont déjà été :
        1. Importées dans la table de staging.
        2. Contrôlées lors de la DATA QUALITY.
        3. Transformées.
        4. Insérées dans la table finale order_items.

    Ce script est uniquement destiné à la validation finale.

    Contrôles effectués :
        1. Nombre total de lignes.
        2. Unicité de la clé primaire composée.
        3. Valeurs NULL.
        4. Intégrité avec orders.
        5. Intégrité avec products.
        6. Intégrité avec sellers.
        7. Validité des montants.
        8. Aperçu des données finales.
====================================================================*/


/*--------------------------------------------------------------------
    1. NOMBRE TOTAL DE LIGNES
--------------------------------------------------------------------*/

SELECT 
    COUNT(*) AS total_order_items
FROM order_items;
GO


/*--------------------------------------------------------------------
    2. CONTRÔLE DE LA CLÉ PRIMAIRE COMPOSÉE

    Chaque combinaison :
        order_id + order_item_id

    doit être unique.
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_item_id,
    COUNT(*) AS nombre_occurrences
FROM order_items
GROUP BY
    order_id,
    order_item_id
HAVING COUNT(*) > 1;
GO


/*--------------------------------------------------------------------
    3. CONTRÔLE DES VALEURS NULL

    Les colonnes suivantes sont obligatoires :
        order_id
        order_item_id
        product_id
        seller_id
        price
        freight_value
--------------------------------------------------------------------*/

SELECT
    SUM(CASE WHEN order_id IS NULL THEN 1 ELSE 0 END) 
        AS null_order_id,

    SUM(CASE WHEN order_item_id IS NULL THEN 1 ELSE 0 END) 
        AS null_order_item_id,

    SUM(CASE WHEN product_id IS NULL THEN 1 ELSE 0 END) 
        AS null_product_id,

    SUM(CASE WHEN seller_id IS NULL THEN 1 ELSE 0 END) 
        AS null_seller_id,

    SUM(CASE WHEN shipping_limit_date IS NULL THEN 1 ELSE 0 END) 
        AS null_shipping_limit_date,

    SUM(CASE WHEN price IS NULL THEN 1 ELSE 0 END) 
        AS null_price,

    SUM(CASE WHEN freight_value IS NULL THEN 1 ELSE 0 END) 
        AS null_freight_value

FROM order_items;
GO


/*--------------------------------------------------------------------
    4. CONTRÔLE DE L'INTÉGRITÉ AVEC ORDERS

    Chaque order_id de order_items doit correspondre à une commande
    existante dans orders.
--------------------------------------------------------------------*/

SELECT
    oi.order_id
FROM order_items oi
LEFT JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;
GO


/*--------------------------------------------------------------------
    5. CONTRÔLE DE L'INTÉGRITÉ AVEC PRODUCTS

    Chaque product_id doit correspondre à un produit existant.
--------------------------------------------------------------------*/

SELECT
    oi.product_id
FROM order_items oi
LEFT JOIN products p
    ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;
GO


/*--------------------------------------------------------------------
    6. CONTRÔLE DE L'INTÉGRITÉ AVEC SELLERS

    Chaque seller_id doit correspondre à un vendeur existant.
--------------------------------------------------------------------*/

SELECT
    oi.seller_id
FROM order_items oi
LEFT JOIN sellers s
    ON oi.seller_id = s.seller_id
WHERE s.seller_id IS NULL;
GO


/*--------------------------------------------------------------------
    7. CONTRÔLE DES MONTANTS

    Le prix et les frais de transport ne doivent pas être négatifs.
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_item_id,
    price,
    freight_value
FROM order_items
WHERE price < 0
   OR freight_value < 0;
GO


/*--------------------------------------------------------------------
    8. CONTRÔLE DE L'IDENTIFIANT DE L'ARTICLE

    order_item_id doit être strictement positif.
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_item_id
FROM order_items
WHERE order_item_id <= 0;
GO


/*--------------------------------------------------------------------
    9. APERÇU DES DONNÉES FINALES
--------------------------------------------------------------------*/

SELECT TOP 20
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
FROM order_items
ORDER BY order_id, order_item_id;
GO