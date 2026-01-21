# Sample Queries (Impala)

## User Activity (Daily)
```sql
SELECT 
    dt,
    count(distinct user_id) as dau
FROM app_db.user_logs
WHERE dt >= '2024-01-01'
GROUP BY 1
ORDER BY 1;
```

## Revenue by Product Category
```sql
SELECT 
    p.category,
    SUM(t.amount) as total_revenue
FROM sales_db.transactions t
JOIN sales_db.products p ON t.product_id = p.id
WHERE t.date >= '2024-01-01'
  AND t.status = 'COMPLETED'
GROUP BY 1
ORDER BY 2 DESC;
```

## Cohort Retention (Template)
```sql
WITH cohort AS (
    SELECT user_id, MIN(date_trunc('month', signup_date)) as cohort_month
    FROM users
    GROUP BY 1
)
SELECT ...
```
