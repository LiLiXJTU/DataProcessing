import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import SimpleITK as sItk
import cv2
import glob

folder_path = r'D:\data\body\SUV'
yuan_path = r'D:\data\body\label_show'
num=0
list = glob.glob(yuan_path+'/*')
image_names = [list_name.split("\\")[-1] for list_name in list] # 提取文件名并保存为列表
i=0
xun_list = glob.glob(folder_path+'/*')
xun_img_names = [xun_list_name.split("\\")[-1] for xun_list_name in xun_list]
for a in image_names:
    new = a[:-4]+'.nii'
    if new not in xun_img_names:
        print(new)
    else:
        i = i+1
print(i)