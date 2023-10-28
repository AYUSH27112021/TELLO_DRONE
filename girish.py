from djitellopy import Tello
import time

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_down(60)
tello.set_speed(80)
tello.move_forward(30)
tello.set_speed(60)
tello.move_forward(20)
tello.set_speed(30)
tello.move_forward(10)
tello.land()
