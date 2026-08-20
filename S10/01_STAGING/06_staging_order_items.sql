/*====================================================================
    TABLE DE STAGING : ORDER_ITEMS
----------------------------------------------------------------------
    Objectif :
    Créer une table intermédiaire destinée à recevoir les données
    brutes des articles de commande provenant du fichier CSV.

    Cette table constitue la première étape du processus ETL.
    Les données sont conservées dans leur format brut avant les
    contrôles de qualité, les nettoyages et les transformations.

    Colonnes :

    1. order_id
       Identifiant de la commande.
       Stocké temporairement en VARCHAR afin de conserver la donnée
       brute avant validation.

    2. order_item_id
       Numéro de l'article dans une commande.
       Stocké en VARCHAR dans le staging afin d'éviter une erreur
       lors de l'importation et de permettre une conversion contrôlée
       vers INT lors de la transformation.

    3. product_id
       Identifiant du produit associé à l'article.

    4. seller_id
       Identifiant du vendeur associé à l'article.

    5. shipping_limit_date
       Date limite d'expédition de l'article.
       Conservée temporairement en VARCHAR afin de contrôler son
       format avant conversion vers DATETIME.

    6. price
       Prix du produit.
       Conservé en VARCHAR dans le staging afin de contrôler les
       valeurs numériques avant conversion vers DECIMAL(10,2).

    7. freight_value
       Montant des frais de transport.
       Conservé en VARCHAR afin de contrôler et nettoyer les valeurs
       avant conversion numérique.

    Principe :
    Aucune PRIMARY KEY, FOREIGN KEY ou contrainte NOT NULL n'est
    appliquée à cette étape.

    Les contraintes seront appliquées uniquement dans la table finale
    après validation de la qualité des données.

    Prochaines étapes :
        1. Importer le fichier CSV.
        2. Vérifier le nombre de lignes.
        3. Contrôler les doublons.
        4. Contrôler les valeurs NULL ou vides.
        5. Contrôler les formats numériques.
        6. Contrôler les dates.
        7. Vérifier les relations avec orders, products et sellers.
        8. Transformer les données.
        9. Charger la table finale order_items.
====================================================================*/

CREATE TABLE staging_order_items (
    order_id VARCHAR(50),
    order_item_id VARCHAR(50),
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date VARCHAR(100),
    price VARCHAR(50),
    freight_value VARCHAR(50)
);
GO
/*====================================================================
    ÉTAPE 2 : IMPORT DES DONNÉES BRUTES
----------------------------------------------------------------------
    Objectif :
    Importer le fichier CSV des articles de commande dans la table
    staging_order_items.

    À ce stade, aucune transformation ni conversion métier n'est
    effectuée. Les données sont conservées dans leur format brut
    afin de permettre les contrôles de qualité lors de l'étape
    suivante.
====================================================================*/

BULK INSERT staging_order_items
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_order_items_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    FIRSTROW = 2,
    CODEPAGE = 'UTF-8'
);
GO


/*====================================================================
    VÉRIFICATION DU NOMBRE DE LIGNES IMPORTÉES
====================================================================*/

SELECT 
    COUNT(*) AS total_staging_order_items
FROM staging_order_items;
GO


/*====================================================================
    APERÇU DES DONNÉES IMPORTÉES
====================================================================*/

SELECT TOP 20 *
FROM staging_order_items;
GO