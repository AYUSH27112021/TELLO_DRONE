from djitellopy import TelloSwarm
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_up(50)
tello.move_forward(50)
'''
                       A
                       -
                       -
          b-------------\---------------c
                       -
                       -
                       B
'''            
#forward           
# def mov_forward():
#     tello.go_xyz_speed(50,0,5,50)
#     tello.go_xyz_speed(-50,0,5,50)
# #left
# def mov_left():
#     tello.go_xyz_speed(0,-50,5,50)
#     tello.go_xyz_speed(0,50,5,50)
# #right
# def mov_right():
#     tello.go_xyz_speed(0,50,5,50)
#     tello.go_xyz_speed(0,-50,5,50)
# #back
# def mov_back():
#     tello.go_xyz_speed(-50,0,5,50)
#     tello.go_xyz_speed(50,0,5,50)

# mov_forward()
y=tello.get_current_state()
print(y)
# mov_back()
# mov_left()
# mov_right()
tello.land()

