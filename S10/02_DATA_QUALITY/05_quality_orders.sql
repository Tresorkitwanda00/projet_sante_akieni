/*====================================================================
    DATA QUALITY : ORDERS
----------------------------------------------------------------------
    Objectif :
    Contrôler la qualité, la complétude, l'unicité et la cohérence
    des données présentes dans staging_orders avant leur chargement
    dans la table finale orders.

    Les contrôles portent principalement sur :

        1. Unicité de order_id
        2. Valeurs NULL ou vides
        3. Validité des customer_id
        4. Cohérence avec la table customers
        5. Validité de order_status
        6. Validité des dates
        7. Cohérence chronologique des événements
        8. Cohérence de la date estimée de livraison

    Principe :
    Les anomalies sont d'abord identifiées et documentées.
    Aucune donnée n'est supprimée automatiquement à cette étape.
====================================================================*/


/*--------------------------------------------------------------------
    TEST 1 : UNICITÉ DE ORDER_ID
----------------------------------------------------------------------
    Hypothèse :
    Chaque commande doit posséder un identifiant unique.

    Résultat attendu :
    Aucune ligne retournée.
--------------------------------------------------------------------*/

SELECT
    order_id,
    COUNT(*) AS nombre_occurrences
FROM staging_orders
GROUP BY order_id
HAVING COUNT(*) > 1;


/*--------------------------------------------------------------------
    TEST 2 : VALEURS NULL OU VIDES
----------------------------------------------------------------------
    Hypothèse :
    Les colonnes obligatoires ne doivent pas être NULL ou vides.

    Colonnes obligatoires :
        - order_id
        - customer_id
        - order_status
        - order_purchase_timestamp
        - order_estimated_delivery_date
--------------------------------------------------------------------*/

SELECT
    SUM(
        CASE
            WHEN order_id IS NULL
              OR TRIM(order_id) = ''
            THEN 1 ELSE 0
        END
    ) AS null_order_id,

    SUM(
        CASE
            WHEN customer_id IS NULL
              OR TRIM(customer_id) = ''
            THEN 1 ELSE 0
        END
    ) AS null_customer_id,

    SUM(
        CASE
            WHEN order_status IS NULL
              OR TRIM(order_status) = ''
            THEN 1 ELSE 0
        END
    ) AS null_order_status,

    SUM(
        CASE
            WHEN order_purchase_timestamp IS NULL
              OR TRIM(order_purchase_timestamp) = ''
            THEN 1 ELSE 0
        END
    ) AS null_purchase_date,

    SUM(
        CASE
            WHEN order_estimated_delivery_date IS NULL
              OR TRIM(order_estimated_delivery_date) = ''
            THEN 1 ELSE 0
        END
    ) AS null_estimated_delivery_date

FROM staging_orders;


/*--------------------------------------------------------------------
    TEST 3 : VALIDITÉ DES DATES
----------------------------------------------------------------------
    Hypothèse :
    Les valeurs des colonnes de dates doivent pouvoir être converties
    correctement en DATETIME.

    TRY_CAST permet de détecter les valeurs invalides sans provoquer
    l'arrêt de la requête.
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
FROM staging_orders
WHERE
       (
           order_purchase_timestamp IS NOT NULL
           AND TRY_CAST(
               TRIM(order_purchase_timestamp)
               AS DATETIME
           ) IS NULL
       )
    OR (
           order_approved_at IS NOT NULL
           AND TRIM(order_approved_at) <> ''
           AND TRY_CAST(
               TRIM(order_approved_at)
               AS DATETIME
           ) IS NULL
       )
    OR (
           order_delivered_carrier_date IS NOT NULL
           AND TRIM(order_delivered_carrier_date) <> ''
           AND TRY_CAST(
               TRIM(order_delivered_carrier_date)
               AS DATETIME
           ) IS NULL
       )
    OR (
           order_delivered_customer_date IS NOT NULL
           AND TRIM(order_delivered_customer_date) <> ''
           AND TRY_CAST(
               TRIM(order_delivered_customer_date)
               AS DATETIME
           ) IS NULL
       )
    OR (
           order_estimated_delivery_date IS NOT NULL
           AND TRY_CAST(
               TRIM(order_estimated_delivery_date)
               AS DATETIME
           ) IS NULL
       );


/*--------------------------------------------------------------------
    TEST 4 : INTÉGRITÉ RÉFÉRENTIELLE
----------------------------------------------------------------------
    Hypothèse :
    Chaque customer_id présent dans orders doit exister dans
    la table customers.

    Ce contrôle est essentiel avant l'application de la
    FOREIGN KEY FK_orders_customers.
--------------------------------------------------------------------*/

SELECT
    s.customer_id,
    COUNT(*) AS nombre_commandes
FROM staging_orders AS s
LEFT JOIN customers AS c
    ON TRIM(s.customer_id) = TRIM(c.customer_id)
WHERE c.customer_id IS NULL
GROUP BY s.customer_id;


/*--------------------------------------------------------------------
    TEST 5 : VALIDITÉ DU STATUT DE COMMANDE
----------------------------------------------------------------------
    Hypothèse :
    order_status doit appartenir aux statuts connus du dataset Olist.

    Statuts attendus :
        - delivered
        - shipped
        - canceled
        - unavailable
        - invoiced
        - processing
        - created
        - approved
--------------------------------------------------------------------*/

SELECT DISTINCT
    order_status
FROM staging_orders
WHERE order_status IS NULL
   OR TRIM(order_status) = ''
   OR LOWER(TRIM(order_status)) NOT IN (
        'delivered',
        'shipped',
        'canceled',
        'unavailable',
        'invoiced',
        'processing',
        'created',
        'approved'
   );


/*--------------------------------------------------------------------
    TEST 6 : COHÉRENCE CHRONOLOGIQUE
----------------------------------------------------------------------
    Hypothèse :
    Les événements d'une commande doivent respecter un ordre
    chronologique logique.

    Exemple :
        achat
          ↓
        approbation
          ↓
        remise au transporteur
          ↓
        livraison client
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date
FROM staging_orders
WHERE
       (
           TRY_CAST(order_approved_at AS DATETIME)
           <
           TRY_CAST(order_purchase_timestamp AS DATETIME)
       )
    OR (
           TRY_CAST(order_delivered_carrier_date AS DATETIME)
           <
           TRY_CAST(order_purchase_timestamp AS DATETIME)
       )
    OR (
           TRY_CAST(order_delivered_customer_date AS DATETIME)
           <
           TRY_CAST(order_purchase_timestamp AS DATETIME)
       )
    OR (
           TRY_CAST(order_delivered_customer_date AS DATETIME)
           <
           TRY_CAST(order_delivered_carrier_date AS DATETIME)
       );


/*--------------------------------------------------------------------
    TEST 7 : COHÉRENCE DE LA DATE ESTIMÉE
----------------------------------------------------------------------
    Hypothèse :
    La date estimée de livraison ne devrait normalement pas être
    antérieure à la date d'achat.
--------------------------------------------------------------------*/

SELECT
    order_id,
    order_purchase_timestamp,
    order_estimated_delivery_date
FROM staging_orders
WHERE
    TRY_CAST(order_estimated_delivery_date AS DATETIME)
    <
    TRY_CAST(order_purchase_timestamp AS DATETIME);
GO