# Hospital Simulator

## Overview

The Hospital Simulator is responsible for generating realistic daily operational healthcare data. It simulates how a hospital or healthcare organization produces data every day before it enters the data engineering pipeline.

Each execution generates a new daily delivery inside the raw data lake.

Example:

```
data/raw/
├── 2026-07-01/
├── 2026-07-02/
├── 2026-07-03/
└── ...
```

Each daily folder may contain:

- patients.csv
- claims.csv
- appointments.csv
- prescriptions.csv

Provider information is maintained as master reference data.

---

## Architecture

```
Hospital Simulator
        │
        ├── metadata_manager.py
        ├── patient_service.py
        ├── claim_service.py
        ├── appointment_service.py
        ├── prescription_service.py
        │
        ▼
Daily Hospital Delivery
```

---

## Components

### hospital_simulator.py

Main entry point of the simulator.

Responsibilities:

- Loads metadata
- Loads master data
- Generates a new hospital delivery
- Updates metadata
- Writes daily CSV files

Run:

```bash
PYTHONPATH=python python3 python/simulator/hospital_simulator.py
```

---

### metadata_manager.py

Maintains the simulator state.

Tracks:

- Last generated date
- Last patient ID
- Last provider ID
- Last claim ID
- Last appointment ID
- Last prescription ID
- Number of simulated days

---

### patient_service.py

Generates newly registered patients for each day.

Features:

- Random patient demographics
- Unique patient IDs
- Updates the master patient registry

---

### claim_service.py

Generates insurance claims.

Features:

- Valid patient/provider IDs
- Diagnosis codes
- Procedure codes
- Claim amounts
- Claim status

---

### appointment_service.py

Generates patient appointments.

Features:

- Appointment type
- Appointment status
- Valid patient/provider relationships

---

### prescription_service.py

Generates patient prescriptions.

Features:

- Medication names
- Dosages
- Valid patient/provider relationships

---

## Output

Example:

```
data/raw/2026-07-07/

patients.csv
claims.csv
appointments.csv
prescriptions.csv
```

---

## Next Stage

The generated daily files become the input for the ETL pipeline.

```
Hospital Simulator
        │
        ▼
Raw Data Lake
        │
        ▼
Extract
        │
        ▼
Transform
        │
        ▼
Load
        │
        ▼
PostgreSQL Warehouse
```