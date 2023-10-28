
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
import math
tello = Tello()
connectcount = 0
takeoffcount = 0
landcount = 0
flipcount = 0
rotatecount = 0
def hands():
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
            tello.land()
            t.join()
            break


def TelloCommands(gesname, commence=True):
    global connectcount, takeoffcount, landcount, flipcount, rotatecount
    

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
            if gesname == 'fist':
                flipcount = 1
                ip = input("Do you want to flip Y/N\n")
                if ip == 'y' or ip == 'Y':
                    print("sending: flip")
                    tello.flip_forward()

        if rotatecount == 0:
            if gesname == 'stop':
                rotatecount == 1
                print("Moving")
                points, temp = calc_pts_circle(30, 4, 50)
                submit_command_rc(points, temp)

        if landcount == 0:    
            if gesname == 'thumbs down':
                landcount = 1
                print("landing")
                time.sleep(3)
                tello.land()
            



def calc_pts_circle(velo, div, rad):
    points = []
    grad_angle = 360/div
    rad_angle = (grad_angle * math.pi)/180
    p0x = rad
    p0y = 0
    p0z = 0
    points.append((p0x,p0y,p0z))

    temp = (2.0 * float(rad)/float(velo)) * math.sin(float(rad_angle)/2.0)

    for item in range(div):
        p = item + 1
        px = math.sin(rad)
        py = math.cos(rad)
        pz = 0.1 * rad
        points.append((round(px), round(py), round(pz)))
    
    return points, temp

def arc(velo, div, rad, p_init, p_fin):
    points, temp = calc_pts_circle(velo, div, rad)

    new_points = []

    if p_init > p_fin:
        p_fin = p_fin + div 

    for item in range(p_init, p_fin+1):
        pos = item
        if pos >= div:
            pos = pos - div

        new_points.append(points[pos])
    return new_points, temp

def submit_command_rc(points, temp):
    if len(points) > 3:
        for item in points:
            x = item[0]
            y = item[1]
            z = item[2]
            print(f"[{x},{y},{z}]")
            tello.send_rc_control(x,y,z,0)
            # tello.send_rc_control(x,y,z,0)
            print("time:",temp)
            time.sleep(temp)

    elif len(points) <= 3:
        x = points[0]
        y = points[1]
        z = points[2]
        print(f"[{x},{y},{z}")
        tello.send_rc_control(x,y,z,0)
        # tello.send_rc_control(x,y,z,0)
        time.sleep(3)

    tello.move_up(30)
   
   
   
   


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # tello.move_up(30)






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
    
