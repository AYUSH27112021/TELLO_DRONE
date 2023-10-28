# -*- coding: utf-8 -*-
from djitellopy import TelloSwarm
from djitellopy import Tello
import time
#102-f1d, 106-cc0, 107-f03, 109-eca
swarm = TelloSwarm.fromIps([
    "192.168.0.102", #F1D
    "192.168.0.106", #CC0
    "192.168.0.107", #F03
    "192.168.0.109"  #ECA   
])

swarm_1_F1D = TelloSwarm.fromIps([
    "192.168.0.102"
    ])

swarm_2_CC0 = TelloSwarm.fromIps([
    "192.168.0.106"
    ])

swarm_3_F03 = TelloSwarm.fromIps([
    "192.168.0.107"
    ])

swarm_4_ECA = TelloSwarm.fromIps([
    "192.168.0.109"
    ])

swarm_diag_1 = TelloSwarm.fromIps([
    "192.168.0.102",
    "192.168.0.107"    
])

swarm_diag_2 = TelloSwarm.fromIps([
    "192.168.0.106",
    "192.168.0.109"
])

swarm.connect()
swarm.takeoff()
swarm.set_speed(50)
swarm.curve_xyz_speed(10, 0, 20, 65, 0, 50, 30) #give params x y z speed
swarm_diag_1.move_up(40)
swarm_diag_2.move_down(30)
swarm_diag_1.rotate_clockwise(45)
swarm_diag_2.rotate_counter_clockwise(45)
swarm.move_back(90)
swarm.flip_forward()
swarm.land() 
swarm.end()
