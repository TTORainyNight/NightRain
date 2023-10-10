# Python库
import os
import sys
import time
import json
import asyncio
import random
import pdb
import argparse
import glob
from multiprocessing import *
import copy
import math
import traceback
import functools

# 第三方库
import scipy
import torch
import numpy as np
import PyQt6
from PyQt6.QtWidgets import QApplication, QLabel
import edge_tts
import pygame
import pydub
import openai
import ffmpeg
import pyworld as pw
import parselmouth
import faiss
import librosa
import torchcrepe

# 自定义库
from Code.API import *
from Code.GUI import *
from Code.lib import *
from Code.ui import *

# 环境检测
def NightRain():
    print("os：\n", os.getcwd())
    print("sys：\n", sys.version)
    print("time：\n", time.time())
    json_data = {"author": "TTORainyNight", "web": "github search TTORainyNight"}
    print("json：\n", json.dumps(json_data))
    print("random：\n", random.uniform(0.0, 1.0))
    print("copy：\n", hasattr(copy, 'deepcopy'))
    print("math：\n", hasattr(math, 'sqrt'))
    print("functools：\n", hasattr(functools, 'reduce'))
    print("SciPy：\n", scipy.mean(scipy.array([1, 2, 3, 4, 5])))
    print("torch：\n", torch.rand(2, 3))
    print(torch.__version__)
    print("numpy：\n", np.zeros((3, 3)))
    print("PyQt6：\n  请在命令执行完毕后查看GUI界面。")
    print("pygame：\n  请在命令执行完毕后查看GUI界面。")
    print("openai：\n", openai.__version__)
    print("ffmpeg：\n", os.popen("ffmpeg -version").read())
    print("pyworld：\n", pw.__version__)
    print("parselmouth：\n", parselmouth.__version__)
    print("faiss：\n", faiss.__version__)
    print("librosa：\n", librosa.__version__)
    # GPU支持情况
    print("PyTorch-GPU支持：\n", torch.cuda.is_available())
    print(torch.cuda.device_count())
    print(torch.cuda.get_device_name(0))
    print("PyTorch-CUDA支持：\n", torch.version.cuda)
    print("PyTorch-cuDNN支持：\n", torch.backends.cudnn.version())

# PyQt6检测
def PyQt6_test():
    app = QApplication([])
    label = QLabel("PyQt6库测试成功!")
    label.show()
    app.exec()

# pygame检测
def pygame_test():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Pygame Test Window")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    NightRain()
    PyQt6_test()
    pygame_test()