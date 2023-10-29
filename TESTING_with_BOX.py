import numpy as np
import cv2
import time
from keras.models import load_model

from IMAGE_PREPROCESS_files import preprocessing
from tensorflow.keras.utils import to_categorical
import csv
import os
import datetime


from imutils.object_detection import non_max_suppression
model = load_model('Fighting.h5')
print("Model Loaded")

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def get(stream):
        fgbg = cv2.createBackgroundSubtractorMOG2()
        font = cv2.FONT_HERSHEY_PLAIN

        hog = cv2.HOGDescriptor()
        #hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        
        cap = cv2.VideoCapture(stream)
        print("video loaded")
        kk = 0
        def Label_decode(argument): 
                switcher = { 
                        0: " ", 
                        1: "Suspicious Activity",
                        
                } 
                return switcher.get(argument, "nothing") 
        d = 0
        while(cap.isOpened()):

            ret, frame = cap.read()
            frame1 = frame
            height, width = frame.shape[:2]            
            img = cv2.resize(frame, (50,50))
            img_d = cv2.resize(frame, (480,320))

            X = preprocessing.image.img_to_array(img)


            X = np.expand_dims(X, axis=0)
            predictions = model.predict(X)
            result = Label_decode(np.argmax(predictions[0]))
            #print(result) 

            if(height > width):
                    frame = np.rot90(frame)
                    frame = np.rot90(frame)
                    frame = np.rot90(frame)
                    img_d = cv2.resize(frame, (480,320))

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img_d,result, (25,25), font, 1.0, (0, 0, 255), 2)
            
            (rects, weights) = hog.detectMultiScale(img_d, winStride=(4, 4), padding=(8, 8), scale=1.05)
            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)


            for (xA, yA, xB, yB) in pick:
                    if(xA > 5):
                            if(np.argmax(predictions[0]) == 1):
                                    if(d == 1):
                                            now = datetime.datetime.now()
                                            list = os.listdir('./Suspicious_Activity/') # dir is your directory path
                                            image_name = 'Suspicious_Activity_' + str(len(list)+1) + '.png'
##                                            speaker.Speak(result)
                                            cv2.imwrite('./Suspicious_Activity/'+ image_name ,img_d)
                                            d = 0
                                            with open('Suspicious_Activity_Logs.csv', 'a', newline='') as csvfile:
                                                    fieldnames = ['Date', 'Time', 'Image_name']
                                                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                                    writer.writerow({'Date':now.strftime("%d-%m-%Y"),'Time':now.strftime("%H:%M") ,'Image_name': image_name })

                                    cv2.rectangle(img_d, (xA, yA), (xB, yB), (0, 0, 255), 4)
                                    cv2.putText(img_d,'x', (int((xA + xB)/2),int((yA + yB)/2)), font, 1.0, (0, 0, 255), 2)
                            else:
                                    d = 1
                                    cv2.rectangle(img_d, (xA, yA), (xB, yB), (0, 255, 0), 4)
                                    cv2.putText(img_d,'x', (int((xA + xB)/2),int((yA + yB)/2)), font, 1.0, (0, 255, 0), 2)


            cv2.imshow('Output_video',img_d)
            gray = cv2.cvtColor (img_d, cv2.COLOR_BGR2GRAY)
           # fgmask = fgbg.apply (gray)
         #   cv2.imshow('Background_substraction',fgmask)
            speaker.Speak(result)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

get(r"C:\Users\SSharma\Downloads\Theft.mp4")
