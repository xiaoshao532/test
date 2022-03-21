import scrapy
from newhouse.items import NewhouseItem

class NewSpider(scrapy.Spider):
    name = 'new'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://heyuan.58.com/xinfang/']

    url = 'https://heyuan.58.com/xinfang/loupan/all/p%d/?PGTID=0d0091a8-028e-342b-c0a4-95b5a0af0899&ClickID=1'

    pageNum = 0

    def parse(self, response):
        # pass
        div_list = response.xpath('//div[@class="key-list imglazyload"]/div')

        for div in div_list:
            xiaoqu = div.xpath('normalize-space(./div/a[1]/span)').extract()[0]
            didian = div.xpath('normalize-space(./div/a[2]/span)').extract()[0]
            ziduan1 = div.xpath('normalize-space(./div/a[4]/div/i[1])').extract()[0]
            leixing = div.xpath('normalize-space(./div/a[4]/div/i[2])').extract()[0]
            money = div.xpath('normalize-space(./a[2]/p/span)').extract()[0]

            item = NewhouseItem()
            item['xiaoqu'] = xiaoqu
            item['didian'] = didian
            item['ziduan1'] = ziduan1
            item['leixing'] = leixing
            item['money'] = money

            yield item

        if self.pageNum <= 3:
            self.pageNum += 1
            print("爬取：%d 页" % self.pageNum)
            new_url = self.url % self.pageNum
            yield scrapy.Request(url=new_url, callback=self.parse)