N = 35
p = [0] * N  # 用来存储中序遍历中每一个结点的位置
n = int(input())  # n个结点
a = list(map(int, input().split()))  # 存储后序遍历的结点
b = list(map(int, input().split()))  # 存储中序遍历的结点
lev = [[] for i in range(N)]  # 这里相当于C++中的vector,用来存储层次遍历每一层的结点


# 递归
def dfs(al, ar, bl, br, d):  # 这里是传入了后序遍历的最左边位置、最右边位置、中序遍历最左边位置、最右边位置、二叉树的层数
    if al > ar: return
    val = a[ar]
    lev[d].append(val)
    k = p[val]
    dfs(al, k - 1 + al - bl, bl, k - 1, d + 1)
    dfs(k - bl + al, ar - 1, k + 1, br, d + 1)


for i in range(n):
    p[b[i]] = i
dfs(0, n - 1, 0, n - 1, 0)
# 这里是去遍历二维列表里的子列表
for i in range(n):
    if lev[i]:  # 判断子列表为不为空
        print(*lev[i], end=' ')  # 依次输出子列表中的每一个元素，并用空格隔开，注意这里*代表了所有元素
