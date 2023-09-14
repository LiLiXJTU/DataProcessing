import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import SimpleITK as sItk
import cv2
import glob
label_folder_path = r'D:\data\body\labels'
show_path = r'D:\data\body\label_show/'
CT_show_path = r'D:\data\body\CT_show/'
CT_folder_path = r'D:\data\body\CT/'
PET_show_path = r'D:\data\body\PET_show/'
PET_folder_path = r'D:\data\body\PET/'
SUV_folder_path = r'D:\data\body\SUV/'
# 开始读取nii文件
txt_path = r"D:\data\body"
folder_path = r'D:\data\1'
train_num=0
val_num=0
test_num = 0
list = glob.glob(show_path+'*.png')
image_names = [list_name.split("\\")[-1] for list_name in list] # 提取文件名并保存为列表
patient = [patient_name.split("\\")[-1][:-8] for patient_name in list]
patient = np.unique(patient)
train_patient = patient[76:]
val_patient = patient[38:76]
test_patient = patient[:38]
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file = files[2]
        name = root[66:82]
        #name = root[80:96]
        file_path = os.path.join(root, file)
        # 处理文件，这里可以根据需要进行自定义操作
        #print(file_path)
        img = nib.load(file_path)
        img_fdata = img.get_fdata()  # api 已完成转换，读出来的即为CT值
        # 开始转换为图像
        (x, y, z) = img_fdata.shape

        for i in range(z):  # z是图像的序列
            name='PETCT_9521502dbb'
            name_new  = name + "-" + str(i + 1)+'.png'
            silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
            silce = cv2.resize(silce, (224, 224), interpolation=cv2.INTER_NEAREST)
            print(name_new)
            if name_new in image_names:
                print(1)
                train_num = train_num + 1
                temp = SUV_folder_path+name_new[:-4]+'.nii'
                silce = sItk.GetImageFromArray(silce)
                sItk.WriteImage(silce, temp)
                print('train_num:',train_num)
                # if name in train_patient:
                #     train_num = train_num + 1
                #     temp = SUV_folder_path+'Train/'+name_new[:-4]+'.nii'
                #     silce = sItk.GetImageFromArray(silce)
                #     sItk.WriteImage(silce, temp)
                #     print('train_num:',train_num)
                # elif name in val_patient:
                #     val_num = val_num + 1
                #     temp = SUV_folder_path+'Val/'+name_new[:-4]+'.nii'
                #     silce = sItk.GetImageFromArray(silce)
                #     sItk.WriteImage(silce, temp)
                #     print('val_num:', val_num)
                # elif name in test_patient:
                #     test_num = test_num + 1
                #     temp = SUV_folder_path+'Test/'+name_new[:-4]+'.nii'
                #     silce = sItk.GetImageFromArray(silce)
                #     sItk.WriteImage(silce, temp)
                #     print('test_num:', test_num)



