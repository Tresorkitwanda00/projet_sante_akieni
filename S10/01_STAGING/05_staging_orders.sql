/*====================================================================
    TABLE DE STAGING : ORDERS
----------------------------------------------------------------------
    Objectif :
    Recevoir les données brutes du fichier CSV des commandes.

    Les colonnes sont volontairement stockées en VARCHAR afin de
    permettre l'importation complète des données avant les contrôles
    de qualité et les conversions de types.

    Les types définitifs seront appliqués lors du chargement dans
    la table finale orders.
====================================================================*/

CREATE TABLE staging_orders (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(50),
    order_purchase_timestamp VARCHAR(50),
    order_approved_at VARCHAR(50),
    order_delivered_carrier_date VARCHAR(50),
    order_delivered_customer_date VARCHAR(50),
    order_estimated_delivery_date VARCHAR(50)
);
GO
/*====================================================================
    IMPORTATION DES DONNÉES DU CSV
====================================================================*/

BULK INSERT staging_orders
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_orders_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    FIRSTROW = 2,
    CODEPAGE = 'UTF-8'
);
GO
/*====================================================================
    VÉRIFICATION APRÈS IMPORTATION
====================================================================*/

-- Vérification du nombre de commandes importées
SELECT COUNT(*) AS nombre_lignes
FROM staging_orders;

-- Vérification d'un échantillon des données
SELECT TOP 20 *
FROM staging_orders;
GO