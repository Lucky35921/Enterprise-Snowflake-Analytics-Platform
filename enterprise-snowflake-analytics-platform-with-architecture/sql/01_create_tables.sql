CREATE TABLE IF NOT EXISTS stg_customers (
 customer_id TEXT PRIMARY KEY, customer_name TEXT NOT NULL, region TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS stg_orders (
 order_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL, order_date TEXT NOT NULL,
 amount REAL NOT NULL, status TEXT NOT NULL
);
