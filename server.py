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

#load in the model (created and pickled from a seperate python file - don't need
# to call that here though because the model itself is pickled)
model = pickle.load(open('linreg.p', 'rb'))

#create an inference route
#GET method 
@app.route('/inference', methods=['POST'])
def inference():
    req = request.get_json()
    print(req)
    c,h,w = req['cylinders'],req['horsepower'],req['weight']
    prediction = list(model.predict([[c,h,w]]))
    return jsonify({'c':c, 'h':h, 'w':w, 'prediction':prediction})

#Create a route for plotting
@app.route('/plot', methods = ['GET'])
def plot():
    df = pd.read_csv('cars.csv')
    data = list(zip(df.mpg, df.weight))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)
