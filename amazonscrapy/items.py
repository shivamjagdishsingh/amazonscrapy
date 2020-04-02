# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    asin = scrapy.Field()
    productlink = scrapy.Field()
    stars = scrapy.Field()
    ratings = scrapy.Field()
    datetime = scrapy.Field()
    rank1 = scrapy.Field()
    rank2 = scrapy.Field()
    imagelink = scrapy.Field()
