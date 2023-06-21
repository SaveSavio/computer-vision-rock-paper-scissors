# Computer Vision RPS
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins.

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play against the computer using a webcam.

<br>

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

<br>

## Testing the enviroment and the model
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
The terminal will stream the predictions made by the model.

<br>

## The camera_rps class
The file camera_rps.py contains the necessary packages requiring import and the *camera_rps* class that contains all the relevant methods of the game.

```python
def __init__(self):
```
initializes the class by loading the model and the labels that are going to be used.

```python
def get_winner(self, computer_choice, player_choice):
```
defines the rules of the game
```python
def countdown(self, seconds):
```
defines a *"3...2...1...shoot!"* countdown necessary to simulate the game rules but it is also necessary to determine the moment in time in which a snapshot from the webcam is taken and passed to the Tensorflow engine".

```python
def get_prediction(self):
```
is the "engine" of the game, taking a snapshot from the camera, passing it to Tensorflow and returning one of the classes *rock, paper, scissors* based on their likelyhood (the class with higher confidence score is returned).

```python
def get_computer_choice(self):
```
simply randomly chooses between the three availabe classes which are stored in an array of strings.

## main.py

The *main* file contains the necessary instructions to win the game.

```python
from camera_rps import camera_rps

def play_game():
    
    # initilize the number of computer and user wins to zero
    computer_wins = 0
    user_wins = 0
    # create an instance of the class camera_rps called game
    game = camera_rps()
    while True:
        # get the player choice through the camera
        player_choice = game.get_prediction()
        # get the computer choice by randomly selecting a c lass
        computer_choice = game.get_computer_choice()
        # use the method get_winner to determine the winner of the turn
        user_win, computer_win = game.get_winner(computer_choice, player_choice)
        # increment the number of wins
        user_wins += user_win
        computer_wins += computer_win

        # checks if one between the player and the computer has reached three turn victories,
        # otherwise continutes the loop
        if computer_wins == 3:
            print("Computer wins the game")
            break
        elif user_wins == 3:
            print("You win, congrats!")
            break
        else:
            print(f"User score: {user_wins}\nComputer score: {computer_wins}")
            print('Play another turn')

    # I should add a way of exiting the game (use ESC)
    return


play_game()
```