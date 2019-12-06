import numpy as np
# 符号函数


def sign(x):
    return 1 if x >= 0 else -1


def perceptron(training_data, weight, bias, learning_rate):
    # 将特征向量与标签分离
    if(len(training_data)==0):
        print("The training data can't be empty!")
        exit()

    vec = training_data[:, :-1]
    label = training_data[:, -1]

    if(len(vec[0]) != len(weight)):
        print("The weight vector is not equal to traning vector!")
        exit()
    # 在这里没有采用随机选取一个点的方法
    # 而是从0开始,当模型遇到误分类点则更新w,b
    # 再次从0开始预测...
    i = 0
    while i < len(training_data):
        predict_results = sum([vec[i][j]*weight[j]
                               for j in range(len(weight))])+bias
        if sign(predict_results) != label[i]:

            weight = [weight[j]+learning_rate*label[i]*vec[i][j]
                      for j in range(len(weight))]

            bias = bias+learning_rate*label[i]
            i = 0
        else:
            i = i+1

    return weight, bias

def perceptron_test(testing_data, weight, bias):
    wrong = 0
    right = 0
    for item in testing_data:
        predict_results = sum(item[i]*weight[i]
                              for i in range(len(weight)))+bias
        if sign(predict_results) != item[-1]:
            wrong = wrong+1
        else:
            right = right+1
    print("The accuracy is "+str(right/(right+wrong)))
