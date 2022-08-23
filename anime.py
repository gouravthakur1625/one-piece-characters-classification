# Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'E:/Anime project/model_anime2.h5'

model = load_model(filepath)
print(model)

print("Model Loaded Successfully")


def pred_tomato_dieas(tomato_plant):
    test_image = load_img(tomato_plant, target_size=(224, 224))  # load image
    print("@@ Got Image for prediction")

    test_image = img_to_array(test_image) / 255  # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis=0)  # change dimention 3D to 4D

    result = model.predict(test_image)  # predict diseased palnt or not
    print('@@ Raw result = ', result)

    pred = np.argmax(result, axis=1)
    print(pred)
    if pred == 0:
        return "Ace", 'Ace_info.html'
    elif pred == 1:
        return "Big Mom", 'Bigmom_info.html'
    elif pred == 2:
        return "Blackbeard", 'Blackbeard_info.html'
    elif pred == 3:
        return "Brook", 'Brook_info.html'
    elif pred == 4:
        return "Buggy", 'Buggy_info.html'    
    elif pred == 5:
        return "Chopper", 'Chopper_info.html'
    elif pred == 6:
        return "Crocodile", 'Crocodile_info.html'
    elif pred == 7:
        return "Doflamingo", 'Doflamingo_info.html'
    elif pred == 8:
        return "Dragon", 'Dragon_info.html'
    elif pred == 9:
        return "Kid", 'Eustass_info.html'
    elif pred == 10:
        return "Franky", 'Franky_info.html'
    elif pred == 11:
        return "Jinbe", 'Jinbei_info.html'
    elif pred == 12:
        return "Kaido", 'Kaido_info.html'
    elif pred == 13:
        return "Law", 'Law_info.html'
    elif pred == 14:
        return "Luffy", 'luffy_info.html'
    elif pred == 15:
        return "Mihawk", 'Mihawk_info.html'
    elif pred == 16:
        return "Nami", 'Nami_info.html'
    elif pred == 17:
        return "Robin", 'Robin_info.html'
    elif pred == 18:
        return "Roger", 'Roger_info.html'
    elif pred == 19:
        return "Sabo", 'Sabo_info.html'
    elif pred == 20:
        return "Sanji", 'sanji_info.html'
    elif pred == 21:
        return "Shanks", 'Shanks_info.html'
    elif pred == 22:
        return "Usopp", 'Usopp_info.html'
    elif pred == 23:
        return "Whitebeard", 'Whitebeard_info.html'
    elif pred == 24:
        return "Zoro", 'zoro_info.html'

# Create flask instance
app = Flask(__name__)


# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']  # fet input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join(
            'E:/Anime project/static/upload/',
            filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)

        return render_template(output_page, pred_output=pred, user_image=file_path)


# For local system & cloud
if __name__ == "__main__":
    #app.debug = True
    app.run(threaded=False, port=8080)

