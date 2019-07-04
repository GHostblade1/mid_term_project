from BFS import DFS
from ip代理池 import Pool
import requests
import json
from lxml import etree
import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='zl_zhaopin', port=3306, charset='utf8')
cursor = conn.cursor()
url = 'http://search.jiayuan.com/v2/search_v2.php'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'guider_quick_search=on; SESSION_HASH=a087db0efda0a43d75b2ee098ae75bccbe3a6d06; accessID=20190613191144830242; PHPSESSID=3e96e78a510570933caaa5b94bd401bc; main_search:212244111=%7C%7C%7C00; is_searchv2=1; user_access=1; save_jy_login_name=18366106164; stadate1=149141826; myloc=37%7C3702; myage=26; PROFILE=150141826%3AHADES%3Am%3Aat3.jyimg.com%2Fe2%2Fd8%2F53e775f22739e6b5c8718d286a83%3A1%3A%3A1%3A53e775f22_3_avatar_p.jpg%3A1%3A1%3A50%3A10%3A4.0; mysex=m; myuid=149141826; myincome=20; mylevel=2; COMMON_HASH=e253e775f22739e6b5c8718d286a83d8; sl_jumper=%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2018-12-25; last_login_time=1560424984; upt=Geb0%2AkRZUXjI%2AX81xcoJ-CG7wp7w5OlDJX-skTYssBqBYg8qjj1jHtZL52H4pa12YstAraW3op1wFfUxiEssHS73cAs.; user_attr=000000; main_search:150141826=%7C%7C%7C00; RAW_HASH=3KdY2Ouj7omCnw7VQfsRciADwe2h6qKXn95fZpYqEgMADqBIuYfC2uCKLMKt3labG71H5lF8ZKq-hE5oQs%2AVwRpJPkP3hbV4Cka2HqI-%2A72Gk4Y.; pop_time=1560425352739',
    'Host': 'search.jiayuan.com',
    'Origin': 'http://search.jiayuan.com',
    'Referer': 'http://search.jiayuan.com/v2/index.php?key=&sex=f&stc=2:18.30,3:165.175,23:1,1:11&sn=default&sv=1&p=1&pt=5190&ft=off&f=select&mt=d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
formdata = {
    'sex': 'f',
    'key':'',
    'stc': '2:18.30,3:165.175,1:11,23:1',
    'sn': 'default',
    'sv': '1',
    'p': '4',
    'f': 'select',
    'listStyle': 'bigPhoto',
    'pri_uid': '150141826',
    'jsversion': 'v5',
    }
# pool = Pool(20)
# ip = pool.get_ip()
cookies = {
    'SESSION_HASH':'a087db0efda0a43d75b2ee098ae75bccbe3a6d06',
    'accessID':'20190613191144830242',
    'ip_loc':'11',
    'PHPSESSID':'7d4775d3cd0b91c76f003a4a4a3d1146',
    'main_search:212244111':'%7C%7C%7C00',
    'is_searchv2':'1',
    'user_access':'1',
    'save_jy_login_name':'18366106164',
    'stadate1':'149141826',
    'myloc':'37%7C3702',
    'myage':'26',
    'PROFILE':'150141826%3AHADES%3Am%3Aat3.jyimg.com%2Fe2%2Fd8%2F53e775f22739e6b5c8718d286a83%3A1%3A%3A1%3A53e775f22_3_avatar_p.jpg%3A1%3A1%3A50%3A10%3A4.0',
    'mysex':'m',
    'myuid':'149141826',
    'myincome':'20',
    'mylevel':'2',
    'COMMON_HASH':'e253e775f22739e6b5c8718d286a83d8',
    'last_login_time':'1560424984',
    'upt':'Geb0%2AkRZUXjI%2AX81xcoJ-CG7wp7w5OlDJX-skTYssBqBYg8qjj1jHtZL52H4pa12YstAraW3op1wFfUxiEssHS73cAs.',
    'user_attr':'000000',
    'main_search':'150141826=%7C%7C%7C00',
    'RAW_HASH':'3KdY2Ouj7omCnw7VQfsRciADwe2h6qKXn95fZpYqEgMADqBIuYfC2uCKLMKt3labG71H5lF8ZKq-hE5oQs%2AVwRpJPkP3hbV4Cka2HqI-%2A72Gk4Y.',
    'pop_time':'1560430461739'
    }
start = 510
while True:
    formdata['p'] = start
    text = requests.post(url=url, data=formdata).text[11:-13]
    datas = json.loads(text)['userInfo']
    #print(datas)
    for i in datas:
        url_details = 'http://www.jiayuan.com/'+str(i['realUid'])
        text = requests.get(url_details, cookies=cookies).text
        html = etree.HTML(text)
        title = html.xpath('//title//text()')
        name = html.xpath('//h4//text()')
        member_info = html.xpath('//div[@class="member_info_r yh"]//text()')
        member_info1 = []
        for i in member_info:
            if '\t' in i or '\n' in i:
                continue
            else:
                member_info1.append(i)
        member_info = member_info1
        infor = html.xpath('//div[@class="js_text"]//text()')
        print(67, title)
        #print(68, name)
        #print(69, member_info)
        #print(70, infor)
        inser_sql = 'insert into t_sjjy (title, name, member_info, infor) values (%s,%s,%s,%s)'
        cursor.execute(inser_sql, [str(title), str(name), str(member_info), str(infor)])
        conn.commit()
        start += 1
    with open('sjjy_start.txt', 'w')as w:
      w.write(str(start))