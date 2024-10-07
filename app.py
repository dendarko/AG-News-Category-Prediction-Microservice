from fastai.text.all import load_learner
from flask import Flask, request, render_template
from google.cloud import storage
import os

app = Flask(__name__)

def download_model(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

# Bucket and folder details
bucket_name = 'agnewsbucket-2024project-1'  # Your bucket name
subfolder = 'agnewsdeployment'  # The folder inside your bucket

# Download the model from Google Cloud Storage
source_blob_name = f'{subfolder}/text_classification_model.pkl'
destination_file_name = 'text_classification_model.pkl'
download_model(bucket_name, source_blob_name, destination_file_name)

# Load the model
model = load_learner(destination_file_name)

# Mapping of numeric labels to category names
label_to_category = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = model.predict(text)
    category_name = label_to_category[prediction[1].item()]  # Convert the numeric label to category name
    return render_template('index.html', prediction=category_name, text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
