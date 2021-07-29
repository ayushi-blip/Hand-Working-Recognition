import cv2
import numpy as np

hand=cv2.imread('capture3.jpg', 0)
ret, thresh= cv2.threshold(hand, 75, 255, cv2.THRESH_BINARY)
# to create image black and white


# hierarchy contour no of images so we need only contour thats why use underscore
# contour count the connected pixels and draw the area of image
# result=cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = result if len(result) == 2 else result[1:3]



hull = [cv2.convexHull(c) for c in contours]
final = cv2.drawContours(hand, hull, -1, (255, 0, 0))

cv2.imshow('Original Image', hand)
cv2.imshow('Thresh', thresh)
cv2.imshow('Convex Hull', final)

cv2.waitKey(0)
cv2.destroyAllWindows()