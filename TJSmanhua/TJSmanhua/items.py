# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TjsItem(scrapy.Item):
    img = scrapy.Field()
    page = scrapy.Field()
