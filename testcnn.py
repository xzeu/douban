import keras
from keras import backend as K
from PIL import Image
from keras.models import load_model
import numpy as np
import h5py
import pandas as pd
from matplotlib import pyplot as plt
import random
import os

# os.chdir(r'all')  # 跳转到训练集目录
import string
#
# # CHRS = string.ascii_lowercase + string.digits  # 字符列表
CHRS = string.ascii_lowercase  # 字符列表
#
num_classes = 26  # 共要识别36个字符（所有小写字母+数字），即36类
batch_size = 128
epochs = 12
#
# # 输入图片的尺寸
img_rows, img_cols = 12, 20
# # 根据keras的后端是TensorFlow还是Theano转换输入形式
if K.image_data_format() == 'channels_first':
    input_shape = (1, img_rows, img_cols)
else:
    input_shape = (img_rows, img_cols, 1)

import requests
import io

model = load_model(r'E:\python\2017_9\model_test.h5')


def get_bin_table(threshold=98):
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

def get_image(fn):
    '''
    从教务处网站获取验证码
    '''
    # extra_code = 'azuuwd2ijh40vlnfg1ajdhbn'
    # url_base = 'http://xsweb.scuteo.com/(%s)/' % extra_code
    # # url_base = requests.get('http://xsweb.scuteo.com/default2.aspx').url.replace('default2.aspx', '')
    # url_veri_img = url_base + 'CheckCode.aspx'
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    # }
    # res = requests.get(url_veri_img, headers=headers)
    # image_file = io.BytesIO(res.content)
    # image = Image.open(image_file)
    # for i in range(300):
    #     image = "image/{}.png".format(i)
    #     yield image
    # name = random.randint(0, 100)
    # print(fn)
    # image = "image/{}.png".format(fn)
    image = "{}.png".format(fn)
    image = Image.open(image)
    plt.imshow(image)
    return image

def handle_split_image(image):
    '''
    切割验证码，返回包含四个字符图像的列表
    '''
    # im = image.point(lambda i: i != 43, mode='1')
    # y_min, y_max = 0, 22 # im.height - 1 # 26
    # split_lines = [5,17,29,41,53]
    # ims = [im.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
    # # w = w.crop(w.getbbox()) # 切掉白边 # 暂不需要
    # print(image)
    img = image
    # 转化到灰度图
    imgry = img.convert('L')
    # 保存图像
    # imgry.save('g'+name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(get_bin_table(), '1')
    a = np.array(out)
    pd.DataFrame(a.sum(axis=0)).plot.line()  # 画出每列的像素累计值
    plt.imshow(a)  # 画出图像
    split_lines = [1, 13, 25, 30, 42, 48, 60]
    y_min, y_max = 0, 20
    image = [out.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
    ims = []
    for i in range(0, 8, 2):
        plt.subplot(1, 4, i / 2 + 1)
        # print(i)
        if (i == 0):
            ims.append(image[int(i)])
            # plt.imshow(ims[int(i)], interpolation='none')
        else:
            ims.append(image[int(i - 1)])
            # plt.imshow(ims[int(i - 1)], interpolation='none')
    # print(ims)
    return ims

def predict(images):
    '''
    使用模型对四个字符的列表对应的验证码进行预测
    '''
    Y = []
    for i in range(4):
        im = images[i]
        test_input = np.concatenate(np.array(im))
        test_input = test_input.reshape(1, *input_shape)
        y_probs = model.predict(test_input)
        Y.append(CHRS[y_probs[0].argmax(-1)])
    return ''.join(Y)

def multi_process(fn):
    '''
    获取预测并保存图片，图片名为预测值
    '''
    image = get_image(fn)
    images = handle_split_image(image)
    print('测试验证码为：{}'.format(predict(images)))
    image.save( 'rest/'+predict(images) + '.png')


from multiprocessing.dummy import Pool

import datetime
now = datetime.datetime.now

# for x in range(30):
#     multi_process(str(x))
multi_process('b')
# with Pool(30) as pool:
#     pool.map(multi_process,[i for i in range(30)] )
start = now()
print('耗时 -> %s' % (now()-start))
