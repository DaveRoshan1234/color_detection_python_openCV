import cv2
import numpy as np
from PIL import Image

webcam=cv2.VideoCapture(0)

while True:
    ret,frame=webcam.read()

    hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # BGR range of the color yellow
    lower = np.array([20, 100, 100])
    upper = np.array([35, 255, 255])

    mask=cv2.inRange(hsv_img,lower,upper)
    mask_1=Image.fromarray(mask) # converts array to pillow (to use pillow only features)

    bbox=mask_1.getbbox() # bounding box
    # print(bbox)

    if bbox is not None:

        x1,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask) # the mask window that detects the color

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()