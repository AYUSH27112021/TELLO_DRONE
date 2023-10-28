from djitellopy import TelloSwarm
from djitellopy import Tello
import time
import math


tello = Tello()

swarmall = TelloSwarm.fromIps([
    "192.168.0.107",#F1D
    "192.168.0.108",#ECA
    "192.168.0.106",#CCO
    "192.168.0.105",#FO3
    # "192.168.0.102"
])


single = TelloSwarm.fromIps([
    "192.168.0.102"
])

swarmall.parallel(lambda i, tello:tello.connect())
# swarmall.parallel(lambda i, tello:tello.land())
# swarmall.parallel(lambda i, tello:tello.takeoff())
# points = [(35,35,0,0),(19,46,0,0),(50,0,0,0),(46,19,0,0),(35,35,0,0),(19,46,0,0),(0,50,0,0)]
# for i in points :
#     x = i[0]
#     y = i[1]
#     z = i[2]
#     yaw = i[3]
#     swarmall.parallel(lambda i, tello:tello.send_rc_control(x,y,z,yaw))
#     time.sleep(0.6503010733870942)
    
# swarmall.parallel(lambda i, tello:tello.move_up(30))
# time.sleep(3)
# swarmall.parallel(lambda i, tello:tello.land())
# # swarmall.parallel(lambda i, tello:tello.send_rc_control(19,46,0))
# # swarmall.parallel(lambda i, tello:tello.send_rc_control(50,0,0))
# # swarmall.parallel(lambda i, tello:tello.send_rc_control(46,19,0))
# # swarmall.parallel(lambda i, tello:tello.send_rc_control(35,35,0))
# # swarmall.parallel(lambda i, tello:tello.send_rc_control(0,50,0))
# # [35,35,0]
# # [19,46,0]
# # [50,0,0]
# # [46,19,0]
# # [35,35,0]
# # [19,46,0]
# # [0,50,0]