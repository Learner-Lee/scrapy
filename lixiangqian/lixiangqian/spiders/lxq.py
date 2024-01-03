from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lixiangqian.items import LixiangqianItem


class LxqSpider(CrawlSpider):
    name = 'lxq'
    allowed_domains = ['www.huadu.gov.cn']
    start_urls = ['https://www.huadu.gov.cn/hdzx/tzgg/index.html']
    # href="https://www.huadu.gov.cn/hdzx/tzgg/index_2.html"
    # link = LinkExtractor(allow=r'https://www.huadu.gov.cn/hdzx/tzgg/index_\d+\.html')
    link = LinkExtractor(allow=r'https://www.huadu.gov.cn/hdzx/tzgg/index.*\.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        sel = Selector(response)
        # //*[@id="page"]/div/div/div/div/div/div[3]/div[2]/div/ul/li[1]
        words_list = sel.xpath('//*[@id="page"]/div/div/div/div/div/div[3]/div[2]/div/ul/li')
        print(len(words_list))
        for words in words_list:
            item = LixiangqianItem()
            headline = words.xpath('./a/text()').extract_first()
            data = words.xpath('./span/text()').extract_first()
            print(headline,data)
            item['headline'] = headline
            item['data'] = data
            yield item
        pass
