import scrapy, re
import json, time
from fake_useragent import UserAgent
from lxml import etree

from ..items import EndItemZlgItem
from urllib import parse
# scrapy.Spider 所有spider都要继承这个类
class ZhiLianSpider(scrapy.Spider):
    name = 'zpg'  # 区分spider
    #start_urls=['http://www.baidu.com'] # 起始urls
    # 起始请求 携带参数，cookie，headers，proxy
    count1 = 0
    data = {
        'pageSize': '1',
        'pageNo': '25',
        'keyStr': '',
        'companyName': '',
        'schoolName': '',
        'keyStrPostion': '',
        'postionStr': '',
        'startDegrees': '-1',
        'endDegress': '-1',
        'startAge': '0',
        'endAge': '0',
        'gender': '-1',
        'region': '',
        'timeType': '-1',
        'startWorkYear': '-1',
        'endWorkYear': '-1',
        'beginTime': '',
        'endTime': '',
        'isMember': '-1',
        'hopeAdressStr': '',
        'cityId': '1',
        'updateTime': '',
        'tradeId': '',
        'startDegreesName': '',
        'endDegreesName': '',
        'tradeNameStr': '',
        'regionName': '',
        'isC': '0',
        'is211_985_school': '0',
        'clientNo': '',
        'userToken': '9B1D96E588F1D1E6AE1DD878EDA08AC5',
        'clientType': '2'
    }
    headers = {
        'Host': 'qiye.zhaopingou.com',
        'Origin': 'https://qiye.zhaopingou.com',
        'Accept': 'multipart/form-data',
        'Accept - Encoding': 'gzip,deflate, br',
        'Accept - Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content - Length': '438',
        'Content - type': 'application/x-www-form-urlencoded',
        'Referer': 'https://qiye.zhaopingou.com/resume?pn=4',
        'Cookie': 'JSESSIONID=02E1D93523EFEDC6B7CC67E9E6F804CD; certCode=0b82c41812144cd2b1fc29a91e8a73c7; Hm_lvt_b025367b7ecea68f5a43655f7540e177=1561347111,1561445524; rd_apply_lastsession_code=2; hrkeepToken=9B1D96E588F1D1E6AE1DD878EDA08AC5; zhaopingou_account=15315017485; zhaopingou_login_callback=/; JSESSIONID=5F7D0F39724210203B5047796D6A909D; Hm_lpvt_b025367b7ecea68f5a43655f7540e177=1561445564; zhaopingou_select_city=-1; zhaopingou_htm_cookie_register_userName=; zhaopingou_htm_cookie_newDay=2019-06-25',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    ua = UserAgent()
    data3 = {}
    def start_requests(self):
        # 请求如果没有全部发出去，后续请求都不会发
        data1 = {
            'pageSize': '1',
            'pageNo': '25',
            'keyStr': '',
            'companyName': '',
            'schoolName': '',
            'keyStrPostion': '',
            'postionStr': '',
            'startDegrees': '-1',
            'endDegress': '-1',
            'startAge': '0',
            'endAge': '0',
            'gender': '-1',
            'region': '',
            'timeType': '-1',
            'startWorkYear': '-1',
            'endWorkYear': '-1',
            'beginTime': '',
            'endTime': '',
            'isMember': '-1',
            'hopeAdressStr': '',
            'cityId': '1',
            'updateTime': '',
            'tradeId': '',
            'startDegreesName': '',
            'endDegreesName': '',
            'tradeNameStr': '',
            'regionName': '',
            'isC': '0',
            'is211_985_school': '0',
            'clientNo': '',
            'userToken': '9B1D96E588F1D1E6AE1DD878EDA08AC5',
            'clientType': '2'
        }
        with open(r'F:\real_python\git_project\end_item_zlg\end_item_zlg\GB2312汉字.txt','r') as g:
            kws = g.read()
        for p in kws:
            data1['keyStr'] = p
            self.headers['User-Agent'] = self.ua.random
            self.data3 = data1
            url = 'https://qiye.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new?timestamp='+str(time.time())[:14].replace('.','')
            yield scrapy.FormRequest(url, headers=self.headers, formdata=data1)  # 可以return 返回，也可以使用yield将方法变成生成器，由引擎交给调度器
    # 回调函数(解析列表页响应)，接收请求对应的响应
    def parse(self, response):
        # text=response.text # 获取文本数据
        #response.body# 二进制流
        #title=response.xpath('//title/text()').extract() #返回一个列表，列表中是节点对象  .extract()获得节点对象中的数据
        # print(text)
        #print(23, response.text)
        print(114, response.text)
        data2 = {
            'resumeHtmlId': '6877457',
            'keyStr':'',
            'keyPositionName':'',
            'tradeId':'',
            'postionStr':'',
            'jobId': '0',
            'companyName':'',
            'schoolName':'',
            'clientNo':'',
            'userToken': '9B1D96E588F1D1E6AE1DD878EDA08AC5',
            'clientType': '2'
        }
        data = json.loads(response.text)
        print(126, data)
        count = data['total']
        datas = data['warehouseList']
        for d in datas:
            time.sleep(2)
            self.headers['Referer'] = 'https://qiye.zhaopingou.com/resume/detail?resumeId='+str(d['resumeHtmlId'])
            data2['resumeHtmlId'] = str(d['resumeHtmlId'])
            url = 'https://qiye.zhaopingou.com/zhaopingou_interface/zpg_find_resume_html_details?timestamp='+str(time.time())[:14].replace('.','')
            yield scrapy.FormRequest(url=url, headers=self.headers, formdata=data2, callback=self.pares1)
        self.count1 += 1
        if self.count1*25 + 25 < count:
            self.data3['pageSize'] = str(self.count1)
            url2 = 'https://qiye.zhaopingou.com/zhaopingou_interface/find_warehouse_by_position_new?timestamp='+str(time.time())[:14].replace('.','')
            yield scrapy.FormRequest(url=url2, headers=self.headers, formdata=self.data3)
        else:
            self.count1 = 0
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
        print(156, resp.text)
        result = json.loads(resp.text)
        print(156, result)
        text = result['jsonHtml']
        html = etree.HTML(text)
        name = html.xpath('//div[@class="resumeb-head-top"]/h2/text()')[0]
        print(160, name)
        con = html.xpath('//div[@class="resumeb-head-con"]/ul/li/span/text()')
        list_con = ['','','','','','']
        for c in con:
            if re.search('男', c) or re.search('女', c):
                list_con[0] = c
            elif re.search('婚', c):
                list_con[1] = c
            elif re.search('岁', c):
                list_con[2] = c
            elif re.search('本科', c) or re.search('大专', c) or re.search('硕士', c) or re.search('MBA', c) or re.search('博士', c) or re.search('高中', c):
                list_con[3] = c
            elif re.search('国籍', c):
                list_con[4] = c
            elif re.search('群众', c) or re.search('党员', c) or re.search('团员', c) or re.search('派', c):
                list_con[5] = c
        print(176, list_con)
        contact = html.xpath('//div[@class="resumeb-head-contact"]/p/text()')
        l_c = ['', '', '']
        for t in range(len(contact)):
            l_c[t] = contact[t]
        print(181, l_c)
        resume = html.xpath('//dl[@class="resume-box"]/dd/p//text()')
        print(183, resume)
        l_r = ['', '', '', '', '', '', '']
        l_r[-1] = resume[-1]
        for r in range(len(resume)):
            if re.search('求职状态', resume[r]):
                l_r[0] = resume[r + 1]
            elif re.search('期望地点', resume[r]):
                l_r[1] = resume[r + 1]
            elif re.search('期望职位', resume[r]):
                l_r[2] = resume[r + 1]
            elif re.search('工作性质', resume[r]):
                l_r[3] = resume[r + 1]
            elif re.search('期望行业', resume[r]):
                l_r[4] = resume[r + 1]
            elif re.search('期望薪资', resume[r]):
                l_r[5] = resume[r + 1]
        print(198, l_r)
        edu = html.xpath('//div[@class="resume_detail_html"]/dl/dd//text()')
        edu = ''.join(edu)
        item=EndItemZlgItem()
        item['name'] = name
        item['sex'] = list_con[0]
        item['marry'] = list_con[1]
        item['age'] = list_con[2]
        item['academic'] = list_con[3]
        item['nation'] = list_con[4]
        item['politics'] = list_con[5]
        item['exper'] = l_c[0]
        item['addr'] = l_c[1]
        item['census'] = l_c[2]
        item['job_status'] = l_r[0]
        item['job_addr'] = l_r[1]
        item['job_p'] = l_r[2]
        item['job_ind'] = l_r[4]
        item['job_salary'] = l_r[5]
        item['edu'] = edu
        item['job_exp'] = l_r[3]
        # #return item
        # print(65, position, addr)
        yield item # 由引擎将item交给pipeline
        # pass