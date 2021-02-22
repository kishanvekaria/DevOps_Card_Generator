from flask import Flask, render_template, Response, request
import requests
import random
app = Flask(__name__)

@app.route('/card_number', methods= ['GET'])
def card_number():
    faces = ["Ace", "King", "Queen", "Jack"]
    first_face= random.choices(faces)
    second_face= random.choices(faces)
    return Response(first_face, mimetype="text/plain")

#@app.route('/card_face', methods= ['GET'])
#def card_face():
#    faces = ["Ace", "King", "Queen", "Jack"]
#    first_face= random.choices(faces)
#    second_face= random.choices(faces)
#    diction_faces = {
#        "face1": first_face,
#        "face1": second_face
#    }
#    res_face= json.dumps(diction_faces)
#    return res_face


#@app.route('/suit', methods=['POST'])
#def suit():
#    face= request.data.decode('utf-8')
#    if face == "Ace":
#        suit = "Spades"
#    elif face == "King":
#        suit = "Diamond"
#    elif face == "Queen":
#        suit = "Hearts"
#    elif face == "Jack":
#        suit = "Clubs"
#    return Response(suit, mimetype="text/plain")

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)