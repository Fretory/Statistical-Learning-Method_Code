# 此部分对书上的4.1进行了复现
# 使用的是极大似然估计


def traning(dataSets):
    labelCount = {}
    # 遍历获取有多少个类别
    for item in dataSets:
        labelCount[item[-1]] = labelCount.get(item[-1], 0) + 1

    # print(labelCount)
    #计算不同类别的先验概率
    for key, value in labelCount.items():
        labelCount.update({key: value / len(dataSets)})

    #为计算后验概率做准备
    vecFeature = {}
    for key, values in labelCount.items():
        vecFeature[key] = {}

    for i in range(len(dataSets[0]) - 1):
        #为每一个维度设置字典并记数
        for key, value in vecFeature.items():
            value.update({i: {}})
            vecFeature.update({key: value})
        for item in dataSets:
            vecFeature[item[-1]][i][item[i]] = vecFeature[item[-1]][i].get(
                item[i], 0) + 1

    for key_1, value_1 in vecFeature.items():
        for key_2, value_2 in value_1.items():
            for key_3, value_3 in value_2.items():
                value_2.update({key_3: value_3 / len(dataSets)})

    return labelCount, vecFeature

def query(labelCount,vecFeature,data):
    
    label=None
    maxP=0.0

    for key,value in labelCount.items():
        tempP=value
        for i in range(len(data)):
            tempP=tempP*vecFeature[key][i][data[i]]
        if tempP>maxP:
            maxP=tempP
            label=key
    return label
if __name__ == "__main__":
    trainingData = ([[1, 'S', -1], [1, 'M', -1], [1, 'M', 1], [1, 'S', 1],
                     [1, 'S', -1], [2, 'S', -1], [2, 'M', -1], [2, 'M', 1],
                     [2, 'L', 1], [2, 'L', 1], [3, 'L', 1], [3, 'M', 1],
                     [3, 'M', 1], [3, 'L', 1], [3, 'L', -1]])
    label,feature=traning(trainingData)
    testData=[2,'S']
    q=query(label,feature,testData)
    print(q)