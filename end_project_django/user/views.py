from django.shortcuts import render, redirect, HttpResponse
import re, time, requests, os, base64
from info.models import TUser, TLog
from lxml import etree
from geetest import GeetestLib
from django.contrib import auth
from django.http import JsonResponse
#from django.shortcuts import render
# Create your views here.
def trace_func(func):
    '''''
    A decorate function to track all function invoke information with DEBUG level
    Usage:
    @trace_func
    def any_function(any parametet)
    '''

    def tmp(*args, **kargs):
        t = time.strftime("%Y-%m-%d %X", time.localtime())
        print(15, args[0].META)
        ip = args[0].META['REMOTE_ADDR']
        print(18, '本次访问的ip为', ip)
        path = args[0].META['PATH_INFO']
        print(16, ip)
        if ip != '127.0.0.1':
            url = 'https://www.baidu.com/s?wd=' + ip
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
            # url = 'https://www.baidu.com/s?wd=' + '172.15.10.11'
            try:
                res = requests.get(url=url, headers=headers).text
                # print(res)
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
def login(request):
    
    return render(request, 'login.html')


@trace_func
def register(request):
    
    return render(request, 'register.html')


@trace_func
def login_logic(request):
    name = request.POST.get('userid')
    pwd = request.POST.get('psw')
    result = TUser.objects.filter(name=name, password=pwd)
    if result:
        return redirect('info:main')
    else:
        return redirect('user:login')


@trace_func
def register_logic(request):
    
    return redirect('user:login')


@trace_func
def re_check_name(request):
    name = request.GET.get('name')
    if name[0].isdigit():
        return HttpResponse('0')
    else:

        if re.match('^\S{1,16}$', name):
            return HttpResponse('1')
        else:
            return HttpResponse('0')


@trace_func
def re_check_phone(request):
    phone = request.GET.get('user_phone')
    if re.match('^1\d{1,11}$', phone):
        return HttpResponse('1')
    else:
        return HttpResponse('0')


@trace_func
def re_check_pwd(request):
    user_pwd = request.GET.get('user_pwd')
    print(54, user_pwd)
    if re.search('[A-Z]', user_pwd) and re.search('[a-z]', user_pwd):
        print(56, '成功')
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def login_code(request):
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)  # 将登录用户赋值给 request.user
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login.html")
# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


# 处理极验 获取验证码的视图
def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)



def loginFaceCheck(request):

    ## 人脸登陆验证

    if request.method == "POST" and request.is_ajax():
        # 获取base64格式的图片
        faceImage = request.POST.get('faceImg')
        # 提取出base64格式，并进行转换为图片
        index = faceImage.find('base64,')
        base64Str = faceImage[index+6:]
        img = base64.b64decode(base64Str)
        # 将文件保存
        backupDate = time.strftime("%Y%m%d_%H%M%S")
        if int(request.POST.get('id')) == 0 :
            fileName = BASE_LOGIN_LEFT_PATH +"LeftImg_%s.jpg" % (backupDate)
        else:
            fileName = BASE_LOGIN_RIGHT_PATH + "RightImg_%s.jpg" % (backupDate)
        file = open(fileName, 'wb')
        file.write(img)
        file.close()
        # 删除多余的图片
        filesLeft = os.listdir(BASE_LOGIN_LEFT_PATH)
        filesLeft.sort()
        leftImgCount = filesLeft.__len__()
        filesRight = os.listdir(BASE_LOGIN_RIGHT_PATH)
        filesRight.sort()
        RightImgCount = filesRight.__len__()

        if leftImgCount > 100:
            # 图片超过100个，删除一个
            os.unlink(BASE_LOGIN_LEFT_PATH +filesLeft[0])
        if RightImgCount > 100:
            # 图片超过100个，删除一个
            os.unlink(BASE_LOGIN_RIGHT_PATH + filesRight[0])

        # 对图片进行人脸识别比对
        canLogin = False
        AuthName = "未授权用户"

        # 1> 加载相机刚拍摄的人脸
        unknown_face = face_recognition.load_image_file(fileName)
        unknown_face_tmp_encoding = []
        try:
            unknown_face_tmp_encoding = face_recognition.face_encodings(unknown_face)[0]
        except IndexError:
            canLogin = False  # 图片中未发现人脸

        # 2> 进行比对

        ### 第一种方法
        # results = face_recognition.face_distance(known_face,unknown_face_tmp_encoding)
        # 小于0.6即对比成功。但是效果不好，因此我们设置阈值为0.4,
        # for i, face_distance in enumerate(results):
        #     if face_distance <= 0.4:
        #         canLogin = True
        #         AuthName = os.listdir(BASE_LOGIN_AUTH_PATH)[i][:-4]

        ### 第二中方法
        results1 = face_recognition.compare_faces(known_face,unknown_face_tmp_encoding,0.4)
        for i, face_distance in enumerate(results1):
            if face_distance == True:
                canLogin = True
                AuthName = os.listdir(BASE_LOGIN_AUTH_PATH)[i][:-4]

        JsonBackInfo = {
            "canLogin": canLogin,
            "AuthName": AuthName
        }

        return JsonResponse(JsonBackInfo)