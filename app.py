import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
#from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func, inspect
import sqlite3

app = Flask(__name__)

#################################################
# Database Setup
#################################################


conn = sqlite3.connect("data/cacao_bean.sqlite")

cur = conn.cursor()
cur.execute("SELECT * FROM cacao_clean_withbean")
cacao_table = cur.fetchall()
# print(cacao_table)
# Save references to each table
# tableList = Base.classes.keys()
# print(tableList)
# cacao_table = Base.classes.cacao_clean_withbean

# print(cacao_table)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def index():
    """Return the homepage."""
    if request.method == 'POST':
        alcohol = request.form['alcohol']
        data = {'fixed acidity':  [5.8, 7.1],
            'volatile acidity': [0.300, 0.26],
            'citric acid': [0.33, 0.49],
            'residual sugar': [3.5, 2.2],
            'chlorides': [0.033, 0.032],
            'free sulfur dioxide': [25.0, 31.0],
            'total sulfur dioxide': [116.0, 113.0],
            'density': [0.99057, 0.9903],
            'pH': [3.2, 3.37],
            'sulphates': [0.44, 0.42],
            'alcohol': [11.7, 12.9]
        }
        df = pd.DataFrame (data, columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)
        encoded_predictions = model.predict_classes(test_scaled[:2])
        return render_template('index.html', prediction = encoded_predictions)
    else:
        return render_template('index.html')

@app.route("/manufacturing/<location>")
def manufacturing(location):
    """Return the MetaData for a given location."""
    # results = cur.execute(f"SELECT * FROM cacao_clean_withbean WHERE company_location='{location}'").fetchall()
    # Create a dictionary entry for each row of metadata information
    cacao_data = jsonify(cacao_table)
    return cacao_data



if __name__ == "__main__":
    app.run()
