# Computer Vision RPS
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins.
<br><br>
This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera. 

## Create a computer vision system (model)

We created a computer vision system with the tool provided by https://teachablemachine.withgoogle.com/

Teacheable Machines is *"A fast, easy way to create machine learning models for your sites, apps, and more – no expertise or coding required"*

We have selected a "Image Project" the "Standard Image Project". We have trained the model to recognize four cases (or Classes): Rock, Paper, Scissors, and Nothing from snapshots recorded whilst forming the three shapes with our right hands.

After a quick validation with the online tool, we have exported using the options:
- Tensoflow
- Keras

therefore creating a .zip file containing the following:
- keras_model.h5
- labels.txt

We have also copied the testing file for OpenCV.

## Enviroment
The code has been tested on a ARM64 M1 using Tensorflow-macos, Tensorflow-metal and OpenCV.

Package requirements can be found in the file
- requirements.txt

## Testing the enviroment and model
Once all the requirements are installed, the model can be tested with the code provided, in the Export Window, by Teacheable Machines.

```python
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
```
##