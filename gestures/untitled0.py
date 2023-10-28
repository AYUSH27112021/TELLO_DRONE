# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:59:18 2022

@author: Dell
"""

import cv2
from djitellopy import Tello
import time
tello = Tello()
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
tello.move_up(80)
#tello.move_up(100)
#tello.move_up(100)
#tello.move_up(100)
time.sleep(3)
cv2.imwrite("picture1.png", frame_read.frame)
time.sleep(1)
cv2.imwrite("picture.png", frame_read.frame)
time.sleep(1)
cv2.imwrite("picture2.png", frame_read.frame)

tello.land()
