import cv2
import glob
import numpy
import tifffile as tiff
folder_path = r'D:\data\body\label_show/'
# 读取二进制掩码图像
mask_path = glob.glob(folder_path+'*.png')  # 替换为你的掩码图像路径
i=0
for path in mask_path:
    mask = cv2.imread(path)
# 计算标签为 1 的区域面积
    area = np.count_nonzero(mask == 255)
    if area>300:
        i=i+1
        print(i)
        print(path)
        print("标签为 1 的区域面积大小：", area)