import cv2 as cv
import numpy as np

video = cv.VideoCapture(1)

if not video.isOpened():
    print("Camera couldn't be opened")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = video.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    # Display the resulting frame
    cv.imshow("CoinScanner v0.1", frame)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
video.release()
cv.destroyAllWindows()
