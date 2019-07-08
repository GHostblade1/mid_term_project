from django.shortcuts import render
from info.models import TInfo, TLog
from django.core.paginator import Paginator
from lxml import etree
import requests, time
# Create your views here.
def trace_func(func):
    '''''
    A decorate function to track all function invoke information with DEBUG level
    Usage:
    @trace_func
    def any_function(any parametet)
    '''
    def tmp(*args, **kargs):
        t = time.strftime("%Y-%m-%d %X",time.localtime())
        print(15, args[0].META)
        ip = args[0].META['REMOTE_ADDR']
        print(18, '本次访问的ip为', ip)
        path = args[0].META['PATH_INFO']
        print(16, ip)
        if ip != '127.0.0.1':
            url = 'https://www.baidu.com/s?wd='+ip
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Cookie': 'BAIDUID=BCF318849C9AA39E69B487FC7E8CA0A8:FG=1; BIDUPSID=BCF318849C9AA39E69B487FC7E8CA0A8; PSTM=1559737821; BD_UPN=12314753; BDUSS=93OURHTHR2a1Vrdk95bVhiaUFLWExuZzBPZm9Mb3p2VFJ6YU56SkNrTEdielpkSUFBQUFBJCQAAAAAAAAAAAEAAAAJ2HdUs8e9x73WtcTQoba5trkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMbiDl3G4g5dWm; BDSFRCVID=lkCOJeC627XtFwjwX0SCEXY-EeK2T1JTH6aoYpgM1phwS3wDBiyVEG0PjU8g0KubLClVogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJkO_D-2JCD3f-op-P__jj_qhUKX5-RLfK8Hbp7F5l8-hlONjbQ83b-RDbbD0lvkHmT-aKomtlcxOKQphPn2qfIf3tc-5lJf-HTNBIbN3KJmOhC9bT3v5tD7jfcl2-biWbRL2MbdbDnP_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDFKhItle5tKD5PW5ptXt6oL26LX3b7EfbROEp7_bf--D6-R5-jfaJbvtN7mKxnwHl5qOIo2Df6xy5K_hnrjKMuD-IbfbKO53poEJfQHQT3mMlQbbN3i-4jr0KJpWb3cWKJV8UbS567PBTD02-nBat-OQ6npaJ5nJq5nhMtRy66jK4JKjGKJt6bP; H_PS_PSSID=1430_21080_18560_29135_29237_28518_29098_28835_29220_29439; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_645EC=6193qXdMbLxoWW63lpR9o1od1jOJpmeU%2BSs%2FHtokKBofVMxWRsKMt4JqCpE; BDSVRTM=248',
                'Host': 'www.baidu.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            }
            #url = 'https://www.baidu.com/s?wd=' + '172.15.10.11'
            try:
                res = requests.get(url=url, headers=headers).text
                #print(res)
                html = etree.HTML(res)
                node = html.xpath('//div[@class="c-span21 c-span-last op-ip-detail"]/table//text()')
                print(37, '地点', node)
            
                node1 = node[-1:]
                node1[0] = node1[0].replace(' ', '')
                node1[0] = node1[0].replace('\t', '')
                node1[0] = node1[0].replace('\n', '')
                addr = node1[0]
            except:
                print(45, '---地点未捕获---')
                addr = '未知'
        else:
            addr = '本地'
        a = '{}-在时间-{}-地点-{}-访问了-{}-url-{}'.format(ip, t, addr, func.__name__, path)
        TLog.objects.create(ip=ip, time=t, addr=addr, func=func.__name__, url=path)
        print(a)
        return func(*args, **kargs)
    return tmp


@trace_func
def main(rquest):
    return render(rquest, 'main.html')


@trace_func
def intro(request):
    return render(request, 'introduce.html')


@trace_func
def menu(request):
    num = request.GET.get('num')
    city = request.GET.get('city')
    position = request.GET.get('position')
    kw = request.GET.get('kw')
    se = request.GET.get('se')
    print(city, position, kw, str(se), se)
    if num == 'None' or num == None:
        num = 1
    if kw == None or kw == '':
        infos = TInfo.objects.filter(job_addr__icontains=city, job_p__icontains=position)
    else:
        if se == None or se == '':
            infos = TInfo.objects.filter(job_addr__icontains=city, job_p__icontains=position, name__icontains=kw)
        else:
            if se == 'city':
                infos = TInfo.objects.filter(job_addr__icontains=kw)
            else:
                infos = TInfo.objects.filter(job_p__icontains=kw)
    pagtor = Paginator(infos, per_page=10)
    page = pagtor.page(str(num))
    return render(request, 'menu.html', {'page': page, 'city': city, 'position': position})
