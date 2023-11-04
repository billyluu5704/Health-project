from re import S
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['Users_database']
users_collection = db['users']
class User:
    def __init__(self, name, age, height, weight, phone, email, password, td, medic):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.phone = phone
        self.email = email
        self.password = password
        self.td = td
        self.medic = medic
    def sign_up(self, name, age, height, weight, phone, email, password):
        Name = input("Enter your name: ")
        Age = int(input("Enter your age: "))
        while (Age < 0):
            print("Invalid age")
            Age = int(input("Enter your age: "))
        Height = float(input("Enter your height: "))
        Weight = float(input("Enter your weight: "))
        Phone = input("Enter your phone number: ")
        Email = input("Enter your email: ")
        while ('@' not in Email):
            print ("Invalid email")
            Email = input("Enter your email:")
        Password = input("Enter your password: ")
        while (len(Password) < 12):
            print("Password must be at least 12 characters long")
            Password = input("Enter your password: ")
        TD = int(input("Enter your type of diabetes (1 or 2): "))
        while (TD != 1 and TD != 2):
            print("Invalid type of diabetes")
            TD = int(input("Enter your type of diabetes (1 or 2): "))
        Medic = input("Enter your medication you are taking: ")
        user_data = {
            'name': Name,
            'age': Age,
            'height': Height,
            'weight': Weight,
            'phone': Phone,
            'email': Email,
            'password': Password,
            'td': TD,
            'medic': Medic
        }
        users_collection.insert_one(user_data)
        self.name = Name
        self.age = Age
        self.height = Height
        self.weight = Weight
        self.phone = Phone
        self.email = Email
        self.password = Password
        self.td = TD
        self.medic = Medic
        print("You have successfully signed up!")
    def sign_in(self, email, password):
        Email = input("Enter your email: ")
        Password = input("Enter your password: ")
        while (Email != self.email and Password != self.password):
            print("Invalid email or password, Retry!")
            Email = input("Enter your email: ")
            Password = input("Enter your password: ")
    
            
        
        
        
        
        
