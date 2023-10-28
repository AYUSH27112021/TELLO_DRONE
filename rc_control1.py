#from djitellopy import TelloSwarm
from djitellopy import Tello
import time

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_down(60)
#forward
def mov_forward():
    for i in range(0,10,1):
        tello.send_rc_control(i*5,0,5,0)
        print(i)
        time.sleep(0.6503010733870942)
    for i in range(0,10,1):
        tello.send_rc_control(-i*5,0,5,0)
        time.sleep(0.6503010733870942)
    time.sleep(1)

mov_forward()

tello.land()