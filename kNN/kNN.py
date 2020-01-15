from numpy import *
import operator
from os import listdir#列出给定目录的所有文件名

def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    #距离度量 度量公式为欧氏距离
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5

    #将距离排序：从小到大
    sortedDistIndicies=distances.argsort()
    classCount={}

    #选取前K个最短距离， 选取这K个中最多的分类类别
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index +=1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    """
    Desc:
        归一化特征值，消除特征之间量级不同导致的影响
    parameter:
        dataSet: 数据集
    return:
        归一化后的数据集 normDataSet. ranges和minVals即最小值与范围，并没有用到

    归一化公式：
        Y = (X-Xmin)/(Xmax-Xmin)
        其中的 min 和 max 分别是数据集中的最小特征值和最大特征值。该函数可以自动将数字特征值转化为0到1的区间。
    """
    # 计算每种属性的最大值、最小值、范围
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 极差
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    # 生成与最小值之差组成的矩阵
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 将最小值之差除以范围组成矩阵
    normDataSet = normDataSet / tile(ranges, (m, 1))  # element wise divide
    return normDataSet, ranges, minVals


def datingClassTest(k):
    # 设置测试数据的的一个比例（训练数据集比例=1-hoRatio）
    hoRatio=0.10# 测试范围,一部分测试一部分作为样本
    # 从文件中加载数据
    datingDataMat,datingLabels=file2matrix(r'datingTestSet2.txt')
    # 归一化数据
    normalMat,ranges,minVals=autoNorm(datingDataMat)
    # m 表示数据的行数，即矩阵的第一维
    m=normalMat.shape[0]
    # 设置测试的样本数量， numTestVecs:m表示训练样本的数量
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    for i in range(numTestVecs):
         # 对数据测试
        classifierResult=classify0(normalMat[i,:],normalMat[numTestVecs:m,:],datingLabels[numTestVecs:m],k)
        print('the classifier came back with :%d,the real answer is :%d'%(classifierResult,datingLabels[i]))
        if (classifierResult!=datingLabels[i]):
            errorCount+=1.0
    print('The total error rate is :%f'%(errorCount/float(numTestVecs)))

