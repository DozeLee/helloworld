from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#图片对比前提相同大小的图片内容，不同处是颜色或形状
img1 = np.array(Image.open(r'E:\e1.jpg'))
img2 = np.array(Image.open(r'E:\e2.jpg'))
print(img1.shape)
print(img1.shape)
rows1, cols1, high1 = img1.shape
rows2, cols2, high2 = img2.shape
print(img1[110, 408, 2] == img2[110, 408, 2])
#循环3维数组，判断如果k值不相等，即赋值为红色将其覆盖
for i in range(rows1):
    for j in range(cols1):
        for k in range(high1):
            if img1[i, j, k] == img2[i, j, k]:
                k += 1
            else:
                img1[i, j, ] = [255, 0, 0]
        j += 1
    i += 1

plt.figure("panda")
plt.imshow(img1)
plt.axis('off')
plt.show()
