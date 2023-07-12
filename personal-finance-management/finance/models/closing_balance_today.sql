-- models/closing_balance_today.sql

WITH latest_transaction AS (
  SELECT 
    t.transaction_date,
    t.closing_balance
  FROM 
    {{ source('aditi_finance', 'bank-statements') }} t
  WHERE 
    t.transaction_date = (
      SELECT 
        MAX(t_inner.transaction_date)
      FROM 
        {{ source('aditi_finance', 'bank-statements') }} t_inner
      WHERE 
        t_inner.transaction_date <= CURRENT_DATE
    )
  ORDER BY 
    t.transaction_date DESC
  LIMIT 1
)

SELECT * FROM latest_transaction

