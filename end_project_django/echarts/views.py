from django.shortcuts import render
from info.models import TInfo
# Create your views here.



def f_bar(request):
    bj = TInfo.objects.filter(job_addr__icontains='北京').count()
    sh = TInfo.objects.filter(job_addr__icontains='上海').count()
    sz = TInfo.objects.filter(job_addr__icontains='深圳').count()
    gz = TInfo.objects.filter(job_addr__icontains='广州').count()
    return render(request, 'echats/bar.html', {'bj': bj, 'sh': sh, 'sz': sz, 'gz': gz})


def broken_line(request):
    bj = TInfo.objects.filter(job_addr__icontains='北京').count()
    sh = TInfo.objects.filter(job_addr__icontains='上海').count()
    sz = TInfo.objects.filter(job_addr__icontains='深圳').count()
    gz = TInfo.objects.filter(job_addr__icontains='广州').count()
    return render(request, 'echats/broken_line.html', {'bj': bj, 'sh': sh, 'sz': sz, 'gz': gz})


def f_map(request):
    bj = TInfo.objects.filter(job_addr__icontains='北京').count()
    sh = TInfo.objects.filter(job_addr__icontains='上海').count()
    sz = TInfo.objects.filter(job_addr__icontains='深圳').count()
    gz = TInfo.objects.filter(job_addr__icontains='广州').count()
    tj = TInfo.objects.filter(job_addr__icontains='天津').count()
    cq = TInfo.objects.filter(job_addr__icontains='重庆').count()
    hb = TInfo.objects.filter(job_addr__icontains='河北').count()
    sx = TInfo.objects.filter(job_addr__icontains='山西').count()
    ln = TInfo.objects.filter(job_addr__icontains='辽宁').count()
    jl = TInfo.objects.filter(job_addr__icontains='吉林').count()
    hlj = TInfo.objects.filter(job_addr__icontains='黑龙江').count()
    js = TInfo.objects.filter(job_addr__icontains='江苏').count()
    zj = TInfo.objects.filter(job_addr__icontains='浙江').count()
    ah = TInfo.objects.filter(job_addr__icontains='安徽').count()
    fj = TInfo.objects.filter(job_addr__icontains='福建').count()
    jx = TInfo.objects.filter(job_addr__icontains='江西').count()
    sd = TInfo.objects.filter(job_addr__icontains='山东').count()
    hn = TInfo.objects.filter(job_addr__icontains='河南').count()
    hn2 = TInfo.objects.filter(job_addr__icontains='海南').count()
    sc = TInfo.objects.filter(job_addr__icontains='四川').count()
    gz2 = TInfo.objects.filter(job_addr__icontains='贵州').count()
    yn = TInfo.objects.filter(job_addr__icontains='云南').count()
    sx2 = TInfo.objects.filter(job_addr__icontains='陕西').count()
    gs = TInfo.objects.filter(job_addr__icontains='甘肃').count()
    qh = TInfo.objects.filter(job_addr__icontains='青海').count()
    xz = TInfo.objects.filter(job_addr__icontains='西藏').count()
    gx = TInfo.objects.filter(job_addr__icontains='广西').count()
    nng = TInfo.objects.filter(job_addr__icontains='内蒙古').count()
    nx = TInfo.objects.filter(job_addr__icontains='宁夏').count()
    xj = TInfo.objects.filter(job_addr__icontains='新疆').count()
    xg = TInfo.objects.filter(job_addr__icontains='香港').count()
    am = TInfo.objects.filter(job_addr__icontains='澳门').count()
    tw = TInfo.objects.filter(job_addr__icontains='台湾').count()
    hb2 = TInfo.objects.filter(job_addr__icontains='湖北').count()
    return render(request, 'echats/map.html', {'bj': bj, 'sh': sh, 'sz': sz, 'gz': gz, 'tj': tj, 'cq': cq, 'hb': hb, 'sx': sx, 'ln': ln, 'jl': jl,
                                               'hlj': hlj, 'js': js, 'zj': zj, 'ah': ah, 'fj': fj, 'jx': jx, 'sd': sd, 'hn': hn,
                                               'hn2': hn2, 'sc': sc, 'gz2': gz2, 'yn': yn, 'sx2': sx2, 'gs': gs, 'qh': qh, 'xz': xz,
                                               'gx': gx, 'nng': nng, 'nx': nx, 'xj': xj, 'xg': xg, 'am': am, 'tw': tw, 'hb2': hb2})


def f_pie(request):
    bj = TInfo.objects.filter(job_addr__icontains='北京').count()
    sh = TInfo.objects.filter(job_addr__icontains='上海').count()
    sz = TInfo.objects.filter(job_addr__icontains='深圳').count()
    gz = TInfo.objects.filter(job_addr__icontains='广州').count()
    return render(request, 'echats/pie.html', {'bj': bj, 'sh': sh, 'sz': sz, 'gz': gz})


def globe(request):
    
    
    return render(request, 'echats/3d_globe.html')
    


