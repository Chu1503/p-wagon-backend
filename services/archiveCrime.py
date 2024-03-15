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


def archiveCrime(crimeId):
    db.child("crimes").child(crimeId).update({"status": False})
    list_rpis = db.child("rpis").get().val()
    for rpi in list_rpis:
        db.child("rpis").child(rpi).child(crimeId).remove()
        if (rpi not in db.child("rpis").get().val()):
            db.child("rpis").update({rpi: False})

    return "Crime archived successfully"


# print(archiveCrime("TN37WY1238_1710536688735"))
