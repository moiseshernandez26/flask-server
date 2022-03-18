from flask import Flask,request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hola serna</p>"

@app.route("/api/serna", methods=['GET'])
@cross_origin()
def serna():
    return "<h1>Hola</h1>"

