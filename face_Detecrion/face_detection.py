from utillity import *
import cv2
w, h=360,240
pid=[0.5,0.5,0]
pError=0
startCounter=1  #for no flight 1 and for flight 0

myDrone = intializeTello()

while True:
    if startCounter==0:
        myDrone.takeoff()
        startCounter=1
    imgd = telloGetFrame(myDrone,w,h)
    #step 2
    img=findFace(imgd)
    info=img
    #step 3
    pError=trackFace(myDrone,info,w,pid,pError)
    print(info[0][0])
    cv2.imshow("MyResult", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break