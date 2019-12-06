import perceptron
import numpy as np

if __name__ == "__main__":
    # 此处按照书上的样例2.1加载整型的数据
    # {<3,3,1>,<4,3,1>,<1,1,-1>}
    # 将特征向量与类别分离
    filename = r"perceptron/test.txt"
    data = np.loadtxt(filename)
    weight = np.zeros(len(data)-1)   # 权值 weight vector
    bias = 0.0                       # 偏置 bias
    learning_rate = 1.0             # 学习率 learning rate

    weight, bias = perceptron.perceptron(data, weight, bias, learning_rate)
    for i in weight:
        print(i, end=" ")
    print(bias)

    perceptron.perceptron_test(data, weight, bias)
