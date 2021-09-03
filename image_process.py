import os
import cv2
from matplotlib import pyplot as plt

path_dir = os.getcwd + '/'
original_dir = path_dir + 'original/'
result_dir = path_dir + 'result/'

file_list = os.listdir(original_dir)

for page, file in enumerate(file_list):
    img = cv2.imread(original_dir + file)
    img_equalized = cv2.equalizeHist(img)
    images = [img, img_equalized]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    colors = [h, s, v]
    img_labels = ['original', 'equalized']
    hsv_labels = ['original', 'normalized']
    color_labels = ['h', 's', 'v']

    for i, img_label in enumerate(img_labels):
        plt.subplot(451+i*5)
        plt.imshow(images[i])
        for j, color_label in enumerate(color_labels):
            plt.subplot(451+i*5+j)
            hist = cv2.calcHist([colors[i]], [0], None, [256], [0, 255])
            plt.plot(hist)