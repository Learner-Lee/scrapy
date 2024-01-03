import requests
import scrapy
from scrapy import Selector

from TJSmanhua.items import TjsItem


class MhSpider(scrapy.Spider):

    name = "MH"
    allowed_domains = ["a.com"]
    # start_urls = ["http://a.com/page/{}".format(i) for i in range(613411, 613414)]
    for i in range(613411, 613414):
        start_urls = ["http://a.com/page/{}".format(i) for i in range(i, i+1)]

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.xpath('//div[@class="comic-view clearfix"]/div[3]/img')

        i = 0
        for list_item in list_items:
            i = i + 1
            Tjs = TjsItem()
            Tjs['img'] = list_item.xpath('.//@data-src').extract_first()
            Tjs['page'] = i
            yield Tjs
