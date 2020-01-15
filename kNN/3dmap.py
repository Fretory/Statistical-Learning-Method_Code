import kNN
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#coding: utf-8

import matplotlib.pyplot as plt

plt.rcParams ['font.sans-serif'] = ['SimHei'] #Used to display Chinese labels normally

plt.rcParams ['axes.unicode_minus'] = False #Used to display negative signs normally

#There are situations in Chinese that require u'content '

vector,label=kNN.file2matrix(r'datingTestSet2.txt')

x1=[]
x2=[]
x3=[]
y1=[]
y2=[]
y3=[]
z1=[]
z2=[]
z3=[]
for i in range(len(label)):
    if(label[i]==1):
        x1.append(vector[i][0])
        y1.append(vector[i][1])
        z1.append(vector[i][2])
    if(label[i]==2):
        x2.append(vector[i][0])
        y2.append(vector[i][1])
        z2.append(vector[i][2])
    if(label[i]==3):
        x3.append(vector[i][0])
        y3.append(vector[i][1])
        z3.append(vector[i][2])


fig = plt.figure(figsize=(8, 5), dpi=80)
ax = Axes3D(fig)
type1=ax.scatter(x1, y1, z1)
type2=ax.scatter(x2, y2, z2)
type3=ax.scatter(x3, y3, z3)
ax.set_zlabel(u'每周消费的冰淇淋公升数', fontdict={'size': 15, 'color': 'black'})
ax.set_ylabel(u'玩视频游戏的占比', fontdict={'size': 15, 'color': 'black'})
ax.set_xlabel(u'飞行常客里程数', fontdict={'size': 15, 'color': 'black'})
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)
plt.show()
