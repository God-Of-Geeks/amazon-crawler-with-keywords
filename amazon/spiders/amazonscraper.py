# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem
from scrapy.http import Request

class AmazonscraperSpider(scrapy.Spider):
    name = 'amazon'
    keyword = input("Enter the keyword to search: ")
    start_urls = [
    "https://www.amazon.in/s?k="+ keyword +"&ref=nb_sb_noss_2"
    ]

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('.a-size-medium.a-color-base.a-text-normal').css('::text').extract() or ['product names unavailable please check the name or the css selector']
        product_by=response.css('.sg-col-20-of-28 .a-link-normal.a-text-bold').css('::text').extract() or ['product seller not listed']
        amazon_product_price = response.css('.sg-col-20-of-28 .a-price-whole').css('::text').extract() or ['price unavailable']
        stars = response.css('.a-size-small .a-size-base').css('::text').extract() or ['starts not available']
        amazon_url = response.url or ['url unavailable']

        items['product_name']=product_name
        items['product_by']=product_by
        items['amazon_product_price']=amazon_product_price
        items['amazon_url']=amazon_url
        items['stars']=stars
        yield items
