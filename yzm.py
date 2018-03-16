from PIL import Image, ImageEnhance
import pytesseract
import PIL.ImageOps
import cv2 as cv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def clear_border(img,img_name):
  filename = './out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
  h, w = img.shape[:2]
  for y in range(0, w):
    for x in range(0, h):
      if y < 2 or y > w - 2:
        img[x, y] = 255
      if x < 2 or x > h -2:
        img[x, y] = 255

  # cv2.imwrite(filename,img)
  return img
def get_bin_table(threshold=100):
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

rep={
    # 'O':'0',
    # 'I':'1',
    #  'L':'1',
     '|':'j',
    '—':''
    # 'Z':'2',
    # 'S':'8'
    }
def  getverify1(img):
    #打开图片
    # im = Image.open(name)
    #转化到灰度图
    imgry = img.convert('L')
    #保存图像
    # imgry.save('g'+name)
    #二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(get_bin_table(),'1')
    # out.save('b'+name)
    #识别
    text = pytesseract.image_to_string(out, lang='eng', config='-psm 7')
    #识别对吗
    text = text.strip()
    text = text.replace(' ', '')
    # text = text.upper()
    for r in rep:
        text = text.replace(r,rep[r])
    print('image:image/' + str(i) + '.png,识别文字为：' +  text)

    # out.save(text+'.jpg')
    # print(text)
    return text
for i in range(50,60):

    im = Image.open('image/'+str(i)+'.png')
    getverify1(im)
    # imgry = im.convert('L')
    # # imgry.show()
    # table = get_bin_table()
    # out = imgry.point(table, '1')
    # out.show()
    # binaryImage = im.point(get_bin_table(),'1')
    # print(binaryImage)
    # im1 = binaryImage.convert('L')
    # im2 = PIL.ImageOps.invert(im1)
    # im3 = im2.convert('1')
    # im4 = im3.convert('L')
    # out = im4.resize((240,60))
    # asd = pytesseract.image_to_string(out,lang='eng')
    # print(asd)
    # # print(out.show())
    # imgry = im.convert('L')
    # table = get_bin_table()
    # out = imgry.point(table, '1')
    # out = out.resize((240, 60))
    # text = pytesseract.image_to_string(out, lang='eng')
    # print('image:image/'+str(i)+'.png,识别文字为：'+text.replace(' ',''))
    # out.save('image/'+str(i)+'.png')

# sharpness = ImageEnhance.Contrast(imgry)
# sharp_img = sharpness.enhance(2.0)
# sharp_img.save('image/0.png')
# text = pytesseract.image_to_string(Image.open('image/0.png'), lang='chi_sim')
# print(text)


# img = cv.imread('image/0.png')
# cv.namedWindow("IMAGE")
# cv.imshow("Image",img)
# cv.waitKey(0)
# cv.destroyAllWindows()