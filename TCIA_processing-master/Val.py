import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import SimpleITK as sItk
import cv2
import glob
import numpy as np
folder_path = r'D:\data\body\label_show'
yuan_path = r'D:\data\body\Val\label'
num=0
list = glob.glob(yuan_path+'/*')
image_names = [list_name.split("\\")[-1][:16] for list_name in list] # 提取文件名并保存为列表

xun_list = glob.glob(folder_path+'/*')
xun_img_names = [xun_list_name.split("\\")[-1] for xun_list_name in xun_list]
for a in image_names:
    if a not in xun_img_names:
        print(a)