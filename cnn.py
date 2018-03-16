import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from PIL import Image
from keras.models import load_model
import numpy as np
import h5py
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
import os

os.chdir(r'all')  # 跳转到训练集目录
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

import glob

X, Y = [], []
for f in glob.glob('*.png')[:]:  # 遍历当前目录下所有png后缀的图片

    t = 1.0 * np.array(Image.open(f))
    t = t.reshape(*input_shape)  # reshape后要赋值
    X.append(t)  # 验证码像素列表

    s = f.split('_')[0]  # 获取文件名中的验证码字符
    Y.append(CHRS.index(s))  # 将字符转换为相应的0-35数值

X = np.stack(X)  # 将列表转换为矩阵
Y = np.stack(Y)
# print("y:{}".format(Y))
# print("x:{}".format(X))
# 此时Y形式为 array([26, 27, 28, ..., 23, 24, 25])

# 对Y值进行one-hot编码 # 可尝试 keras.utils.to_categorical(np.array([0,1,1]), 3) 理解
Y = keras.utils.to_categorical(Y, num_classes)
print('lenY:{}'.format(len(Y)))
split_point = len(Y) - 36  # 简单地分割训练集与测试集
print('split_point:{}'.format(split_point))
x_train, y_train, x_test, y_test = X[:split_point], Y[:split_point], X[split_point:], Y[split_point:]

# 以下模型和mnist-cnn相同
# 两层3x3窗口的卷积(卷积核数为32和64)，一层最大池化(MaxPooling2D)
# 再Dropout(随机屏蔽部分神经元)并一维化(Flatten)到128个单元的全连接层(Dense)，最后Dropout输出到36个单元的全连接层（全部字符为36个）
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (2, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
model.save(r'E:\python\2017_9\model_test.h5')
