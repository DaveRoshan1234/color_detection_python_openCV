import os
import cv2

img=cv2.imread(r"C:\Users\Dave Roshan\OneDrive\Desktop\CV_plan\man.jpg")

img_blur=cv2.blur(img,(10,10)) # larger the number,stronger the blur
img_blur2=cv2.GaussianBlur(img,(9,9),3)
img_blur3=cv2.medianBlur(img,9) # used to remove noise from the image

# gaussian blur preserves edges better and keeps centre pixels with more weight...
# gaussian blur needs to be odd numbers inorder to have a centre to work with...

cv2.imshow("median blur",img_blur3)
cv2.imshow("blur",img_blur)
cv2.imshow('frame',img)
cv2.imshow("gaussian blur",img_blur2)

cv2.waitKey(0)