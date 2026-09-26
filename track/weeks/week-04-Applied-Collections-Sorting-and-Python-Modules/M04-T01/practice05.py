# Build a Patient Index using Patient IDs

def build_patient_index(patients):
    patient_by_id = {}

    # Build and return the patient index
    for patient in patients:
        patient_id = patient["patient_id"]
        patient_by_id[patient_id] = patient

    return patient_by_id


n = int(input())
patients = []

for _ in range(n):
    patient_id, name, age, blood_group = input().split()

    patients.append({
        "patient_id": patient_id,
        "name": name,
        "age": int(age),
        "blood_group": blood_group
    })

required_id = input()

patient_by_id = build_patient_index(patients)
patient = patient_by_id.get(required_id)

if patient is None:
    print("Patient not found")
else:
    print(patient["name"])
    print(patient["age"])
    print(patient["blood_group"])