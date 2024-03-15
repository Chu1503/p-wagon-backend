import pyrebase
import os
from dotenv import load_dotenv
import json
import datetime
import base64

load_dotenv()
firebaseConfig = {
    'apiKey': os.getenv('FIREBASE_API_KEY'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': os.getenv('FIREBASE_APP_ID'),
    'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


def postSpottings(crimeId, location, timeStamp, plateNo):
    spottingData = {
        "location": location,  # The randomized location of the spotting
        "timeStamp": timeStamp,
        "license": plateNo  # The License plate OCR variable here
    }
    db.child("crimes").child(crimeId).child("spottings").push(spottingData)
    return "Spotting posted successfully"


# print(postSpottings("TN38BB8981_1710468513229",
#       "Katpadi", "12:30 PM IST", "TN38BBB981"))
