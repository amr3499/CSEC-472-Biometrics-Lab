import skimage

import numpy as np # computations in the mse command
from PIL import Image, ImageChops, ImageStat  # Image Library

import glob # Import file paths
import mahotas
import pylab
import random # shuffle array
import math

def compare_prints(imageA, imageB):
    imA = Image.open(imageA)
    imB = Image.open(imageB)
    stat1 = ImageStat.Stat(imA)
    stat2 = ImageStat.Stat(imB)
    difference = math.fabs(stat1.rms[0] - stat2.rms[0])/(stat1.rms[0])
    return(1-difference)

