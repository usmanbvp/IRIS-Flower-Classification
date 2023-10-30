from flask import Flask, render_template,request
import pickle
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)

with open ('models/model.pkl','rb') as f:
    model = pickle.load(f) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        spl = float(request.form['spl'])
        spw = float(request.form['spw'])
        ptl = float(request.form['ptl'])
        ptw = float(request.form['ptw'])

        data = [[spl, spw, ptl, ptw]]
        prediction = model.predict(data)[0]
    return render_template('index.html', prediction = prediction)


if __name__ == "__main__":
    app.run(debug = True)