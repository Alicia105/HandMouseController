# Hand Mouse Controller 🖐️🖱️


## **Description**  
This project is a hand gesture-based mouse controller built using Python, OpenCV, and MediaPipe. It lets you control your computer's mouse using just your hand.


## **Table of Contents**  
- [Features](#features)
- [Tech Stack](#teck-stack)
- [Requirements](#requirements)
- [Notes](#notes)
- [Installation](#installation) 
- [How to use](#how-to-use)

## 📊**Features** 
- ☝️ Move your mouse by moving your index finger
- 🖱️ Left click, Right click, and Double click detection via gestures
- ✋ Left and Right hand classification
- 🤲 Multi-hand support (several hands can be detected independently)
- 🎯 Visual cursor (a circle drawn on your fingertip)
- ⚡Smooth and real-time performance

## 🛠️ **Tech Stack**
- Python 3.10+
- OpenCV
- Mediapipe
- Numpy
- pyautogui

## 📄**Requirements**
- Python 3.10+
- Webcam
- A decent CPU for real-time performance

## ❗**Notes**
- Make sure your camera has a good view of your hand.
- Good lighting improves hand detection accuracy.
- Only your thumb, index and middle finger gestures are important.
- Only one hand can be used as a controller. It's the right hand by default  

## 🧪**Installation**  
- Clone or download the repository
<pre> git clone https://github.com/Alicia105/HandMouseController.git</pre>
- Navigate to the project directory
<pre> cd HandMouseController</pre>
- Install needed dependencies
<pre> pip install -r requirement.txt</pre>


## 🚀**How to use** 

1. Navigate to the project source code directory
<pre> cd HandMouseController/src</pre>

2. Launch the app
<pre> python main.py</pre>

3. To move the mouse you have to bend your thumb
![Move the mouse](images/moving_mouse.jpg)

4. To do any click you have to unfold your thumb. Bend your index to a left click
![Left click](images/left_click.jpg)

5. Bend your middle finger to do a right click
![Right click](images/right_click.jpg)

6. Bend your index and middle finger to do a double click
![Double click](images/double_click.jpg)


