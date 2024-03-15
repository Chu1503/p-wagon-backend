from flask import Flask, request
from flask_cors import CORS
import json
from services import fetchCrime as fc
from services import postSpottings as ps
from services import postAlert as pa
from services import archiveCrime as ac
from services import unarchiveCrime as uc
from services import fetchRpi as fr

app = Flask(__name__)
CORS(app)

app.secret_key = 'secret'



@app.route('/')
def hello_world():
    return "Backend for p-wagon!"


@app.route('/api/fetchCrimes', methods=['GET'])
def fetchCrimes():
    return fc.fetchCrime()


@app.route('/api/postAlert', methods=['POST'])
def postAlert():
    req = request.get_json()
    rpi_id = req['rpi_id']
    description = req['description']
    color = req['color']
    plateNo = req['plateNo']
    estimatedTime = req['estimatedTime']
    return pa.postAlert(rpi_id, description, color, plateNo, estimatedTime)


@app.route('/api/fetchRpi', methods=['GET'])
def fetchRpi():
    rpi_id = request.args.get('rpi_id')
    return fr.fetchRpi(rpi_id)


@app.route('/api/postSpottings', methods=['POST'])
def postSpottings():
    req = request.get_json()
    crimeId = req['crimeId']
    location = req['location']
    timeStamp = req['timeStamp']
    plateNo = req['plateNo']
    return ps.postSpottings(crimeId, location, timeStamp, plateNo)


@app.route('/api/archiveCrime', methods=['POST'])
def archiveCrime():
    req = request.get_json()
    crimeId = req['crimeId']
    return ac.archiveCrime(crimeId)


@app.route('/api/unarchiveCrime', methods=['POST'])
def unarchiveCrime():
    req = request.get_json()
    crimeId = req['crimeId']
    return uc.unarchiveCrime(crimeId)


# # main driver function
if __name__ == '__main__':
    app.run(port=8080, debug=True)
