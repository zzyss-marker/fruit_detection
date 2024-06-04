import cv2
import numpy as np

# 读取图像
image = cv2.imread('tradition\fresh_peach_7.jpg')
# 转换到HSV色彩空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 设置HSV阈值来识别特定颜色范围的缺陷
lower_hsv = np.array([20, 50, 50])
upper_hsv = np.array([40, 255, 255])

# 创建掩膜
mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

# 对原图像和掩膜进行位运算
result = cv2.bitwise_and(image, image, mask=mask)

# 显示结果
cv2.imshow('Fruit', image)
cv2.imshow('Defects', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
