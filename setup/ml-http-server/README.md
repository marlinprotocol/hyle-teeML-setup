# FERPlus

We used the dataset FERPlus https://github.com/microsoft/FERPlus and followed the README to prepare it for use.

# Giza account

Please follow Giza documentation to set up an account, so you can use their api here https://docs.gizatech.xyz/welcome/quickstart

# Train the XGBoost model

```
python3 ./run_training.py
```

It creates a json file containing the trained model, that can be transpiled with Giza

# Register model to Giza

```
 giza transpile serialized_optimized.json --output-path xgboost_onnx
 ```

it will create a folder locally called xgboost_onnx that contains the cairo program generated by Giza. You can build it with `scarb build`

# Deploy endpoint to make the model available
```
giza endpoints deploy --model-id 844 --version-id 6
```

# Call the model

Modify  `./run_call.py` accordingly
```
MODEL_ID = 844  # Update with your model ID
VERSION_ID = 6  # Update with your version ID
```
Then
```
python3 ./run_call.py
```