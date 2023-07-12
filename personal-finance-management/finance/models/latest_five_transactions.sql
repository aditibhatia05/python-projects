-- models/latest_five_transactions.sql

-- models/latest_five_transactions.sql

WITH latest_transactions AS (
  SELECT 
    t.transaction_date, 
    t.narration, 
    CASE
      WHEN t.transaction_type = 'Debit' THEN t.withdrawal_amt
      WHEN t.transaction_type = 'Credit' THEN t.deposit_amt
      ELSE NULL
    END AS transaction_amt,
    t.transaction_type,
    t.category
  FROM 
    {{ ref('categorised-bank-statements') }} t
  ORDER BY 
    t.transaction_date DESC
  LIMIT 5
)

SELECT * FROM latest_transactions


