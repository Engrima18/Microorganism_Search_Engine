from flask import Flask, request, render_template
import weaviate
import base64
import cv2
import re
from os import listdir
from tqdm import tqdm
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import io

app = Flask(__name__)

# Initialize Weaviate client
client = weaviate.Client(url='http://localhost:8080')
client.get_meta()

# Define Weaviate configuration
micor_obj = {
    'class': 'Microorganism',
    'vectorizer': 'img2vec-neural',
    'vectorIndexType': 'hnsw',
    'properties': [
        {'name': 'species', 'dataType': ['text']},
        {'name': 'filepath', 'dataType': ['text']},
        {'name': 'image', 'dataType': ['blob']},
    ],
    'moduleConfig': {
        'img2vec-neural': {
            'imageFields': ['image'],
        }
    }
}

# Define the dataset folder
dataset_folder = 'C:\\Users\\engri\\Desktop\\uni_ds\\CLC\\final-proj\\bacteria-images\\'

# Load dataset
dataset = []

for filename in tqdm(listdir(dataset_folder)):
    species_name = re.sub(r'_\d*|\.jpg|\.png', '', filename)
    filename = dataset_folder + filename
    img64 = cv2.imread(filename)
    try:
        img64 = cv2.imencode('.jpg', img64)
    except:
        print('skipped', filename)
        continue
    img64 = base64.b64encode(img64[1]).decode('utf-8')
    dataset.append(dict(species=species_name, filepath=filename, image=img64))

# Add dataset to Weaviate
for obj in tqdm(dataset):
    client.batch.add_data_object(obj, 'Microorganism')

# Wait for batch request to finish
client.batch.wait_for_completion()

# Set up Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get uploaded image
        uploaded_image = request.files['image']
        image_data = uploaded_image.read()

        # Perform similarity search
        res = client.query \
            .get('Microorganism', ['filepath', 'species']) \
            .with_near_image(io.BytesIO(image_data), 'image') \
            .with_limit(3) \
            .with_additional(['distance', 'certainty']) \
            .do()
        
        # Extract results
        res_list = res["data"]["Get"]["Microorganism"]

        # Prepare images for display
        result_images = []
        for elem in res_list:
            image = mpimg.imread(elem["filepath"])
            result_images.append(image)

        # Render template with results
        return render_template('results.html', result_images=result_images)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
