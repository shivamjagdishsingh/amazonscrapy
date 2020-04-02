# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class AmazonscrapyPipeline(object):

    def process_item(self, item, spider):
        return item

    # def open_spider(self, spider):
    #     hostname = 'localhost'
    #     username = 'shivam'
    #     password = '123'
    #     database = 'scrapy'
    #     self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    #     self.cur = self.connection.cursor()
    #
    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.connection.close()
    #
    # def process_item(self, item, spider):
    #     self.cur.execute(
    #         "insert into amazon(name,price,brand,asin,productlink,datetime,stars,ratings,rank1,rank2,imagelink) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    #         (item['name'], item['price'], item['brand'], item['asin'],
    #          item['productlink'], item['datetime'], item['stars'], item['ratings'], item['rank1'], item['rank2'],
    #          item['imagelink']))
    #     self.connection.commit()
    #     return item
