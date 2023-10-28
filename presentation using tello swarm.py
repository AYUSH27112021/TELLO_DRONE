# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 06:29:04 2022

@author: Dell
"""
from djitellopy import TelloSwarm
from djitellopy import Tello
import time
#102-f1d, 106-cc0, 107-f03, 109-eca
swarm = TelloSwarm.fromIps([
    #"192.168.0.102", #F1D
    "192.168.0.103", #CC0
    "192.168.0.101", #F03
    #"192.168.0.109"  #ECA   
])

swarm.connect()
#swarm.takeoff()
swarm.parallel(lambda i, tello:tello.takeoff())
swarm.parallel(lambda i, tello:tello.move_up(30))
swarm.parallel(lambda i, tello:tello.flip_back())
swarm.parallel(lambda i, tello:tello.land())
#time.sleep(5)
#swarm.curve_xyz_speed(10, 0, 20, 65, 0, 50, 30) #give params x y z speed
# swarm_diag_up.move_up(40) #give params dist
# swarm_diag_2.move_down(20) #give params dist
# swarm_diag_up.move_down(40) #give params dist
# swarm.move_up(20) #give params dist
# swarm.flip_forward()
# swarm.land() 
#swarm.flip_backward()
