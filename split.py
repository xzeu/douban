from PIL import Image, ImageEnhance
import pytesseract
import PIL.ImageOps
import cv2 as cv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def get_bin_table(threshold=105):
    """
    获取灰度转二值的映射table
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table
def spimg():
    # 打开图片
    img = Image.open("{}.png".format('b'))
    # 转化到灰度图
    imgry = img.convert('L')
    # 保存图像
    # imgry.save('g'+name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(get_bin_table(), '1')
    a = np.array(out)
    pd.DataFrame(a.sum(axis=0)).plot.line() # 画出每列的像素累计值
    plt.imshow(a) # 画出图像
    split_lines = [1,13,25,30,42,48,60]
    vlines = [plt.axvline(i, color='r') for i in split_lines] # 画出分割线
    plt.show()
    y_min, y_max = 0,20

    ims = [out.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
    for i in range(0,8,2):
        plt.subplot(1, 4, i/2 + 1)
        # print(i)
        if (i == 0):
            # ims[int(i)].save('b/'+ str(b) + '_'+str(i)+'.png')
            plt.imshow(ims[int(i)], interpolation='none')
        elif (i == 2):
            # ims[int(i-1)].save('b/'+ str(b) + '_' + str(i-1) + '.png')
            plt.imshow(ims[int(i-1)], interpolation='none')
        else:
            pass
            # ims[int(i - 1)].save('b/' + str(x) + '_' + str(int(i/2)) + '.png')
    # plt.show()
spimg()
