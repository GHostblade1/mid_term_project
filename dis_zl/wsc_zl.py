from wsc_spider import WscSpider, MyResponse, Db
db = Db()
url = 'https://fe-api.zhaopin.com/c/i/sou'
params = '''start: 0
pageSize: 90
cityId: 538
workExperience: -1
education: -1
companyType: -1
employmentType: -1
jobWelfareTag: -1
kw: 爬虫
kt: 3
_v: 0.96604045
x-zp-page-request-id: 00f9f0ef6b664f1481e911f15f6f212b-1560240487911-578524
x-zp-client-id: b787921d-2fc4-4db2-e1aa-b0f485be5319'''
params = WscSpider.get_dict_from_params(params)

proxy = ''
# a = MyResponse(wsc_spider.get(url=url, params=params).text).json
# print(a)
for kw in ['AI', '爬虫', '数据挖掘与数据分析', '大数据', 'web开发']:
    for city in [682, 622, 765, 763, 530, 538, 531, 801, 653, 736, 600, 613, 635, 702, 703, 639,599, 854, 719, 749, 551, 654, 681, 565, 664, 773]:
        start = 0
        while True:
            print(26, params['kw'])
            params['kw'] = kw
            params['cityId'] = str(city)
            params['start'] = str(start)
            print(params)
            urls = [data['positionURL'] for data in MyResponse(WscSpider.get(url=url, params=params).text).json['data']['results']]
            count = MyResponse(WscSpider.get(url=url, params=params).text).json['data']['count']
            print(33, count)
            resps = WscSpider.gets(urls)
            # print(urls)
            nums = 0
            for resp in resps:
                #print(resp.text)
                nums += 1
                try:
                    title = resp.get_element_from_xpath('//title/text()')
                    position = resp.get_element_from_xpath('//h3[@class="summary-plane__title"]/text()')
                    salary = resp.get_element_from_xpath('//span[@class="summary-plane__salary"]/text()')
                    addr = resp.get_element_from_xpath('//span[@class ="job-address__content-text"]//text()')
                    company = resp.get_element_from_xpath('//a[@class ="company__title"]//text()')
                    print(title)
                    items = {'title': title, 'position': position, 'salary': salary, 'addr': addr, 'company': company}
                    db.storage(items)
                    print(kw, city, nums, '存储成功！')
                except:
                    print(kw, city, nums, '该条存储失败！')
            start += 90
            print(50, start)
            if start >= count:
                break