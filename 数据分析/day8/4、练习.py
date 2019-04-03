import time
def judge(list,k):
    return list[0]==k


def solve(init_list,k):
    n=len(init_list)
    if n==1:
        return judge(init_list,k)
    left_list=init_list[:n//2]
    right_list=init_list[n//2:]
    return solve(left_list,k) or solve(right_list,k)

if __name__ == '__main__':
    init_list=[x for x in range(10**7)]

    k=int(input('请输入一个数：'))
    start_time = time.time()
    result=solve(init_list,k)
    print('是否存在：',result)
    end_time=time.time()
    print(end_time-start_time)