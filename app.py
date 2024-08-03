from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

with open('migraine_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    data = [float(x) for x in request.form.values()]
    # Predict using the loaded model
    prediction = model.predict([data])
    return render_template('index.html', prediction_text=f'The predicted type of migraine is: {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)