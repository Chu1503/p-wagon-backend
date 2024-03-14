from flask import Flask
from services import fetchCrime as fc
app = Flask(__name__)

app.secret_key = 'secret'

@app.route('/')
def hello_world():
    return "Backend for p-wagon!"

@app.route('/api/fetchCrimes', methods=['GET'])
def fetchCrimes():
    return fc.fetchCrime()

# # main driver function
if __name__ == '__main__':
   app.run(port=8080, debug=True)