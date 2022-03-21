import scrapy
from Second import SecondItem


class HouseSpider(scrapy.Spider):
    name = 'house'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://heyuan.58.com/ershoufang']

    url = 'https://heyuan.58.com/ershoufang/p%d/?PGTID=0d30000c-028e-370b-9c88-bede06485ccc&ClickID=2'

    pageNum = 0

    def parse(self, response):
        div_list = response.xpath('//div[@class="property"]')
        for div in div_list:
            jianjie = div.xpath('normalize-space(./a/div[2]/div[1]/div[1]/h3/text())').extract()
            l1 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[1]/span[1]/text())').extract()
            l2 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[1]/span[2]/text())').extract()
            l3 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[1]/span[3]/text())').extract()
            l4 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[1]/span[4]/text())').extract()
            l5 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[1]/span[5]/text())').extract()
            l6 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[1]/span[6]/text())').extract()
            square = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[2]/text())').extract()
            chaoxiang = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[3]/text())').extract()
            louceng = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[4]/text())').extract()
            time = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[1]/p[5]/text())').extract()
            diqu = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[2]/p[1]/text())').extract()
            diqu1 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[2]/p[2]/span[1]/text())').extract()
            diqu2 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[2]/p[2]/span[2]/text())').extract()
            diqu3 = div.xpath('normalize-space(./a/div[2]/div[1]/section/div[2]/p[2]/span[3]/text())').extract()
            zongjia = div.xpath('normalize-space(./a/div[2]/div[2]/p[1]/span[1]/text())').extract()
            danjia = div.xpath('normalize-space(./a/div[2]/div[2]/p[2]/text())').extract()

            jianjie = jianjie[0] if jianjie else ''
            l1 = l1[0] if l1 else ''
            l2 = l2[0] if l2 else ''
            l3 = l3[0] if l3 else ''
            l4 = l4[0] if l4 else ''
            l5 = l5[0] if l5 else ''
            l6 = l6[0] if l6 else ''
            square = square[0] if square else ''
            chaoxiang = chaoxiang[0] if chaoxiang else ''
            louceng = louceng[0] if louceng else ''
            time = time[0] if time else ''
            diqu = diqu[0] if diqu else ''
            diqu1 = diqu1[0] if diqu1 else ''
            diqu2 = diqu2[0] if diqu2 else ''
            diqu3 = diqu3[0] if diqu3 else ''
            zongjia = zongjia if zongjia else ''
            danjia = danjia if danjia else ''


            item = SecondItem()
            item['jianjie'] = jianjie
            item['l1'] = l1
            item['l2'] = l2
            item['l3'] = l3
            item['l4'] = l4
            item['l5'] = l5
            item['l6'] = l6
            item['square'] = square
            item['chaoxiang'] = chaoxiang
            item['louceng'] = louceng
            item['time'] = time
            item['diqu'] = diqu
            item['diqu1'] = diqu1
            item['diqu2'] = diqu2
            item['diqu3'] = diqu3
            item['zongjia'] = zongjia
            item['danjia'] = danjia

            yield item

        if self.pageNum <= 49:
            self.pageNum += 1
            print("爬取：%d 页" % self.pageNum)
            new_url = self.url % self.pageNum
            yield scrapy.Request(url=new_url, callback=self.parse)
