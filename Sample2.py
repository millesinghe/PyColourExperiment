import numpy as np
import cv2

cap2 = cv2.VideoCapture(3)
cap4 = cv2.VideoCapture(4)
# Check if the webcam is opened correctly
if not cap2.isOpened():
    raise IOError("Cannot open webcam2")
if not cap4.isOpened():
    raise IOError("Cannot open webcam4")

while True:
    # Capture frame-by-frame
    ret2, bright = cap2.read()
    cv2.imshow('original', bright)

    ret4, dark = cap4.read()
    # Convert BGR to HSV

    green_channel = bright[:, :, 1]
    cv2.imshow('green_channel', green_channel)

    brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
    darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)
    cv2.imshow('brightLAB', brightLAB)
    cv2.imshow('darkLAB', darkLAB)

    brightLABHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
    darkLABHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)
    cv2.imshow('brightLABHSV', brightLABHSV)
    cv2.imshow('darkLABHSV', darkLABHSV)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap2.release()
cap4.release()
cv2.destroyAllWindows()

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#   print_hi('PyCharm')
