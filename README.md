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

Healthcare Source Files
        │
        ▼
Raw Daily Data (CSV)
        │
        ▼
Apache Airflow
        │
        ▼
Python ETL
        │
        ▼
PostgreSQL
        │
        ▼
PySpark
        │
        ▼
AWS S3 Data Lake
        │
        ▼
dbt
        │
        ▼
Power BI

---

# 📁 Project Structure

python/
│
├── simulator/
│   ├── hospital_simulator.py
│   ├── patient_service.py
│   ├── provider_service.py
│   ├── claim_service.py
│   ├── appointment_service.py
│   ├── prescription_service.py
│   ├── metadata_manager.py
│   └── utils.py
│
└── etl/
    ├── extract.py
    ├── transform.py
    ├── load.py
    └── transformers/
        ├── validation.py
        ├── patient_transformer.py
        ├── claim_transformer.py
        ├── appointment_transformer.py
        └── prescription_transformer.py

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

## Data Engineering Stack

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
| Sprint 2 – Hospital Data Simulator | ✅ Complete |
| Sprint 3 – ETL Pipeline (Extract & Transform) | ✅ Complete |
| Sprint 4 – Load Data into PostgreSQL | ⏳ Next |
| Sprint 5 – Apache Airflow Orchestration | ⏳ Planned |
| Sprint 6 – PySpark Processing | ⏳ Planned |
| Sprint 7 – AWS Data Lake Integration | ⏳ Planned |
| Sprint 8 – dbt Analytics Engineering | ⏳ Planned |
| Sprint 9 – Power BI Dashboard | ⏳ Planned |
| Sprint 10 – Documentation & Deployment | ⏳ Planned |

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

# 📌 Current Features

- Dockerized PostgreSQL environment
- Healthcare relational database schema
- Modular hospital data simulator
- Incremental daily data generation
- Metadata-driven delivery tracking
- Master patient and provider registries
- Modular ETL architecture
- Automatic extraction of latest daily delivery
- Data validation and cleansing pipeline
- Reusable transformation utilities
- Version-controlled development with Git & GitHub

---

## Objectives:

- Select a real-world healthcare dataset
- Explore and understand the dataset
- Store raw files inside `data/raw`
- Design the ingestion strategy
- Build the first Python ETL pipeline
- Load healthcare data into PostgreSQL

---
## Sprint 2 - Hospital Data Simulator ✅

Completed:
- Built a realistic hospital data simulator
- Implemented modular simulator architecture
- Created master patient registry
- Created master provider registry
- Implemented metadata manager to track daily deliveries
- Generated incremental daily hospital data
- Created automatic date-based folder structure
- Simulated new patient registrations each day
- Simulated daily claims
- Simulated daily appointments
- Simulated daily prescriptions
- Updated master patient registry after each delivery
- Tracked generator state using metadata

## Daily Delivery Structure:

data/raw/
├── 2026-07-01/
│   ├── patients.csv
│   ├── claims.csv
│   ├── appointments.csv
│   └── prescriptions.csv
│
├── 2026-07-02/
│   ├── patients.csv
│   ├── claims.csv
│   ├── appointments.csv
│   └── prescriptions.csv
│
└── ...

Reference Data:

data/sample/
├── master_patients.csv
└── master_providers.csv

Metadata:

data/metadata/
└── generator_state.json

Simulator Components:

python/simulator/
├── hospital_simulator.py
├── metadata_manager.py
├── patient_service.py
├── claim_service.py
├── appointment_service.py
├── prescription_service.py
└── utils.py

Tech Stack:
- Python
- Pandas
- Faker
- CSV

## Sprint 3 - ETL Pipeline ✅

Completed:
- Built modular ETL architecture
- Implemented extract layer
- Automatic latest delivery detection
- Implemented patient transformer
- Implemented claim transformer
- Implemented appointment transformer
- Implemented prescription transformer
- Added reusable validation utilities
- Validated schemas and IDs
- Removed duplicate records
- Standardized text and date fields

Current ETL Flow:

Hospital Simulator
        ↓
Raw Daily Data
        ↓
Extract
        ↓
Transform
        ↓
Ready for Load

# 📚 Learning Objectives

Through this project, the following concepts will be demonstrated:

- Docker fundamentals
- Relational database design
- SQL
- Building modular ETL pipelines
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