# coding: utf-8
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/prix')
def get():
    distance = request.args.get('distance')
    devise = request.args.get('devise')
    prix=0.2*float(distance)
    if devise == 'dollar':
        prix = prix * 1.2
    elif devise == 'livre':  
        prix = prix*0.88 
    prix = round(prix,2)
    return str(prix)
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)