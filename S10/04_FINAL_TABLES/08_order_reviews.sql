-- ============================================================
-- CONTRÔLE FINAL DE LA TABLE order_reviews
-- ============================================================

-- 1. Vérifier le nombre total de lignes
SELECT
    COUNT(*) AS total_lignes
FROM order_reviews;
GO


-- 2. Vérifier les identifiants et l'unicité du couple
--    review_id + order_id
SELECT
    COUNT(*) AS total_lignes,
    COUNT(DISTINCT review_id) AS review_ids_uniques,
    COUNT(DISTINCT CONCAT(review_id, '|', order_id)) AS couples_uniques
FROM order_reviews;
GO


-- 3. Vérifier les valeurs manquantes
SELECT
    SUM(CASE
        WHEN review_id IS NULL OR TRIM(review_id) = ''
        THEN 1 ELSE 0
    END) AS review_id_manquant,

    SUM(CASE
        WHEN order_id IS NULL OR TRIM(order_id) = ''
        THEN 1 ELSE 0
    END) AS order_id_manquant,

    SUM(CASE
        WHEN review_score IS NULL
        THEN 1 ELSE 0
    END) AS review_score_manquant,

    SUM(CASE
        WHEN review_comment_title IS NULL
          OR TRIM(review_comment_title) = ''
        THEN 1 ELSE 0
    END) AS titre_manquant,

    SUM(CASE
        WHEN review_comment_message IS NULL
          OR TRIM(review_comment_message) = ''
        THEN 1 ELSE 0
    END) AS message_manquant,

    SUM(CASE
        WHEN review_creation_date IS NULL
        THEN 1 ELSE 0
    END) AS date_creation_manquante,

    SUM(CASE
        WHEN review_answer_timestamp IS NULL
        THEN 1 ELSE 0
    END) AS date_reponse_manquante

FROM order_reviews;
GO


-- 4. Vérifier que les valeurs de remplacement
--    no_title et no_comment sont bien présentes
SELECT
    COUNT(*) AS nombre_no_title
FROM order_reviews
WHERE review_comment_title = 'NO_TITLE';
GO

SELECT
    COUNT(*) AS nombre_no_comment
FROM order_reviews
WHERE review_comment_message = 'NO_COMMENT';
GO


-- 5. Vérifier que les commentaires sont bien en majuscules
SELECT TOP 20
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message
FROM order_reviews
ORDER BY review_id;
GO


-- 6. Vérifier les types des colonnes
SELECT
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'order_reviews'
ORDER BY ORDINAL_POSITION;
GO