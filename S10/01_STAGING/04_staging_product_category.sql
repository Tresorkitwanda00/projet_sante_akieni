/*====================================================================
    TABLE DE STAGING : PRODUCT CATEGORY NAME TRANSLATION
----------------------------------------------------------------------
    Objectif :
    Créer une table intermédiaire destinée à recevoir les données
    brutes de traduction des catégories de produits provenant du
    fichier CSV.

    Cette table constitue la première étape du processus ETL.

    Les données seront d'abord importées dans leur format brut,
    puis contrôlées et nettoyées avant leur chargement dans la table
    finale product_category_name_translation.

    Colonnes :

    1. product_category_name
       Nom de la catégorie dans la langue d'origine.

    2. product_category_name_english
       Traduction anglaise de la catégorie.

    Principe :
    Aucune contrainte PRIMARY KEY n'est appliquée dans la staging
    afin de pouvoir détecter d'éventuels doublons avant le chargement
    dans la table finale.

    Prochaines étapes :
        1. Importer les données du CSV.
        2. Vérifier le nombre de lignes.
        3. Contrôler l'unicité de product_category_name.
        4. Rechercher les valeurs NULL ou vides.
        5. Vérifier les doublons.
        6. Nettoyer les espaces et normaliser les valeurs.
        7. Charger les données dans la table finale.
        8. Effectuer les contrôles finaux.
====================================================================*/

CREATE TABLE staging_product_category_name_translation (
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100)
);
GO
/*--------------------------------------------------------------------
    IMPORTATION DES DONNÉES DU CSV
--------------------------------------------------------------------*/

BULK INSERT staging_product_category_name_translation
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\product_category_name_translation.csv'
WITH (
    FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    FIRSTROW = 2,
    CODEPAGE = 'UTF-8'
);
GO
/*--------------------------------------------------------------------
    VÉRIFICATION APRÈS IMPORTATION
--------------------------------------------------------------------*/

SELECT COUNT(*) AS total_staging_categories
FROM staging_product_category_name_translation;

SELECT TOP 20 *
FROM staging_product_category_name_translation;
GO