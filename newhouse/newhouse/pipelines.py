# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewhousePipeline:

    def open_spider(self, spider):
        print('开始爬虫......')

    def process_item(self, item, spider):
        xiaoqu = item['xiaoqu']
        didian = item['didian']
        ziduan1 = item['ziduan1']
        leixing = item['leixing']
        money = item['money']
        return item

    def close_spider(self, spider):
        print('结束爬虫!')