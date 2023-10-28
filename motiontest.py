from djitellopy import TelloSwarm
from djitellopy import Tello
import time
import math

swarmall = TelloSwarm.fromIps([
    "192.168.0.102",#ECA
    "192.168.0.103",#CC0
    "192.168.0.104",#F1D
    "192.168.0.105",#FO3
    # "192.168.0.102"
])


single = TelloSwarm.fromIps([
    # "192.168.0.102"
])

swarm = TelloSwarm.fromIps([
    "192.168.0.102",#ECA
    "192.168.0.103",#CC0
    "192.168.0.104",#F1D
    "192.168.0.105"#F03
])

# swarm.parallel(lambda i, tello:tello.land())


def calc_pts_circle(velo, div, rad):
    points = []
    grad_angle = 90/div
    rad_angle = (grad_angle * math.pi)/180
    p0x = rad
    p0y = 0
    p0z = 0
    points.append((p0x,p0y,p0z))

    temp = (2.0 * float(rad)/float(velo)) * math.sin(float(rad_angle)/2.0)

    for item in range(div):
        p = item + 1
        px = rad * math.cos(p * rad_angle)
        py = rad * math.sin(p * rad_angle)
        points.append((round(px), round(py), 0))
    
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
            swarm.parallel(lambda i, tello:tello.send_rc_control(x,y,z,0))
            # tello.send_rc_control(x,y,z,0)
            print("time:",temp)
            time.sleep(temp)

    elif len(points) <= 3:
        x = points[0]
        y = points[1]
        z = points[2]
        print(f"[{x},{y},{z}")
        swarm.parallel(lambda i, tello:tello.send_rc_control(x,y,z,0))
        #tello.send_rc_control(x,y,z,0)
        time.sleep(3)

    swarm.parallel(lambda i, tello:tello.move_up(30))
    # tello.move_up(30)

points, temp = arc(30, 4, 50, 2, 8)

swarmall.parallel(lambda i, tello:tello.takeoff())
# single.rotate_clockwise(360)

submit_command_rc(points, temp)
swarm.parallel(lambda i, tello:tello.curve_xyz_speed(55, 40, 50, 70, 40, 80, 50))
# single.connect()
swarm.parallel(lambda i, tello:tello.rotate_counter_clockwise(90))
swarm.parallel(lambda i, tello:tello.flip_forward())
# swarm.parallel(lambda i, tello:tello.move_forward(30))
# points, temp = arc(30, 4, 40, 2, 8)
# submit_command_rc(points, temp)
# swarm.parallel(lambda i, tello:tello.curve_xyz_speed(70, 70, 0,  140, 0,  0, 40))
# single.move_up(40)

# single.flip_forward()
# single.connect()
# swarm.parallel(lambda i, tello:tello.rotate_clockwise(45))
# swarmall.parallel(lambda i, tello:tello.move_forward(30))
swarmall.land()