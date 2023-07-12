-- models/categorised-bank-statements.sql

WITH categorized_transactions AS (
  SELECT 
      distinct t.transaction_date, t.narration, t.withdrawal_amt, t.deposit_amt, t.closing_balance,
      CASE 
        WHEN t.Withdrawal_Amt is not null THEN 'Debit'
        WHEN t.Deposit_Amt is not null THEN 'Credit'
        ELSE 'Unknown'
      END AS transaction_type,
      COALESCE(c.Category, 'Miscellaneous') as Category
  FROM {{ source('aditi_finance', 'bank-statements') }} AS t
  LEFT JOIN {{ source('aditi_finance', 'category_lookup') }} AS c
  ON LOWER(t.Narration) LIKE CONCAT('%', LOWER(c.Keyword), '%')
)

SELECT * FROM categorized_transactions
