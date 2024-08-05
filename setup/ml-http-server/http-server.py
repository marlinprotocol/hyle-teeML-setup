import pandas as pd
import joblib
from flask import Flask, request, jsonify

def prediction(input, model):
    input_df = pd.DataFrame([input])
    result = model.predict(input_df)
    return result

# Load the local classifier
print("Loading XGBClassifier...")
model = joblib.load("serialized_optimized.pkl")

app = Flask(__name__)

@app.route('/prediction', methods=['POST'])
def predict():
    data = request.get_json()
    image = data['image']
    print(image)
    result = prediction(image, model)
    return jsonify({'prediction': result.tolist()})

# Comment out or remove below lines to run in prod
# if __name__ == '__main__':
#     app.run(debug=True)

# To run the app in production, use the following command:
# gunicorn -w 1 -b 127.0.0.1:5000 http-server:app