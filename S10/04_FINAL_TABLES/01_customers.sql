/*--------------------------------------------------------------------
    VÉRIFICATION FINALE DE LA TABLE CUSTOMERS
----------------------------------------------------------------------
    Objectif :
    Effectuer un dernier contrôle de la table finale après
    transformation et chargement afin de s'assurer que les données
    sont correctement intégrées et prêtes pour l'utilisation.
--------------------------------------------------------------------*/

-- Nombre total de clients chargés
SELECT COUNT(*) AS nombre_clients
FROM customers;


-- Vérification de l'unicité de customer_id
SELECT
    customer_id,
    COUNT(*) AS nombre_occurrences
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- Aperçu des données finales
SELECT TOP 20 *
FROM customers;