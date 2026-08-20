/*====================================================================
    TEST 7 : COHERENCE CHRONOLOGIQUE DES DATES DE COMMANDE
---------------------------------------------------------------------- 
    Objectif :
    Vérifier que les différentes étapes d'une commande respectent
    une chronologie logique.

    Ordre attendu :
        1. Achat
        2. Approbation
        3. Livraison au transporteur
        4. Livraison au client

    Une anomalie est détectée lorsqu'une date apparaît avant
    une étape qui devrait normalement la précéder.

    Décision :
    Les dates incohérentes ne sont pas corrigées artificiellement.
    Elles sont conservées pour préserver la donnée source et
    pourront être exclues ou traitées lors des analyses temporelles.
====================================================================*/

SELECT
    order_id,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date,

    CASE
        WHEN order_approved_at IS NOT NULL
             AND order_approved_at < order_purchase_timestamp
            THEN 'ANOMALIE : approbation avant achat'

        WHEN order_delivered_carrier_date IS NOT NULL
             AND order_approved_at IS NOT NULL
             AND order_delivered_carrier_date < order_approved_at
            THEN 'ANOMALIE : transporteur avant approbation'

        WHEN order_delivered_customer_date IS NOT NULL
             AND order_delivered_carrier_date IS NOT NULL
             AND order_delivered_customer_date < order_delivered_carrier_date
            THEN 'ANOMALIE : livraison client avant transporteur'

        WHEN order_delivered_customer_date IS NOT NULL
             AND order_delivered_customer_date < order_purchase_timestamp
            THEN 'ANOMALIE : livraison avant achat'

        ELSE 'VALIDE'
    END AS diagnostic

FROM staging_orders
WHERE
       (order_approved_at IS NOT NULL
        AND order_approved_at < order_purchase_timestamp)

    OR (order_delivered_carrier_date IS NOT NULL
        AND order_approved_at IS NOT NULL
        AND order_delivered_carrier_date < order_approved_at)

    OR (order_delivered_customer_date IS NOT NULL
        AND order_delivered_carrier_date IS NOT NULL
        AND order_delivered_customer_date < order_delivered_carrier_date)

    OR (order_delivered_customer_date IS NOT NULL
        AND order_delivered_customer_date < order_purchase_timestamp);
/*==============================================================
    TEST 7 - STATISTIQUE DES ANOMALIES CHRONOLOGIQUES
==============================================================*/

SELECT
    COUNT(*) AS total_anomalies
FROM staging_orders
WHERE
       (order_approved_at IS NOT NULL
        AND order_approved_at < order_purchase_timestamp)

    OR (order_delivered_carrier_date IS NOT NULL
        AND order_approved_at IS NOT NULL
        AND order_delivered_carrier_date < order_approved_at)

    OR (order_delivered_customer_date IS NOT NULL
        AND order_delivered_carrier_date IS NOT NULL
        AND order_delivered_customer_date < order_delivered_carrier_date)

    OR (order_delivered_customer_date IS NOT NULL
        AND order_delivered_customer_date < order_purchase_timestamp);
SELECT
    SUM(
        CASE
            WHEN order_approved_at IS NOT NULL
             AND order_approved_at < order_purchase_timestamp
            THEN 1 ELSE 0
        END
    ) AS approbation_avant_achat,

    SUM(
        CASE
            WHEN order_delivered_carrier_date IS NOT NULL
             AND order_approved_at IS NOT NULL
             AND order_delivered_carrier_date < order_approved_at
            THEN 1 ELSE 0
        END
    ) AS transporteur_avant_approbation,

    SUM(
        CASE
            WHEN order_delivered_customer_date IS NOT NULL
             AND order_delivered_carrier_date IS NOT NULL
             AND order_delivered_customer_date < order_delivered_carrier_date
            THEN 1 ELSE 0
        END
    ) AS client_avant_transporteur,

    SUM(
        CASE
            WHEN order_delivered_customer_date IS NOT NULL
             AND order_delivered_customer_date < order_purchase_timestamp
            THEN 1 ELSE 0
        END
    ) AS livraison_avant_achat

FROM staging_orders;

/*====================================================================
    TEST 7.1 : ANALYSE DES ANOMALIES TRANSPORTEUR
---------------------------------------------------------------------- 
    Objectif :
    Mesurer l'écart entre la date d'approbation et la date de
    livraison au transporteur pour les commandes concernées.
====================================================================*/

SELECT
    COUNT(*) AS nombre_anomalies,
    MIN(DATEDIFF(DAY, order_delivered_carrier_date, order_approved_at))
        AS ecart_minimum_jours,
    MAX(DATEDIFF(DAY, order_delivered_carrier_date, order_approved_at))
        AS ecart_maximum_jours,
    AVG(
        CAST(
            DATEDIFF(
                DAY,
                order_delivered_carrier_date,
                order_approved_at
            ) AS FLOAT
        )
    ) AS ecart_moyen_jours
FROM staging_orders
WHERE
    order_delivered_carrier_date IS NOT NULL
    AND order_approved_at IS NOT NULL
    AND order_delivered_carrier_date < order_approved_at;
SELECT
    COUNT(*) AS anomalies_plus_24h
FROM staging_orders
WHERE
    order_delivered_carrier_date IS NOT NULL
    AND order_approved_at IS NOT NULL
    AND order_delivered_carrier_date < DATEADD(
        HOUR,
        -24,
        order_approved_at
    );