import cv2
import numpy as np
from numpy import uint8

def get_limits(color):
    c= np.uint8([[color]])
    hsvC= cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit= hsvC[0][0][0]- 10, 100, 100
    upperLimit= hsvC[0][0][0]+ 10, 255, 255
    
    lowerLimit= np.array(lowerLimit, uint8)
    upperLimit= np.array(upperLimit, uint8)

    return lowerLimit, upperLimit