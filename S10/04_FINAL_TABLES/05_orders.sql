/*====================================================================
    TABLE FINALE : ORDERS
----------------------------------------------------------------------
    Objectif :
    Vérifier que les données transformées provenant de la table
    staging_orders ont été correctement chargées dans la table finale
    orders.

    Les données ont déjà été nettoyées et transformées avant
    l'insertion. Ce script est donc consacré aux contrôles finaux
    d'intégrité et de qualité des données.

    Contrôles effectués :
        1. Vérification du nombre total de commandes.
        2. Vérification de l'unicité de order_id.
        3. Vérification des valeurs NULL sur les colonnes obligatoires.
        4. Vérification de l'existence des clients référencés.
        5. Vérification des dates incohérentes.
        6. Aperçu des données finales.
====================================================================*/


/*====================================================================
    1. CONTRÔLE DU NOMBRE DE LIGNES
====================================================================*/

SELECT 
    COUNT(*) AS total_orders
FROM orders;
GO


/*====================================================================
    2. CONTRÔLE DE L'UNICITÉ DE order_id

    order_id étant la clé primaire, aucune commande ne doit apparaître
    plusieurs fois.
====================================================================*/

SELECT 
    order_id,
    COUNT(*) AS nombre_occurrences
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;
GO


/*====================================================================
    3. CONTRÔLE DES VALEURS NULL

    Les colonnes order_id, customer_id, order_status,
    order_purchase_timestamp et order_estimated_delivery_date
    sont obligatoires.
====================================================================*/

SELECT
    SUM(CASE WHEN order_id IS NULL THEN 1 ELSE 0 END) 
        AS null_order_id,

    SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) 
        AS null_customer_id,

    SUM(CASE WHEN order_status IS NULL THEN 1 ELSE 0 END) 
        AS null_order_status,

    SUM(CASE WHEN order_purchase_timestamp IS NULL THEN 1 ELSE 0 END) 
        AS null_purchase_date,

    SUM(CASE WHEN order_estimated_delivery_date IS NULL THEN 1 ELSE 0 END) 
        AS null_estimated_delivery_date
FROM orders;
GO


/*====================================================================
    4. CONTRÔLE DE L'INTÉGRITÉ RÉFÉRENTIELLE

    Chaque customer_id présent dans orders doit correspondre à un
    client existant dans la table customers.
====================================================================*/

SELECT 
    o.order_id,
    o.customer_id
FROM orders o
LEFT JOIN customers c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO


/*====================================================================
    5. CONTRÔLE DES DATES

    Recherche des commandes dont la date d'achat est postérieure
    à la date estimée de livraison.
====================================================================*/

SELECT
    order_id,
    order_purchase_timestamp,
    order_estimated_delivery_date
FROM orders
WHERE order_purchase_timestamp > order_estimated_delivery_date;
GO


/*====================================================================
    6. APERÇU DES DONNÉES FINALES
====================================================================*/

SELECT TOP 20 *
FROM orders
ORDER BY order_purchase_timestamp;
GO