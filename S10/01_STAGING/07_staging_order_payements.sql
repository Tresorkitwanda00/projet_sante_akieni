/*====================================================================
    TABLE DE STAGING : ORDER_PAYMENTS
----------------------------------------------------------------------    
    Objectif :
    Créer une table intermédiaire destinée à recevoir les données
    brutes des paiements provenant du fichier CSV.

    La staging table permet de conserver les données originales avant
    les contrôles de qualité, les conversions de types et la
    normalisation.

    Colonnes :

    1. order_id
       Identifiant de la commande.

    2. payment_sequential
       Numéro séquentiel du paiement associé à la commande.

    3. payment_type
       Type de paiement utilisé par le client.

    4. payment_installments
       Nombre de mensualités du paiement.

    5. payment_value
       Montant du paiement.

    Principe :
    Aucune contrainte métier n'est appliquée dans la staging table.
    Les contraintes seront appliquées dans la table finale après
    validation des données.
====================================================================*/

CREATE TABLE staging_order_payments (
    order_id VARCHAR(50),
    payment_sequential VARCHAR(50),
    payment_type VARCHAR(50),
    payment_installments VARCHAR(50),
    payment_value VARCHAR(50)
);
GO
/*====================================================================
    IMPORT DES DONNÉES BRUTES
----------------------------------------------------------------------    
    Chargement du fichier CSV dans la table staging_order_payments.
====================================================================*/

BULK INSERT staging_order_payments
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_order_payments_dataset.csv'
WITH (
    FORMAT = 'CSV',
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    FIRSTROW = 2,
    CODEPAGE = 'UTF-8'
);
GO
/* Vérification du nombre total de lignes importées */
SELECT COUNT(*) AS total_staging_order_payments
FROM staging_order_payments;
GO

/* Aperçu des premières lignes */
SELECT TOP 20 *
FROM staging_order_payments;
GO