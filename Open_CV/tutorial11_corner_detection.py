import cv2
import numpy as np

img = cv2.imread('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
# good features to track do znajdowania narożników
corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
corners = np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
