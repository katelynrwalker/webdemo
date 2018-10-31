from flask import Flask,render_template, request,jsonify,Response
import pickle
import pandas as pd

app = Flask(__name__)

#create the home page
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

#create the mpg page
@app.route('/mpg', methods = ['GET'])
def mpg():
    return render_template('mpg.html')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)
