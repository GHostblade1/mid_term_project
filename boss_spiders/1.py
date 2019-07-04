import MySQLdb
import requests
from lxml import etree
conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='crawler', port=3306,charset='utf8')
cursor = conn.cursor()
url = 'https://www.zhipin.com/c101010100/'
params = {'query': '爬虫', 'page': '1', 'ka': 'page-next'}
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'sid=sem; toUrl=/; __g=sem; lastCity=101010100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1561082535,1561082567; __c=1561082567; __l=r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D5u_-dqcCl1A5qJ1A834PR6FH-CLc-cEqKnioVC8bM8d3E6hlwgLcAg3iNEiuSltR%26wd%3D%26eqid%3Dfca5a35400002d35000000035d0c3a9e&l=%2Fwww.zhipin.com%2F&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26utm_source%3Dbaidu%26utm_medium%3Dcpc%26utm_campaign%3DPC-yixian-pinpaici-2C%26utm_content%3DBOSSzhipin-hexin%26utm_term%3DBOSSzhipinwangz; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1561083258; __a=73534768.1561082533.1561082533.1561082567.14.2.13.14',
}
#proxy ={'http': '47.107.190.212:8118'}
for q in ['AI', '大数据', '爬虫']:
    params['query'] = q
    for p in range(9):
        params['page'] = str(p)
        text = requests.get(url=url, params=params, headers=headers).text
        html = etree.HTML(text)
        #print(text)
        nodes = html.xpath('//ul/li/div/div/h3/a/@href')
        for n in nodes:
            url = 'https://www.zhipin.com'+n
            text1 = requests.get(url=url, headers=headers).text
            html1 = etree.HTML(text1)
            try:
                title = html1.xpath('//title/text()')[0]
                print(22, title)
                salary = html1.xpath('//div[@class="name"]/span[@class="salary"]/text()')[0]
                print(24, salary)
                company = html1.xpath('//div[@class="company-info"]/a/@title')[0]
                print(27, company)
                position = html1.xpath('//div[@class="name"]/h1/text()')[0]
                print(28, position)
                sql = "insert into t_boss (title,salary,company,position) values(%s, %s, %s, %s)"
                cursor.execute(sql, [title, salary, company, position])
                conn.commit()
            except:
                print('该条采集失败！')
