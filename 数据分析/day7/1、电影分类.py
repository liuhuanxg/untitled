
import math

#构造数据
movie_data = {"宝贝当家": [45, 2, 9, "喜剧片"],
              "美人鱼": [21, 17, 5, "喜剧片"],
              "澳门风云3": [54, 9, 11, "喜剧片"],
              "功夫熊猫3": [39, 0, 31, "喜剧片"],
              "谍影重重": [5, 2, 57, "动作片"],
              "叶问3": [3, 2, 65, "动作片"],
              "伦敦陷落": [2, 3, 55, "动作片"],
              "我的特工爷爷": [6, 4, 21, "动作片"],
              "奔爱": [7, 46, 4, "爱情片"],
              "夜孔雀": [9, 39, 8, "爱情片"],
              "代理情人": [9, 38, 2, "爱情片"],
              "新步步惊心": [8, 34, 17, "爱情片"]}

#第二步：计算一个新样本与数据集中所有数据的距离
x = [23,3,17]
KNN = []
for key,v in movie_data.items():
    d = math.sqrt((x[0]-v[0])**2+(x[1]-v[1])**2+(x[2]-v[2])**2)
    KNN.append([key,round(d,2),v[3]])
print('原数据：',KNN)

for i in range(len(KNN)):
    for j in  range(len(KNN)-1):
        if KNN[j][1]>KNN[j+1][1]:
            KNN[j],KNN[j+1]=KNN[j+1],KNN[j]
print(KNN)

#第三步：按距离进行排序，选取k=5个样本。
# KNN.sort(key=lambda movie:movie[1] )
# print('排序后：',KNN)

#第四步：确实前k个样本所在类别出现的频率，并输出出现频率最高的类别
# t_x = 0#喜剧片计数器
# t_d = 0#动作片计数器
# t_a = 0#爱情片计数器
#
# for i in range(5):
#     movie = KNN[i]
#     t = movie[2]
#     if t=='喜剧片':
#         t_x +=1
#     elif t=='动作片':
#         t_d +=1
#     elif t=='爱情片':
#         t_a +=1
#
# result_list = [['喜剧片',t_x],['动作片',t_d],['爱情片',t_a]]
# result_list.sort(key=lambda result:result[1],reverse=True)
# print(result_list[0],'就是结果')

#
# labels = {'喜剧片':0,'动作片':0,'爱情片':0}
# for movie in KNN[:]:

    # label = movie_data[movie[0]]
    # print(label)
    # labels[movie[2]]+=1

# print(labels)
# result = sorted(labels.items(),key=lambda i:i[1],reverse=True)
# print('预测结果：',result[0])

