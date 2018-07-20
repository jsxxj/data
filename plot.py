# -*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
#plt.figure(figsize=(9,6))
n = 9
X = np.arange(n)+2
#X是1,2,3,4,5,6,7,8,柱的个数
# numpy.random.uniform(low=0.0, high=1.0, size=None), normal
#uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
Y1 = (59,87,119,168,198,218,247,276,300)
Y2 = (241,213,181,132,102,82,53,24,0)
plt.bar(X,Y1,width = 0.35,facecolor = 'lightskyblue',edgecolor = 'white')
#width:柱的宽度
plt.bar(X+0.35,Y2,width = 0.35,facecolor = 'yellowgreen',edgecolor = 'white')
#水平柱状图plt.barh，属性中宽度width变成了高度height
#打两组数据时用+
#facecolor柱状图里填充的颜色
#edgecolor是边框的颜色
#想把一组数据打到下边，在数据前使用负号
#plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
#给图加text
for x,y in zip(X,Y1):
    plt.text(x+0.3, y+0.05, '%.0f' % y, ha='center', va= 'bottom')
    
for x,y in zip(X,Y2):
    plt.text(x+0.6, y+0.05, '%.0f' % y, ha='center', va= 'bottom')
    
plt.ylim(0,320)
plt.show()
