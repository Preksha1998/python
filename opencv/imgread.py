import cv2

img = cv2.imread("resources/prexa.jpg")
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()