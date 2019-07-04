import time
from urllib import parse
from lxml import etree

from boss_spiders.wsc_spider import WscSpider, MyResponse, Db
db = Db()
url = 'https://www.zhipin.com/c101010100/'
params = {'query': '爬虫', 'page': '1', 'ka': 'page-next'}
#params = WscSpider.get_dict_from_params(params)
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'sid=sem; toUrl=/; __g=sem; lastCity=101010100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1561082535,1561082567; __c=1561082567; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D5u_-dqcCl1A5qJ1A834PR6FH-CLc-cEqKnioVC8bM8d3E6hlwgLcAg3iNEiuSltR%26wd%3D%26eqid%3Dfca5a35400002d35000000035d0c3a9e&l=%2Fwww.zhipin.com%2F&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26utm_source%3Dbaidu%26utm_medium%3Dcpc%26utm_campaign%3DPC-yixian-pinpaici-2C%26utm_content%3DBOSSzhipin-hexin%26utm_term%3DBOSSzhipinwangz; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1561083258; __a=73534768.1561082533.1561082533.1561082567.14.2.13.14',
}

proxy = ''
# proxy = 'http://183.129.207.89:28087'
# a = MyResponse(wsc_spider.get(url=url, params=params).text).json
# print(a)
for kw in ['人工智能', 'python开发', '大数据', 'web开发', '数据挖掘与数据分析', 'AI', '爬虫']:
    for start in range(1, 10):
        print('----------------------'+str(start)+'-----------------------')
        #time.sleep(2)
        params['query'] = kw
        params['page'] = str(start)
        url = 'https://www.zhipin.com/c101010100/?query='+parse.quote(kw)+'&page='+str(start)+'&ka=page-next'
        print(url)
        req = WscSpider.get(url=url, headers=headers, proxy=proxy)
        text = req.text
        print(22, text)
        html = etree.HTML(text)
        urls = []
        for url in html.xpath('//ul/li/div/div/h3/a/@href'):
            print(20, url)
            urls.append('https://www.zhipin.com/'+url)
        resps = WscSpider.gets(urls, headers=headers, proxy=proxy)
        # print(urls)
        nums = 0
        for resp in resps:
            #print(resp.text)
            nums += 1
            html2 = etree.HTML(resp.text)
            try:
                title = html2.xpath('//title/text()')[0]
                print(22, title)
                salary = html2.xpath('//div[@class="name"]/span[@class="salary"]/text()')[0]
                print(24, salary)
                company = html2.xpath('//div[@class="company-info"]/a/@title')[0]
                print(27, company)
                position = html2.xpath('//div[@class="name"]/h1/text()')[0]
                print(28, position)
                items = {'title': title, 'position': position, 'salary': salary, 'company': company}
                db.storage(items)
                print(kw, nums, '存储成功！')
            except:
                print(kw, nums, '该条存储失败！')
