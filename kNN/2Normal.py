import kNN
vector,label=kNN.file2matrix(r'datingTestSet2.txt')
print("before autoNorm")
print(vector)
normalDataSet,ranges,minVals=kNN.autoNorm(vector)
print("\n\n\n\n\nafter autoNorm")
print(normalDataSet)
