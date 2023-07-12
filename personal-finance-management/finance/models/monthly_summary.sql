-- models/monthly_summary.sql

SELECT
    distinct FORMAT_TIMESTAMP('%Y-%m-01', transaction_date) as Month,
    Category,
    SUM(Withdrawal_Amt) as Total_Withdrawal,
    SUM(Deposit_Amt) as Total_Deposit
FROM {{ ref('categorised-bank-statements') }}
GROUP BY Month, Category
