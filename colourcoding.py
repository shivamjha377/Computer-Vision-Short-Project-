import cv2
import numpy as np
from colourconvert import get_limits
from PIL import Image

yellow= [0,255,255] #colour in BGR colour space
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsvImage= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = get_limits(color=yellow)
    
    mask= cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_1 = Image.fromarray(mask)
    bbox = mask_1.getbbox()
    # print(bbox)
    if bbox is not None:
        x1,y1,x2,y2= bbox
        
        frame= cv2.rectangle(frame,(x1,y1),(x2,y2), (0,255,0), 6)


    cv2.imshow('frame', frame)

    # Wait for 1 millisecond and check if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
