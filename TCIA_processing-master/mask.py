import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import SimpleITK as sItk
import cv2
label_folder_path = r'D:\data\FDG-PET-CT-Lesions\labels'
show_path = r'D:\data\FDG-PET-CT-Lesions\label_show/'
# 开始读取nii文件
txt_path = r"D:\data\body"
folder_path = r'D:\data\FDG-PET-CT-Lesions\manifest-1654187277763\tcia_nifti\FDG-PET-CT-Lesions'
num=0
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file = files[3]
        #name = root[66:82]
        name = root[80:96]
        file_path = os.path.join(root, file)
        # 处理文件，这里可以根据需要进行自定义操作
        #print(file_path)
        img = nib.load(file_path)
        img_fdata = img.get_fdata()  # api 已完成转换，读出来的即为CT值
        # 开始转换为图像
        (x, y, z) = img_fdata.shape

        for i in range(z):  # z是图像的序列
            silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
            silce = cv2.resize(silce, (224, 224), interpolation=cv2.INTER_NEAREST)
            if np.unique(silce).max()!=0:
                num = num + 1
                # temp = name + "-" + str(i + 1) + ".tif"
                # # imageio.imwrite(os.path.join(img_f_path, temp),
                # #                 silce[int((x - 512) / 2):int((x - 512) / 2) + 512])
                # imageio.imwrite(os.path.join(label_folder_path, temp), silce)
                img_path = show_path+name + "-" + str(i + 1)+'.png'
                cv2.imwrite(img_path, silce * 255)
                print(num)

# img_path = os.path.join(filepath, f)
# img = nib.load(img_path)  # 读取nii
# img_fdata = img.get_fdata()  # api 已完成转换，读出来的即为CT值
# fname = f.replace('.nii.gz', '')  # 去掉nii的后缀名
# # 开始转换为图像
# (x, y, z) = img_fdata.shape
# for i in range(z):  # z是图像的序列
#     silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
#     silce = cv2.resize(silce, (224, 224), interpolation=cv2.INTER_NEAREST)
#     temp = name + "-" + str(i + 1) + ".tif"
#     # imageio.imwrite(os.path.join(img_f_path, temp),
#     #                 silce[int((x - 512) / 2):int((x - 512) / 2) + 512])
#     imageio.imwrite(os.path.join(label_folder_path, temp), silce)
#     img_path = show_path+name + "-" + str(i + 1)+'.png'
#     cv2.imwrite(img_path, silce * 255)
#     print(temp)



