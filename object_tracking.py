import cv2
import time
import math
p1 = 530
p2 = 300
xs = []
ys = []

video = cv2.VideoCapture("bb3.mp4")
returned, img = video.read()
tracker = cv2.TrackerCSRT_create()
bBox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bBox)
print(bBox)

def drawbox(img, bBox):
    x, y, w, h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])
    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255,0,255), 3, 1)
    cv2.putText(img, "Tracking!", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

def goal_track(img, bBox):
    x, y, w, h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img, (c1, c2), 2, (0,0,255), 5)
    cv2.circle(img, (p1, p2), 2, (0,255,0), 3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    if(dist<=20):
        cv2.putText(img, "Goal!", (300, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    xs.append(c1)
    ys.append(c2)
    for i in range(len(xs)-1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0,0,255), 5)
        
while True:
    check,img = video.read()   
    success, bBox = tracker.update(img)
    if success:
        drawbox(img, bBox)
    else:
        cv2.putText(img, "Lost!", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    
    goal_track(img, bBox)
    
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break

video.release()
cv2.destroyALLwindows()



