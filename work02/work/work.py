"""
需求
1.要爬取的url:  https://api-hmugo-web.itheima.net/api/public/v1/home/swiperdata
2.使用requests 访问服务器端，获取json数据
3.使用jsonpath解析json数据，获取 所有key为image_src 的值（图片的url）
4.使用requests把所有图片下载并保存到本地
"""

import requests
import jsonpath


class work():
    def __init__(self):
        self.url = 'https://api-hmugo-web.itheima.net/api/public/v1/home/swiperdata'
        self.headers = {
            "User-Agent": ""
        }

    def run(self):
        content = self.getjson()
        urlist = self.getPurl(content)
        print(urlist)
        self.saveP(urlist)



    def getjson(self):
        # 使用requests库发送GET请求获取JSON数据
        response = requests.get(url=self.url, headers=self.headers)
        print(response)

        # 检查响应状态码，200表示成功
        if response.status_code == 200:
            # 解析JSON数据
            json_data = response.json()
            # 现在，变量json_data包含了从服务器端获取的JSON数据
            print(json_data,type(json_data))
            return json_data
        else:
            print("Failed to retrieve JSON data. Status code:", response.status_code)

    def getPurl(self,json):
        # 提取所有job的value值
        # jsonpath可以根据key值的名称提取任意层级结构的value，返回一个列表
        # $.. 定位规则：定位任意层级结构的键值对
        image_src = jsonpath.jsonpath(json, '$..image_src')
        print(image_src,type(image_src))
        return image_src


    def saveP(self,urlist):
        i = 1
        for url in urlist:
            print(url)
            response = requests.get(url=url, headers=self.headers)
            with open("{}.png".format(i), 'wb') as f:
                f.write(response.content)
            i = i+1



if __name__ == '__main__':
    work = work()
    work.run()


