# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import requests


class TjsmanhuaPipeline:
    def __init__(self):
        self.headers = {
            "Accept": "",
            "Accept-Language": "",
            "USER_AGENT": ""
        }

    def process_item(self, item, spider):
        jpg_list = item['img']
        page_list = item['page']
        print("pipeline:",jpg_list,page_list)
        response = requests.get(url=jpg_list, headers=self.headers)
        with open("G:/USB flash driver/python爬虫/实战/MH/{}.png".format(page_list), 'wb') as f:
            f.write(response.content)
        return item
