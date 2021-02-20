from flask import Flask, render_template, Response, request
import requests
import random
app = Flask(__name__)

@app.route('/card_suit', methods= ['GET'])
def card_number():
    card_suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    return Response(random.choices(card_suits), mimetype="text/plain")

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)