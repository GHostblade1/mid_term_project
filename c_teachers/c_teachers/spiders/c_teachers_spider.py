import scrapy, re
import json, time
from fake_useragent import UserAgent
from lxml import etree

from ..items import CTeachersItem
from urllib import parse
# scrapy.Spider 所有spider都要继承这个类
class ZhiLianSpider(scrapy.Spider):
    name = 'ct'  # 区分spider
    #start_urls=['http://www.baidu.com'] # 起始urls
    # 起始请求 携带参数，cookie，headers，proxy

    def start_requests(self):
        # 请求如果没有全部发出去，后续请求都不会发
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'think_template=chqs; _qscms111e6c4d86d3e03bc9141216dd8b7106=think%3A%7B%229871d3a2c554b27151cacf1422eec048%22%3A%22726499%22%2C%225f4dcc3b5aa765d61d8327deb882cf99%22%3A%227325610d810308e69e150d89897f0c67%22%7D; PHPSESSID=bb7kulm5fgh8iu31c9e0ogrop0; think_language=zh-CN; Hm_lvt_a80ca2e71dadaf4eeb7bac424f55db43=1561548951,1562031303,1562032102,1562147550; Hm_lpvt_a80ca2e71dadaf4eeb7bac424f55db43=1562147550',
            'Host': 'www.jiaoshi.com.cn',
            'Referer': 'http://www.jiaoshi.com.cn/resume/resume_list.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        cookies = {'PHPSESSID':'bb7kulm5fgh8iu31c9e0ogrop0'}
        for p in range(1,10000):
            url = 'http://www.jiaoshi.com.cn/resume/resume_list/page/'+str(p)+'.html'
            yield scrapy.Request(url, headers=headers, dont_filter=True, cookies=cookies)  # 可以return 返回，也可以使用yield将方法变成生成器，由引擎交给调度器
    # 回调函数(解析列表页响应)，接收请求对应的响应
    def parse(self, response):
        text=response.text # 获取文本数据
        #print(text)
        html = etree.HTML(text)
        #print(html)
        urls = html.xpath('//div[@class="listb J_allListBox"]/div/div/a/@href')
        for url in urls:
            print(37, url)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Cookie': 'think_template=chqs; _qscms111e6c4d86d3e03bc9141216dd8b7106=think%3A%7B%229871d3a2c554b27151cacf1422eec048%22%3A%22726499%22%2C%225f4dcc3b5aa765d61d8327deb882cf99%22%3A%227325610d810308e69e150d89897f0c67%22%7D; PHPSESSID=bb7kulm5fgh8iu31c9e0ogrop0; think_language=zh-CN; Hm_lvt_a80ca2e71dadaf4eeb7bac424f55db43=1561548951,1562031303,1562032102,1562147550; Hm_lpvt_a80ca2e71dadaf4eeb7bac424f55db43=1562147550',
                'Host': 'www.jiaoshi.com.cn',
                'Referer': 'http://www.jiaoshi.com.cn/resume/resume_list.html',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            }
            cookies = {'PHPSESSID': 'bb7kulm5fgh8iu31c9e0ogrop0'}
            yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.pares1, dont_filter=True)
    # 详情页解析规则
    def pares1(self,resp):
        #print(156, resp.text)
        #result = json.loads(resp.text)
        #print(156, result)
        #text = result['jsonHtml']
        html = etree.HTML(resp.text)
        name = ' '
        sex = ' '
        marry = ' '
        age = ' '
        academic = ' '
        nation = ' '
        politics = ' '
        exper = ' '
        addr = ' '
        census = ' '
        job_status = ' '
        job_addr = ' '
        job_p = ' '
        job_ind = ' '
        job_salary = ' '
        edu = ' '
        job_exp = ' '
        title = html.xpath('//title/text()')[0]
        print(60, title)
        name = html.xpath('//div[@class="name"]/text()')[0]
        print(62, name)
        conm = html.xpath('//div[@class="info"]/div[@class="inr"]/div[@class="txt"]/text()')
        print(81, conm)
        for c in conm:
            if re.search('性别', c):
                sex = c.split('：')[1]
            elif re.search('年龄', c):
                age = c.split('：')[1]
            # elif re.search('身高', c):
            #     sex = c.split('：')[1]
            elif re.search('最高学历', c):
                academic = c.split('：')[1]
            elif re.search('工作经验', c):
                exper = c.split('：')[1]
            elif re.search('婚姻状况', c):
                marry = c.split(':')[1]
            # elif re.search('所学专业', c):
            #     sex = c.split(':')[1]
            elif re.search('户籍', c):
                census = c.split('：')[1]
            elif re.search('现居住', c):
                addr = c.split('：')[1]
        #print(64, conm)
        edu1 = html.xpath('//div[@class="items"]//text()')
        print(103, edu1)
        for e in edu1:
            # if re.search('求职意向', e):
            #     sex = edu[edu.index(e)+1]
            if re.search('期望职位', e):
                job_p = edu1[edu1.index(e)+1]
            # elif re.search('身高', e):
            #     sex = edu[edu.index(e)+1]
            elif re.search('期望行业', e):
                job_ind = edu1[edu1.index(e)+1]
            elif re.search('期望薪资', e):
                job_salary = edu1[edu1.index(e)+1]
            elif re.search('期望地区', e):
                job_addr = edu1[edu1.index(e)+1]
            # elif re.search('所学专业', e):
            #     sex = edu[edu.index(e)+1]
            elif re.search('求职状态', e):
                job_status = edu1[edu1.index(e)+1]
            # elif re.search('现居住', e):
            #     addr = edu[edu.index(e)+1]
            elif re.search('教育经历', e):
                edu = ''.join(edu1[edu1.index(e)+1:])
                edu = edu.replace('\r', '')
                edu = edu.replace('\n', '')
                edu = edu.replace(' ', '')
        print(128, edu)
        # con = html.xpath('//div[@class="resumeb-head-con"]/ul/li/span/text()')
        # list_con = ['','','','','','']
        # for c in con:
        #     if re.search('男', c) or re.search('女', c):
        #         list_con[0] = c
        #     elif re.search('婚', c):
        #         list_con[1] = c
        #     elif re.search('岁', c):
        #         list_con[2] = c
        #     elif re.search('本科', c) or re.search('大专', c) or re.search('硕士', c) or re.search('MBA', c) or re.search('博士', c) or re.search('高中', c):
        #         list_con[3] = c
        #     elif re.search('国籍', c):
        #         list_con[4] = c
        #     elif re.search('群众', c) or re.search('党员', c) or re.search('团员', c) or re.search('派', c):
        #         list_con[5] = c
        # print(176, list_con)
        # contact = html.xpath('//div[@class="resumeb-head-contact"]/p/text()')
        # l_c = ['', '', '']
        # for t in range(len(contact)):
        #     l_c[t] = contact[t]
        # print(181, l_c)
        # resume = html.xpath('//dl[@class="resume-box"]/dd/p//text()')
        # print(183, resume)
        # l_r = ['', '', '', '', '', '', '']
        # l_r[-1] = resume[-1]
        # for r in range(len(resume)):
        #     if re.search('求职状态', resume[r]):
        #         l_r[0] = resume[r + 1]
        #     elif re.search('期望地点', resume[r]):
        #         l_r[1] = resume[r + 1]
        #     elif re.search('期望职位', resume[r]):
        #         l_r[2] = resume[r + 1]
        #     elif re.search('工作性质', resume[r]):
        #         l_r[3] = resume[r + 1]
        #     elif re.search('期望行业', resume[r]):
        #         l_r[4] = resume[r + 1]
        #     elif re.search('期望薪资', resume[r]):
        #         l_r[5] = resume[r + 1]
        # print(198, l_r)
        # edu = html.xpath('//div[@class="resume_detail_html"]/dl/dd//text()')
        # edu = ''.join(edu)
        item=CTeachersItem()
        item['name'] = name
        item['sex'] = sex
        item['marry'] = marry
        item['age'] = age
        item['academic'] = academic
        item['nation'] = nation
        item['politics'] = politics
        item['exper'] = exper
        item['addr'] = addr
        item['census'] = census
        item['job_status'] = job_status
        item['job_addr'] = job_addr
        item['job_p'] = job_p
        item['job_ind'] = job_ind
        item['job_salary'] = job_salary
        item['edu'] = edu
        item['job_exp'] = job_exp
        # #return item
        # print(65, position, addr)
        yield item # 由引擎将item交给pipeline
        # pass