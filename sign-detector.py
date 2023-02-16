import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow
from keras.preprocessing.image import img_to_array
from keras.models import load_model 
import os

def predict_output(roi):
    img = roi
    # img = cv2.resize(img,(28,28))
    img = img_to_array(img)
    img = img/255
    img = np.expand_dims(img,axis=0)
    prediction = model.predict(img)
    prediction = np.argmax(prediction,axis=1)
    # prediction = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"][prediction[0]]
    return prediction
    print(roi)
    return 1

cap = cv2.VideoCapture(0)
model = load_model('mainModel.h5')

while True:
    ret, frame = cap.read()
    # adefine region of interest

    roi = frame[100:400, 320:620]
    cv2.imshow( 'roi', roi)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(roi, (28, 28), interpolation = cv2. INTER_AREA)

    cv2.imshow("rot sacled and Eray", roi)
    copy = frame.copy()
    cv2.rectangle(copy, (320, 100), (620, 400), (255,0,0), 5)

    roi = roi.reshape(28,28)
    classes = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
    result = str(classes[predict_output(roi)[0]-1])
    cv2.putText(copy, result, (300,100), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
    cv2.imshow("frame", copy)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.distroyAllWindows()