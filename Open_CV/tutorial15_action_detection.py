import cv2
import numpy as np
import matplotlib.pyplot as plt
# foreground detection
# Background subtraction BS - looking for action
# foreground mask = moving objects in the scene
# detecting moving objects from static cameras, mostly to be used inside because of factors like wind, reflections and animals
# 1.Background initialization
cap = cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('Background reducer',fgmask)

    k = cv2.waitKey(30) & 0xff
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()
