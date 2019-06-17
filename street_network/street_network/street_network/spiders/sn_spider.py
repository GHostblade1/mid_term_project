import scrapy
from ..items import StreetNetworkItem
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

class StreetNetworkSpider(CrawlSpider):
    name = 'sn'

    def start_requests(self):
        for i in [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,50,51,52,53,54,61,62,63,64,65,80,81]:
            url = 'https://s.dajie.com/job-ci'+str(i)+'0000-pa1/'
            yield scrapy.Request(url)
    rules = (Rule(link_extractor=LinkExtractor(restrict_xpaths='//div[@class="search-list-con"]'), callback='parse1'),
             Rule(link_extractor=LinkExtractor(restrict_xpaths='//a[@class="next"]'), follow=True)
             )

    def parse1(self, response):
        item = StreetNetworkItem()
        title = response.xpath('//title/text()').extract()[0]
        print(18, response.xpath('//title/text()').extract()[0])
        #response.xpath('')
        name = response.xpath('//span[@class="job-name"]/text()').extract()[0]
        print(21, name)
        scripts = response.xpath('//div[@class="top"]/ul//text()').extract()
        scripts1 = []
        for s in range(len(scripts)):
            if s in (4, 11, 28):
                scripts1.append(scripts[s])
        scripts = '、'.join(scripts1)
        # scripts = scripts.replace('\t', '')
        # scripts = scripts.replace('\n', '')
        scripts = scripts.replace(' ', '')
        print(25, scripts)
        duty = response.xpath('//div[@class="centerContent"]//text()').extract()[5:-2]
        duty = '、'.join(duty)
        # duty = duty.replace('\t', '')
        # duty = duty.replace('\n', '')
        duty = duty.replace(' ', '')
        print(29, duty)
        #print(25, duty)
        item['title'] = title
        item['name'] = name
        item['scripts'] = scripts
        item['duty'] = duty
        yield item