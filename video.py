
#from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('cascadef2.xml')

camera = cv2.VideoCapture(0)
#camera = VideoStream(src=0).start()
#initialise the first frame in the video stream

#loop over the frames of the video


while True:
    (grabbed, gray) = camera.read()
   # gray=cv2.GaussianBlur(gray,(21,21),0)
    
    #if the frame could not grabbed, then we have reached the end of the video
    if not grabbed:
        break
    
    
    
    #gray = imutils.resize(gray,width=750)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #kernel = np.ones((5,5), dtype = np.uint8)
    #gray = cv2.erode(gray, kernel, iterations = 1)
    #ogray = cv2.dilate(gray, kernel, iterations = 1)

    #gray = cv2.GaussianBlur(gray, (5,5), 0)


    
    gun = gun_cascade.detectMultiScale(gray, 1.05 ,65 , minSize = (75,75))

    try:
        
        (x,y,w,h)=gun[-1]
        gray = cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
    

    
    #draw the text and timestamp on the frame
        cv2.putText(gray,datetime.datetime.now().strftime("%A %d %B %Y %I: %M:%S%p"),(10,gray.shape[0] -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1)
        if len(gun) > 0 :
            cv2.putText(gray, "Weapon", (x+15,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (20,20,255), 2)
            print("gun detected")
    #show the frame and record if the user a key
        else:
            print("gun not detected")
    except:
        None

    cv2.imshow("Security feed",gray)
    
    
    if cv2.waitKey(5) & 0xFF == (ord('q')):
        break


    
#cleaning the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
