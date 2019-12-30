from multiprocessing import Pool
import time
# def zuoye(name):
#     print(name+'在写代码')
#     time.sleep(1)
#     return name+'写完代码了'
# def wan(status):
#     print('出去玩，'+status)
# if __name__ == '__main__':
#     p=Pool(1)
#     # callback--回调
#     p.apply_async(zuoye,('张三',),callback=wan)
#     p.close()
#     p.join()

# 下载器
def downLoad(movie):
    for i in range(5):
        print(movie,'下载进度%.2f%%'%((i+1)/5*100))
        time.sleep(1)
    return movie
def alert(name):
    print(name,'下载完毕，请收看')
if __name__ == '__main__':
    movies=['哪吒','金刚葫芦娃','黑猫警长','小青龙','亚洲飞鹰','A计划']
    p=Pool(4)
    for movie in movies:
        p.apply_async(downLoad,(movie,),callback=alert)
    p.close()
    p.join()