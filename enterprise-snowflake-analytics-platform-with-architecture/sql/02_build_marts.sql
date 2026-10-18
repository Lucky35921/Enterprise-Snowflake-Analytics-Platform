DROP TABLE IF EXISTS dim_customers;
CREATE TABLE dim_customers AS
SELECT customer_id, customer_name, region FROM stg_customers;

DROP TABLE IF EXISTS fct_daily_sales;
CREATE TABLE fct_daily_sales AS
SELECT order_date, customer_id, COUNT(*) AS completed_orders,
       ROUND(SUM(amount), 2) AS total_revenue
FROM stg_orders WHERE status = 'COMPLETED'
GROUP BY order_date, customer_id;
