-- ============================================================
-- INSERTION DES DONNÉES NETTOYÉES DANS LA TABLE FINALE
-- ============================================================

INSERT INTO order_reviews (
    review_id,                  -- Identifiant de l'avis
    order_id,                   -- Identifiant de la commande
    review_score,               -- Note attribuée par le client
    review_comment_title,       -- Titre du commentaire
    review_comment_message,     -- Contenu du commentaire
    review_creation_date,       -- Date de création de l'avis
    review_answer_timestamp     -- Date et heure de réponse à l'avis
)

-- ============================================================
-- SÉLECTION ET TRANSFORMATION DES DONNÉES DE LA STAGING
-- ============================================================

SELECT
    -- Suppression des espaces inutiles au début et à la fin
    -- de l'identifiant de l'avis
    TRIM(review_id),

    -- Suppression des espaces inutiles autour de l'identifiant
    -- de la commande
    TRIM(order_id),

    -- Suppression des espaces puis conversion de la note
    -- du type VARCHAR vers le type INT
    -- TRY_CAST retourne NULL si la conversion échoue,
    -- au lieu de provoquer une erreur SQL
    TRY_CAST(TRIM(review_score) AS INT),

    -- Suppression des espaces inutiles et conversion du texte
    -- en majuscules pour uniformiser les données
    UPPER(TRIM(review_comment_title)),

    -- Suppression des espaces inutiles et conversion du texte
    -- en majuscules pour uniformiser les données
    UPPER(TRIM(review_comment_message)),

    -- Suppression des espaces puis conversion de la date
    -- du type texte vers DATETIME
    TRY_CAST(TRIM(review_creation_date) AS DATETIME),

    -- Suppression des espaces puis conversion du timestamp
    -- du type texte vers DATETIME
    TRY_CAST(TRIM(review_answer_timestamp) AS DATETIME)

-- ============================================================
-- SOURCE DES DONNÉES
-- ============================================================

FROM staging_order_reviews;
GO