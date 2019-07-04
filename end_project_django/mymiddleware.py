from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse
from info import models
import datetime


class Md1(MiddlewareMixin):
    def process_request(self, request):
        url = request.path
        if url.startswith('/favicon.ico'):
            return HttpResponse


class Md2(MiddlewareMixin):
    def process_request(self, request):
        now_time = datetime.datetime.now()
        host = request.META.get('REMOTE_ADDR')
        ret = models.InfoHostinfo.objects.filter(host=host).first()
        if ret:
            aa = now_time - ret.start_time
            if aa.seconds >= 60:
                ret.count = 1
                ret.start_time = now_time
                ret.is_lock = '2'
                ret.save()
                return None
            if aa.seconds < 60 and ret.is_lock == '1':
                return HttpResponse('登陆次数频繁，一分钟后再试')

            if ret.count < 4 and ret.is_lock == '2':
                if ret.count == 2:
                    ret.is_lock = '1'
                    ret.count = 0
                    ret.save()
                else:
                    ret.count += 1
                    ret.start_time = now_time
                    ret.save()
                return None

        else:
            models.InfoHostinfo.objects.create(host=host, start_time=now_time, count=1)
            return None
