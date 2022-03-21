import scrapy
from bysj.items import BysjItem


class HouseSpider(scrapy.Spider):
    name = 'house'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://heyuan.58.com/chuzu']

    url = 'https://heyuan.58.com/chuzu/pn%d/?PGTID=0d3090a7-028e-3854-3192-ae9442ba1816&ClickID=2'


    pageNum = 0

    def parse(self, response):

        div_list = response.xpath('//li[@class="house-cell "]')

        for div in div_list:
            mode = div.xpath('normalize-space(./div[2]/h2/a/text())').extract()
            type1 = div.xpath('normalize-space(./div[2]/p[1]/text())').extract()
            place = div.xpath('normalize-space(./div[2]/p[2]/a[1]/text())').extract()
            community = div.xpath('normalize-space(./div[2]/p[2]/a[2]/text())').extract()
            money = div.xpath('normalize-space(./div[3]/div[2]/b/text())').extract()

            mode = mode[0] if mode else ''
            type1 = type1[0] if type1 else ''
            place = place[0] if place else ''
            community = community[0] if community else ''
            money = money[0] if money else ''

            item = BysjItem()
            item['mode'] = mode
            item['type1'] = type1
            item['place'] = place
            item['community'] = community
            item['money'] = money

            yield item

        if self.pageNum <= 69:
            self.pageNum += 1
            print("爬取：%d 页" % self.pageNum)
            new_url = self.url % self.pageNum
            yield scrapy.Request(url=new_url, callback=self.parse)
