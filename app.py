
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import os
from MLproject.pipeline.Prediction import PredictionPipeline

app = Flask(__name__) # initializing the flask app


@app.route('/', methods = ['GET']) #route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train',methods = ['GET'])
def training():
    os.system("python main.py")
    return "Trained the Model sucessfully"


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)