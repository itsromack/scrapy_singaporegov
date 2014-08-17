# -*- coding: utf-8 -*-
import re
import scrapy
from singaporegov.items import SingaporegovItem

class PersonsSpider(scrapy.Spider):
    counter = 0
    name = "persons"
    allowed_domains = ["sgdi.gov.sg"]
    start_urls = (
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000021815', #MCI
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000022693', #MCCY
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000002', #MINDEF
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000003', #MOE
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000005', #MOF
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000006', #MFA
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000007', #MOH
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000008', #MHA
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000010', #MINLAW
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000011', #MOM
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000012', #MND
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000022193', #MSF
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000004', #MEWR
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000013', #MTI
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000001', #MOT
        'http://app.sgdi.gov.sg/listing.asp?agency_subtype=dept&agency_id=0000000014'  #PMO
    )

    def parse(self, response):
        ministry = response.xpath('//div[contains(@class, "contentArea")]/h3/text()').extract()[0].strip().strip('\n').strip('\r').strip('\t').strip('\n').strip('\t').strip('\r')
        department = response.xpath('//div[contains(@class, "tableHeading")]/text()').extract()[0].strip().strip('\n').strip('\r').strip('\t').strip('\n').strip('\t').strip('\r')
        items = response.xpath('//table[contains(@class, "peopleList")]/tr')
        for item in items:
            fullname = ''.join(item.xpath('.//td/font/a/text()').extract()).strip().strip('\n').strip('\t').strip('\r')
            if fullname != '':
                job_title = item.xpath('td/font/text()').extract()[0]
                email = ''.join(item.xpath('.//script/text()').extract()).strip().strip('\n').strip('fn_emailScramble(\'').strip('\');').strip('\n').strip('\r').replace("','", '@')
                f = open('persons.csv', 'a')
                f.write(','.join([ministry, department, job_title, fullname, email, response.url, '\n\r']))
                f.close()
