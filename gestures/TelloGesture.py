                                                                                                                                                                                              
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
    mpHands = mp.solutions.hands#line changed
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils#line changed

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


def TelloCommands(gesname, commence=True):
    global connectcount, takeoffcount, landcount, flipcount 
    

    if commence == True:
        if  connectcount == 0:
            if gesname == 'peace':
                connectcount = 1
                print("sending: connect")
                tello.connect()
                
        if takeoffcount == 0:
            if gesname == 'thumbs up':
                takeoffcount = 1
                print("takeoff")
                tello.takeoff()

        if flipcount == 0:    
            if gesname == 'stop':
                flipcount = 1
                print("sending: flip")
                tello.flip_forward()

        if landcount == 0:    
            if gesname == 'thumbs down':
                landcount = 1
                print("landing")
                time.sleep(3)
                tello.land()
            
    # tello.send_rc_control(up_down,for_back,left_right,0)
    
            


# def tellocoms(self,):
#       gesture_id = gesture_buffer.get_gesture()
#       print("GESTURE", gesture_id)

#       if not self._is_landing:
#           if gesture_id == 0:  # Forward
#               self.forw_back_velocity = 30
#           elif gesture_id == 1:  # STOP
#               self.forw_back_velocity = self.up_down_velocity = \
#                   self.left_right_velocity = self.yaw_velocity = 0
#           if gesture_id == 5:  # Back
#               self.forw_back_velocity = -30

#           elif gesture_id == 2:  # UP
#               self.up_down_velocity = 25
#           elif gesture_id == 4:  # DOWN
#               self.up_down_velocity = -25

#           elif gesture_id == 3:  # LAND
#               self._is_landing = True
#               self.forw_back_velocity = self.up_down_velocity = \
#                   self.left_right_velocity = self.yaw_velocity = 0
#               self.tello.land()

#           elif gesture_id == 6: # LEFT
#               self.left_right_velocity = 20
#           elif gesture_id == 7: # RIGHT
#               self.left_right_velocity = -20

#           elif gesture_id == -1:
#               self.forw_back_velocity = self.up_down_velocity = \
#                   self.left_right_velocity = self.yaw_velocity = 0

#           self.tello.send_rc_control(self.left_right_velocity, self.forw_back_velocity,
#                                      self.up_down_velocity, self.yaw_velocity)


hands()
    
