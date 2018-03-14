import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('ryj.png')
img2 = cv2.imread('z_bratem.jpg')

orb = cv2.ORB_create()
# keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

# matplotlibw RGB a openCV w BGR

plt.imshow(img3)
plt.show()

#
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
