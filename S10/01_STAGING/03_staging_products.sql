/*====================================================================
    TABLE DE STAGING : PRODUCTS
----------------------------------------------------------------------
    Objectif :
    Créer une table intermédiaire destinée à recevoir les données
    brutes des produits provenant du fichier CSV.

    Cette table constitue la première étape du processus ETL.
    Les données sont d'abord importées dans leur format brut afin
    de permettre les contrôles de qualité et les transformations
    avant leur chargement dans la table finale products.

    Colonnes :

    1. product_id
       Identifiant unique du produit.

    2. product_category_name
       Nom de la catégorie à laquelle appartient le produit.

    3. product_name_lenght
       Longueur du nom du produit.

    4. product_description_lenght
       Longueur de la description du produit.

    5. product_photos_qty
       Nombre de photos associées au produit.

    6. product_weight_g
       Poids du produit exprimé en grammes.

    7. product_length_cm
       Longueur du produit exprimée en centimètres.

    8. product_height_cm
       Hauteur du produit exprimée en centimètres.

    9. product_width_cm
       Largeur du produit exprimée en centimètres.

    Principe :
    Les colonnes contenant initialement des valeurs numériques sont
    temporairement stockées en VARCHAR afin de conserver les données
    brutes lors de l'importation.

    Les conversions vers les types numériques appropriés seront
    réalisées lors de l'étape de transformation, après vérification
    de la qualité des données.

    Prochaines étapes :
        1. Importer les données du fichier CSV.
        2. Vérifier le nombre de lignes importées.
        3. Contrôler l'unicité de product_id.
        4. Rechercher les valeurs NULL ou vides.
        5. Vérifier les formats des données numériques.
        6. Vérifier les valeurs incohérentes ou négatives.
        7. Transformer et normaliser les données.
        8. Charger les données dans la table finale products.
====================================================================*/

CREATE TABLE staging_products (
    product_id VARCHAR(255),
    product_category_name VARCHAR(255),
    product_name_lenght VARCHAR(50),
    product_description_lenght VARCHAR(50),
    product_photos_qty VARCHAR(50),
    product_weight_g VARCHAR(50),
    product_length_cm VARCHAR(50),
    product_height_cm VARCHAR(50),
    product_width_cm VARCHAR(50)
);
GO


/*--------------------------------------------------------------------
    1. IMPORTATION DES DONNÉES DU CSV
----------------------------------------------------------------------
    Objectif :
    Charger les données brutes du fichier CSV des produits dans
    la table staging_products.

    Paramètres utilisés :
        - FIELDTERMINATOR = ',' :
          Les colonnes du fichier CSV sont séparées par des virgules.

        - ROWTERMINATOR = '0x0a' :
          Définit le caractère de fin de ligne.

        - FIRSTROW = 2 :
          Ignore la première ligne contenant les noms des colonnes.

        - CODEPAGE = 'UTF-8' :
          Permet de conserver correctement les caractères accentués
          et les caractères encodés en UTF-8.

    Source :
        olist_products_dataset.csv

    Destination :
        staging_products
--------------------------------------------------------------------*/

BULK INSERT staging_products
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_products_dataset.csv'
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
    2. VÉRIFICATION APRÈS IMPORTATION
----------------------------------------------------------------------
    Objectif :
    Vérifier que les données ont correctement été importées dans
    la table staging_products.

    Contrôles :
        1. Vérifier le nombre total de lignes importées.
        2. Afficher un échantillon des données.

    Interprétation :
        - Le nombre de lignes doit être cohérent avec le fichier CSV.
        - Les colonnes doivent contenir les données attendues.
--------------------------------------------------------------------*/

-- 2.1 Nombre total de lignes importées
SELECT COUNT(*) AS total_staging_products
FROM staging_products;


-- 2.2 Vérification visuelle des données
SELECT TOP 10 *
FROM staging_products;
GO