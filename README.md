# 🏥 Healthcare Claims Data Platform

An end-to-end **Data Engineering** project that simulates a real-world healthcare claims data platform. This project demonstrates how healthcare data is ingested, stored, processed, orchestrated, transformed, and prepared for analytics using modern Data Engineering tools and best practices.

The project is being built incrementally using an agile sprint-based approach to mirror how real-world data engineering projects are developed.

---

# 🎯 Project Goal

Build a production-style healthcare data platform that:

- Ingests healthcare datasets from raw source files
- Stores operational data in PostgreSQL
- Automates workflows using Apache Airflow
- Processes large datasets using PySpark
- Builds analytics-ready models with dbt
- Stores data in a cloud data lake (AWS S3)
- Creates business dashboards using Power BI

---

# 🏗️ Planned End-to-End Architecture

```
                    Healthcare Source Files
                              │
                              ▼
                     Raw CSV Files
                              │
                              ▼
                   Python ETL Pipeline
                              │
                              ▼
                     PostgreSQL Database
                              │
                              ▼
                 Apache Airflow Orchestration
                              │
                              ▼
                  PySpark Transformations
                              │
                              ▼
                    AWS S3 Data Lake
                              │
                              ▼
                  dbt Analytics Models
                              │
                              ▼
                   Power BI Dashboard
```

---

# 📁 Project Structure

```
healthcare-data-platform/
│
├── airflow/
│   └── dags/
│
├── architecture/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── dbt/
│
├── docker/
│
├── docs/
│
├── postgres/
│   └── schema.sql
│
├── pyspark/
│
├── python/
│
├── screenshots/
│
├── tests/
│
├── warehouse/
│
├── docker-compose.yml
│
└── README.md
```

---

# 🛠️ Tech Stack

## Version Control

- Git
- GitHub

## Development

- VS Code

## Infrastructure

- Docker
- Docker Compose

## Database

- PostgreSQL
- DBeaver

## Upcoming Technologies

- Python
- Pandas
- Apache Airflow
- PySpark
- AWS S3
- dbt
- Power BI

---

# ✅ Sprint Progress

| Sprint | Status |
|---------|--------|
| Sprint 0 – Project Initialization | ✅ Complete |
| Sprint 1 – Infrastructure Setup | ✅ Complete |
| Sprint 2 – Healthcare Dataset & Python ETL | ⏳ Planned |
| Sprint 3 – Apache Airflow Orchestration | ⏳ Planned |
| Sprint 4 – PySpark Processing | ⏳ Planned |
| Sprint 5 – AWS Data Lake Integration | ⏳ Planned |
| Sprint 6 – dbt Analytics Engineering | ⏳ Planned |
| Sprint 7 – Power BI Dashboard | ⏳ Planned |
| Sprint 8 – Documentation & Deployment | ⏳ Planned |

---

# ✅ Sprint 0 - Project Initialization

Completed:

- Created GitHub repository
- Created project folder structure
- Configured VS Code workspace
- Initialized Git repository
- Created project README
- Planned end-to-end project architecture

---

# ✅ Sprint 1 - Infrastructure Setup

Completed:

- Installed Docker Desktop
- Learned Docker fundamentals
- Created Docker Compose configuration
- Deployed PostgreSQL inside a Docker container
- Connected PostgreSQL to DBeaver
- Created the healthcare database
- Designed the initial relational database schema
- Created the following tables:

  - Patients
  - Providers
  - Claims
  - Appointments
  - Prescriptions

- Verified successful database connectivity
- Verified all database tables were created successfully

---

# 🗄️ Current Database Schema

Current tables:

- patients
- providers
- claims
- appointments
- prescriptions

Relationships:

```
Patients
    │
    ├──────────────┐
    ▼              ▼
Claims       Appointments
    ▲              ▲
    │              │
Providers──────────┘
    │
    ▼
Prescriptions
```

---

# 🏗️ Current Infrastructure

```
VS Code
     │
     ▼
Docker Desktop
     │
     ▼
PostgreSQL Container
     │
     ▼
healthcare_db
     │
     ▼
DBeaver
```

---

# 📌 Current Features

- Dockerized PostgreSQL environment
- Relational healthcare database schema
- Local database development environment
- Professional project structure
- Version-controlled development using Git & GitHub

---

# 🚀 Upcoming Sprint (Sprint 2)

Objectives:

- Select a real-world healthcare dataset
- Explore and understand the dataset
- Store raw files inside `data/raw`
- Design the ingestion strategy
- Build the first Python ETL pipeline
- Load healthcare data into PostgreSQL

---

# 📚 Learning Objectives

Through this project, the following concepts will be demonstrated:

- Docker fundamentals
- Relational database design
- SQL
- Python ETL
- Workflow orchestration
- Batch processing with Spark
- Data lake architecture
- Analytics engineering with dbt
- Cloud data engineering concepts
- Dashboard development

---

# 👩‍💻 Author

**Pratyusha Gadasanthala**

Building this project to strengthen hands-on experience in modern Data Engineering and demonstrate production-style data pipeline development using industry-standard tools.