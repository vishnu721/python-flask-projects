from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
mongo = PyMongo(app)
db = mongo.db

# define the home page route
@app.route('/')
def hello_world():
    return render_template("index.html")


# route to get data from html form and insert data into database
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        data['Name'] = request.form['name']
        data['Email'] = request.form['email']
        data['Age'] = request.form['age']
        data['DOB'] = request.form['dob']
        data['Department'] = request.form['department']
        data['Gender'] = request.form['gender']
        data['Address'] = request.form['address']
        data['Pincode'] = request.form['pincode']
        lang = []
        for i in "1234567":
            try:
                if request.form['language' + i] != "":
                    lang.append(request.form['language' + i])
            except Exception as e:
                pass
        data['Language'] = lang
        db.studentData.insert_one(data)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=False)