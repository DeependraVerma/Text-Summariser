from flask import Flask, render_template, request
import os
from textSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train')
def training():
    try:
        os.system("python main.py")
        return "Training successful !!"
    except Exception as e:
        return f"Error Occurred! {e}"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form['text']
        obj = PredictionPipeline()
        summarized_text = obj.predict(text)
        return summarized_text
    except Exception as e:
        return f"Error Occurred! {e}"

if __name__ == '__main__':
    app.run(debug=True)
