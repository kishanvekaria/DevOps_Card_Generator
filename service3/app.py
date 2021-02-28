from flask import Flask, render_template, Response, request, jsonify, make_response
import requests
import random

app = Flask(__name__)

@app.route('/card_suit', methods= ['GET'])
def card_suit():
    suits = ["Piques", "Carreaux", "Coeurs", "Trèfles"]
    first_suit= random.choices(suits)
    second_suit= random.choices(suits)
    return Response(first_suit, mimetype="text/plain")



if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)