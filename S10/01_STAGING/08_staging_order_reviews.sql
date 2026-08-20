-- ============================================================
-- ÉTAPE 1 : CRÉATION DE LA TABLE DE STAGING
-- ============================================================
-- Cette table temporaire/logique sert à recevoir les données
-- brutes du fichier CSV des avis clients (order reviews).
--
-- On utilise principalement le type VARCHAR pour les colonnes
-- qui proviennent directement du CSV afin d'éviter les erreurs
-- de conversion lors du chargement initial.
-- Les transformations et conversions seront effectuées
-- ultérieurement lors du passage vers la table finale.
-- ============================================================

CREATE TABLE staging_order_reviews (

    -- Identifiant unique de l'avis client
    review_id VARCHAR(100),

    -- Identifiant de la commande concernée par l'avis
    order_id VARCHAR(100),

    -- Note attribuée par le client, conservée temporairement
    -- en VARCHAR afin d'éviter une erreur de conversion
    -- pendant l'importation du fichier CSV
    review_score VARCHAR(50),

    -- Titre du commentaire de l'avis.
    -- NVARCHAR(MAX) permet de stocker des textes longs
    -- et prend également en charge les caractères Unicode.
    review_comment_title NVARCHAR(MAX),

    -- Message détaillé laissé par le client.
    -- NVARCHAR(MAX) permet de stocker un texte de longueur variable.
    review_comment_message NVARCHAR(MAX),

    -- Date de création de l'avis.
    -- Elle est d'abord chargée sous forme de texte (VARCHAR)
    -- puis pourra être convertie en DATE/DATETIME dans la table finale.
    review_creation_date VARCHAR(100),

    -- Date et heure de réponse à l'avis.
    -- Conservée temporairement sous forme de texte avant transformation.
    review_answer_timestamp VARCHAR(100)
);
GO


-- ============================================================
-- ÉTAPE 2 : CHARGEMENT DES DONNÉES DU FICHIER CSV
-- ============================================================
-- BULK INSERT permet d'importer rapidement un grand volume
-- de données depuis un fichier CSV vers SQL Server.
-- ============================================================

BULK INSERT staging_order_reviews

-- Chemin complet vers le fichier CSV contenant les avis clients
FROM 'D:\Programme Akieni\Programme Akieni\DataScience\projet_sante_akieni\S10\00_DATASOURCE\olist_order_reviews_dataset.csv'

WITH (

    -- La première ligne du fichier contient les noms des colonnes.
    -- Elle est donc ignorée lors de l'importation.
    FIRSTROW = 2,

    -- Indique que le fichier est au format CSV.
    -- SQL Server gère ainsi les séparateurs et les champs entourés
    -- de guillemets, notamment lorsque les commentaires contiennent
    -- des virgules.
    FORMAT = 'CSV',

    -- 65001 correspond à l'encodage UTF-8.
    -- Cela permet de conserver correctement les caractères
    -- accentués et autres caractères Unicode présents dans les données.
    CODEPAGE = '65001'
);
GO

SELECT COUNT(*) AS nombres_lignes FROM staging_order_reviews
SELECT TOP 300 * FROM staging_order_reviews