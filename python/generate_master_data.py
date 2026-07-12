import os
import pandas as pd
import random
from datetime import datetime, timedelta

MASTER_DIR = "data/sample"

os.makedirs(MASTER_DIR, exist_ok=True)

def random_date(start_year=1950, end_year=2010):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).strftime("%Y-%m-%d")

def generate_patients(count=1000):
    patients = []

    first_names = ["John", "Mary", "David", "Sarah", "Michael", "Linda", "James", "Patricia", "Robert", "Jennifer"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Taylor", "Anderson", "Thomas", "Moore", "Martin"]
    states = ["TX", "CA", "NY", "FL", "IL", "AZ", "GA", "NC"]

    for i in range(1, count + 1):
        patients.append({
            "patient_id": f"P{i:06d}",
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "gender": random.choice(["Male", "Female"]),
            "date_of_birth": random_date(),
            "state": random.choice(states)
        })

    return pd.DataFrame(patients)

def generate_providers(count=200):
    providers = []

    provider_names = ["HealthOne Clinic", "CarePlus Hospital", "Metro Medical", "Wellness Center", "United Care"]
    specialties = ["Cardiology", "Primary Care", "Orthopedics", "Dermatology", "Neurology", "Pediatrics"]
    hospitals = ["St. Mary Hospital", "Clear Lake Medical", "Houston General", "Northside Health", "Bay Area Medical"]
    states = ["TX", "CA", "NY", "FL", "IL", "AZ", "GA", "NC"]

    for i in range(1, count + 1):
        providers.append({
            "provider_id": f"PR{i:05d}",
            "provider_name": random.choice(provider_names),
            "specialty": random.choice(specialties),
            "hospital_name": random.choice(hospitals),
            "state": random.choice(states)
        })

    return pd.DataFrame(providers)

def main():
    patients_df = generate_patients()
    providers_df = generate_providers()

    patients_df.to_csv(f"{MASTER_DIR}/master_patients.csv", index=False)
    providers_df.to_csv(f"{MASTER_DIR}/master_providers.csv", index=False)

    print("Master data generated successfully.")
    print(f"Patients: {len(patients_df)} rows")
    print(f"Providers: {len(providers_df)} rows")
    print(f"Location: {MASTER_DIR}")

if __name__ == "__main__":
    main()