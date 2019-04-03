#自定义一个中间件
from  selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse

class TaobaoDownloaderMiddleware(object):
    def __init__(self):
        self.browser = webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    def process_request(self, request, spider):
        # 详情页使用无界面浏览器
        if request.meta.get('PhantomJS',False):
            self.browser.get(request.url)
            # try:
            #     element = WebDriverWait(driver, 10).until(
            #         EC.presence_of_element_located((By.ID, "content_left"))
            #     )
            time.sleep(3)
            content=self.browser.page_source  #响应信息

            #将信息封装成一个response对象，传给回调方法
            response=HtmlResponse(url=request.url,encoding='utf-8',body=content,request=request)

            return response