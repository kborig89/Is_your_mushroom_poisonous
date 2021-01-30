import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request
from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# load model
model = load_model("mushrooms_deeplearn2.h5")
# summarize model.
model.summary()

from sklearn.preprocessing import MinMaxScaler

@app.route("/", methods=['GET', 'POST'])
def index():
    
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
        if encoded_predictions[0] == 1:
            final_prediction = "Likely Poisionous"
        else: 
            final_prediction = "Likely Safe"
        return render_template('index.html', prediction = final_prediction)
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
