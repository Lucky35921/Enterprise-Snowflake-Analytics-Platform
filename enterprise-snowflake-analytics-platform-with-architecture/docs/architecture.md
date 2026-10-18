# Architecture

```mermaid
flowchart LR
 A[Retail SaaS / CSV / DB] --> B[Ingestion - planned]
 B --> C[Snowflake RAW - planned]
 C --> D[dbt staging - planned]
 D --> E[dbt marts - planned]
 E --> F[BI - planned]
```

**Local runnable slice:** retail CSV → SQLite staging → customer dimension + daily sales mart → data quality checks.

**Production roadmap:** Snowflake RBAC, external stages, dbt tests and docs, SCD2 snapshots, incremental materializations, orchestration, observability and cost controls.
