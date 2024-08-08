import pandas as pd
import joblib
from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.asymmetric import ed25519
from base64 import b64encode
from hashlib import sha256
from datetime import datetime

def prediction(input, model):
    input_df = pd.DataFrame([input])
    result = model.predict(input_df)
    return result

# Load the local classifier
print("Loading XGBClassifier...")
model = joblib.load("serialized_optimized.pkl")

# Load the secret key from the id.sec file
with open("/app/id.sec", "rb") as key_file:
    secret_key_bytes = key_file.read()

# The secret key consists of 32 bytes for the private scalar and 32 bytes for the public key.
private_scalar = secret_key_bytes[:32]
public_key_bytes = secret_key_bytes[32:]

# Create a private key object
private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_scalar)

app = Flask(__name__)

@app.route('/prediction', methods=['POST'])
def predict():
    data = request.get_json()
    image = data['image']
    prediction_result = prediction(image, model)
    image_hash = sha256(str(image).encode()).hexdigest()
    timestamp = datetime.utcnow().isoformat()

    data_to_sign = f"{str(prediction_result)}{image_hash}{timestamp}"

    data_to_sign_bytes = data_to_sign.encode()
    signature = private_key.sign(data_to_sign_bytes)
    signature_base64 = b64encode(signature).decode('utf-8')
    return jsonify({
        'prediction': prediction_result.tolist(),
        'attestation': signature_base64,
        'image_identifier': image_hash,
        'timestamp': timestamp
    })

# Comment out or remove below lines to run in prod
# if __name__ == '__main__':
#     app.run(debug=True)

# To run the app in production, use the following command:
# gunicorn -w 1 -b 127.0.0.1:5000 http-server:app