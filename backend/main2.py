from flask import Flask, render_template, redirect, request, url_for 
from werkzeug.utils import secure_filename
import tensorflow as tf
import os
import numpy as np
from cv2 import cv2
from googletrans import Translator
import pytesseract



translator = Translator()


UPLOAD_FOLDER = '/Users/juhiemotiani/Documents/CHARUSAT/SEM 5/SGP/uploaded_images/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app = Flask("__main__")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def prepare(filepath):
    IMG_SIZE = 70
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1,IMG_SIZE,IMG_SIZE,1)

def hindi2Eng(inputText):
    translation = translator.translate(inputText,dest="en")
    translated_sentence = (f"{translation.text}")
    return translated_sentence

def eng2Hindi(inputText):
    translation = translator.translate(inputText,dest="hi")
    translated_sentence = (f"{translation.text}")
    return translated_sentence

def eng2Eng(filename):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    reduced_noise = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,12)
    # cv2.imshow("",reduced_noise)
    # cv2.waitKey(0)
    # print("\nImage is loaded succesfully")

    text=pytesseract.image_to_string(reduced_noise,lang='eng')
    print("The text is :\n",text)
    output = eng2Hindi(text)
    return output


def predictThis(filename):
    model = tf.keras.models.load_model("/Users/juhiemotiani/Documents/CHARUSAT/SEM 5/SGP/my_model2.h5")
    indexVals =[2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2354, 2357, 2358, 2359, 2360, 2361, 42, 42, 42, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2413, 2414, 2415]

    # for image in images:
    imgPath = "/Users/juhiemotiani/Documents/CHARUSAT/SEM 5/SGP/uploaded_images/" + filename
    prediction = model.predict([prepare(imgPath)])
    index=0
    for values in prediction[0]:
        if(values == 1):
            predicted_output = chr(indexVals[index])
            print(predicted_output)
            index=0
            break
        index+=1
    return predicted_output



@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        selectedVal = request.form.get('select1')
        print(selectedVal)
        if selectedVal == 'hindiChar':
            myFile = request.files['myImage']
            # print(myFile.filename)
            filename = secure_filename(myFile.filename)
            myFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output=predictThis(filename)
            return render_template('index.html', token=output)
        if selectedVal == 'hindi':
            myFile = request.files['myImage']
            # print(myFile.filename)
            filename = secure_filename(myFile.filename)
            myFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output = eng2Eng(filename)
            # output=predictThis(filename)
            return render_template('index.html', token=output)
        if selectedVal == 'english':
            # inputText = request.form.get('inpText')
            # print(inputText)
            # outputText = hindi2Eng(inputText)
            return render_template('index.html')
    else:
        return render_template('index.html')
   

app.run(port=3000)