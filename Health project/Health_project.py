from pymongo import MongoClient
from bson.objectid import ObjectId
# put your pa
import datetime
import schedule
import os
import Users as user
import Doctor as doc
import patient as pat

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

def message():
    medications()
    

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
            user.sign_up()
        elif choice == 2:
            choose = 0
            print("Welcome to the sign in page!")
            user.sign_in()
        else:
            continue
client.close()
if __name__ == "__main__":
    main()


        
        
        
        
