import glob
import random
import os
import numpy as np
import torch

from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

# from sklearn.cross_validation import train_test_split
try:
    import ipdb
except:
    import pdb as ipdb


class ImageDataset(Dataset):
    def __init__(self, root, transforms_=None, mode='train'):
        self.transform = transforms.Compose(transforms_)
        # ipdb.set_trace()
        rootPath = root + '/{}'.format(mode)
        filename = os.listdir(rootPath)
        path = rootPath + '/' + filename[0]

        self.imgs = np.load(path)

    def __getitem__(self, index):
        img_A_a = self.imgs[index][:, :64, :]
        img_B_b = self.imgs[index][:, 64:, :]
        imgsa = Image.fromarray(img_A_a.astype(np.uint8))
        imgsb=Image.fromarray(img_B_b.astype(np.uint8))
        img_A = self.transform(imgsa)  # 京黑
        img_B = self.transform(imgsb)  # 黑体

        return {'A': img_A, 'B': img_B}

    def __len__(self):
        return len(self.imgs)##等长