import cv2 as cv 
import json 
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt


images= tf.data.Dataset.list_files('E:\OpenCv\Tensor.karas\sample\Har cascade mou apu\*.jpg',shuffle=False)

images.as_numpy_iterator.next()