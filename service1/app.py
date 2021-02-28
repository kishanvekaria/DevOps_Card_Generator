from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")
app.config['SECRET_KEY'] = getenv("SEC_KEY")
db = SQLAlchemy(app)


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    card_string = db.Column(db.String(100))

db.drop_all()
db.create_all()

@app.route('/', methods= ['GET'])
def index():

    firstcardis = requests.get("http://service4:5003/cardis")
    stringfirstcard= firstcardis.text
    new_card= Storage(card_string = stringfirstcard)
    db.session.add(new_card)
    db.session.commit()
    cardquery = Storage.query.all()
    col=Storage.id
    for i in cardquery:
        cardquery2 = i.card_string
    return render_template('index.html', firstcardis=firstcardis.text, cardquery= cardquery, col=col) 


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
