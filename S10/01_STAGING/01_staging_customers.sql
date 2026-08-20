/*====================================================================
    PROJET : CONTRÔLE ET PRÉPARATION DES DONNÉES OLIST
    TABLE   : CUSTOMERS
    ÉTAPE   : STAGING ET CONTRÔLES DE QUALITÉ DES DONNÉES
====================================================================*/


/*--------------------------------------------------------------------
    1. CRÉATION DE LA TABLE DE STAGING
----------------------------------------------------------------------
    Objectif :
    Créer une table temporaire/intermédiaire permettant de recevoir
    les données brutes provenant du fichier CSV avant toute
    transformation ou intégration dans le modèle final.

    Principe :
    - Les données sont volontairement stockées sous forme relativement
      souple afin de pouvoir détecter les éventuelles anomalies.
    - Les contraintes métier (PK, FK, NOT NULL, etc.) seront appliquées
      après validation de la qualité des données.
--------------------------------------------------------------------*/

CREATE TABLE staging_customers (
    customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix VARCHAR(10),
    customer_city VARCHAR(100),
    customer_state CHAR(2)
);
GO


/*--------------------------------------------------------------------
    2. IMPORTATION DES DONNÉES DU CSV VERS LA TABLE DE STAGING
----------------------------------------------------------------------
    Objectif :
    Charger les données brutes du fichier CSV dans la table
    staging_customers.

    Paramètres importants :
    - FIELDTERMINATOR = ',' :
      Les colonnes du fichier CSV sont séparées par des virgules.

    - ROWTERMINATOR = '0x0a' :
      Indique la fin de chaque ligne du fichier.

    - FIRSTROW = 2 :
      Ignore la première ligne du fichier, qui contient les noms
      des colonnes.

    - CODEPAGE = 'UTF-8' :
      Permet de conserver correctement les caractères accentués
      et autres caractères Unicode présents dans le fichier.
--------------------------------------------------------------------*/

BULK INSERT staging_customers
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_customers_dataset.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    FIRSTROW = 2,
    CODEPAGE = 'UTF-8'
);
GO


/*--------------------------------------------------------------------
    3. VÉRIFICATION APRÈS IMPORTATION
----------------------------------------------------------------------
    Objectif :
    Vérifier que les données ont correctement été chargées dans
    la table de staging.

    Contrôles effectués :
    1. Vérifier le nombre total de lignes importées.
    2. Afficher un échantillon des premières lignes afin de contrôler
       visuellement la structure et le contenu des données.

    Résultat attendu :
    - Le nombre de lignes doit être cohérent avec le fichier CSV.
    - Les colonnes doivent contenir les valeurs attendues.
--------------------------------------------------------------------*/

-- 3.1 Vérification du nombre total de lignes importées
SELECT COUNT(*) AS nombre_lignes
FROM staging_customers;


-- 3.2 Vérification visuelle d'un échantillon des données
SELECT TOP 20 *
FROM staging_customers;

