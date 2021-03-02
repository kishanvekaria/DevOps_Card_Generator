from flask import Flask, render_template, Response, request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/cardis', methods= ['GET', 'POST'])
def cardis():
    card_number= requests.get("http://service2:5001/card_number")
    card_suit = requests.get("http://service3:5002/card_suit")
    stringcardnum= (card_number.text)
    stringcardsuit= (card_suit.text)
    firstcardis= stringcardnum + " de " + stringcardsuit
    return Response(firstcardis, mimetype="text/plain")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
