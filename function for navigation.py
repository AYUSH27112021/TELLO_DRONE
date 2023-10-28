# -*- coding: utf-8 -*-
from djitellopy import Tello
from xlwt import Workbook
import math

wb = Workbook()
count=0
# create and connect
tello = Tello()
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # forward detection only
tello.takeoff()
def getdir():
    count=0
    a=tello.get_mission_pad_distance_x()
    b=tello.get_mission_pad_distance_y()
  #  tello.get_mission_pad_distance_z()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(1, 0, 'x')
    sheet1.write(2, 0, 'y')
    sheet1.write(1, count, (a/111320)+77.7646657)#assuming pad x to be 77.76
    sheet1.write(2, count, (40075000 * math.cos((b/111320))) / 360+56.556745)#assuming pad y to 56.55
    count=count+1#40075 km * cos((b/111320)) / 360
tello.move_forward(50)
getdir()
tello.land()
