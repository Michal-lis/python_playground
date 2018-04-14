import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Morphological operations: Podstawowe operacje na obrazach : Erozja, dilation ,


    lower_red = np.array([150, 150, 50])
    upper_red = np.array([180, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    # inRange zwraca 0 lub 1
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel= np.ones((5,5),np.uint8)
    # erosion - removing the pixel that is not fitting
    erosion = cv2.erode(mask, kernel, iterations = 1)
    # dilation - the opposite, emplifing the noise in the background
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    # opening - removing false positives
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # closing - removing false negatives
    closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


    # cv2.imshow('res', res)
    # cv2.imshow('frame', frame)
    # cv2.imshow('erosion', erosion)
    # cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    # smoothing - tracimy clarity ale jest troche lepiej
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
