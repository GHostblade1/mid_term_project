from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from main.models import TBook, BookClassify, TUserInfo
# Create your views here.


def index(request):

    return render(request, 'main/index.html')


def add(request):
    class1 = BookClassify.objects.filter(c_id__isnull=False).values()

    return render(request, 'main/add.html', {'class1': class1})


def dzlist(request):
    num = request.GET.get('num')
    if num == None or num == 'None':
        num = 1
    books = TUserInfo.objects.all().order_by('-id')
    pagtor = Paginator(books, per_page=10)
    page = pagtor.page(num)
    return render(request, 'main/dzlist.html', {'page': page})


def list(request):
    num = request.GET.get('num')
    if num == None or num == 'None':
        num= 1
    books = TBook.objects.all()
    pagtor = Paginator(books, per_page=10)
    page = pagtor.page(num)
    return render(request, 'main/list.html', {'page': page})


def splb(request):
    num = request.GET.get('num')
    if num == None or num == 'None':
        num = 1
    books = BookClassify.objects.all()
    pagtor = Paginator(books, per_page=20)
    page = pagtor.page(num)
    return render(request, 'main/splb.html', {'page': page})


def test(request):

    return render(request, 'main/test.html')


def zjsp(request):

    return render(request, 'main/zjsp.html')


def zjzlb(request):
    class1 = BookClassify.objects.filter(c_id__isnull=True).values()

    return render(request, 'main/zjzlb.html', {"class1": class1})


def add_book(request):
    name = request.POST.get('name')
    writer = request.POST.get('writer')
    press = request.POST.get('press')
    public = request.POST.get('public')
    p_c_id = request.POST.get('p_c_id')
    print(59, name, writer, press, public, p_c_id)
    try:
        with transaction.atomic():
            TBook.objects.create(name=name, writer=writer, press=press, p_time=public, book_id=p_c_id)
            return HttpResponse('1')
    except:
        print('添加商品异常！')
        return HttpResponse('0')


def add_p_c(request):
    name = request.POST.get('name')
    print(name)
    try:
        with transaction.atomic():
            BookClassify.objects.create(name=name)
            return HttpResponse('1')
    except:
        print('添加商品父类异常！')
        return HttpResponse('0')


def add_c_c(request):
    p_c_id = request.POST.get('p_c_id')
    c_name = request.POST.get('c_name')
    print(95, c_name, p_c_id)
    try:
        with transaction.atomic():
            BookClassify.objects.create(name=c_name, c_id=p_c_id)
            return HttpResponse('1')
    except:
        print('添加商品子类异常！')
        return HttpResponse('0')
    #return HttpResponse('1')


def delete_books(request):
    id_books = request.POST.get('bb')
    #print(109, id_books)
    list_id_b = id_books.split('-')
    #print(111, list_id_b)
    del list_id_b[0]
    tuple_id_b = tuple(list_id_b)
    #print(113, tuple_id_b)
    try:
        with transaction.atomic():
            TBook.objects.filter(id__in=tuple_id_b).delete()
            # print(118, TBook.objects.filter(id__in=tuple_id_b))
            return HttpResponse('1')
    except:
        print('删除商品异常！')
    return HttpResponse('0')

