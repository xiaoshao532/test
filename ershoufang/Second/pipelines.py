# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class SecondPipeline:

    def open_spider(self, spider):
        print('开始爬虫......')


    def process_item(self, item, spider):
        jianjie = item['jianjie']
        l1 = item['l1']
        l2 = item['l2']
        l3 = item['l3']
        l4 = item['l4']
        l5 = item['l5']
        l6 = item['l6']
        square = item['square']
        chaoxiang = item['chaoxiang']
        louceng = item['louceng']
        time = item['time']
        diqu = item['diqu']
        diqu1 = item['diqu1']
        diqu2 = item['diqu2']
        diqu3 = item['diqu3']
        zongjia = item['zongjia']
        danjia = item['danjia']

        return item

    def close_spider(self, spider):
        print('结束爬虫!')
