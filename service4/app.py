from flask import Flask, render_template, Response, request
import requests
#import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://qatraining:password@104.196.239.146/flaskdb"
#app.config['SECRET_KEY'] = 'SECRET_KEY'
#db = SQLAlchemy(app)

#class Storage(db.Model):
#    id = db.Column(db.Integer, primary_key =True)
#    card_string = db.Column(db.String(30))

@app.route('/cardis', methods= ['GET', 'POST'])
def cardis():
    card_number= requests.get("http://0.0.0.0:5001/card_number")
    card_suit = requests.get("http://0.0.0.0:5002/card_suit")
    stringcardnum= (card_number.text)
    stringcardsuit= (card_suit.text)
    firstcardis= stringcardnum + " of " + stringcardsuit
    #new_card= Storage(card_string = firstcardis)
    #db.session.add(new_card)
    #db.session.commit()
    return Response(firstcardis, mimetype="text/plain")



#json if necessary later
#@app.route('/cardis', methods= ['GET', 'POST'])
#def cardis():
#    card_number= requests.get("http://0.0.0.0:5001/card_number")
#    
#    res_suit = requests.get("http://0.0.0.0:5002/card_suit").json()
#    res_suit_string= json.dumps(res_suit)
#    py_suit = json.loads(res_suit_string)
#    first_suit_brackets = str(py_suit["suit1"])
#    first_suit= first_suit_brackets[2:-2]
#    stringcardnum= (card_number.text)
#    firstcardis= stringcardnum + " of " + first_suit
#    return Response(firstcardis, mimetype="text/plain")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)