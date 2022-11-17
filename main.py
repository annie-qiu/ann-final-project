# –––– Import packages ––––
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import tensorflow_addons as tfa

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pathlib

import numpy as np

# –––– Import Datasets ––––
landscape_dir = pathlib.Path("flicker_scraper/images/europe_landscapes")
impressionist_dir = pathlib.Path("impressionist_landscapes_resized_1024")

lanscape_count = len(list(data_dir.glob('*/*.jpg')))
print(lanscape_count)
