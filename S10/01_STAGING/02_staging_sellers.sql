/*====================================================================
    TABLE DE STAGING : SELLERS
----------------------------------------------------------------------
    Objectif :
    Créer une table intermédiaire destinée à recevoir les données
    brutes des vendeurs provenant du fichier CSV.

    Cette table constitue la première étape du processus ETL.
    Les données y sont stockées avant d'être contrôlées, nettoyées,
    transformées puis chargées dans la table finale sellers.

    Colonnes :
    
    1. seller_id
       Identifiant du vendeur.
       Stocké temporairement en VARCHAR afin de conserver les données
       brutes avant la validation de son format et de son unicité.

    2. seller_zip_code_prefix
       Préfixe du code postal du vendeur.
       Stocké temporairement en VARCHAR afin de préserver les données
       originales lors de l'importation.

    3. seller_city
       Ville dans laquelle se situe le vendeur.
       La valeur brute est conservée avant les opérations éventuelles
       de nettoyage et de normalisation.

    4. seller_state
       Code de l'État brésilien associé au vendeur.
       La valeur brute est conservée avant les contrôles de format
       et la normalisation.

    Principe :
    La table de staging ne contient volontairement aucune contrainte
    métier telle que PRIMARY KEY, FOREIGN KEY ou NOT NULL.
    Les contraintes seront envisagées après les contrôles de qualité.

    Prochaines étapes :
        1. Importer les données du fichier CSV.
        2. Vérifier le nombre de lignes importées.
        3. Contrôler l'unicité de seller_id.
        4. Rechercher les valeurs NULL ou vides.
        5. Vérifier le format du code postal.
        6. Vérifier le format de seller_state.
        7. Transformer et normaliser les données.
        8. Charger les données dans la table finale sellers.
====================================================================*/

CREATE TABLE staging_sellers (
    seller_id VARCHAR(100),
    seller_zip_code_prefix VARCHAR(50),
    seller_city VARCHAR(255),
    seller_state VARCHAR(50)
);
GO


/*--------------------------------------------------------------------
    1. IMPORTATION DES DONNÉES DU CSV
----------------------------------------------------------------------
    Objectif :
    Charger les données brutes du fichier CSV des vendeurs dans la
    table staging_sellers.

    Paramètres utilisés :
        - FIELDTERMINATOR = ',' :
          Les colonnes du fichier CSV sont séparées par des virgules.

        - ROWTERMINATOR = '0x0a' :
          Définit le caractère de fin de ligne du fichier.

        - FIRSTROW = 2 :
          Ignore la première ligne contenant les noms des colonnes.

        - CODEPAGE = 'UTF-8' :
          Permet de conserver correctement les caractères encodés
          en UTF-8, notamment les caractères accentués.

    Source :
        olist_sellers_dataset.csv

    Destination :
        staging_sellers
--------------------------------------------------------------------*/

BULK INSERT staging_sellers
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_sellers_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    FIELDQUOTE = '"',
    FIRSTROW = 2,
    CODEPAGE = 'UTF-8'
);
GO


/*--------------------------------------------------------------------
    2. VÉRIFICATION APRÈS IMPORTATION
----------------------------------------------------------------------
    Objectif :
    Vérifier que les données du fichier CSV ont correctement été
    chargées dans la table de staging.

    Contrôles effectués :
        1. Vérifier le nombre total de lignes importées.
        2. Afficher un échantillon des données importées.

    Interprétation :
        - Le nombre de lignes doit être cohérent avec le fichier CSV.
        - Les premières lignes doivent présenter une structure
          conforme aux colonnes de staging_sellers.
--------------------------------------------------------------------*/

-- 2.1 Vérification du nombre total de lignes importées
SELECT COUNT(*) AS total_staging_sellers
FROM staging_sellers;


-- 2.2 Vérification visuelle des premières lignes
SELECT TOP 5 *
FROM staging_sellers;
GO