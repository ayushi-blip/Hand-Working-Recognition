import numpy as np
import cv2
import math

 # OPEN CAMERA- grab camera and save it on capture
capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()  # output show in frame
# it check that jb tk camera open ho live field kaam kre

# get hand data from rectangle sub window
cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)  # (x1,y1,colour,width of rect
crop_image = frame[100:300, 100:300]  # crop it x1 ,y1 height width

# Apply gaussian blur
blur = cv2.GaussianBlur(crop_image, (3, 3), 0)

# change colorspace from bgr->hsv
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

# create an binary image with where white will be skin color and black is rest
mask2 = cv2.inRange(hsv, np.array([2, 0, 0]), np.array([20, 255, 255]))

# now to extract any boundary is lost in image capturing we use kernel
kernel = np.ones((5, 5))  # kernel for morphological transformation

# apply morphological to remove background noise
dilation = cv2.dilate(mask2, kernel, iterations=1)
erosion = cv2.erode(dilation, kernel, iterations=1)

# apply gaussian blur and threshold
filtered= cv2.GaussianBlur(erosion, (3, 3), 0)
ret, thresh = cv2.threshold(filtered, 127, 255, 0)

# show threshold image
cv2.imshow("Thresholded", thresh)

# find contours
image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

try:
    # find contour with maxim area
    contour = max(contours, key=lambda x: cv2.contourArea(x))

    # creating bounding reactangle around the contour
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)
    # find convex hull
    hull = cv2.convexHull(contour)
    # draw contour
    drawing = np.zeros(crop_image.shape, np.uint8)
    cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], -1, (0, 255, 0), 0)

    # find convexity defects
    hull=cv2.convexHull(contour, returnPoints=False)
    defects=cv2.convexityDefects(contour, hull)

    count_defects=0
    for i in range(defects.shape[0]):
      s, e, f, d=defects[i, 0]
      start=tuple(contour[s][0])
      end=tuple(contour[e][0])
    far = tuple(contour[f][0])
    a=math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
    angle=(math.acos((b ** 2 + c ** 2 - a ** 2)/(2 * b * c)) * 180) / 3.14

 # if angle is more than 90 draw a circle at far point
    if angle<=90:
      count_defects+=1
      cv2.circle(crop_image, far, 1, [0, 0, 255], -1)
      cv2.line(crop_image, start, end, [0, 255, 0], 2)

    # print number of fingers
    if count_defects==0:
       cv2.putText(frame, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    elif count_defects==1:
       cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    elif count_defects==2:
       cv2.putText(frame, "THREE", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    elif count_defects==3:
        cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    elif count_defects==4:
        cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    else:
        pass
except:
        pass


#show required images
cv2.imshow("Gesture", frame)
all_image = np.hstack((drawing, crop_image))
cv2.imshow('Contours', all_image)

if cv2.waitKey(1) == ord('q'):
    breakpoint(0)

capture.release()
cv2.destroyAllWindows()
