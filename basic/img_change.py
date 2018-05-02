import cv2
import numpy as np 
import matplotlib.pyplot as plt

# #缩放cv2.INTER_AREA,拓展cv2.INTER_CUBIC
# img = cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg')
# #设置了缩放因子
# res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# #or直接设置输出图像的尺寸
# height , width =img.shape[:2]
# res = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

# while(1):
#     cv2.imshow('res',res)
#     cv2.imshow('img',img)

#     if cv2.waitKey(1)&0xFF ==ord('q'):
#         break
# cv2.destroyAllWindows()

# #平移
# img=cv2.imread('C:/Users/admin/Desktop/cv/HR.jpg',1)
# rows,cols,channel=img.shape

# M=np.float32([[1,0,100],[0,1,50]])
# dst=cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destoryALLWindows()#error,cv.cv.


# # 旋转
# img=cv2.imread('C:/Users/admin/Desktop/cv/HR.jpg',1)
# rows,cols,channel=img.shape
# #第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
# #第三个参数为图像的尺寸中心
# dst=cv2.warpAffine(img,M,(2*cols,2*rows))
# while(1):
#     cv2.imshow('img',dst)
#     if cv2.waitKey(1)&0xFF ==ord('q'):
#         break
# cv2.destroyAllWindows()


# #仿射变换，原图中的三个点，输出图上对应的位置
# img=cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg')
# rows,cols,ch = img.shape
# pts1=np.float32([[50,50],[200,50],[50,200]])
# pts2=np.float32([[10,100],[200,50],[100,250]])
# M=cv2.getAffineTransform(pts1,pts2)
# dst=cv2.warpAffine(img,M,(cols,rows))
# plt.subplot(121)
# plt.imshow(img)
# plt.title('Input')
# plt.subplot(122)
# plt.imshow(dst)
# plt.title('Output')
# plt.show()


# 透视变换,原图上四个点，输出图上对应的位置
img=cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg')
rows,cols,ch=img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
