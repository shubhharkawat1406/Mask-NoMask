import cv2
import numpy as np
haar_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

from tensorflow.keras.models import load_model
model = load_model('mask_detection_model.h5')

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if success:
        faces = haar_data.detectMultiScale(img)
        for x, y, w, h in faces:
            face = img[y:y+h, x:x+w, :]
            face = cv2.resize(face, (128, 128))        
            face = np.array(face)
            face = face.reshape(1,128,128,3)
            if model.predict(face) > 0.5:
                state = 'Mask'
                color = (0,255,0)
            else:
                state = 'No Mask'
                color = (0,0,255)
            cv2.rectangle(img, (x,y), (x+w,y+h), color, 4)
            cv2.putText(img, state, (x,y), cv2.FONT_HERSHEY_PLAIN,2,color,2)
            
        cv2.imshow('Faces', img)
        
        if cv2.waitKey(1) == 27:
            break
            
cap.release()
cv2.destroyAllWindows()