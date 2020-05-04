import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'            # Hide TensorFlow GPU Warnings
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.backend import clear_session
import numpy as np
import cv2
from static_ui import window


clear_session()

# --------------------- Import Classifiers ---------------------
face_classifier = cv2.CascadeClassifier('model\haarcascade_frontalface_default.xml')
classifier = load_model('model\emotion_vgg_model.h5')

# --------------------- Variables ---------------------
class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
img_dimension = 48
rgb_color = (255, 0, 0)
text_font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# ------------------ Cap Video ------------------
cap = cv2.VideoCapture(0)
emotion_check = 'Neutral'


# --------------------- Emotion Recognition Loop ---------------------
def emotion_recognition(e, dui):
    global emotion_check
    if e.is_set():
        print('Emotion Recognition Stopped.')
        return
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 6)
    current_emotion = 'Neutral'

    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), rgb_color, 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (img_dimension, img_dimension), interpolation=cv2.INTER_AREA)

        cv2.rectangle(frame, (x, y), (x + w, y + h), rgb_color, 2)
        roi_frame = frame[y:y + h, x:x + w]
        roi_frame = cv2.resize(roi_frame, (img_dimension, img_dimension), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]
            label_position = (x, y)
            cv2.putText(frame, label, label_position, text_font, 2, rgb_color, 3)
        else:
            cv2.putText(frame, 'No Face Found', (20, 60), text_font, 2, rgb_color, 3)
        if label != 'Neutral':
            emotion_check = label
        current_emotion = label

    dui.frame_stream(label=current_emotion)
    dui.face_stream(frame)
    window.after(10, lambda: emotion_recognition(e, dui))


def action():
    return emotion_check
