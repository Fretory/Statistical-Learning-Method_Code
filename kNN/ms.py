import numpy as np

#随机生成10*3的矩阵
mySimple=np.random.randint(1,50,(10,3))
print(mySimple)

#分别取第一维，第二维，第三维度的数据
dim1=mySimple[:,0]
dim2=mySimple[:,1]
dim3=mySimple[:,2]

#算出三个维度的平均值
av1=sum(dim1)/len(dim1)
av2=sum(dim2)/len(dim2)
av3=sum(dim3)/len(dim3)

#每一个特征-其平均值
sub1=dim1-av1
sub2=dim2-av2
sub3=dim3-av3

#协方差
cov12=sum(sub1*sub2)/len(dim1)
cov13=sum(sub1*sub3)/len(dim2)
cov23=sum(sub2*sub3)/len(dim3)

#方差
var1=sum(sub1*sub1)/len(dim1)
var2=sum(sub2*sub2)/len(dim2)
var3=sum(sub3*sub3)/len(dim3)

C=np.array([[var1,cov12,cov13],[cov12,var2,cov23],[cov13,cov23,var3]])
print(C)