import cv2
img = cv2.imread("resources/butterfly.jpg")
cv2.imshow('original Image',img)
cv2.imwrite('resources/output.jpg',img)
cv2.imwrite('resources/output.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()