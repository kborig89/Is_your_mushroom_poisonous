import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request
from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)


# load model
deep_learning_model = load_model('model/mushrooms_deeplearn2.h5')


@app.route("/", methods=['GET', 'POST'])
def index():
    
    """Return the homepage."""
    if request.method == 'POST':
        cap-shape = request.form['cap-shape']
        cap-surface = request.form['cap-surface']
        cap-color = request.form['cap-color']
        odor = request.form['odor']
        spore-print-color = request.form['spore-print-color']
        population = request.form['population']

        data = {'cap-shape':  [5.8, cap-shape],
                'cap-surface': [0.300, cap-surface],
                'cap-color': [0.33, cap-color],
                'odor': [3.5, odor],
                'spore-print-color': [0.033, spore-print-color],
                'population': [25.0, population],
                }
    


         df = pd.DataFrame (data, columns = ['cap-shape', 'cap-surface', 'cap-color', 'odor', 'spore-print-color', 'population'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)
        encoded_predictions= model.predict_classes(test_scaled[])
        if encoded_predictions[0] == 1:
            final_prediction = "Likely Poisionous"
        else: 
            final_prediction = "Likely Safe"
        return render_template('index.html', prediction = final_prediction)
    else:
        return render_template('index.html')




@app.route("/manufacturing")
def manufacturingMain():
    return render_template("manufacturing.html")

   






if __name__ == "__main__":
    app.run()
