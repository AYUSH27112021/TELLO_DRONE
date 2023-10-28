from turtle import forward
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.python.keras.models import load_model
from djitellopy import Tello
import time
import threading 
import os
tello = Tello()
connectcount = 0
takeoffcount = 0
landcount = 0
flipcount = 0
def hands():
    global takeoffcount
    mpHands = mp.solutions.mediapipe.python.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.mediapipe.python.solutions.drawing_utils

    model = load_model('mp_hand_gesture')

    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    print(classNames)
    commandlist = ["PH", "connect", "takeoff", "land", "PH", "flip", "PH", "PH", "PH", "PH"]
    # [‘okay’, ‘peace’, ‘thumbs up’, ‘thumbs down’, ‘call me’, ‘stop’, ‘rock’, ‘live long’, ‘fist’, ‘smile’]
    # [0,      1,          2,          3,              4,       5,     6,         7,         8,       9]
    cap = cv2.VideoCapture(0)
    clearcount = 0
    while True:
        _, frame = cap.read()

        x, y, c = frame.shape

        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)

        className = ''
        comm = ''
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

            
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            
                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = classNames[classID]
                comm = commandlist[classID]

        cv2.putText(frame, comm, (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
        cv2.imshow("Output", frame) 
        if clearcount == 0:
            os.system('cls')
            clearcount = 1
                   
             
        
        t = threading.Thread(target=TelloCommands, args=(className,))
        t.start()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("process terminated")
            t.join()
            break

count = 0
for_back = 0
left_right = 0
up_down = 0
def TelloCommands(gesname, commence=True):
    global connectcount, takeoffcount, count, left_right, for_back, up_down
    
    
    
    if commence == True:

        if gesname == "fist":
            if takeoffcount == 0:
                takeoffcount == 1
                tello.takeoff()
            

        if count != 0:
            time.sleep(3)
            count+=1

        if gesname == 'peace':
            for_back = 30
            print(for_back)
            tello.send_rc_control(up_down,for_back,left_right,0)
            time.sleep(10)            
        
        if gesname == 'thumbs up':
            up_down = 30
            print(up_down)
            tello.send_rc_control(up_down,for_back,left_right,0)
            time.sleep(10)
        
        if gesname == 'thumbs down':
            print("landing")
            tello.land()

        if gesname == 'stop':
            left_right = 30
            print(left_right)
            tello.send_rc_control(up_down,for_back,left_right,0)
            time.sleep(10)
        
        

hands()