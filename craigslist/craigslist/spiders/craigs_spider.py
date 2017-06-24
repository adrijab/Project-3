import scrapy
from craigslist.items import CraigslistItem
from scrapy.selector import HtmlXPathSelector
from bs4 import BeautifulSoup as bs


class CraigsSpider(scrapy.Spider):
    name = "craigs"
    start_urls = ['https://craigslist.org/']

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        city = hxs.select("///li[@class='s']//a")
        url = response.xpath().extract()
        # titles = response.xpath('//h2/a/@title').extract()
        # links = response.xpath('//h2/a/@href').extract()
        # companies = response.xpath('//span[@class="company"]/span').extract()
        for index, node in enumerate(hxs.select("///li[@class='s']//a")):
            x = node.select("@href").extract()[0].encode('utf-8')
            y = node.select("///li[@class='s']//a/text()").extract()[index]
            item = CraigslistItem()
            item['city'] = y
            item['url'] = x
            yield item
