
-- ============================================================
-- DATA QUALITY - TABLE : staging_order_reviews
-- ============================================================
-- Objectif :
-- Vérifier la qualité des données AVANT de les transformer
-- et de les charger dans la table finale.
--
-- Les contrôles portent sur :
--   1. Volume des données
--   2. Valeurs NULL / vides
--   3. Doublons
--   4. Validité des review_score
--   5. Validité des dates
--   6. Cohérence temporelle
--   7. Distribution des notes
-- ============================================================


-- ============================================================
-- 1. NOMBRE TOTAL DE LIGNES
-- ============================================================
-- Permet de connaître le volume réellement importé.
-- C'est le premier contrôle à effectuer après un BULK INSERT.

SELECT
    COUNT(*) AS total_lignes
FROM staging_order_reviews;
GO


-- ============================================================
-- 2. APERÇU DES DONNÉES
-- ============================================================
-- Permet de vérifier visuellement si les données semblent
-- correctement importées dans les différentes colonnes.

SELECT TOP 20 *
FROM staging_order_reviews;
GO


-- ============================================================
-- 3. CONTRÔLE DES VALEURS MANQUANTES
-- ============================================================
-- On recherche :
--   - les valeurs NULL
--   - les chaînes vides ''
--   - les valeurs contenant uniquement des espaces
--
-- Pourquoi ?
-- Les valeurs manquantes peuvent avoir un impact sur les
-- analyses statistiques et les indicateurs futurs.

SELECT
    COUNT(*) AS total_lignes,

    SUM(CASE
        WHEN review_id IS NULL
          OR TRIM(review_id) = ''
        THEN 1 ELSE 0
    END) AS review_id_manquant,

    SUM(CASE
        WHEN order_id IS NULL
          OR TRIM(order_id) = ''
        THEN 1 ELSE 0
    END) AS order_id_manquant,

    SUM(CASE
        WHEN review_score IS NULL
          OR TRIM(review_score) = ''
        THEN 1 ELSE 0
    END) AS review_score_manquant,

    SUM(CASE
        WHEN review_comment_title IS NULL
          OR TRIM(review_comment_title) = ''
        THEN 1 ELSE 0
    END) AS review_comment_title_manquant,

    SUM(CASE
        WHEN review_comment_message IS NULL
          OR TRIM(review_comment_message) = ''
        THEN 1 ELSE 0
    END) AS review_comment_message_manquant,

    SUM(CASE
        WHEN review_creation_date IS NULL
          OR TRIM(review_creation_date) = ''
        THEN 1 ELSE 0
    END) AS review_creation_date_manquante,

    SUM(CASE
        WHEN review_answer_timestamp IS NULL
          OR TRIM(review_answer_timestamp) = ''
        THEN 1 ELSE 0
    END) AS review_answer_timestamp_manquant

FROM staging_order_reviews;
GO


-- ============================================================
-- 4. TAUX DE VALEURS MANQUANTES
-- ============================================================
-- Le nombre de valeurs manquantes seul ne suffit pas.
-- On calcule également leur pourcentage.
--
-- Exemple :
-- 1 000 valeurs manquantes sur 100 000 lignes = 1 %
-- 1 000 valeurs manquantes sur 2 000 lignes = 50 %
--
-- L'impact Data Quality est donc très différent.

SELECT
    COUNT(*) AS total_lignes,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN review_score IS NULL
                  OR TRIM(review_score) = ''
                THEN 1 ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS taux_review_score_manquant,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN review_comment_message IS NULL
                  OR TRIM(review_comment_message) = ''
                THEN 1 ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS taux_commentaire_manquant,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN review_answer_timestamp IS NULL
                  OR TRIM(review_answer_timestamp) = ''
                THEN 1 ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS taux_date_reponse_manquante

FROM staging_order_reviews;
GO


-- ============================================================
-- 5. CONTRÔLE DE L'UNICITÉ DE review_id
-- ============================================================
-- review_id représente l'identifiant de l'avis.
--
-- On recherche les identifiants apparaissant plusieurs fois.
-- Attention : une répétition doit être analysée avant de
-- supprimer automatiquement les lignes.

SELECT
    review_id,
    COUNT(*) AS nombre_occurrences
FROM staging_order_reviews
GROUP BY review_id
HAVING COUNT(*) > 1
ORDER BY nombre_occurrences DESC;
GO


-- ============================================================
-- 6. NOMBRE DE DOUBLONS POTENTIELS
-- ============================================================
-- Permet d'obtenir une vision globale des répétitions
-- d'identifiants review_id.

SELECT
    COUNT(*) AS total_lignes,
    COUNT(DISTINCT review_id) AS review_id_uniques,
    COUNT(*) - COUNT(DISTINCT review_id) AS difference
FROM staging_order_reviews;
GO


-- ============================================================
-- 7. CONTRÔLE DE review_score
-- ============================================================
-- Dans le dataset Olist, review_score doit être compris
-- entre 1 et 5.
--
-- Comme la colonne est actuellement VARCHAR, on utilise
-- TRY_CONVERT() pour tester si les valeurs peuvent être
-- converties correctement en nombre entier.

SELECT
    review_score,
    COUNT(*) AS nombre_observations
FROM staging_order_reviews
GROUP BY review_score
ORDER BY review_score;
GO


-- ============================================================
-- 8. DÉTECTION DES review_score INVALIDES
-- ============================================================
-- Cette requête détecte :
--   - les valeurs non numériques
--   - les valeurs inférieures à 1
--   - les valeurs supérieures à 5
--
-- TRY_CONVERT() retourne NULL lorsqu'une conversion est
-- impossible, sans provoquer l'arrêt de la requête.

SELECT *
FROM staging_order_reviews
WHERE
    review_score IS NOT NULL
    AND TRIM(review_score) <> ''
    AND (
        TRY_CONVERT(INT, review_score) IS NULL
        OR TRY_CONVERT(INT, review_score) NOT BETWEEN 1 AND 5
    );
GO


-- ============================================================
-- 9. CONTRÔLE DES DATES DE CRÉATION
-- ============================================================
-- On vérifie si les valeurs présentes dans
-- review_creation_date peuvent être converties en DATETIME.

SELECT *
FROM staging_order_reviews
WHERE
    review_creation_date IS NOT NULL
    AND TRIM(review_creation_date) <> ''
    AND TRY_CONVERT(
        DATETIME,
        review_creation_date
    ) IS NULL;
GO


-- ============================================================
-- 10. CONTRÔLE DES DATES DE RÉPONSE
-- ============================================================
-- Même contrôle pour review_answer_timestamp.

SELECT *
FROM staging_order_reviews
WHERE
    review_answer_timestamp IS NOT NULL
    AND TRIM(review_answer_timestamp) <> ''
    AND TRY_CONVERT(
        DATETIME,
        review_answer_timestamp
    ) IS NULL;
GO


-- ============================================================
-- 11. INTERVALLE DES DATES
-- ============================================================
-- On recherche la date la plus ancienne et la date la plus
-- récente pour vérifier que les données temporelles semblent
-- cohérentes.

SELECT
    MIN(
        TRY_CONVERT(DATETIME, review_creation_date)
    ) AS date_creation_min,

    MAX(
        TRY_CONVERT(DATETIME, review_creation_date)
    ) AS date_creation_max,

    MIN(
        TRY_CONVERT(DATETIME, review_answer_timestamp)
    ) AS date_reponse_min,

    MAX(
        TRY_CONVERT(DATETIME, review_answer_timestamp)
    ) AS date_reponse_max

FROM staging_order_reviews;
GO


-- ============================================================
-- 12. COHÉRENCE TEMPORELLE
-- ============================================================
-- Une réponse à un avis ne devrait normalement pas être
-- antérieure à la création de cet avis.
--
-- On détecte donc les éventuelles incohérences.

SELECT
    review_id,
    order_id,
    review_creation_date,
    review_answer_timestamp
FROM staging_order_reviews
WHERE
    TRY_CONVERT(
        DATETIME,
        review_answer_timestamp
    )
    <
    TRY_CONVERT(
        DATETIME,
        review_creation_date
    );
GO


-- ============================================================
-- 13. DISTRIBUTION DES NOTES
-- ============================================================
-- Cette requête permet d'observer la fréquence de chaque note.
--
-- Elle constitue également une première étape d'analyse
-- exploratoire (EDA).
--
-- On cherche notamment à savoir si les notes sont fortement
-- concentrées sur certaines valeurs.

SELECT
    TRY_CONVERT(INT, review_score) AS review_score,
    COUNT(*) AS nombre_avis
FROM staging_order_reviews
WHERE
    TRY_CONVERT(INT, review_score) BETWEEN 1 AND 5
GROUP BY
    TRY_CONVERT(INT, review_score)
ORDER BY
    review_score;
GO


-- ============================================================
-- 14. POURCENTAGE DE CHAQUE NOTE
-- ============================================================
-- Permet de comparer les proportions plutôt que seulement
-- les nombres absolus.

SELECT
    TRY_CONVERT(INT, review_score) AS review_score,

    COUNT(*) AS nombre_avis,

    ROUND(
        100.0 * COUNT(*)
        / SUM(COUNT(*)) OVER (),
        2
    ) AS pourcentage
FROM staging_order_reviews
WHERE
    TRY_CONVERT(INT, review_score) BETWEEN 1 AND 5
GROUP BY
    TRY_CONVERT(INT, review_score)
ORDER BY
    review_score;
GO


-- ============================================================
-- 15. STATISTIQUES DESCRIPTIVES SUR review_score
-- ============================================================
-- Avant de réaliser un test d'hypothèse, on commence par
-- comprendre la variable étudiée.
--
-- On calcule :
--   - nombre d'observations
--   - minimum
--   - maximum
--   - moyenne
--
-- Ces informations constituent la base de l'analyse
-- exploratoire.

SELECT

    COUNT(*) AS nombre_avis,

    MIN(
        TRY_CONVERT(INT, review_score)
    ) AS note_minimale,

    MAX(
        TRY_CONVERT(INT, review_score)
    ) AS note_maximale,

    AVG(
        CAST(
            TRY_CONVERT(INT, review_score)
            AS FLOAT
        )
    ) AS note_moyenne

FROM staging_order_reviews
WHERE
    TRY_CONVERT(INT, review_score) BETWEEN 1 AND 5;
GO


-- ============================================================
-- 16. IDENTIFICATION DES AVIS AVEC ET SANS RÉPONSE
-- ============================================================
-- Cette information pourra être utilisée plus tard pour
-- construire une hypothèse statistique.
--
-- Exemple de question :
--
-- "Les clients ayant reçu une réponse donnent-ils des notes
-- différentes de ceux qui n'ont pas reçu de réponse ?"

SELECT

    CASE
        WHEN review_answer_timestamp IS NULL
          OR TRIM(review_answer_timestamp) = ''
        THEN 'Sans réponse'
        ELSE 'Avec réponse'
    END AS groupe,

    COUNT(*) AS nombre_avis

FROM staging_order_reviews

GROUP BY

    CASE
        WHEN review_answer_timestamp IS NULL
          OR TRIM(review_answer_timestamp) = ''
        THEN 'Sans réponse'
        ELSE 'Avec réponse'
    END;
GO


-- ============================================================
-- 17. PREMIÈRE ANALYSE COMPARATIVE
-- ============================================================
-- On compare la note moyenne entre :
--
--   Groupe 1 : avis avec réponse
--   Groupe 2 : avis sans réponse
--
-- ATTENTION :
-- Cette requête ne constitue PAS encore un test statistique.
-- Elle fournit seulement une statistique descriptive.
--
-- Le test d'hypothèse sera réalisé ensuite avec Python/R
-- selon le test statistique approprié.

SELECT

    CASE
        WHEN review_answer_timestamp IS NULL
          OR TRIM(review_answer_timestamp) = ''
        THEN 'Sans réponse'
        ELSE 'Avec réponse'
    END AS groupe,

    COUNT(*) AS nombre_avis,

    AVG(
        CAST(
            TRY_CONVERT(INT, review_score)
            AS FLOAT
        )
    ) AS note_moyenne

FROM staging_order_reviews

WHERE
    TRY_CONVERT(INT, review_score) BETWEEN 1 AND 5

GROUP BY

    CASE
        WHEN review_answer_timestamp IS NULL
          OR TRIM(review_answer_timestamp) = ''
        THEN 'Sans réponse'
        ELSE 'Avec réponse'
    END;
GO
--------------------hpothese 5 -----------------------------------
/*

Contrôle des doublons : l'analyse de la table staging_order_reviews 
révèle 99 224 lignes et 98 410 review_id distincts. Toutefois, 
la combinaison review_id + order_id compte également 99 224 valeurs distinctes, 
soit exactement le nombre total de lignes. Il n'existe donc aucun doublon sur cette combinaison. 
Les 789 review_id apparaissant plusieurs fois correspondent à des avis associés à plusieurs
commandes et ne constituent pas des doublons exacts.
*/
SELECT
    COUNT(*) AS total_lignes,
    COUNT(DISTINCT review_id) AS review_ids_uniques,
    COUNT(DISTINCT CONCAT(review_id, '|', order_id)) AS couples_uniques
FROM staging_order_reviews;
GO

UPDATE staging_order_reviews
SET review_comment_title = 'no_title'
WHERE review_comment_title IS NULL
   OR TRIM(review_comment_title) = '';
GO
UPDATE staging_order_reviews
SET review_comment_message = 'no_comment'
WHERE review_comment_message IS NULL
   OR TRIM(review_comment_message) = '';
GO

SELECT
    SUM(CASE
        WHEN review_comment_title IS NULL
          OR TRIM(review_comment_title) = ''
        THEN 1 ELSE 0
    END) AS titres_encore_manquants,

    SUM(CASE
        WHEN review_comment_message IS NULL
          OR TRIM(review_comment_message) = ''
        THEN 1 ELSE 0
    END) AS commentaires_encore_manquants
FROM staging_order_reviews;
GO