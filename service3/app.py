from flask import Flask, render_template, Response, request, jsonify, make_response
import requests
import random
import json
app = Flask(__name__)

#@app.route('/jason', methods= ['POST'])
#def jason():
    #response = requests.post("http://0.0.0.0:5002/jason", json={"message": "hello"})
   # return 

#suit =requests.post("http://0.0.0.0:5001/suit", data=card_number.text)

@app.route('/card_suit', methods= ['GET'])
def card_suit():
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    first_suit= random.choices(suits)
    second_suit= random.choices(suits)
    diction = {
        "suit1": first_suit,
        "suit2": second_suit
    }
    res_suit= json.dumps(diction)
    return res_suit

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)