from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb://localhost:27017')
db = client['admin']
patient_data = db['patient info']
users_collection = db['Users']    

def view():
    phone = input("Enter your phone number: ")
    patient = patient_data.find_one({'phone': phone})
    if patient:
        print(f"Name: {patient['fname']} {patient['lname']}")
        print(f"Phone number: {patient['phone']}")
        print(f"Type of diabete: {patient['type']}")
        print(f"Medication: {patient['medication']}")
        print(f"Dosage: {patient['dosage']}")
    else:
        print("Patient not found. Please retry.")
   

def Patient():
    print("Welcome to the patient portal!")
    choice = 0
    while(choice != 2):
        print("1. View your information")
        print("2. Sign out")
        choice = int(input("Enter your choice (1/2): "))
        while (choice != 1 and choice != 2):
            print("Invalid choice. Please retry.")
            choice = int(input("Enter your choice (1/2): "))
        if choice == 1:
            view()
        else:
            continue
