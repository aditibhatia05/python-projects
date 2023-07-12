-- models/yearly_summary.sql

SELECT
    distinct FORMAT_TIMESTAMP('%Y', transaction_date) as Year,
    Category,
    SUM(Withdrawal_Amt) as Total_Withdrawal,
    SUM(Deposit_Amt) as Total_Deposit
FROM {{ ref('categorised-bank-statements') }}
GROUP BY Year, Category


