# encoding = utf-8
# 开发者：xxx
# 开发时间： 13:26 
# "Stay hungry，stay foolish."

from scrapy import cmdline
cmdline.execute("scrapy crawl lxq -o 1.csv".split())