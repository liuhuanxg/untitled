# import string
# import random
# def guess_words(words,hash_table):
#     len_words = len(words)
#     print("*"*len_words)
#     answer = ""
#     frequency = 0
#     i = 0
#     j = 0
#     while i <= len_words:
#         hash_table.sort(key=lambda x:x["count"][str(i)],reverse=True)
#         print(hash_table)
#         input_words = hash_table[j].get("words")
#         print(input_words)
#         if input_words == words[i]:
#             answer += input_words
#             i+=1
#         frequency +=1
#     return  "答案正确，猜测了{}".format(frequency)
#
# if __name__ == '__main__':
#     words = "apple"
#     ascii_lowercase = string.ascii_lowercase
#     hash_table = [
#         {"words":"a","count":{"0":30,"1":9,"2":60,"3":10,"4":5}},
#         {"words":"b","count":{"0":20,"1":6,"2":60,"3":10,"4":5}},
#         {"words":"p","count":{"0":10,"1":50,"2":50,"3":10,"4":5}},
#         {"words":"l","count":{"0":5,"1":20,"2":60,"3":10,"4":5}},
#         {"words":"e","count":{"0":15,"1":5,"2":60,"3":10,"4":50}},
#         {"words":"c","count":{"0":20,"1":10,"2":60,"3":10,"4":5}},
#     ]
#     print(guess_words(words, hash_table))

from functools import wraps
def outer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return inner
@outer
def func():
    try:
        return 1/0
    except Exception as error:
        return error
print(outer(func)())


# from selenium import webdriver
# driver_path = "c:/"
# driver = webdriver.Chrome(driver_path)
# driver.get("https://*****")
# driver.maximize_window() # 浏览器最大化
# driver.find_element_by_id("username").send_keys("Zhangsan")

