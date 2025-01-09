import cv2          #imporrt computer vision library

img = cv2.imread("ts.png")     # Read the source
cv2.imshow("photo.jpg",img)
cv2.imwrite("signal.jpg",img)    # rewrite the source

cv2.waitKey(10000)              # built-in fun
cv2.destroyAllWindows()
