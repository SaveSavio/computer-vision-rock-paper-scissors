import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5', compile =  False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# print('data shape: ', data.shape)
# print('data[0] shape: ', data[0].shape)


while True: 
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)

    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    print('normalized image shape: ', normalized_image.shape)
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
