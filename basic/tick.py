import cv2 
import numpy as np 

img1 = cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg')

e1 = cv2.getTickCount()
for i in range(5,19,2):
    img1 = cv2.medianBlur(img1,i)
    # cv2.imshow('img_medianblur',img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)

# cv2.useOptimized()  #return T or F
# cv2.setUseOptimized(True)

#x**2比np.square(x)快
#避免使用循环
#利用缓存一致性
#数组复制是浪费
