# -*- coding: utf-8 -*-
from djitellopy import Tello 
import time
import math as m
import arrray as arr
gpsmatrix = []

def readdata():
    N = int(input("Enter the number of rows:"))
    print("Enter the entries rowwise:")
    for i in range(2):		 
    	a =[]
    for j in range(N):
	       a.append(int((input())/(180/m.pi)))
    gpsmatrix.append(a)

    #for i in range(R):
        # j in range(C):
            #matrix[i][j], end = " ")
	            #print()
                

def calculate_distance_gps(N):
    l=1
    x =[]
    for i in range(2):
        for j in range(N-1):
            x[l]= 6, 378.8 * m.acos[( m.sin(gpsmatrix[1][j]) * m.sin(gpsmatrix[2][j]) )+( m.cos(gpsmatrix[1][j]) * m.cos(gpsmatrix[2][j]) ) * (m.cos(gpsmatrix[2][j+1] - gpsmatrix[1][j+1]))]

        #Distance, d = 3963.0 * arccos[(sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 – long1)]
     
def get_angle():
    m=0
    m = (((gpsmatrix[2][j+1])-(gpsmatrix[1][j+1]))/((gpsmatrix[2][j+1])-(gpsmatrix[1][j])))
    if:((m>0.9)|(m<0.9))
        calculate_distance_gps()
    else:
        
        
        
    


tello =Tello()
tello.connect()
