from multiprocessing import Pool
import time


def downLoad(movie):
    for i in range(5):
        print(movie, "下载进度{}".format((i + 1) / 5))
        time.sleep(1)
    return movie


def alert(name):
    print(name, "下载完毕，请收看。")


def main():
    movies = ["哪吒", "金刚葫芦娃", "黑猫警长", "小青龙", "亚洲飞鹰", "A计划"]
    p = Pool(6)
    for movie in movies:
        # q = p.apply_async(downLoad, args=(movie,))
        q = p.apply_async(downLoad, args=[movie], callback=alert)
        print(q.get())
    p.close()
    p.join()


if __name__ == '__main__':
    main()
