import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request
from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Sequential
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.callbacks import EarlyStopping


def train():



    # Read the CSV and Perform Basic Data Cleaning
    df = pd.read_csv("mushrooms3.csv")

    #Create a Train Test Split
    y = df["class"]
    X = df.drop(columns=["class"])
    print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)

    label_encoder = LabelEncoder()
    label_encoder.fit(y_train)
    encoded_y_train = label_encoder.transform(y_train)
    encoded_y_test = label_encoder.transform(y_test)

    y_train_categorical = to_categorical(encoded_y_train)
    y_test_categorical = to_categorical(encoded_y_test)

    # Pre-processing
    # Scale your data

    X_scaler = MinMaxScaler().fit(X_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)

    #train the model
    model = Sequential()
    model.add(Dense(units=100, activation='relu', input_dim=6))
    model.add(Dense(units=100, activation='relu'))
    model.add(Dense(units=2, activation='softmax'))

    #   Compile and fit the model
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# set early stopping as callback
    callbacks = [EarlyStopping(monitor='loss', patience=2)]
    model.fit(
        X_train_scaled,
        y_train_categorical,
        callbacks=callbacks,
        epochs=60,
        shuffle=True,
        verbose=2
)

    model_loss, model_accuracy = model.evaluate(
        X_test_scaled, y_test_categorical, verbose=2)
    print(
        f"Normal Neural Network - Loss: {model_loss}, Accuracy: {model_accuracy}")

    encoded_predictions = model.predict_classes(X_test_scaled[:6])
    prediction_labels = label_encoder.inverse_transform(encoded_predictions)

    print(f"Predicted classes: {prediction_labels}")
    print(f"Actual Labels: {list(y_test[:6])}")

# Load the model
    from tensorflow.keras.models import load_model

# save fitted model to file
    model.save("mushrooms_deeplearn2.h5")

# @app.route("/manufacturing/<location>")
# def manufacturing(location):
#     """Return the MetaData for a given location."""
#     # results = cur.execute(f"SELECT * FROM cacao_clean_withbean WHERE company_location='{location}'").fetchall()
#     # Create a dictionary entry for each row of metadata information
#     cacao_data = jsonify(cacao_table)
#     return cacao_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("hello")
    return render_template("index.html")

@app.route("/manufacturing", methods=["GET"])
def manufacturing():
    return render_template("manufacturing.html")

@app.route("/marketplace", methods=["GET"])
def marketplace():
    return render_template("manufacturing.html")

if __name__ == "__main__":
    app.run()
