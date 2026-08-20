USE OlistCommerce;
GO

-- ============================================================
-- VALIDATION GLOBALE DES TABLES DE PRODUCTION
-- ============================================================
-- Cette requête permet de vérifier le nombre total d'enregistrements
-- présents dans chaque table finale (tables de production).
--
-- Elle sert notamment à :
--   1. Vérifier que les données ont bien été chargées.
--   2. Comparer les volumes de données avec les tables de staging.
--   3. Détecter rapidement une table vide ou incomplètement chargée.
--   4. Effectuer un contrôle général après les transformations ETL.
-- ============================================================


-- Sélection du nombre d'enregistrements présents dans la table customers
SELECT
    'customers' AS Table_Nom,
    COUNT(*) AS Total_Enregistrements
FROM customers

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table sellers
SELECT
    'sellers',
    COUNT(*)
FROM sellers

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table products
SELECT
    'products',
    COUNT(*)
FROM products

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table
-- de traduction des catégories de produits
SELECT
    'product_category_name_translation',
    COUNT(*)
FROM product_category_name_translation

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table orders
SELECT
    'orders',
    COUNT(*)
FROM orders

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table order_items
SELECT
    'order_items',
    COUNT(*)
FROM order_items

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table
-- des paiements associés aux commandes
SELECT
    'order_payments',
    COUNT(*)
FROM order_payments

UNION ALL

-- Sélection du nombre d'enregistrements présents dans la table
-- des avis clients
SELECT
    'order_reviews',
    COUNT(*)
FROM order_reviews;

GO


-- ============================================================
-- RÉSULTAT ATTENDU
-- ============================================================
-- La requête retourne un tableau contenant deux colonnes :
--
--   Table_Nom              | Total_Enregistrements
--   ------------------------------------------------
--   customers              | nombre de lignes
--   sellers                 | nombre de lignes
--   products                | nombre de lignes
--   product_category...     | nombre de lignes
--   orders                  | nombre de lignes
--   order_items             | nombre de lignes
--   order_payments          | nombre de lignes
--   order_reviews           | nombre de lignes
--
-- Une valeur de 0 peut indiquer qu'une table n'a pas été chargée.
-- Une différence inattendue avec les données sources peut également
-- signaler un problème lors de l'importation ou de la transformation.
-- ============================================================