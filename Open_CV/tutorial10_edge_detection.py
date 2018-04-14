import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # operator Sobela, jeden z operatorów w cyfrowym przetwarzaniu obrazów umożliwiający aproksymację pochodnych kierunkowych w jednm z ośmiu kierunkach co 45 stopni
    sobelx = cv2.Sobel(frame, cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F,0,1,ksize=5)
    # Algorytm Canny-ego:
    # detekcja - wykrycie tak duzej ilości krawędzi jak tylko możliwe
    # umiejscowienie - jak najbliżej rzeczywistej krawędzi na obrazie
    # minimalna odpowiedź - dana krawędź powinna występować tylko raz, bez szumu
    edges = cv2.Canny(frame,50,50)

    cv2.imshow('original',frame)
    # cv2.imshow('laplacian',laplacian)
    # cv2.imshow('sobelx',sobelx)
    # cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
