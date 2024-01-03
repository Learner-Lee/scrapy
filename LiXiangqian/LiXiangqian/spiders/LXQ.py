import scrapy
from scrapy import Selector

from LiXiangqian.items import ZFItem


class LxqSpider(scrapy.Spider):
    name = 'LXQ'
    allowed_domains = ['gz.lianjia.com']
    start_urls = ['https://gz.lianjia.com/zufang/huadou/pg1/#contentList'.format(i) for i in range(1,10)]
    # start_urls = ['https://gz.lianjia.com/zufang/huadou/pg1/#contentList'.format(i) for i in range(1, 10)]

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.xpath('//div[@class="content__list--item"]')
        print(len(list_items))
        for list_item in list_items:
            ZF_item = ZFItem()
            a = list_item.xpath('.//a[@class="twoline"]/text()').extract_first(default='')
            b = list_item.xpath('.//a[@class="content__list--item--aside"]/img/@alt').extract_first(default='')
            ZF_item['tital'] = a if a else b
            # ZF_item['tital'] = list_item.xpath('.//a[@class="twoline"]/text()').extract_first()
            detail = list_item.xpath('.//p[@class="content__list--item--des"]//text()').extract()
            str = ' '.join(detail)
            ZF_item['detail'] = str.replace('\n   ', '').replace('/', '-').replace(' ', '')
            ZF_item['price'] = list_item.xpath('.//span[@class="content__list--item-price"]//text()').extract_first()
            print(ZF_item['tital'], ZF_item['detail'], ZF_item['price'])
            yield ZF_item
