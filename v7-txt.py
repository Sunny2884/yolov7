import os
import glob
from PIL import Image
from torch.utils.data import Dataset


# train_img_dir = "data/ZHUQIAN/images/train"
# val_img_dir = "data/ZHUQIAN/images/val"
# train_img_path = os.listdir(train_img_dir)
# val_img_path = os.listdir(val_img_dir)

root_path = os.getcwd()
train_images = glob.glob(fr"{root_path}\data\ZHUQIAN\images\train\*.jpg")
# train_images.sort(key= lambda x: int(x.split(sep='\\')[-1].split(sep='.')[0]))
val_images = glob.glob(fr"{root_path}\data\ZHUQIAN\images\val\*.jpg")
# val_images.sort(key= lambda x: int(x.split(sep='\\')[-1].split(sep='.')[0]))

for item in train_images:
    with open(fr"{root_path}\dataset\my_zhuqian\train.txt", 'a') as f:
        f.write(item+'\n')

for item in val_images:
    with open(fr"{root_path}\dataset\my_zhuqian\val.txt", 'a') as f:
        f.write(item+'\n')
