# 任务需求： 使用requests爬取北京公交网信息，使用xpath解析1路车的 公交车名称，类型，运行时间，参考票价，公交公司名称
#
# 网址：https://beijing.8684.cn
#
# https://beijing.8684.cn/x_322e21c5

from lxml import etree
import requests


class work():
    def __init__(self):
        self.url = 'https://beijing.8684.cn/x_322e21c5'
        self.headers = {
            "User-Agent": ""
        }

    def run(self):
        data = self.gethtml()
        self.parse01(data)

    def gethtml(self):
        # 使用requests库发送GET请求获取JSON数据
        response = requests.get(url=self.url, headers=self.headers)
        # print(response.text)
        # with open("web.html","w",encoding="utf-8") as f :
        #     f.write(response.text)
        return response.text

    def parse01(self, text):
        html = etree.HTML(text)
        # print(type(html))
        # print(etree.tostring(html))a
        tital = html.xpath('//div[@class = "info"]/h1/span/text()')
        type = html.xpath('//div[@class = "info"]/h1/a/text()')
        time = html.xpath('//div[@class = "info"]/ul[@class = "bus-desc"]/li[1]/text()')
        free = html.xpath('//div[@class = "info"]/ul[@class = "bus-desc"]/li[2]/text()')
        fram_name = html.xpath('//div[@class = "info"]/ul[@class = "bus-desc"]/li[3]/span/text()')
        fram_data = html.xpath('//div[@class = "info"]/ul[@class = "bus-desc"]/li[3]/a/text()')
        least = html.xpath('//div[@class = "info"]/ul[@class = "bus-desc"]/li[4]/span/text()')

        print(tital[0], type[0])
        print(time[0])
        print(free[0])
        print(fram_name[0], ":", fram_data[0])
        print(least[0])


if __name__ == '__main__':
    work = work()
    work.run()
