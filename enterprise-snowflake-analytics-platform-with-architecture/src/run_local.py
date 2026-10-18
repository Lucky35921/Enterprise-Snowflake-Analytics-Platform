"""Runnable SQLite proof of concept for retail analytics ELT."""
import argparse
import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def build(db_path):
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as db:
        db.executescript((ROOT / "sql/01_create_tables.sql").read_text())
        for table, file, columns in [
            ("stg_customers", "customers.csv", "customer_id,customer_name,region"),
            ("stg_orders", "orders.csv", "order_id,customer_id,order_date,amount,status"),
        ]:
            with (ROOT / "sample_data" / file).open(newline="") as f:
                rows = list(csv.DictReader(f))
            db.execute(f"DELETE FROM {table}")
            placeholders = ",".join("?" for _ in columns.split(","))
            db.executemany(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})",
                           [[row[col] for col in columns.split(",")] for row in rows])
        db.executescript((ROOT / "sql/02_build_marts.sql").read_text())
        orphan_count = db.execute("SELECT COUNT(*) FROM stg_orders o LEFT JOIN dim_customers c ON o.customer_id=c.customer_id WHERE c.customer_id IS NULL").fetchone()[0]
        if orphan_count:
            raise ValueError(f"Found {orphan_count} orphan orders")
        revenue = db.execute("SELECT ROUND(COALESCE(SUM(total_revenue),0),2) FROM fct_daily_sales").fetchone()[0]
        print(f"Built {path}; completed order revenue: {revenue:.2f}")
        return revenue

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="output/retail_analytics.db")
    args = parser.parse_args()
    build(args.output)
