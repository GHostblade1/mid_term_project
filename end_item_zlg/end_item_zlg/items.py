# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EndItemZlgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    marry = scrapy.Field()
    age = scrapy.Field()
    academic = scrapy.Field()
    nation = scrapy.Field()
    politics = scrapy.Field()
    exper = scrapy.Field()
    addr = scrapy.Field()
    census = scrapy.Field()
    job_status = scrapy.Field()
    job_addr = scrapy.Field()
    job_p = scrapy.Field()
    job_ind = scrapy.Field()
    job_salary = scrapy.Field()
    edu = scrapy.Field()
    job_exp = scrapy.Field()
