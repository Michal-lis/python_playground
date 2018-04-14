import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1 - COLOR
# 0 - GRAYSCALE
# -1 - UNCHANGED

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output2.avi',fourcc,.0,(1920,1080))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


