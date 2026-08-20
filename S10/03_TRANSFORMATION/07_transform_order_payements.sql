/*====================================================================
    TRANSFORMATION : ORDER_PAYMENTS
----------------------------------------------------------------------    
    Objectif :
    Transformer et normaliser les données présentes dans la table
    staging_order_payments avant leur chargement dans la table finale.

    Transformations appliquées :

    1. order_id
       - Suppression des espaces inutiles avec TRIM().
       - Conservation du format VARCHAR.

    2. payment_sequential
       - Suppression des espaces inutiles.
       - Conversion de VARCHAR vers INT.

    3. payment_type
       - Suppression des espaces inutiles.
       - Normalisation en majuscules.

    4. payment_installments
       - Suppression des espaces inutiles.
       - Conversion de VARCHAR vers INT.

    5. payment_value
       - Suppression des espaces inutiles.
       - Conversion de VARCHAR vers DECIMAL(10,2).

    Les données sources de la staging table ne sont pas modifiées
    pendant cette étape.
====================================================================*/

/*====================================================================
    TRANSFORMATION ET CHARGEMENT DANS LA TABLE TRANSFORM
----------------------------------------------------------------------*/

INSERT INTO order_payments (
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
)
SELECT
    TRIM(order_id) AS order_id,

    TRY_CAST(TRIM(payment_sequential) AS INT)
        AS payment_sequential,

    UPPER(TRIM(payment_type))
        AS payment_type,

    TRY_CAST(TRIM(payment_installments) AS INT)
        AS payment_installments,

    TRY_CAST(TRIM(payment_value) AS DECIMAL(10,2))
        AS payment_value

FROM staging_order_payments;
