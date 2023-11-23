import cv2

face_cascade=cv2.CascadeClassifier("/Users/durbht1/Pythonpractice/program_examples/haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)