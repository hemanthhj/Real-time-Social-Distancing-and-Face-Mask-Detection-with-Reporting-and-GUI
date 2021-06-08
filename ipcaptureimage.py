import cv2
import requests
import numpy

videoCaptureObject = cv2.VideoCapture('http://hjk:005@192.168.43.1:8080/shot.jpg')
result = True
while result:
    ret, frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg", frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
