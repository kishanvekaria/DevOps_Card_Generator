from flask import Flask, render_template, Response, request, jsonify, make_response
import requests
import random
#import json
app = Flask(__name__)

@app.route('/card_suit', methods= ['GET'])
def card_suit():
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    first_suit= random.choices(suits)
    second_suit= random.choices(suits)
    return Response(first_suit, mimetype="text/plain")


#jason if necessary later    
#
#@app.route('/card_suit', methods= ['GET'])
#def card_suit():
#    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
#    first_suit= random.choices(suits)
#    second_suit= random.choices(suits)
#    diction = {
#        "suit1": first_suit,
#        "suit2": second_suit
#    }
#    res_suit= json.dumps(diction)
#    return res_suit


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)