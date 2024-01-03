如果爬取文件含有lazy属性可以在中间件中使用

```python
from scrapy import signals
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
from selenium import webdriver
from itemadapter import is_item, ItemAdapter


class MHdownloadMiddleware:
    def __init__(self):
        options = Options()
        options.chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.driver = webdriver.Chrome(options=options)

    def process_request(self, request, spider):
        print(request.url)
        # 这个方法中，通过driver访问第一个连接
        self.driver.get(request.url)
        # 获取 page_shource, 在把page_source的源代码 传递到 爬虫parse方法的 response对象
        data = self.driver.page_source
        # print(data)

        # 返回响应对象，并且在响应对象中加入 page_source 的源代码
        return HtmlResponse(url=request.url,body=data,request=request,encoding='utf-8')
```

PS：需注意selenium的版本问题

```
pip install --upgrade selenium
```

