from pymongo import MongoClient
from bson.objectid import ObjectId
import Doctor as doc
import patient as pat
client = MongoClient('mongodb://localhost:27017')
db = client['admin']
users_collection = db['Users']

def sign_up():
    FName = input("Enter your first name: ")
    LName = input("Enter your last name: ")
    Phone = input("Enter your phone number: ")
    pos = input("What are you? (1.Patient or 2.Doctor) Enter (1/2): ")
    while pos != '1' and pos != '2':
        print("Invalid choice. Please retry.")
        pos = input("What are you? (1.Patient or 2.Doctor) Enter (1/2): ")
    if pos == '1':
        Position = 'Patient'
    else:
        Position = 'Doctor'
    Email = input("Enter your email: ")
    while '@' not in Email:
        print("Invalid email")
        Email = input("Enter your email: ")
    Password = input("Enter your password: ")
    while len(Password) < 8:
        print("Password must be at least 12 characters long")
        Password = input("Enter your password: ")
    Password2 = input("Confirm your password: ")
    while Password != Password2:
        print("Passwords do not match")
        Password2 = input("Confirm your password: ")

    user_data = {
        'fname': FName,
        'lname': LName,
        'phone': '+1' + Phone,
        'position': Position,
        'email': Email,
        'password': Password,
    }
    users_collection.insert_one(user_data)
    print("You have successfully signed up!")
    
def sign_in():
    Email = input("Enter your email: ")
    Password = input("Enter your password: ")
    # Find user by email and password
    check = users_collection.find_one({'email': Email, 'password': Password})
    # Check if user exists (i.e., if user_data is not None)
    while (check is None):
        print("Invalid email or password")
        Email = input("Enter your email: ")
        Password = input("Enter your password: ")
        check = users_collection.find_one({'email': Email, 'password': Password})
    print("You have successfully signed in!")
    if check.get('position') == 'Patient':
        pat.Patient()
    elif check.get('position') == 'Doctor':
        doc.Doctor()
    else:
        print("Invalid position")
        return
     