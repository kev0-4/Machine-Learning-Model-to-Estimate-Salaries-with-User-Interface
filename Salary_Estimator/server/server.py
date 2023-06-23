from flask import Flask, request, jsonify
import util
from flask_cors import CORS #
app = Flask(__name__)
CORS(app)#

@app.route('/get_position')
def get_position():
    response = jsonify({
        'position': util.get_position()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_salary',methods=['GET','POST'])
def predict_salary():
    Age = int(request.form['Age'])
    Gender = request.form['Gender']
    Education = request.form['Education']
    position = request.form['position']
    YOE = int(request.form["YOE"])

    response = jsonify({
        'estimates_salary': util.get_estimated_salary(
            Age,Gender,Education,position,YOE)
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Salary Prediction")
    app.run()