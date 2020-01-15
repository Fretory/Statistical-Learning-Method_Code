

import kNN
import matplotlib
import matplotlib.pyplot as plt
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

for i in range(len(label)):
    if(label[i]==1):
        x1.append(vector[i][0])
        y1.append(vector[i][1])
    if(label[i]==2):
        x2.append(vector[i][0])
        y2.append(vector[i][1])
    if(label[i]==3):
        x3.append(vector[i][0])
        y3.append(vector[i][1])

fig = plt.figure(figsize=(8, 5), dpi=80)
ax= plt.subplot(111)
type1=ax.scatter(x1, y1, s=20, c='red')
type2=ax.scatter(x2, y2, s=40, c='green')
type3=ax.scatter(x3, y3, s=50, c='blue')
ax.set_ylabel(u'玩视频游戏的占比', fontdict={'size': 15, 'color': 'black'})
ax.set_xlabel(u'飞行常客里程数', fontdict={'size': 15, 'color': 'black'})
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)
plt.show()