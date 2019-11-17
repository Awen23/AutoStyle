from sklearn.cluster import KMeans
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os


def RGB2HEX(color):
        return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
def bensCode(image):
    format(type(image))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    
    

    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    clf = KMeans(n_clusters = 14)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
# get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    COLORS = {
    'BLACK': [0, 0, 0],
    'WHITE': [255, 255, 255],
    'RED': [255, 0, 0],
    'RED-ORANGE': [255, 83, 73],
    'ORANGE': [255, 165, 0],
    'YELLOW-ORANGE': [255, 174, 66],
    'YELLOW': [255, 255, 0],
    'YELLOW-GREEN': [154, 205, 50],
    'GREEN': [0, 255, 0],
    'BLUE-GREEN': [13, 152, 186],
    'BLUE': [0, 0, 255],
    'BLUE-VIOLET': [138,43,226],
    'VIOLET': [127, 0, 255],
    'YELLOW': [255, 255, 0],
    'RED-VIOLET': [199, 21, 133]
    }
    list_of_colors = list(COLORS.values())
    def closest(colors,color):
        colors = np.array(colors)
        color = np.array(color)
        distances = np.sqrt(np.sum((colors-color)**2,axis=1))
        index_of_smallest = np.where(distances==np.amin(distances))
        smallest_distance = colors[index_of_smallest]
        return smallest_distance
    listyboi = []
    for i in range(len(rgb_colors)):
      color = rgb_colors[i]
      closest_color = closest(list_of_colors, color)
      listyboi.append(closest_color)
    listyboi_2 = [i[0].tolist() for i in listyboi]
    color_list = list(COLORS.values())
    color_name_list = list(COLORS.keys())
    result = [color_list.index(i) for i in listyboi_2]
    label_list = []
    for i in result:
      label_list.append(color_name_list[i])
    list_of_colors = list(COLORS.values())
    total = sum(counts.values())
    percentage_list = []
    v = list(counts.values())
    for i in v:
      percentage = (i/total)*100
      percentage_list.append(percentage)
    return(percentage_list)
    
