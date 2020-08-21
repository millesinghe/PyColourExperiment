import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    cv2.imshow("Show Me", img)
    hsv4 = cv2.cvtColor(frame4, cv2.COLOR_BGR2HSV)


cap.release()