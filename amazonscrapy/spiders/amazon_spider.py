# -*- coding: utf-8 -*-
import scrapy
from amazonscrapy.items import AmazonscrapyItem
import datetime


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = []
    start_urls = [
        'https://www.amazon.co.uk/s?i=merchant-items&me=A141KPLESCIJJT'
    ]
    download_delay = 1.5

    # def __init__(self, seller='', **kwargs):
    #     self.start_urls = [f'https://www.amazon.co.uk/s?i=merchant-items&me={seller}']  # py36
    #     super().__init__(**kwargs)  # python3

    # def __init__(self, **kwargs):
    #     domains = ['B085L8BTXQ','B073B5W7MJ']
    #     # for line in open('domains.txt', 'r').readlines():
    #     for line in domains:
    #         self.allowed_domains.append(line)
    #         self.start_urls.append('https://www.amazon.co.uk/dp/%s' % line)

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
        # try:
        items = AmazonscrapyItem()
        try:
            imagelink = response.xpath('//div[@id="imgTagWrapperId"]/img/@data-a-dynamic-image').get()

        except:
            imagelink = response.xpath('//div[@id="imgTagWrapperId"]/img/@src').get()

        if imagelink:
            items['imagelink'] = [key for key, value in eval(imagelink).items()][0]
        else:
            items['imagelink'] = 'None'

        name = response.css("#productTitle").css('::text').extract_first()
        if name:
            items['name'] = name.replace('\n', '').replace('  ', '')
        else:
            items['name'] = 'None'
        price1 = response.css('#priceblock_saleprice').css('::text').extract_first()
        price2 = response.css('#priceblock_ourprice').css('::text').extract_first()

        if price1:
            items['price'] = price1
        elif price2:
            items['price'] = price2
        else:
            items['price'] = 'None'
        brand = response.css('#bylineInfo').css('::text').extract_first()
        if brand:
            items['brand'] = brand
        else:
            items['brand'] = 'None'
        items['productlink'] = response.url
        items['datetime'] = datetime.datetime.now()
        stars = response.css('.average_customer_reviews .a-icon-alt::text').get()
        if stars:
            items['stars'] = stars
        else:
            items['stars'] = 'None'
        ratings = response.css('.average_customer_reviews .a-link-normal::text').get()
        if ratings:
            items['ratings'] = ratings
        else:
            items['ratings'] = 'None'
        asin = response.css('.col2 tr:nth-child(1) .value::text').get()
        if asin:
            items['asin'] = asin
        else:
            items['asin'] = 'None'
        rank1 = response.css('#SalesRank .value::text').get()
        if rank1:
            items['rank1'] = rank1.replace("\n", '').replace('(', '')
        else:
            items['rank1'] = 'None'
        rank2 = ' '.join(
            response.css('#SalesRank .zg_hrsr_rank::text,#SalesRank .zg_hrsr_ladder a::text').extract())
        if rank2:
            items['rank2'] = rank2
        else:
            items['rank2'] = 'None'
        return items

        # except:
        #     print("item was old")
