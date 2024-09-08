import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_image(img_path):
    return np.asanyarray(Image.open(img_path)) / 255

RES_DIR = './content/data'
FRAMES_DIR = os.path.join(RES_DIR, 'images')

test_img_path = os.path.join(FRAMES_DIR, os.listdir(FRAMES_DIR)[0])
test_img = load_image(test_img_path)

plt.figure(figsize=(5, 10))
plt.imshow(test_img)
plt.show()
