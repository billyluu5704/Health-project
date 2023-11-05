from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb://localhost:27017')
db = client['admin']
patient_data = db['patient info']
users_collection = db['Users']

import random

def ranint():
    i = random.randint(10000, 99999)
    while (patient_data.find_one({'id': i})):
        i = random.randint(10000, 99999)
    return i

def moreinfo():
    num = ranint()
    fname = input("Enter patient's first name: ")
    lname = input("Enter patient's last name: ")
    phone = input("Enter patient's phone: ")
    first = users_collection.fine_one({'fname': fname})
    last = users_collection.fine_one({'lname': lname})
    Phone = users_collection.find_one({'phone': phone})
    while (first != fname and last != lname and Phone != phone):
        print("Patient not found. Please retry.")
        fname = input("Enter patient's first name: ")
        lname = input("Enter patient's last name: ")
        phone = input("Enter patient's phone: ")
        first = users_collection.fine_one({'fname': fname})
        last = users_collection.fine_one({'lname': lname})
        Phone = users_collection.find_one({'phone': phone})
    print("Patient found!")
    td = int(input("What type of diabete does the patient have? (1/2): "))
    while td != 1 and td != 2:
        print("Invalid choice. Please retry.")
        td = int(input("What type of diabete does the patient have? (1/2): "))
    if td == 1:
        typ = "type 1"
    elif td == 2:
        typ = "type 2"
    med = input("What medication does the patient take? (Insulin or Metformine): ")
    while (med != "Insulin" and med != "Metformine"):
        print("Invalid choice. Please retry.")
        med = input("What medication does the patient take? (Insulin or Metformine): ")
    if med == "Insulin":
        medic = "Insulin"
    elif med == "Metformine":
        medic = "Metformine"
    dose = int(input("Number of doeses should the patient take: "))
    while dose < 0:
        print("Invalid choice. Please retry.")
        dose = int(input("Number of doeses should the patient take: "))
    patient = {
        'id': num,
        'fname': fname,
        'lname': lname,
        'phone': phone,
        'type': typ,
        'medication': medic,
        'dosage': dose,
    }
    patient_data.insert_one(patient)
    print(f"Patient {fname} {lname}, id: {num}, has been updated successfully!")
    
def type1():
    print("Patients who have diabete type 1: \n")
    for patient in patient_data.find({'type': 'type 1'}):
        print(f"ID: {patient['id']}")
        print(f"Name: {patient['fname']} {patient['lname']}")
        print(f"Phone number: {patient['phone']}")
        print(f"Medication: {patient['medication']}")
        print(f"Dosage: {patient['dosage']}")
        
def type2():
    print("Patients who have diabete type 2: \n")
    for patient in patient_data.find({'type': 'type 2'}):
        print(f"ID: {patient['id']}")
        print(f"Name: {patient['fname']} {patient['lname']}")
        print(f"Phone number: {patient['phone']}")
        print(f"Medication: {patient['medication']}")
        print(f"Dosage: {patient['dosage']}")
    

def Doctor():
    print("Welcome to the Doctor's page!")
    choice = 0
    while (choice != 4):
        print("1. Update patient's information")
        print("2. View patients who have diabete type 1")
        print("3. View patients who have diabete type 2")
        print("4. Sign out")
        choice = int(input("Enter your choice (1/2/3/4): "))
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
            print("Invalid choice. Please retry.")
            choice = int(input("Enter your choice (1/2/3/4): "))
        if (choice == 1):
            moreinfo()
        elif (choice == 2):
            type1()
        elif (choice == 3):
            type2()
        else:
            continue
              
