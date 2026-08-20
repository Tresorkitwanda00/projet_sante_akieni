/*--------------------------------------------------------------------
    ÉTAPE : TRANSFORMATION ET CHARGEMENT DES DONNÉES CUSTOMERS
----------------------------------------------------------------------
    Objectif :
    Transformer les données préalablement chargées dans la table
    de staging staging_customers, puis les insérer dans la table
    finale customers.

    Principe :
    Les données de staging sont considérées comme des données brutes.
    Avant leur intégration dans la table finale, certaines transformations
    sont appliquées afin d'améliorer leur qualité et leur homogénéité.

    Transformations appliquées :
    
    1. customer_id
       - Suppression des espaces superflus avec TRIM().
       - Conservation du type de données défini dans la table finale.

    2. customer_unique_id
       - Suppression des espaces superflus avec TRIM().

    3. customer_zip_code_prefix
       - Suppression des espaces avec TRIM().
       - Conversion de VARCHAR vers INT afin d'obtenir un type numérique
         adapté aux traitements et analyses ultérieurs.

    4. customer_city
       - Suppression des espaces superflus avec TRIM().

    5. customer_state
       - Suppression des espaces avec TRIM().
       - Conversion en majuscules avec UPPER() afin de standardiser
         les codes d'état (ex. : "sp" → "SP").

    Source :
        staging_customers

    Destination :
        customers

    Remarque :
    Les transformations sont effectuées au moment du chargement afin
    que la table finale contienne des données standardisées et prêtes
    pour les analyses, les jointures et les traitements futurs.
--------------------------------------------------------------------*/
INSERT INTO customers (
    customer_id, 
    customer_unique_id, 
    customer_zip_code_prefix, 
    customer_city, 
    customer_state
)
SELECT 
    REPLACE(TRIM(customer_id), '"', ''),
    REPLACE(TRIM(customer_unique_id), '"', ''),
    -- On retire les guillemets avant la conversion en INT
    CAST(REPLACE(TRIM(customer_zip_code_prefix), '"', '') AS INT),
    REPLACE(TRIM(customer_city), '"', ''),
    UPPER(REPLACE(TRIM(customer_state), '"', ''))
FROM staging_customers;