import cv2
img = cv2.imread("resources/prexa.jpg")
cv2.imshow('output image',img)

print(img.shape)
print("Height pixel value of imag : ",img.shape[0])
print("width pixel value of imag : ",img.shape[1])
print("How many Layers in your image : ",img.shape[2])
cv2.waitKey(0)
cv2.destroyAllWindows()