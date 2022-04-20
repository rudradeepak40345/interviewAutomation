import cv2
import time
i=0
while(i!=20):
    time.sleep(0.2)
    videoCaptureObject = cv2.VideoCapture(0)
    ret ,frame = videoCaptureObject.read()
    cv2.imwrite("cap/fanta_"+str(i)+".jpg", frame) 
        
    i+=1
    videoCaptureObject.release()
    cv2.destroyAllWindows()
