/*====================================================================
    TRANSFORMATION ET CHARGEMENT : ORDERS
----------------------------------------------------------------------
    Objectif :
    Transformer les données issues de staging_orders avant leur
    insertion dans la table finale orders.

    Transformations appliquées :
    
    1. order_id
       Suppression des espaces superflus avec TRIM().
       
    2. customer_id
       Suppression des espaces superflus avec TRIM().
       
    3. order_status
       Suppression des espaces superflus et normalisation en
       minuscules pour obtenir une valeur homogène.

    4. Dates
       Les dates sont conservées telles quelles.
       Les valeurs NULL sont préservées car elles peuvent représenter
       une étape de commande non encore réalisée ou non disponible.

    IMPORTANT :
    La table staging_orders reste inchangée afin de conserver
    les données originales et les éventuelles anomalies détectées
    lors de la phase de Data Quality.
====================================================================*/

INSERT INTO orders (
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
)
SELECT
    TRIM(order_id) AS order_id,

    TRIM(customer_id) AS customer_id,

    LOWER(TRIM(order_status)) AS order_status,

    order_purchase_timestamp,

    order_approved_at,

    order_delivered_carrier_date,

    order_delivered_customer_date,

    order_estimated_delivery_date

FROM staging_orders;
GO