import numpy as np
import cv2
import mediapipe as mp

vid=cv2.VideoCapture(0)

mp_face_detect=mp.solutions.face_detection # face detection modules loaded into variable
mp_drawing=mp.solutions.drawing_utils 

# creating new object with 2 settings
with mp_face_detect.FaceDetection(model_selection=0,min_detection_confidence=0.9) as face_detection:
    while True:
        ret,frame=vid.read() # takes the frames from cam

        if not ret:
            print("Failed")
            break

        H,W,_=frame.shape # for bbox

        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  
        out=face_detection.process(frame_rgb) # uses NN to process RGB frames and detects face 
        
        if out.detections:
            for detection in out.detections: # iterating through each face in the frame
                location_data=detection.location_data # coordinates of faces and facial features
                bound_box=location_data.relative_bounding_box  # bbox drawn 

                x1,y1,w,h=bound_box.xmin, bound_box.ymin, bound_box.width, bound_box.height

                # pixel positions
                x1=int(x1*W)
                y1=int(y1*H)
                w=int(w*W)
                h=int(h*H)

                cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,255,0),7)

        cv2.imshow("Face Detection",frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()
