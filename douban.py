from lxml import etree
import requests
import pymysql
import numpy as np
import matplotlib.pyplot as plt

def save_mysql(douban):
    """
    :param douban:
    :return:
    """
    print(douban)  # douban在主函数中定义的字典
    for key in douban:
        print(key)
        print(douban[key])
        if key != '':
            try:
                sql = 'INSERT INTO douban(`类别`,`数量`) VALUES(' + "\'" + key + "\'," + "\'" + str(douban[key]) + "\'" + ');'
                # print(sql)
                cur.execute(sql)
                conn.commit()
            except:
                print('插入失败')
                conn.rollback()

def get_page(i):
    """
    :param i: 页数
    :return:  包含影片分类的keys
    """
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    html = requests.get(url).content.decode('utf-8')  # 使用request库获取网页内容
    selector = etree.HTML(html)  # 使用lxml库提取内容
    '''
        通过观察页面就能发现内容在<div class="info">下的一部分
    '''
    content = selector.xpath('//div[@class="info"]/div[@class="bd"]/p/text()')
    # print(content)
    content = [x for x in content if x.strip().replace('\n','') != '']
    for i in content[1::2]:
        i = str(i).split('/')
        i = i[len(i) - 1]
        key = i.strip().replace('\n', '').split(' ')  # 这里的strip和replace的使用目的是去除空格和空行之类
        for i in key:
            if i not in douban.keys():
                douban[i] = 1
            else:
                douban[i] += 1
    return douban


def pylot_show():
    sql = 'select * from douban;'
    cur.execute(sql)
    rows = cur.fetchall()  # 把表中所有字段读取出来
    count = []  # 每个分类的数量
    category = []  # 分类
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 10))
    for row in rows:
        count.append(int(row[2]))
        category.append(row[1])

    y_pos = np.arange(len(category))  # 定义y轴坐标数
    plt.barh(y_pos, count, align='center', alpha=0.4)  # alpha图表的填充不透明度(0~1)之间
    plt.yticks(y_pos, category)  # 在y轴上做分类名的标记

    for count, y_pos in zip(count, y_pos):
        # 分类个数在图中显示的位置，就是那些数字在柱状图尾部显示的数字
        plt.text(count, y_pos, count, horizontalalignment='center', verticalalignment='center', weight='bold')
    plt.ylim(len(category), -1.0)  # 可视化范围，相当于规定y轴范围
    plt.title(u'豆瓣电影250')  # 图表的标题
    plt.ylabel(u'电影分类')  # 图表y轴的标记
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u'分类出现次数')  # 图表x轴的标记
    # plt.show()
    plt.savefig('douban.png')  # 保存图片


# 连接mysql数据库
conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'mysql', charset = 'utf8')  # user为数据库的名字，passwd为数据库的密码，一般把要把字符集定义为utf8，不然存入数据库容易遇到编码问题
cur = conn.cursor()  # 获取操作游标
cur.execute('use douban')  # 使用douban这个数据库

douban = {}
# for x in range(20):
#     get_page(x)
# save_mysql(douban)
pylot_show()
cur.close()
conn.close()