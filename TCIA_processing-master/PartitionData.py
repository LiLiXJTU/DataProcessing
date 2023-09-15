import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import SimpleITK as sItk
import cv2
import glob
import shutil
import numpy as np
folder_path = r'D:\data\body\CT'
num=0
list = glob.glob(folder_path+'/*')
image_names = [list_name.split("\\")[-1][:16] for list_name in list] # 提取文件名并保存为列表
patient_names = np.unique(image_names)
train_data = patient_names[0:225]
val_data = patient_names[225:253]
test_data = patient_names[253:281]
for data in list:
    patient = data.split("\\")[-1][:16]
    data_name = data.split("\\")[-1]
    if patient in train_data:
        path = r'D:\data\body\Train\CT/'+ data_name
        shutil.copyfile(data,path)
    elif patient in val_data:
        path = r'D:\data\body\Val\CT/' + data_name
        shutil.copyfile(data, path)
    elif patient in test_data:
        path = r'D:\data\body\Test\CT/' + data_name
        shutil.copyfile(data, path)