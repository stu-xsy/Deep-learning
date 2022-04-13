import fitlog
import os
import tkinter as tk
from tkinter import filedialog


class Train_opt:
    def __init__(self, opt, root=os.getcwd() + '/output'):
        super(Train_opt, self).__init__()
        # 将opt转为字典类型
        if not isinstance(opt, dict):
            self.opt = vars(opt)
        else:
            self.opt = opt
        self.root = root
        self.mk_use_dirs()

    def __getitem__(self, item):
        return self.opt.__getitem__(item)

    def __setitem__(self, key, value):
        self.opt.__setitem__(key, value)

    # 获得本次输出的根目录
    def get_root(self):
        # 格式：模型/G学习率_D学习率_批大小_epoch
        opt = self.opt
        dir_name = ''
        k_hyper = self.get_key_hyper()
        for k, v in k_hyper.items():
            dir_name += str(k) + str(v)
        root = '%s/%s/%s/train' % (self.root, opt['model_name'], dir_name)
        return root

    # 获得log存放路径
    def get_log_root(self):
        return self.get_root() + '/log/'

    # 获得model存放路径
    def get_model_root(self):
        return self.get_root() + '/model/'

    # 获得img存放路径
    def get_img_root(self):
        return self.get_root() + '/img/'

    # 返回用于命名文件夹的超参
    def get_key_hyper(self):
        k = ['lr', 'batchSize', 'n_epochs']
        v = {key: value for key, value in self.opt.items() if key in k}
        return v

    def get_fitlog_hyper(self):
        k = ['lr', 'batchSize', 'n_epochs', 'model_name']
        v = {key: value for key, value in self.opt.items() if key in k}
        return v

    # 命名可能需要的文件夹
    def mk_use_dirs(self):
        print('创建 ' + self.get_img_root())
        print('创建 ' + self.get_log_root())
        print('创建 ' + self.get_model_root())
        os.makedirs(self.get_log_root(), exist_ok=True)
        os.makedirs(self.get_img_root(), exist_ok=True)
        os.makedirs(self.get_model_root(), exist_ok=True)



