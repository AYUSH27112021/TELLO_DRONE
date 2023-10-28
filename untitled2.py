from djitellopy import Tello

tello = Tello()

tello.connect()
def takeoff():
    tello.takeoff()
def up():
    tello.move_up(50)
def down():
    tello.move_down(50)
def left():
    tello.move_left(100)
def right():
    tello.move_right(100) 
def forward():
    tello.move_forward(100)  
def back():
    tello.move_back(100)
def clock():
    tello.rotate_clockwise(90)
def anticlock():
    tello.rotate_clockwise(90)
def land():
    tello.land()
def default(num1,num2):
    tello.land()
    
switcher = {
    1: takeoff,
    2: up,
    3: down,
    4: left,
    5: right,
    6: forward,
    7: back,
    8: land
    }

def switch(operation):
    return switcher.get(operation, default)()

print('''You can perform operation
      1: takeoff,
      2: up,
      3: down,
      4: left,
      5: right,
      6: forward,
      7: back,
      8: land
)

choice = int(input("Select operation from 1,2,3,4 : "))

print (switch(choice))

