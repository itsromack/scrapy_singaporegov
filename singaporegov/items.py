# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SingaporegovItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	agency_depth = scrapy.Field()
	name = scrapy.Field()
	parent = scrapy.Field()
	did = scrapy.Field()
	email = scrapy.Field()
	unit = scrapy.Field()
	job_title = scrapy.Field()
	ministry = scrapy.Field()
	url = scrapy.Field()
