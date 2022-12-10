from flask import Flask,request,jsonify
import util
app = Flask(__name__)

@app.route('/location')
def get_locaiton_name():
    response = jsonify({
        'location': util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
@app.route('/predict_home_prices',methods = ['POST'])
def predict_home_prices():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk_size = int(request.form['bhk_size'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': util.get_price_estimation(location,total_sqft,bhk_size,bath)
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

    
if __name__ == '__main__':
    print("starting the flask server for home price prediction....")
    util.load_saved_artifacts()
    app.run()