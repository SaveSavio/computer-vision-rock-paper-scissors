# TensorFlow is required for Keras to work
from keras.models import load_model  
# opencv-python
import cv2
import numpy as np
import time
import random


class camera_rps:

    def __init__(self):
        """
        Initializes the class, definining the number of wins necessary to win the match,
        initializing the computer and user wins to zero.
            Parameters:
                the number of wins necessary to win the match (3 by default)
        """

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        self.model = load_model("keras_Model.h5", compile=False)
        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()
        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture(0)


    def get_winner(self, computer_choice, player_choice):
        """
            Defines the rules of the game
                Parameters: computer' and players choice, can be "rock", "paper" or "scissors"
                Returns: nothing. Prints the winner on screen.
        """
        print(f'Player chooses: {player_choice}')
        print(f'Computer chooses: {computer_choice}')
        
        if player_choice == computer_choice:
            print("It's a tie")
            user_win = 0
            computer_win = 0
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Paper" and computer_choice == "Rock")
            or (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            print("You win!")
            user_win = 1
            computer_win = 0
            #return user_win, computer_win
        else:
            print("You lost!")
            user_win = 0
            computer_win = 1

        return user_win, computer_win



    def countdown(self, seconds):
        # import a local instance of "time"
        # this is necessary so to not interfere with the get_prediction instance
        import time as time

        start_time = time.time()
        end_time = start_time + seconds
        
        while time.time() < end_time:
            remaining_seconds = int(end_time - time.time())
            # print remaining time in [s]
            print(remaining_seconds + 1)
            # Add a small delay to prevent the loop from consuming too much CPU
            time.sleep(1)

        #print("Shoot!")



    def get_prediction(self):
        """
            Returns a prediction from the keras RPS model
            
            In your case you only give it one image at a time.
            That means that the first element in the list returned from the model is a list of probabilities
            for the four different classes. Print the response of the model if you are unclear of this.
            
                Parameters:
            
                Returns: the prediction of the RPS keras model
        """
        # set the acquisition duration in seconds
        duration = 3
        # Get the current time
        start_time = time.time()
        # Calculate the end time by adding the duration to the start time
        end_time = start_time + duration

        while time.time() < end_time:
            self.countdown(3)
            print('Shoot!')

            # Grab the webcamera's image.
            ret, image = self.camera.read()
            # Resize the raw image into (224-height,224-width) pixels
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            # Show the image in a window
            cv2.imshow("Webcam Image", image)
            # Make the image a numpy array and reshape it to the models input shape.
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            # Normalize the image array
            image = (image / 127.5) - 1
            
            # Predicts the model
            prediction = self.model.predict(image)
            index = np.argmax(prediction)
            # slice class name to remove part of the string and return only the class (R, P, or S)
            class_name = self.class_names[index][2:-1]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name, end="")
            print("\nConfidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            # Listen to the keyboard for presses.
            keyboard_input = cv2.waitKey(1)
            # 27 is the ASCII for the esc key on your keyboard.
            if keyboard_input == 27:
                break
        
        #TODO: work on this bit of code to solve the issues with workflow
        # read the documentation to understand the expectations
        #self.countdown(3)
        #self.camera.release()
        #cv2.destroyAllWindows()
        cv2.waitKey(2)  # Add this line

        return class_name
    


    def get_computer_choice(self):
        """
            Randomly choose the computer selection
            Parameters: none
            Returns: random choice between rock, paper, scissors
        """
        variables = ['Rock', 'Paper', 'Scissors']
        # randomly chooses from the variables list
        computer_choice = random.choice(variables)
        return computer_choice