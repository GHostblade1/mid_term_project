import re

from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse
from main.models import TUser
# Create your views here.
from user.captcha.image import ImageCaptcha
import random, string, hashlib
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from main import models
from mid_term_project import settings


def hash_code(name, now):
    """
    谁调此方法就为谁返回一个随机的验证码
    :param name:
    :param now:
    :return:
    """
    h = hashlib.md5()
    name += now
    h.update(name.encode())
    return h.hexdigest()


def make_confirm_string(new_user):
    """
    为用户生成随机验证码并将验证码保存在数据库中
    :param new_user:
    :return:
    """
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(32, new_user.id, new_user.password, new_user)
    code = hash_code(new_user.email_addr, now)
    models.Confirm_string.objects.create(code=code, user_id=new_user.id)
    print('35code', code)
    return code


def send_email(email, code):
    subject = 'python157'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/user/user_confirm/?code={}&user={}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1:8080', code, email)
    #发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    # 发送的html文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_confirm(request):
    """
    用户处理用户发起邮箱验证的请求
    :param request: 用户发来的验证码
    :return:
    """
    try:
        with transaction.atomic():
            user_code = request.GET.get('code')
            user = request.GET.get('user')
            confirm = models.Confirm_string.objects.get(code=user_code)
            if confirm:
                # 将用户状态改为可登陆
                request.session['user'] = user
                TUser.objects.filter(email_addr=user)[0].state = 1
                # 删除验证码
                return redirect('user:register_ok_re')
            else:
                #return redirect('user:register_ok')
                return HttpResponse('验证失败')
    except:
        print('出现异常！')
        return HttpResponse('<h1>邮箱验证异常</h1>'
                            '<a href="/user/register/">点击跳转回到注册界面！</a>')


def login(request):
    #request.session['register'] = 'ok'
    name1 = request.COOKIES.get('name')
    pwd1 = request.COOKIES.get('pwd')
    #request.session['html'] = 'index'
    #code = request.session.get('code')
    #print(74, code)
    if name1 != None:
        name1 = name1.encode('latin-1').decode('utf-8')
    if TUser.objects.filter(email_addr=name1, password=pwd1, state=1).count():
        request.session['user'] = name1
        #request.session['login'] = 'ok'
        res = redirect('main:index')
        if request.session.get('html') == 'index':
            res = redirect('main:index')
        elif request.session.get('html') == 'booklist':
            booklist_id1 = request.session.get('booklist_id1')
            booklist_id2 = request.session.get('booklist_id2')
            num = request.session.get('num')
            res = redirect('/book/booklist/?id1={}&id2={}&num={}'.format(booklist_id1, booklist_id2, num))
        elif request.session.get('html') == 'book_details':
            book_id = request.session.get('book_id')
            res = redirect('/book/book_details/?id={}'.format(book_id))
        elif request.session.get('html') == 'car_f':
            res = redirect('car:car_f')
        elif request.session.get('html') == None:
            res = redirect('main:index')
        return res
    return render(request, 'login.html')


def register(request):

    return render(request, 'register.html')


def register_ok(request):
    try:
        with transaction.atomic():
            email_addr = request.POST.get('txt_username')
            password1 = request.POST.get('txt_password')
            password2 = request.POST.get('txt_repassword')
            txt_vcode = request.POST.get('txt_vcode')
            txt_vcode1 = request.session.get('code')
            # email = request.POST.get('email')
            if TUser.objects.filter(email_addr=email_addr):
                return HttpResponse('该用户已存在')
            else:
                if password1 == password2 and txt_vcode.lower() == txt_vcode.lower():
                    request.session['user1'] = email_addr
                    h = hashlib.md5()
                    salt = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits, 3)
                    salt = ''.join(salt)
                    writing = password1+salt
                    h.update(writing.encode())
                    print(30, h.digest())
                    TUser.objects.create(email_addr=email_addr, password=password1, null_1=salt, null_2=h.digest(), state=0)
                    new_user = TUser.objects.filter(email_addr=email_addr, password=password1, null_1=salt, null_2=h.digest(), state=0)[0]
                    print(101, new_user)
                    code = make_confirm_string(new_user)
                    send_email(email_addr, code)
                    print('user117', '邮件发送成功！')
                    return render(request, 'register confirm.html')
                else:
                    return HttpResponse('两次输入的密码不一致')
    except:
        print('出现异常！')
        return HttpResponse('<h1>注册异常</h1>'
                            '<a href="/user/register/">点击跳转回到注册界面！</a>')

def login_logic(request):
    try:
        with transaction.atomic():
            name = request.POST.get('txtUsername')
            password = request.POST.get('txtPassword')
            autologin = request.POST.get('autologin')
            txt_vcode1 = request.POST.get('txt_vcode')
            txt_vcode2 = request.session.get('code')
            print('user134', txt_vcode2, txt_vcode1)
            #print(48, autologin)
            #print(24, name, type(name), password)
            user = TUser.objects.filter(email_addr=name)[0]
            salt = user.null_1
            user_password = user.null_2
            print('user140', user_password, type(user_password))
            h = hashlib.md5()
            writing = password + salt
            h.update(writing.encode())
            print('user144', str(h.digest()), type(h.digest()))
            #print(26, user)
            print(126, request.session.get('html'))
            if user:
                if str(h.digest()) == user_password and txt_vcode1.lower() == txt_vcode2.lower():
                    request.session['login'] = 'ok'
                    request.session['user'] = name
                    res = redirect('main:index')
                    if request.session.get('html') == 'index':
                        res = redirect('main:index')
                    elif request.session.get('html') == 'booklist':
                        booklist_id1 = request.session.get('booklist_id1')
                        booklist_id2 = request.session.get('booklist_id2')
                        num = request.session.get('num')
                        res = redirect('/book/booklist/?id1={}&id2={}&num={}'.format(booklist_id1, booklist_id2, num))
                    elif request.session.get('html') == 'book_details':
                        book_id = request.session.get('book_id')
                        res = redirect('/book/book_details/?id={}'.format(book_id))
                    elif request.session.get('html') == 'car_f':
                        res = redirect('car:car_f')
                    elif request.session.get('html') == None:
                        res = redirect('main:index')
                    #if request.POST.get('cookie'):
                    name = name.encode('utf-8').decode('latin-1')
                    if autologin:
                        res.set_cookie('name', name, max_age=7 * 24 * 3600)
                        res.set_cookie('pwd', password, max_age=7 * 24 * 3600)
                    return res
                else:
                    return HttpResponse('账号密码错误！')
            else:
                return HttpResponse('账号错误')
    except:
        print('出现异常！')
        return HttpResponse('<h1>请输入正确的邮箱密码</h1>'
                            '<a href="/user/login/">点击跳转回到注册界面！</a>')


def reg_check_name(request):
    name = request.GET.get('name')
    #print(46, name)
    user = TUser.objects.filter(email_addr=name)

    def verifyEmail(email):
        pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'

        if re.match(pattern, email) is not None:
            return 1
        else:
            return 0
    if user:
        return HttpResponse('1')
    else:
        if verifyEmail(name):
            return HttpResponse('2')
        else:
            return HttpResponse('0')


def check_pwd(request):
    pwd = request.GET.get('pwd')
    #print(56, pwd)
    if (pwd.isdigit or pwd.isalpha) and len(pwd) <= 4:
        return HttpResponse('1')
    elif 8 > len(pwd) > 4 and (pwd.isdigit or pwd.isalpha):
        return HttpResponse('2')
    else:
        return HttpResponse('3')


def get_captcha(request):
    #request.session['captcha'] = 'ok'
    image = ImageCaptcha()
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits, 3)
    random_code = "".join(code)
    request.session['code'] = random_code
    data = image.generate(random_code)
    print(73, random_code)
    return HttpResponse(data, "image/png")


def quit(request):
    request.session['login'] = None
    request.session['user'] = None
    request.session['cart'] = None
    return HttpResponse('0')


def check_pwd_name(request):
    name = request.GET.get('name')
    pwd = request.GET.get('pwd')
    print(110, name, pwd)
    if TUser.objects.filter(email_addr=name, password=pwd):
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def register_ok_re(request):
    user = request.session.get('user1')
    state = '1' if user else '0'
    return render(request, 'register ok.html', {'state': state, 'user': user})


def check_captcha(request):
    code1 = request.session.get('code')
    code2 = request.GET.get('code')
    print(211, code1, code2)
    if code1.lower() == code2.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')