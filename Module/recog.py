import cv2
import numpy as np
import time
import copy

def pink_detect(img):
    '''RGBtoHSV
    threshold for pink_ball
    [HUE(0to179) threshold should be 0to15,
    Saturation [0,255],Lightness[0,255]
    target may be [327/2,255*0.92,255]'''
    
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    pink_min = np.array([155,50,50])
    pink_max = np.array([165,255,255])
    return cv2.inRange(hsv, pink_min,pink_max)

def find_target(mask):
    img,contours,hierarchy  = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    maxrect=[0,0,0,0]
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        if rect[2]*rect[3] > maxrect[2]*maxrect[3]:
            maxrect = copy.deepcopy(rect)
    return maxrect

def capturevideo():
    #use web camera
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        #_:T or F, frame:frame
        _, frame = cap.read()
        #cv2.GaussianBlur(img,filter_range,variance)
        denoise = cv2.GaussianBlur(frame,(25,25),3)
        mask = pink_detect(frame)
        maskd = pink_detect(denoise)
        cv2.imshow("capture",frame)

        rect = find_target(mask)
        detected = cv2.rectangle(denoise,tuple(rect[0:2]),(rect[0]+rect[2],rect[1]+rect[3]), (0,0,255), thickness=2)
        print("gravity point: {} , {} ".format(rect[0]+rect[2]/2,rect[1]+rect[3]/2))
        cv2.imshow("rect",detected)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()


capturevideo()
