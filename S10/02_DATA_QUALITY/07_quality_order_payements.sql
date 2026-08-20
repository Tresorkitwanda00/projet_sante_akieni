/*====================================================================
    DATA QUALITY — TEST 1 : DOUBLONS
----------------------------------------------------------------------    
    Une même commande peut avoir plusieurs paiements.
    La combinaison order_id + payment_sequential doit donc être unique.
====================================================================*/

SELECT
    TRIM(order_id) AS order_id,
    TRY_CAST(TRIM(payment_sequential) AS INT) AS payment_sequential,
    COUNT(*) AS nombre_occurrences
FROM staging_order_payments
GROUP BY
    TRIM(order_id),
    TRY_CAST(TRIM(payment_sequential) AS INT)
HAVING COUNT(*) > 1;
GO
/*====================================================================
    DATA QUALITY — TEST 2 : VALEURS MANQUANTES
----------------------------------------------------------------------    
    Identification des valeurs NULL ou vides pour chaque colonne.
====================================================================*/

SELECT
    SUM(CASE
        WHEN order_id IS NULL OR TRIM(order_id) = ''
        THEN 1 ELSE 0
    END) AS null_order_id,

    SUM(CASE
        WHEN payment_sequential IS NULL OR TRIM(payment_sequential) = ''
        THEN 1 ELSE 0
    END) AS null_payment_sequential,

    SUM(CASE
        WHEN payment_type IS NULL OR TRIM(payment_type) = ''
        THEN 1 ELSE 0
    END) AS null_payment_type,

    SUM(CASE
        WHEN payment_installments IS NULL OR TRIM(payment_installments) = ''
        THEN 1 ELSE 0
    END) AS null_payment_installments,

    SUM(CASE
        WHEN payment_value IS NULL OR TRIM(payment_value) = ''
        THEN 1 ELSE 0
    END) AS null_payment_value
FROM staging_order_payments;
GO
/*====================================================================
    DATA QUALITY — TEST 3 : PAYMENT_SEQUENTIAL
----------------------------------------------------------------------    
    Vérifie que les valeurs peuvent être converties en entier.
====================================================================*/

SELECT
    payment_sequential,
    COUNT(*) AS nombre
FROM staging_order_payments
WHERE
    payment_sequential IS NOT NULL
    AND TRIM(payment_sequential) <> ''
    AND TRY_CAST(TRIM(payment_sequential) AS INT) IS NULL
GROUP BY payment_sequential;
GO
/*====================================================================
    DATA QUALITY — TEST 4 : PAYMENT_INSTALLMENTS
----------------------------------------------------------------------    
    Les mensualités doivent être numériques et cohérentes.
====================================================================*/

SELECT
    payment_installments,
    COUNT(*) AS nombre
FROM staging_order_payments
WHERE
    payment_installments IS NOT NULL
    AND TRIM(payment_installments) <> ''
    AND TRY_CAST(TRIM(payment_installments) AS INT) IS NULL
GROUP BY payment_installments;
GO

SELECT *
FROM staging_order_payments
WHERE
    TRY_CAST(TRIM(payment_installments) AS INT) <= 0;
GO

/*====================================================================
    DATA QUALITY — TEST 5 : PAYMENT_VALUE
----------------------------------------------------------------------    
    Vérifie que les montants sont numériques.
====================================================================*/

SELECT
    payment_value,
    COUNT(*) AS nombre
FROM staging_order_payments
WHERE
    payment_value IS NOT NULL
    AND TRIM(payment_value) <> ''
    AND TRY_CAST(TRIM(payment_value) AS DECIMAL(10,2)) IS NULL
GROUP BY payment_value;
GO

SELECT *
FROM staging_order_payments
WHERE
    TRY_CAST(TRIM(payment_value) AS DECIMAL(10,2)) < 0;
GO

/*====================================================================
    DATA QUALITY — TEST 6 : TYPES DE PAIEMENT
----------------------------------------------------------------------    
    Liste des différentes valeurs présentes dans les données.
====================================================================*/

SELECT
    UPPER(TRIM(payment_type)) AS payment_type,
    COUNT(*) AS nombre
FROM staging_order_payments
GROUP BY UPPER(TRIM(payment_type))
ORDER BY nombre DESC;
GO


/*====================================================================
    DATA QUALITY — TEST 7 : INTÉGRITÉ RÉFÉRENTIELLE
----------------------------------------------------------------------    
    Recherche les paiements dont la commande n'existe pas
    dans la table orders.
====================================================================*/

SELECT DISTINCT
    TRIM(s.order_id) AS order_id
FROM staging_order_payments AS s
LEFT JOIN orders AS o
    ON TRIM(s.order_id) = o.order_id
WHERE
    s.order_id IS NOT NULL
    AND TRIM(s.order_id) <> ''
    AND o.order_id IS NULL;
GO