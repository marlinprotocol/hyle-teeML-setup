import requests
import json

# Load image data from JSON file
with open("image_array.json", "r") as file:
    image_data = json.load(file)

# Define the URL for the prediction endpoint
url = "http://127.0.0.1:5000/prediction"

# Send a POST request to the prediction endpoint
response = requests.post(url, json=image_data)

# Print the response from the server
print(response.json())