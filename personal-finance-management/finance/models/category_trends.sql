-- models/category_trends.sql

SELECT
    distinct
    t.category,
    EXTRACT(MONTH FROM t.transaction_date) AS Month,
    EXTRACT(YEAR FROM t.transaction_date) AS Year,
    SUM(t.withdrawal_amt) AS Total_Withdrawal,
    SUM(t.deposit_amt) AS Total_Deposit
FROM {{ ref('categorised-bank-statements') }} AS t
GROUP BY t.category, Month, Year
ORDER BY Year, Month, t.category



