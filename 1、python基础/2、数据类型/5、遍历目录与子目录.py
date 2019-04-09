import os
#遍历目录与子目录，抓取.pyc文件
"""第一种方法"""
def get_file(dir,suffix):
    res=[]
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,suf=os.path.splitext(filename)
            if suf ==suffix:
                res.append(os.path.join(root,filename))
    print(res)
get_file('/','.pyc')

"""第二种方法"""
def pick(obj):
    if obj.endswith(".pyc"):
        print("obj：",obj)

def scan_path(ph):
    file_list=os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)
if __name__ == '__main__':
    path="/"
    scan_path(path)