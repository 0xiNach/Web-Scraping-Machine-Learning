# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HackmageddonItem(scrapy.Item):
    # define the fields for your item here like:
    Year = scrapy.Field()
    dat = scrapy.Field()
    Author = scrapy.Field()
    Target = scrapy.Field()
    Description = scrapy.Field()
    Attack = scrapy.Field()
    Target_class = scrapy.Field()
    Attack_class = scrapy.Field()
    Country = scrapy.Field()

