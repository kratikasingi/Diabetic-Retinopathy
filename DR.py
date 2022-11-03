import fastai
from fastai import *
from fastai.vision import *
from fastai.callbacks import *
import cv2

import pandas as pd
import matplotlib.pyplot as plt
# Making pretrained weights work without needing to find the default filename
if not os.path.exists('/tmp/.cache/torch/checkpoints/'):
        os.makedirs('/tmp/.cache/torch/checkpoints/')
!cp '../input/resnet50/resnet50.pth' '/tmp/.cache/torch/checkpoints/resnet50-19c8e357.pth'
!cp '../input/resnet152/resnet152.pth' '/tmp/.cache/torch/checkpoints/resnet152-b121ed2d.pth'
#!cp '../input/densenet161/densenet161-8d451a50.pth' '/tmp/.cache/torch/checkpoints/densenet161-8d451a50.pth'
