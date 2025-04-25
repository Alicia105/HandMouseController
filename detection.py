from math import sqrt 
import numpy as np
import pyautogui
import time

#with a,b,c being points
#Calculate the euclidian norm between two points 
def finger_joints_coordinates(hand,idx1,idx2,idx3,idx4):
    x1, y1, z1 = hand.landmark[idx1].x, hand.landmark[idx1].y, hand.landmark[idx1].z
    x2, y2, z2 = hand.landmark[idx2].x, hand.landmark[idx2].y, hand.landmark[idx2].z
    x3, y3, z3 = hand.landmark[idx3].x, hand.landmark[idx3].y, hand.landmark[idx3].z
    x4, y4, z4 = hand.landmark[idx4].x, hand.landmark[idx4].y, hand.landmark[idx4].z
    a = [x1, y1, z1]
    b = [x2, y2, z2]
    c = [x3, y3, z3]
    d = [x4, y4, z4]

    return [a,b,c,d]

def get_finger(hand,name=""):
    if(name=="thumb"):
        return finger_joints_coordinates(hand,4,3,2,1)
    elif(name=="index"):
        return finger_joints_coordinates(hand,8,7,6,5)
    elif(name=="middle"):
        return finger_joints_coordinates(hand,12,11,10,9)
    elif(name=="ring"):
        return finger_joints_coordinates(hand,16,15,14,13)
    elif(name=="pinky"):
        return finger_joints_coordinates(hand,17,18,19,20)
    return None

def get_distance(a,b):
    norm=sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2)+pow(a[2]-b[2],2))
    return norm

def get_angle(a,b,c):
    n = get_distance(a,c)
    l = get_distance(a,b)
    alpha = np.arctan(n/l)
    return alpha

def isPalmFingerBent(hand,name=""):
    finger=get_finger(hand,name="")
    if finger!=None:
        a=finger[0]
        b=finger[2]
        c=finger[3]
        alpha=get_angle(a,b,c)
        print(f"alpha :{alpha}")
        if alpha==0:
            return True
        return False
    return None #fallback

def isThumbBent(hand):
    thumb=get_finger(hand,name="thumb")
    index=get_finger(hand,name="index")
    if thumb!=None and index!=None:
        a=thumb[0]
        b=thumb[2]
        c=index[3]
        alpha=get_angle(a,b,c)
        print(f"alpha :{alpha}")
        if alpha==0:
            return True
        return False
    return None #fallback

def left_click():
    pyautogui.click()  # Defaults to left click
    print("Left click performed")
    time.sleep(0.2)  # Small delay to avoid multiple clicks

def right_click():
    pyautogui.click(button='right')
    print("Right click performed")
    time.sleep(0.2)

def interactWithScreen(hand,x_screen, y_screen):
    pyautogui.moveTo(x_screen, y_screen)
    if(isPalmFingerBent(hand,name="middle")):
        left_click()
    if(isThumbBent(hand)):
        right_click()
