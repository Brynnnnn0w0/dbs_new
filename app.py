# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:00:15 2022

@author: Brynn
"""

from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return (render_template("index.html",result1 = r1 ,result2 = r2))
    else:
        return (render_template("index.html",result1 = "waiting",result2 = "waiting"))
    
if __name__ == '__main__':
    app.run()
