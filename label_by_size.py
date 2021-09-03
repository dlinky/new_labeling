import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

import labelimg_xml


path_dir = (os.getcwd() + '/').replace(r'\\', '/')
original_dir = path_dir + 'original/'
result_dir = path_dir + 'result/'

img_list = [_ for _ in os.listdir(original_dir) if _.endswith('.jpg')]
xml_list = [_ for _ in os.listdir(original_dir) if _.endswith('.xml')]

hists = []
hists_separated = []
hists_connected = []
sizes = []

bins = np.arange(0, 500, 5)
for page, file in enumerate(img_list):
    #img = cv2.imread(original_dir + img_list[page])
    title, table = labelimg_xml.read_xml(original_dir, xml_list[page])
    filename = file.split('.')[0]

    lengths = [i[3] + i[4] - i[1] - i[2] for i in table]

    hist, bins = np.histogram(lengths, bins)
    if '1.jpg' in file or '2.jpg' in file or '3.jpg' in file:
        plt.figure(1)
        plt.plot(bins[:-1], hist)
        if len(hists_separated) == 0:
            hists_separated = hist

        else:
            hists_separated += hist
    else:
        plt.figure(2)
        plt.plot(bins[:-1], hist)
        if len(hists_connected) == 0:
            hists_connected = hist
        else:
            hists_connected += hist
    plt.figure(3)
    plt.plot(bins[:-1], hist)
    if len(hists) == 0:
        hists=hist.copy()
    else:
        hists += hist
plt.figure(1)
plt.plot(bins[:-1], hists_separated)
plt.show()
plt.savefig(result_dir + 'separated.jpg')
plt.figure(2)
plt.plot(bins[:-1], hists_connected)
plt.savefig(result_dir + 'connected.jpg')
plt.figure(3)
plt.plot(bins[:-1], hists)
plt.savefig(result_dir + 'all.jpg')

'''
for i, bbox in enumerate(table):
    if lengths[i] >= 90:
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)
    cv2.rectangle(img, (bbox[1], bbox[2]), (bbox[3], bbox[4]), color, 2)
cv2.imwrite(result_dir + filename + '.jpg', img)
'''