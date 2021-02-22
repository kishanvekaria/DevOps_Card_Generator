from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def index():
    card_number= requests.get("http://0.0.0.0:5001/card_number")
    res = requests.get("http://0.0.0.0:5002/card_suit")
    #suit =requests.post("http://0.0.0.0:5001/suit", data=card_number.text)
    #res = requests.get("http://0.0.0.0:5002/card_suit").json()
    firstcardis = requests.get("http://0.0.0.0:5003/cardis")
    
    
    return render_template('index.html', card_number=card_number.text, res=res.text, firstcardis=firstcardis.text) #,suit=suit.text





if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)