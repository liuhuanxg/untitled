from numpy import *
import numpy as np
import operator
import time

from os import listdir  #导入列表目录

#内容太大时，强制显示所有内容，不省略
np.set_printoptions(threshold=np.NaN)

'''
1、整理数据读取数据到矩阵
'''
#培训函数
def img2vector(filename):
    #创建向量--用于存储文件的内容
    vect=zeros((1,1024),int)

    #读取文件
    fr=open(filename)
    for i in range(32):   #每个文件有32行
        lineStr=fr.readline()   #读取每行的内容

        for j in range(32):   #每个文件有32个字符
            vect[0,32*i+j]=lineStr[j]
    return vect

def trainingFunc():

    #样本数据的类标签列表
    hwLabels=[]

    #把该目录下的所有文件都放在列表中
    trainList=listdir('digits/trainingDigits')
    # print(trainList)
    m=len(trainList)


    #初始化样本数据矩阵(M*1024)--用于存储所有文件的内容
    trainMat=zeros((m,1024))

    #依次读取所有样本数据到数据矩阵trainMat
    for i in range(m):
        filename=trainList[i]

        #读取单个文件到矩阵中---singleFile
        s='digits/trainingDigits/%s'%filename
        singleFile=img2vector(s)

        #将单个文件数据放到trainMat
        trainMat[i,:]=singleFile

        #存储对应的类标签
        numStr=filename.split('_')[0]   #例如：吧0_101.txt中_前的0取出来
        hwLabels.append(int(numStr))
    print('trainMat:',trainMat.shape)
    print('hwLabels:',len(hwLabels))

    #检验机器学习的准确率
    testFunc(trainMat,hwLabels)


#测试函数
def testFunc(trainMat,hwlables):
    #初始化错误率
    errocount=0
    #读取测试集数据
    testFilelist=listdir('digits/tetDigits')
    for i in range(len(testFilelist)):
        fileNameStr=testFilelist[i]

        #实际结论
        trueResult=fileNameStr.split('_')[0]

        #预测结论
        fullName='digits/tetDigits/%s'%fileNameStr
        singleFileVect=img2vector(fullName)

        #（2）预测---对数据文件经分类
        result = classfy(singleFileVect,trainMat,hwlables,3)
        #错误率统计
        print('实际值：',trueResult,'-----预测值：',result)
        if int(trueResult) !=int(result):
            errocount+=1
            print(fileNameStr)



    rate=1-(errocount/len(testFilelist))
    print('准确率：',rate)

#KNN实现分类器
#功能：通过传入一个文件预测这个文件是哪一个数字

def classfy(inX,dataSet,hwLabels,k):
    #获取样本数据集
    dataSetSize=dataSet.shape[0]  #取出多少条数据
    # 2、计算距离
    #矩阵运算
    #inX---1*1024--->1934*1024
    newX=tile(inX,(dataSetSize,1))   #1934*1024

    #(1)、相减，(2)、平方，
    sq_x=(newX-dataSet)**2
    #(3)、求和，
    sum_x=sq_x.sum(axis=1)
    # (4)、开方
    distances=sum_x**0.5
    #3、排序
    #间接排序----因为不能打乱原始数据的位置，因为原始数据与hwlabels是一一对应的
    sortedDis=distances.argsort()

    #4、选K个样本，做类标签统计
    numDict={}
    for i in range(k):
        #依次取出最近的样本数据
        #记录该样本所属类别--类标签
        num=hwLabels[sortedDis[i]]
        numDict[num]=numDict.get(num,0)+1

    #统计出现次数最多的
    sortedData=sorted(numDict.items(),key=operator.itemgetter(1),reverse=True)

    return sortedData[0][0]


if __name__ == '__main__':
    # print(img2vector('digits/tetDigits/0_0.txt'))
    trainingFunc()