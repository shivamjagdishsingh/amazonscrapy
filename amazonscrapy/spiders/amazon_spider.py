# -*- coding: utf-8 -*-
import scrapy
from amazonscrapy.items import AmazonscrapyItem
import datetime


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'

    start_urls = [
        'https://www.amazon.co.uk/s?i=merchant-items&me=A2U7Q0C25B7FU7'
    ]
    download_delay = 1.5

    # def __init__(self, seller='', **kwargs):
    #     self.start_urls = [f'https://www.amazon.co.uk/s?i=merchant-items&me={seller}']  # py36
    #     super().__init__(**kwargs)  # python3

    def parse(self, response):

        products = response.css(
            '.sg-col-20-of-24.s-result-item.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28')

        for product in products:
            productlink = product.css('.a-link-normal.a-text-normal').css('::attr(href)').extract_first()

            innerlink = response.urljoin(productlink)

            try:
                yield scrapy.Request(innerlink, callback=self.parse_link, dont_filter=True)
            except:
                print('error in code')
        next_page_link = response.css('.a-last a::attr(href)').extract_first()
        next_page_link = response.urljoin(next_page_link)

        yield scrapy.Request(next_page_link, callback=self.parse)

    def parse_link(self, response):
        try:
            items = AmazonscrapyItem()

            items['imagelink'] = response.css('#landingImage::attr(src)').extract_first().replace('\n', '')
            items['name'] = response.css("#productTitle").css('::text').extract_first().replace('\n', '').replace('  ',
                                                                                                                  '')
            items['price'] = response.css('#priceblock_saleprice').css('::text').extract_first()
            if items['price'] is None:
                items['price'] = response.css('#priceblock_ourprice').css('::text').extract_first()
            items['brand'] = response.css('#bylineInfo').css('::text').extract_first()

            items['productlink'] = response.url
            items['datetime'] = datetime.datetime.now()
            items['stars'] = response.css('.average_customer_reviews .a-icon-alt::text').get()
            items['ratings'] = response.css('.average_customer_reviews .a-link-normal::text').get()
            items['asin'] = response.css('.col2 tr:nth-child(1) .value::text').get()
            items['rank1'] = response.css('#SalesRank .value::text').get().replace("\n", '').replace('(', '')
            items['rank2'] = ' '.join(
                response.css('#SalesRank .zg_hrsr_rank::text,#SalesRank .zg_hrsr_ladder a::text').extract())

            return items

        except:
            print("item was old")
