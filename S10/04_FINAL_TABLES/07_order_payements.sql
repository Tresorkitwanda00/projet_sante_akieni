/*====================================================================
    SCRIPT FINAL : ORDER_PAYMENTS
====================================================================*/


/*====================================================================
    3. CONTRÔLE DU NOMBRE DE LIGNES
====================================================================*/

SELECT
    COUNT(*) AS total_order_payments
FROM order_payments;
GO


/*====================================================================
    4. APERÇU DES DONNÉES FINALES
====================================================================*/

SELECT TOP 20 *
FROM order_payments;
GO


/*====================================================================
    5. CONTRÔLE DES TYPES DE PAIEMENT
====================================================================*/

SELECT
    payment_type,
    COUNT(*) AS nombre_paiements
FROM order_payments
GROUP BY payment_type
ORDER BY nombre_paiements DESC;
GO


/*====================================================================
    6. CONTRÔLE DE L'UNICITÉ DE LA CLÉ PRIMAIRE
----------------------------------------------------------------------    
    La combinaison order_id + payment_sequential doit être unique.
====================================================================*/

SELECT
    order_id,
    payment_sequential,
    COUNT(*) AS nombre
FROM order_payments
GROUP BY
    order_id,
    payment_sequential
HAVING COUNT(*) > 1;
GO


/*====================================================================
    7. CONTRÔLE DE L'INTÉGRITÉ RÉFÉRENTIELLE
----------------------------------------------------------------------    
    Vérifie que chaque paiement possède une commande correspondante.
====================================================================*/

SELECT
    p.order_id
FROM order_payments AS p
LEFT JOIN orders AS o
    ON p.order_id = o.order_id
WHERE o.order_id IS NULL;
GO


/*====================================================================
    FIN DU SCRIPT FINAL : ORDER_PAYMENTS
====================================================================*/