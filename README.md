# 爬取豆瓣电影top250提取电影分类进行数据分析
1. 抓取豆瓣TOP250影片分类
2. 使用一个字典将分类进行统计计数
3. 将结果保存到mysql 数据库
4. 使用matplotlib进行数据可视化操作

barh()
主要功能：做一个横向条形图，横向条的矩形大小为: left, left + width, bottom, bottom + height
参数：barh ( bottom , width , height =0.8, left =0, **kwargs )
返回类型：一个 class 类别， matplotlib.patches.Rectangle**实例
参数说明：

    bottom: Bars 的垂直位置的底部边缘
    width: Bars 的长度
    可选参数：
    height: bars 的高度
    left: bars 左边缘 x 轴坐标值
    color: bars 颜色
    edgecolor: bars 边缘颜色
    linewidth: bar 边缘宽度;None 表示默认宽度;0 表示不 i 绘制边缘
    xerr: 若不为 None,将在 bar 图上生成 errobars
    yerr: 若不为 None,将在 bar 图上生成 errobars
    ecolor: 指定 errorbar 颜色
    capsize: 指定 errorbar 的顶部(cap)长度
    align: ‘edge’ (默认) | ‘center’:‘edge’以底部为准对齐;‘center’以 y 轴作为中心
    log: [False|True] False (默认),若为 True,使用 log 坐标

然后就可以显示出图片来了
![数据可视化](https://github.com/xzeu/douban/blob/master/douban.png)