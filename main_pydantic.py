from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient(patient : Patient):
    print("Patient's Name: ", patient.name)
    print("Patient's Age: ", patient.age)
    print("Patient Record Inserted!")

patient_record = {'name':'Ali', 'age':20}

patient1 = Patient(**patient_record)
print(patient1.name)

# insert_patient(patient1)