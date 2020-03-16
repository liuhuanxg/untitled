def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    items = [8, 9, 7, 3, 5, 4, 10]
    re = bin_search(items, 4)
    print(re)
