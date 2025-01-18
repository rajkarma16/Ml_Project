import os
import pickle
from flask import Flask, request, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)



with open("predictions.pkl", "rb") as pred_file:
    predictions = pickle.load(pred_file)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        area = request.form.get("area")
        month = request.form.get("month")

        predictions["Date"] = pd.to_datetime(predictions["Date"])
        predictions["month"] = predictions["Date"].dt.month_name()

        filtered_data = predictions[(predictions["Area"] == area) & (predictions["month"] == month)]

        if filtered_data.empty:
            return render_template("index.html", error="No data found for the selected area and month.")

        output_data = filtered_data[["Crime_Type", "Prediction"]]

        return render_template("index.html", table_data=output_data.to_html(index=False))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
