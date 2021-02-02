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

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test", methods=['GET', 'POST'])
def test():
    
    """Return the homepage."""
    if request.method == 'POST':
        print(request.form)
        cap_shape = request.form['cap-shape']
        cap_surface = request.form['cap-surface']
        cap_color = request.form['cap-color']
        odor = request.form['odor']
        spore_print_color = request.form['spore-print-color']
        population = request.form['population']

        data = {'cap-shape':  [cap_shape],
                'cap-surface': [cap_surface],
                'cap-color': [cap_color],
                'odor': [odor],
                'spore-print-color': [spore_print_color],
                'population': [population],
                }


        df = pd.DataFrame (data, columns = ['cap-shape', 'cap-surface', 'cap-color', 'odor', 'spore-print-color', 'population'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)
        encoded_predictions= deep_learning_model.predict_classes(test_scaled[:2])
        if encoded_predictions[0] == 1:
            final_prediction = "Likely Poisionous" 
        else: 
            final_prediction = "Likely Safe" 
        print(final_prediction)
        return render_template('test.html', prediction = final_prediction)
    else:
        return render_template('test.html')




@app.route("/graphs")
def graphs():
    return render_template("graphs.html")

@app.route("/about")
def about():
    return render_template("about.html")

   






if __name__ == "__main__":
    app.run()
