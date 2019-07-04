from urllib import parse

import scrapy
import json
# from ..items import FirstItem
# scrapy.Spider 所有spider都要继承这个类
class ZhiLianSpider(scrapy.Spider):
    name = 'boss'  # 区分spider
    #start_urls=['http://www.baidu.com'] # 起始urls
    # 起始请求 携带参数，cookie，headers，proxy
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'cookie': 'sid=sem; toUrl=/; __g=sem; lastCity=101010100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1561082535,1561082567; __c=1561082567; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D5u_-dqcCl1A5qJ1A834PR6FH-CLc-cEqKnioVC8bM8d3E6hlwgLcAg3iNEiuSltR%26wd%3D%26eqid%3Dfca5a35400002d35000000035d0c3a9e&l=%2Fwww.zhipin.com%2F&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26utm_source%3Dbaidu%26utm_medium%3Dcpc%26utm_campaign%3DPC-yixian-pinpaici-2C%26utm_content%3DBOSSzhipin-hexin%26utm_term%3DBOSSzhipinwangz; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1561083258; __a=73534768.1561082533.1561082533.1561082567.14.2.13.14',
    }

    def start_requests(self):
        # 请求如果没有全部发出去，后续请求都不会发
        for kw in ['爬虫', 'AI', '数据挖掘与数据分析', '大数据', 'web开发']:
            for start in range(1, 9):
                url = 'https://www.zhipin.com/c101010100/?query='+parse.quote(kw)+'&page='+str(start)+'&ka=page-next'
                yield scrapy.Request(url)  # 可以return 返回，也可以使用yield将方法变成生成器，由引擎交给调度器
    # 回调函数(解析列表页响应)，接收请求对应的响应
    def parse(self, response):
        #text=response.text # 获取文本数据
        #response.body# 二进制流
        title=response.xpath('//title/text()').extract() #返回一个列表，列表中是节点对象  .extract()获得节点对象中的数据
        print(title)
        #print(title)
        #print(23, response.text)
        # d = json.loads(response.text)['data']
        # #print(24, d)
        # datas = d['results']
        # count = d['count']  # 获取总页数
        # # 获取详情页url
        # for data in datas:
        #     yield scrapy.Request(url=data["positionURL"], callback=self.pares1)  # 构造Request对象，发送请求,指定回调函数，去掉()
        # # 翻页,构造下一页的请求
        # dd=response.url.split('&start=') # 对应请求的url
        # if int(dd[1])+90 <count:
        #     new_url=dd[0]+'&start='+str(int(dd[1])+90)
        #     yield scrapy.Request(new_url)
    # 详情页解析规则
    def pares1(self,resp):
        item=FirstItem()
        # title = resp.xpath('//title/text()').extract()[0]
        # salary=resp.xpath('//span[@class="summary-plane__salary"]/text()').extract()[0]
        position = resp.xpath('//h3[@class="summary-plane__title"]/text()').extract()[0]
        salary = resp.xpath('//span[@class="summary-plane__salary"]/text()').extract()[0]
        describe = resp.xpath('//div[@class="describtion__detail-content"]//text()').extract()
        describe_str = ''.join(describe)
        addr = resp.xpath('//span[@class ="job-address__content-text"]//text()').extract()[0]
        company = resp.xpath('//a[@class ="company__title"]//text()').extract()[0]
        year = resp.xpath('//div[@class="summary-plane__left"]//text()').extract()[3]
        high_port = resp.xpath('//div[@class ="highlights__content"]//text()').extract()
        high_port_str = '、'.join(high_port)
        main_business = resp.xpath('//button[@class="company__industry"]//text()').extract()
        main_business_str = '、'.join(main_business)
        company_scale = resp.xpath('//button[@class="company__size"]//text()').extract()[0]
        net_site = resp.xpath('//a[@class="company__page-site"]/@href').extract()[0]
        item['position'] = position
        item['salary'] = salary
        item['describe_str'] = describe_str
        item['addr'] = addr
        item['company'] = company
        item['year'] = year
        item['high_port_str'] = high_port_str
        item['main_business_str'] = main_business_str
        item['company_scale'] = company_scale
        item['net_site'] = net_site
        #return item
        print(65, position, addr)
        yield item # 由引擎将item交给pipeline