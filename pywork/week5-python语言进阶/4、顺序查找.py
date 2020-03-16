def seq_search(items,key):
    """顺序查找"""
    for index,item in enumerate(items):
        if item==key:
            return index
    return -1

if __name__=="__main__":
    items=[8,9,7,3,5,4,10]
    re=seq_search(items,4)
    print(re)