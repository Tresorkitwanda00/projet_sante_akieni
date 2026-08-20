/*====================================================================
    DATA QUALITY — ANALYSE DES MENSUALITÉS À 0
----------------------------------------------------------------------    
    Identification des paiements ayant un nombre de mensualités
    égal à zéro.
====================================================================*/

SELECT
    payment_type,
    payment_installments,
    COUNT(*) AS nombre
FROM staging_order_payments
WHERE TRY_CAST(TRIM(payment_installments) AS INT) = 0
GROUP BY
    payment_type,
    payment_installments
ORDER BY nombre DESC;
GO
/* Analyse détaillée des paiements avec 0 mensualité */

SELECT *
FROM staging_order_payments
WHERE TRY_CAST(TRIM(payment_installments) AS INT) = 0;
GO
/*====================================================================
    NETTOYAGE — PAYMENT_INSTALLMENTS
----------------------------------------------------------------------    
    Les paiements par carte présentant 0 mensualité sont considérés
    comme des paiements comptants.

    La valeur 0 est donc remplacée par 1.
====================================================================*/

UPDATE staging_order_payments
SET payment_installments = '1'
WHERE
    UPPER(TRIM(payment_type)) IN ('CREDIT_CARD', 'DEBIT_CARD')
    AND TRY_CAST(TRIM(payment_installments) AS INT) = 0;
GO
SELECT
    payment_type,
    payment_installments,
    COUNT(*) AS nombre
FROM staging_order_payments
WHERE
    UPPER(TRIM(payment_type)) IN ('CREDIT_CARD', 'DEBIT_CARD')
    AND TRY_CAST(TRIM(payment_installments) AS INT) = 0
GROUP BY
    payment_type,
    payment_installments;
GO