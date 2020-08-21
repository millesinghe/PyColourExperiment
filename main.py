import numpy as np
import cv2

cap2 = cv2.VideoCapture(3)
cap4 = cv2.VideoCapture(0)
# Check if the webcam is opened correctly
if not cap2.isOpened():
    raise IOError("Cannot open webcam2")
if not cap4.isOpened():
    raise IOError("Cannot open webcam4")

while True:
    # Capture frame-by-frame
    ret2, frame2 = cap2.read()
    # Convert BGR to HSV
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    ret4, frame4 = cap4.read()
    # Convert BGR to HSV
    hsv4 = cv2.cvtColor(frame4, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # lower_blue = np.array([110, 50, 50])
    # upper_blue = np.array([130, 255, 255])

    lower_green = np.array([30, 30, 40])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask2 = cv2.inRange(hsv2, lower_green, upper_green)
    mask4 = cv2.inRange(hsv4, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res2 = cv2.bitwise_and(frame2, frame2, mask=mask2)
    res4 = cv2.bitwise_and(frame4, frame4, mask=mask4)

    # cv2.imshow('mask', mask2)
    cv2.imshow('frame2', frame2)
    cv2.imshow('res2', res2)
    cv2.imshow('frame4', frame4)
    cv2.imshow('res4', res4)

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
