# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BysjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mode = scrapy.Field()
    type1 = scrapy.Field()
    place = scrapy.Field()
    community = scrapy.Field()
    money = scrapy.Field()
    # pass
