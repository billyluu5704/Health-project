from pymongo import MongoClient
from bson.objectid import ObjectId
# put your pa
import datetime
import schedule
import os

from twilio import Client
account_sid = 'AC2e9e80653029925585ee52b3ef7c72c8'
auth_token = 'd7b57a65fc3b5576c050171782de0359'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )
current_date_and_time = datetime.datetime.now()
current_hour = current_date_and_time.hour
current_day = current_date_and_time.weekday()
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_day_name = day_names[current_day]

count_breakfast_message = 0
count_lunch_message = 0
count_dinner_message = 0
count_whole_day_message = 0



def doctors_appointment():
    #Twilio api call)
    rewards_for_patients(5)
def rewards_for_patients(rewards):
    #Twilio API Call to recieve a message saying yes
    if msg == "Yes":
        total_rewards += rewards
        if total_rewards >= 18:
            if reward_type == "Kroger":
                #Twilio API Call to send them Kroger Voucher card
                True
            else:
                True
                #Twilio API Call to send them Metro Gift Voucher
            
    


def medications():
    if user.medic == 'i':
        if current_hour <= 8:
            count_breaksfast_message += 1
            if count_breakfast_message == 1:
                schedule.every().day.at("8:00").do(#twilio api call)
                rewards_for_patients(1)
        elif current_hour <= 12:
            count_lunch_message += 1
            if count_lunch message == 1:
                schedule.every().day.at("12:00").do(#twilio api call)
                rewards_for_patients(1)
        elif current_hour <= 18:
            count_dinner_message += 1
            if count_dinner_message == 1:
                schedule.every().day.at("18:00").do(#twilio api call)
                rewards_for_patients(1)
        elif current_hour <= 20:
            count_whole_day_message += 1
            if count_whole_day_message == 1:
                schedule.every().day.at("20:00").do(#twilio api call)
                rewards_for_patients(1)
    elif user.medic == 'm':
        if current_hour <=18:
            count_dinner_message += 1
            user.dosage = 500
            if count_dinner_message == 1:
                schedule.every().day.at("18:00").do(#twilio api call for dosage amount)
                rewards_for_patients(1)
    elif user.medic == 's':
        if current_hour <= 12:
            count_lunch_message += 1
            if count_lunch_message == 1:
                schedule.every().day.at("12:00").do(#twilio api call)
                rewards_for_patients(1)
        if current_hour <=18:
            count_dinner_message += 1
            if count_dinner_message == 1:
                schedule.every().day.at("18:00").do(#twilio api call)
                rewards_for_patients(1)
    elif user.medic == 'd':
        user.dosage = 2.5
        if current_hour <=18:
            count_dinner_message += 1
            if count_dinner_message == 1:
                schedule.every().day.at("18:00").do(#twilio api call)
                rewards_for_patients(1)
    elif user.medic == 'SGLD2':
        user.dosage = 0.025
        if current_hour <=18:
            count_dinner_message += 1
            if count_dinner_message == 1:
                schedule.every().day.at("18:00").do(#twilio api call)
                rewards_for_patients(1)
    elif user.medic == 'g':
        user.dosage = 0.00075
        schedule.every().friday.at("18:00").do(#twilio api call)
        rewards_for_patients(1)
        while True:
            schedule.run_pending()
            time.sleep(1)
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['admin']
users_collection = db['Users']

def sign_up():
    Name = input("Enter your name: ")
    Age = int(input("Enter your age: "))
    while Age < 0:
        print("Invalid age")
        Age = int(input("Enter your age: "))
    Height = float(input("Enter your height: "))
    Weight = float(input("Enter your weight: "))
    Phone = input("Enter your phone number: ")
    Email = input("Enter your email: ")
    while '@' not in Email:
        print("Invalid email")
        Email = input("Enter your email: ")
    Password = input("Enter your password: ")
    while len(Password) < 12:
        print("Password must be at least 12 characters long")
        Password = input("Enter your password: ")
    Password2 = input("Confirm your password: ")
    while Password != Password2:
        print("Passwords do not match")
        Password2 = input("Confirm your password: ")
    TD = int(input("Enter your type of diabetes (1 or 2): "))
    while TD != 1 and TD != 2:
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
    print("You have successfully signed up!")

def sign_in():
    Email = input("Enter your email: ")
    Password = input("Enter your password: ")

    # Find user by email and password
    user_data = users_collection.find_one({'email': Email, 'password': Password})

    if user_data:
        print("Welcome, " + user_data['name'] + "! You have successfully signed in.")
    else:
        print("Invalid email or password. Please retry.")

def main():
    choice = 0
    while (choice != 3):
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = int(input("Enter your choice (1/2/3): "))
        while (choice != 1 and choice != 2 and choice != 3):
            print("Invalid choice. Please retry.")
            choice = input("Enter your choice (1/2/3): ")
        if choice == 1:
            sign_up()
        elif choice == 2:
            sign_in()
        else:
            continue

if __name__ == "__main__":
    main()


        
        
        
        
