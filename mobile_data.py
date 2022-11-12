import cv2,time

video=cv2.VideoCapture(0)
address = "http://192.168.0.101:8080/video"
video.open(address)
while True:
    check,frame = video.read()
    
