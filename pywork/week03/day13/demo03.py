'''
with--使用with方式操作文件，可以不用关闭文件，会自动关闭文件
'''
# with open('d:\\a.txt','r') as f:
#     b=f.read()
#     print(b)

'''
指定文件格式
向文件中保存内容
'''
# with open('a.txt','w',encoding='utf-8') as p:
#     p.write('你好呀')