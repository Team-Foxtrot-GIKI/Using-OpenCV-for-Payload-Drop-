import cv2
import numpy as np
from markerconfig import LOWER_HSV, UPPER_HSV

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
MIN_AREA = 800
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_h, frame_w = frame.shape[:2]#slicing h and w
    frame_center = (frame_w // 2, frame_h // 2)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #open close
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
