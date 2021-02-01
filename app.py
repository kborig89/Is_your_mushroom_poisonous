import os
import pandas as pd
import numpy as np
from flask import Flask, render_template,jsonify, request
# from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

# load model
model = keras.models.load_model('model/model.h5')
# summarize model
model.summary()

# from sklearn.preprocessing import MinMaxScaler


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

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        shape = request.form['shape']
        surface = request.form['surface']
        color = request.form['color']
        odor = request.form['odor']
        print = request.form['print']
        population = request.form['population']
        arr= np.array(([[shape,surface,color,odor,print,population]]))
        pred = model.predict(arr)
        return render_template('index.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)    
        
        