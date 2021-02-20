from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/', methods= ['GET'])
def index():
    card_number= requests.get("http://0.0.0.0:5001/card_number")
    suit =requests.post("http://0.0.0.0:5001/suit", data=card_number.text)
    #hello = requests.post("http://0.0.0.0:5002/jason", json={"message": "hello"})
    res = requests.get("http://0.0.0.0:5002/card_suit").json()
    
    
    return render_template('index.html', card_number=card_number.text, suit=suit.text, res = res)


# response = requests.get('URL')



if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)