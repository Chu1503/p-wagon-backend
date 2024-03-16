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


def unix_time():
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    round_unix_time = round(unix_timestamp)
    return str(round_unix_time)


def postAlert(rpi_id, description, color, plateNo, estimatedTime):
    unixTime = unix_time()
    crimeId = plateNo + '_' + unixTime
    data = {

        "description": description,
        "details": {
            "color": color,
            "license": plateNo
        },
        "estimatedTime": estimatedTime,
        "status": True,
        "spottings": False
    }
    db.child("crimes").child(crimeId).set(data)

    # For now rpi node won't get empty
    db.child("rpis").child(rpi_id).update({crimeId: True})

    # curRpiSearches = db.child("rpis").child(rpi_id).get().val()
    # if curRpiSearches == False:
    #     db.child("rpis").child(rpi_id).set({crimeId: True})
    # else:
    #     db.child("rpis").child(rpi_id).update({crimeId: True})
    # db.child("rpis").child(rpi_id)
    
    return "Alert posted successfully"


# print(postAlert("myRPI", "Abduction", "Black", "TN37WY1238", "7:00 AM IST"))
