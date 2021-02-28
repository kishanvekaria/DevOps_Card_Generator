from flask import Flask, render_template, Response, request
import requests
import random
app = Flask(__name__)

@app.route('/card_number', methods= ['GET'])
def card_number():
    faces = ["As", "Roi", "Dame", "Valet"]
    first_face= random.choices(faces)
    second_face= random.choices(faces)
    return Response(first_face, mimetype="text/plain")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)