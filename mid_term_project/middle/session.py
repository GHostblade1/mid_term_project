from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class MyMiddleAware(MiddlewareMixin):
    def process_request(self, request):
        if 'login' not in request.path:
            print('登录验证')
            session = request.session
            if session.get('login'):
                print('已登录')
            else:
                if session.get('captcha'):
                    print('验证码')
                else:
                    # if session.get('register'):
                    #     print('注册')
                    #     return redirect('user:register')
                    print('未登录')
                    return redirect('user:login')

    def process_response(self, request, response):
        print('response', request, response)
        return response