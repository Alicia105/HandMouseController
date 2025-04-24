import mediapipe as mp
import cv2
import numpy as np
import uuid
import os 

#import handds landmarks and medeiapipe hand tracking model
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap=cv2.VideoCapture(0)
#os.mkdir("../images")
with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands :
    while cap.isOpened():
        ret,frame=cap.read()

        #Flip horizontally
        frame=cv2.flip(frame,1)

        #convert BGR to RGB-->necessary to use mediapipe 
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #set flags
        frame_rgb.flags.writeable=False

        #Detections
        results=hands.process(frame_rgb)

        #Set flag to true
        frame_rgb.flags.writeable=True

        #Convert RGB back to BGR
        image=cv2.cvtColor(frame_rgb,cv2.COLOR_RGB2BGR)

        print(results)
        #Rendering results 
        # Color in BGR in DrawingSpec 
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                            mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2))

        #save our image
        #cv2.imwrite(os.path.join('../images','{}.jpg'.format(uuid.uuid1()),image)) -->to solve
        cv2.imshow("Hand Tracking",image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

