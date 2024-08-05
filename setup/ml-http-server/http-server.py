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
#     training_data = FerPlus('Training', '/home/marlin/FERPlus/fer2013new.csv', '/home/marlin/FERPlus/')
#     batch_size = 2**12

#     # Create data loaders.
#     train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)
#     img_list = []

#     for X, y in training_data:
#         img_list.append(X.numpy().flatten())

#     print(len(img_list))

#     img_dataframe = pd.DataFrame(img_list)

#     # Load the local classifier
#     print("Loading XGBClassifier...")
#     model = joblib.load("serialized_optimized.pkl")
    
#     result = prediction(img_list[0], model)
#     print("Prediction result: ", result)
#     app.run(debug=True)

# To run the app in production, use the following command:
# gunicorn -w 1 -b 127.0.0.1:5000 http-server:app