CREATE TABLE IF NOT EXISTS patients (
    patient_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    date_of_birth DATE,
    state VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS providers (
    provider_id VARCHAR(20) PRIMARY KEY,
    provider_name VARCHAR(100),
    specialty VARCHAR(100),
    hospital_name VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS claims (
    claim_id VARCHAR(20) PRIMARY KEY,
    patient_id VARCHAR(20),
    provider_id VARCHAR(20),
    diagnosis_code VARCHAR(20),
    procedure_code VARCHAR(20),
    claim_amount DECIMAL(10,2),
    claim_date DATE,
    claim_status VARCHAR(30),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id VARCHAR(20) PRIMARY KEY,
    patient_id VARCHAR(20),
    provider_id VARCHAR(20),
    appointment_date DATE,
    appointment_type VARCHAR(50),
    status VARCHAR(30),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);

CREATE TABLE IF NOT EXISTS prescriptions (
    prescription_id VARCHAR(20) PRIMARY KEY,
    patient_id VARCHAR(20),
    provider_id VARCHAR(20),
    medication_name VARCHAR(100),
    dosage VARCHAR(50),
    prescription_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);