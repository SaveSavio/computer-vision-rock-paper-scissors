from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import time

class camera_rps:

    def __init__(self, num_lives = 3):
        #TODO: insert docstring
        """
        """

        self.num_lives = num_lives

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        self.model = load_model("keras_Model.h5", compile=False)
        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()
        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture(0)


    def countdown(self, seconds):
        import time as time_1

        start_time = time_1.time()
        end_time = start_time + seconds
        
        while time_1.time() < end_time:
            remaining_seconds = int(end_time - time_1.time())
            # print remaining time in [s]
            print(remaining_seconds+1)
            # Add a small delay to prevent the loop from consuming too much CPU
            time.sleep(1)

        print("Shoot!")


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
            class_name = self.class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            # print("Class:", class_name[2:], end="")
            # print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            # Listen to the keyboard for presses.
            keyboard_input = cv2.waitKey(1)

            # 27 is the ASCII for the esc key on your keyboard.
            if keyboard_input == 27:
                break

        self.camera.release()
        cv2.destroyAllWindows()

        return class_name, confidence_score