import os
import pandas as pd
import numpy as np
from flask import Flask, render_template,jsonify, request
# from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

load model
model = load_model('model/model.h5')
summarize model.
model.summary()

from sklearn.preprocessing import MinMaxScaler

@app.route("/submit", methods=['GET', 'POST'])
# def index():
    
    """Return the homepage."""
    if request.method == 'POST':
       mushroom = request.form['mushroom']
        data = {'cap-shape':  [, ,]
            'cap-surface': [,],
            'cap-color': [, ,
            'odor': [, ],
            'spore-print-color': [, ]
            
        }

         df = pd.DataFrame (data, columns = ['cap-shape', 'cap-surface', 'cap-color', 'odor', 'spore-print-color'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)
        encoded_predictions= model.predict_classes(test_scaled[])
        if encoded_predictions[0] == 0:
            final_prediction = "Likely Poisionous"
        else: 
            final_prediction = "Likely Safe"
        return render_template('index.html', prediction = final_prediction)
    else:
        return render_template('index.html')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/graphs")
def graphs():
    return render_template("graphs.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')


if __name__ == "__main__":
    app.run(debug=True)