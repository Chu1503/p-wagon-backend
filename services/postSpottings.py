import pyrebase
import os
from dotenv import load_dotenv
import json, datetime, base64

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

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db = firebase.database()

def unix_time():
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    round_unix_time = round(unix_timestamp)
    return str(round_unix_time)

def postSpottings(crimeId, location, timeStamp, plateNo):
    unixTime = unix_time()
    spottingData = {
        "location": location, # The randomized location of the spotting
        "timeStamp": timeStamp,
        "license": plateNo # The License plate OCR variable here
    }
    db.child("crimes").child(crimeId).child("spottings").child(unixTime).set(spottingData)
    return "Spottings posted successfully"

# print(postSpottings("TN38BB89811710462417833", "Vellore", "11:00 PM IST", "TN38BB8981"))