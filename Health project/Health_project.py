from pymongo import MongoClient
from bson.objectid import ObjectId
# put your pa
import datetime
import schedule
import os
import time
import Users as user
import Doctor as doc
import patient as pat
client = MongoClient('mongodb://localhost:27017')
db = client['admin']
patient_data = db['patient info']
users_collection = db['Users']
from twilio.rest import Client
account_sid = 'AC2e9e80653029925585ee52b3ef7c72c8'
auth_token = 'd7b57a65fc3b5576c050171782de0359'
client = Client(account_sid, auth_token)

items = patient_data.find({})



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
    for item in items:
        dosage = item["dosage"]
        patient_number = item["phone"]
        doctors_appointment_message = client.messages \
        .create(
             body="It's been 3 months since your last visit to the doctor and they miss you! Schedule an appointment with them at the link below: . Additionally reply yes to be entered to win extra reward points",
             from_='+18447260269',
             to=patient_number
         )


def medications():
    for item in items:
        dosage = item["dosage"]
        patient_number = item["phone"]
        morning_message = client.messages \
    .create(
         body="Good Morning! Don't forget to take your meds for the day! The dosage required for today is " + user.dosage + ".",
         from_='+18447260269',
         to=patient_number
    )


        afternoon_message = client.messages \
    .create(
         body='Howdy! Hope our day has been great so far. Dont forget to take your meds for the day! The dosage required is ' + dosage + '.',
         from_='+18447260269',
         to=patient_number
     )

        evening_message = client.messages \
    .create(
         body='Cheers! The day is finally over. But dont forget to take your meds for the day! The dosage required is ' + dosage + '.',
         from_='+18447260269',
         to=patient_number
     )

        night_message = client.messages \
    .create(
         body='Time to retire for the day and go to bed! But dont forget to take your meds for the day! The dosage required is ' + dosage + '.',
         from_='+18447260269',
         to=patient_number
     )



        if user.medic == 'Insulin':
            if current_hour <= 8:
                count_breaksfast_message += 1
                if count_breakfast_message == 1:
                    schedule.every().day.at("8:00").do(morning_message)
            elif current_hour <= 12:
                count_lunch_message += 1
                if count_lunch_message == 1:
                    schedule.every().day.at("12:00").do(afternoon_message)
            elif current_hour <= 18:
                count_dinner_message += 1
                if count_dinner_message == 1:
                    schedule.every().day.at("18:00").do(evening_message)
            elif current_hour <= 20:
                count_whole_day_message += 1
                if count_whole_day_message == 1:
                    schedule.every().day.at("20:00").do(night_message)
        elif user.medic == 'Metformine':
            if current_hour <=18:
                count_dinner_message += 1
                user.dosage = 500
                if count_dinner_message == 1:
                    schedule.every().day.at("18:00").do(evening_message)
        elif user.medic == 's':
            if current_hour <= 12:
                count_lunch_message += 1
                if count_lunch_message == 1:
                    schedule.every().day.at("12:00").do(afternoon_message)
            if current_hour <=18:
                count_dinner_message += 1
                if count_dinner_message == 1:
                    schedule.every().day.at("18:00").do(evening_message)
        elif user.medic == 'd':
            user.dosage = 2.5
            if current_hour <=18:
                count_dinner_message += 1
                if count_dinner_message == 1:
                    schedule.every().day.at("18:00").do(evening_message)
        elif user.medic == 'SGLD2':
            user.dosage = 0.025
            if current_hour <=18:
                count_dinner_message += 1
                if count_dinner_message == 1:
                    schedule.every().day.at("18:00").do(evening_message)
        elif user.medic == 'g':
            user.dosage = 0.00075
            schedule.every().friday.at("18:00").do(evening_message)
            while True:
                schedule.run_pending()
                time.sleep(1)


def main():
    medications()
    doctors_appointment()

    
    

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
            user.sign_up()
        elif choice == 2:
            choose = 0
            print("Welcome to the sign in page!")
            user.sign_in()
        else:
            continue

if __name__ == "__main__":
    main()


        
        
        
        
