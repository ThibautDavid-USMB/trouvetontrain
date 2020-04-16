# coding: utf-8
from flask import Flask
from flask import request

app = Flask(__name__)
        
@app.route('/prix')
def get():
    distance = request.args.get('distance')
    devise = request.args.get('devise')
    prix=0.4*float(distance)
    if devise == 'dollar':
        prix = prix * 0.8
    elif devise == 'livre':  
        prix = prix*0.88 
    return str(prix)
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)