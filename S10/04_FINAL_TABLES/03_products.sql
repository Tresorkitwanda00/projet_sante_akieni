/*====================================================================
    VÉRIFICATION FINALE : TABLE PRODUCTS
----------------------------------------------------------------------
    Objectif :
    Vérifier que les données ont correctement été chargées dans la
    table finale products après les différentes étapes du processus ETL.

    1. Vérification du nombre total de lignes
       Cette requête permet de contrôler le volume de données présent
       dans la table finale après le chargement.

    2. Vérification d'un échantillon de données
       La requête TOP 20 permet d'examiner rapidement les premières
       lignes afin de vérifier visuellement que les données ont été
       correctement transformées et chargées.

    Contrôles effectués :
        - Présence des données dans la table finale.
        - Cohérence générale des valeurs.
        - Vérification des valeurs transformées.
        - Vérification des valeurs par défaut telles que
          'NON_SPECIFIE' et 0.
        - Vérification de la structure générale des données.

    Cette étape constitue un contrôle de validation après le
    chargement de la table products.
====================================================================*/

-- 1. Vérification du nombre total de produits chargés
SELECT COUNT(*) AS nombre_lignes
FROM products;

-- 2. Vérification visuelle d'un échantillon des données
SELECT TOP 20 *
FROM products;
GO