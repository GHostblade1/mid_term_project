import scrapy, re, random
import json, time
from fake_useragent import UserAgent
from lxml import etree

from ..items import EndItemWhjswItem
from urllib import parse
# scrapy.Spider 所有spider都要继承这个类
class ZhiLianSpider(scrapy.Spider):
    name = 'whjsw'  # 区分spider
    ua = UserAgent()
    def start_requests(self):
        # 请求如果没有全部发出去，后续请求都不会发
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie':'_job910utmc=c1c5d1b8-9c2f-4777-8bbc-471596188fc8; ASP.NET_SessionId=y34elxlo3tseqtqy5nnnw2a1; Hm_lvt_10fe842eb8d711feaf59d650aee966e0=1561426993,1561508984,1561596146,1561682775; Hm_lpvt_10fe842eb8d711feaf59d650aee966e0=1561682782; _SID=95639; _chat_cuid=Yz4tocn/iTiaKzw45lt46axZxcw1sQd5gCtHQdGEm+egk7XAQywIfuQLKveIScPU; _chat_cuid.sig=3PUWdLMjkwDVh7TudaT6pdhCay0',
            'Host': 'www.job910.com',
            'Referer': 'http://www.job910.com/Company/resume/SearchList.aspx?NowAreaCode=&NowWork=&MinWorkYears=&MaxWorkYears=&UpdateDateScope=&Keyword=&HopeWorkArea=&HopeWork=&MinAge=&MaxAge=&MinDegree=-1&MaxDegree=-1&Marriage=&workMethod=&major=&TechnialPost=&entrytime=&resumeid=&IsHead=&Gender=&type=0&txtsearchName=',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/'
                          '73.0.3683.86Safari/537.36'
            }
        # # with open('GB2312汉字.txt', 'r') as k:
        # #     kws = k.read()
        # # for kw in kws:
        # #headers['User-Agent'] = self.ua.random
        #cookies = {'_job910utmc': '785ceb9e-6bdf-4b7c-9544-8fe1b617cf50'}
        # #     try:
        # for start in range(1, 100000):
        #     #time.sleep(random.random())
        #     url = 'http://www.job910.com/company/resume/searchList.aspx?pageIndex='+str(start)+'&pageSize=20&sortField=&sort=0&keyword=&NowWork=&HopeWork=&hopeWorkArea=&NowAreaCode=&resumeId=-1&salary=0&maxSalary=0&minSalary=0&MinDegree=-1&MaxDegree=-1&MinWorkYears=-1&MaxWorkYears=-1&marriage=-1&isHead=-1&major=&gender=-1&school=&UpdateDateScope=-1&workMethod=&technialPost=&minAge=-1&maxAge=-1&birthPlaceArea=&entrytime=-1&video=-1'
        #     yield scrapy.Request(url=url, headers=headers, cookies=cookies, dont_filter=True)  # 可以return 返回，也可以使用yield将方法变成生成器，由引擎交给调度器
        #     start += 1
        #     print(37, start)
        #     # except:
            #     print(47, '更换关键字', kw)
        for start in range(1000000, 1500000):
            print(41, start)
            url = 'http://www.job910.com/company/resumeview.aspx?userId='+str(start)+'&keyword=&type=search'
            yield scrapy.Request(url=url, headers=headers, dont_filter=True, callback=self.pares1)
    # 回调函数(解析列表页响应)，接收请求对应的响应
    def parse(self, response):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_job910utmc=c1c5d1b8-9c2f-4777-8bbc-471596188fc8; ASP.NET_SessionId=y34elxlo3tseqtqy5nnnw2a1; Hm_lvt_10fe842eb8d711feaf59d650aee966e0=1561426993,1561508984,1561596146,1561682775; Hm_lpvt_10fe842eb8d711feaf59d650aee966e0=1561682782; _SID=95639; _chat_cuid=Yz4tocn/iTiaKzw45lt46axZxcw1sQd5gCtHQdGEm+egk7XAQywIfuQLKveIScPU; _chat_cuid.sig=3PUWdLMjkwDVh7TudaT6pdhCay0',
            'Host': 'www.job910.com',
            'Referer': 'http://www.job910.com/company/resume/searchList.aspx?pageIndex=3&pageSize=20&sortField=&sort=0&keyword=&NowWork=&HopeWork=&hopeWorkArea=&NowAreaCode=&resumeId=-1&salary=0&maxSalary=0&minSalary=0&MinDegree=-1&MaxDegree=-1&MinWorkYears=-1&MaxWorkYears=-1&marriage=-1&isHead=-1&major=&gender=-1&school=&UpdateDateScope=-1&workMethod=&technialPost=&minAge=-1&maxAge=-1&birthPlaceArea=&entrytime=-1&video=-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/'
                          '73.0.3683.86Safari/537.36'
        }
        cookies = {'_job910utmc': 'c1c5d1b8-9c2f-4777-8bbc-471596188fc8'}
        text=response.text # 获取文本数据
        #response.body# 二进制流
        #title=response.xpath('//title/text()').extract() #返回一个列表，列表中是节点对象  .extract()获得节点对象中的数据
        print(text)
        html = etree.HTML(text)
        urls = html.xpath('//table[@class="tablelist"]/tbody/tr/td/a/@href')
        print(62, urls)
        for u in urls:
            print(51, u)
            url1 = 'http://www.job910.com'+u
            #time.sleep(random.random())
            yield scrapy.Request(url=url1, headers=headers, callback=self.pares1, cookies=cookies, dont_filter=True)
    # 详情页解析规则
    def pares1(self,resp):
        html = etree.HTML(resp.text)
        title = html.xpath('//title/text()')
        print(84, title)
        name = html.xpath('//div[@class="base-info"]/div[@class="flexbox align-center"]/span[@class="fts-34 gray-dark"]/text()')
        name = name[0].replace('\n', '')
        #print(87, name)
        info = html.xpath('//div[@class="line-h-2 fts-16 gray m-t-10"]/div/span/text()')
        #print(88, info)
        l_info = ['', '', '', '', '', '', '', '', '']
        for i in info:
            if re.search('女', i) or re.search('男', i):
                l_info[0] = i
            elif re.search('婚', i):
                l_info[1] = i
            elif re.search('岁', i):
                l_info[2] = i.replace('\n', '')
            elif re.search('本科', i) or re.search('硕士', i) or re.search('MBA', i) or re.search('博士', i):
                l_info[3] = i
            elif re.search('群众', i) or re.search('党员', i) or re.search('团员', i) or re.search('派', i):
                l_info[5] = i
            elif re.search('年以上', i) or re.search('应届', i):
                l_info[6] = i.replace('\n', '')
            elif re.search('区', i) or re.search('县', i) or re.search('城', i) or re.search('庄', i) or re.search('疆', i) or re.search('市', i) or re.search('江', i):
                l_info[7] = i
            elif re.search('籍贯', i):
                l_info[8] = i
        #print(108, l_info)
        jobs = html.xpath('//div[@class="unit"]/div[@class="line-h-2 fts-16 gray m-t--10"]/div/span/text()')
        #print(110, jobs)
        job_addr = jobs[1]
        try:
            job_p = jobs[3]
        except:
            job_p = ''
        #print(112, job_addr, job_p)
        sal = html.xpath('//div[@class="line-h-2 fts-16 gray m-t--10"]/div[@class="m-t-10 text-center white-light-bg"]/label/text()')
        #print(114, sal)
        salary = sal[0].replace('\n', '')
        job_exp = sal[1]
        try:
            job_status = sal[2]
        except:
            job_status = ''
        #print(115, salary, job_exp, job_status)
        edu = html.xpath('//div[@class="unit-item-content gray"]/div/text()')
        #print(117, edu)
        edu = ''.join(edu)
        item = EndItemWhjswItem()
        item['name'] = name
        item['sex'] = l_info[0]
        item['marry'] = l_info[1]
        item['age'] = l_info[2]
        item['academic'] = l_info[3]
        item['nation'] = l_info[4]
        item['politics'] = l_info[5]
        item['exper'] = l_info[6]
        item['addr'] = l_info[7]
        item['census'] = l_info[8]
        item['job_status'] = job_status
        item['job_addr'] = job_addr
        item['job_p'] = job_p
        item['job_ind'] = ''
        item['job_salary'] = salary
        item['edu'] = edu
        item['job_exp'] = job_exp
        # # #return item
        # # print(65, position, addr)
        yield item # 由引擎将item交给pipeline
        # # pass