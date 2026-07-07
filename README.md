# 🏥 Healthcare Data Platform

## 📌 Project Overview

The **Healthcare Data Platform** is an end-to-end Data Engineering project that simulates how a healthcare insurance company processes daily healthcare claims.

This project demonstrates how raw healthcare data is ingested, stored, transformed, modeled, and visualized using modern Data Engineering technologies.

The goal is to build a production-style data platform while learning each technology from scratch.

---

# 🎯 Business Problem

Healthcare organizations receive thousands of insurance claims every day from hospitals, clinics, and providers.

The raw data arrives in different formats and must be:

- Collected
- Validated
- Cleaned
- Stored
- Transformed
- Reported

The business needs a centralized platform that automatically processes this data and provides analytics for decision-making.

---

# 🏗️ High-Level Architecture

```
Healthcare Claims Data
        │
        ▼
Python Data Ingestion
        │
        ▼
PostgreSQL
        │
        ▼
Apache Airflow
        │
        ▼
AWS S3 Data Lake
        │
        ▼
PySpark (Databricks)
        │
        ▼
Snowflake
        │
        ▼
dbt
        │
        ▼
Power BI Dashboard
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Programming | Python |
| Database | PostgreSQL |
| Containerization | Docker |
| Workflow Orchestration | Apache Airflow |
| Data Lake | AWS S3 |
| Big Data Processing | PySpark |
| Spark Platform | Databricks |
| Data Warehouse | Snowflake |
| Analytics Engineering | dbt |
| Dashboard | Power BI |
| Version Control | Git & GitHub |

---

# 📂 Repository Structure

```
healthcare-data-platform/

├── architecture/
├── airflow/
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── dbt/
├── docker/
├── docs/
├── postgres/
├── pyspark/
├── python/
├── screenshots/
├── tests/
├── warehouse/
├── README.md
```

---

# 🚀 Development Roadmap

- [x] Project Planning
- [x] Repository Setup
- [ ] Docker Environment
- [ ] PostgreSQL Database
- [ ] Python Data Ingestion
- [ ] Apache Airflow DAG
- [ ] AWS S3 Data Lake
- [ ] PySpark Transformations
- [ ] Databricks Integration
- [ ] Snowflake Data Warehouse
- [ ] dbt Data Models
- [ ] Power BI Dashboard

---

# 🎓 Learning Objectives

This project is designed to understand:

- End-to-end Data Engineering architecture
- ETL / ELT pipelines
- Workflow orchestration
- Data Lakes
- Data Warehouses
- Batch Processing
- Analytics Engineering
- Cloud-based Data Engineering

---

# 📌 Project Status

🚧 Currently under development.

This repository is being built incrementally following Agile development practices.

---

# 👩‍💻 Author

**Pratyusha Gadasanthala**

Graduate Student | Data Engineer

GitHub: https://github.com/gadasanthalapratyusha-collab