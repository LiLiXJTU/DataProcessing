import os
import pydicom
from PIL import Image
import SimpleITK as sItk
# 定义DICOM文件夹和PNG文件夹路径
dcm_folder_path = r'D:\data\CT\Pancreas-CT\Pancreas-CT'
png_folder_path = r'D:\multi_data\TCIA\Train_Folder\img'

for filename in os.listdir(dcm_folder_path):
    img_f_path = os.path.join(dcm_folder_path, filename)
    #filenames = os.listdir(filename)  # 读取dcm外部文件夹
    i = 0
    for file in os.listdir(img_f_path):
        if file.endswith(".dcm"):
            i = i + 1
            # 读取DICOM文件
            dcm_filepath = os.path.join(img_f_path, file)
            dcm_file = pydicom.dcmread(dcm_filepath)
            pixel_array = dcm_file.pixel_array
            #image = Image.fromarray(pixel_array)
            image = sItk.GetImageFromArray(pixel_array)
            # 保存PNG文件
            png_filename = filename[-4:] + '-'+ str(i) + ".nii"
            sItk.WriteImage(image, os.path.join(png_folder_path, png_filename))
            print(png_filename)


            # png_filepath = os.path.join(png_folder_path, png_filename)
            # image.save(png_filepath)