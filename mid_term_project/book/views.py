from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from main.models import TBook, BookClassify


# Create your views here.


def book_details(request):
    id = request.GET.get('id')
    user = request.session.get('user')
    state = '1' if user else '0'
    #print(7, id)
    book = TBook.objects.filter(id=id)[0]
    #print(9,book)
    request.session['html'] = 'book_details'
    request.session['book_id'] = id
    return render(request, 'Book details.html', {'book': book, 'user': user, 'state': state, 'id': id})


def book_list(request):
    id1 = request.GET.get('id1')
    id2 = request.GET.get('id2')
    num = request.GET.get('num')
    user = request.session.get('user')
    state = '1' if user else '0'
    if id1 == None or id1 == 'None':
        id1 = 1
    if num == None or num == 'None':
        num= 1
    if id2 == None or id1 == 'None':
        id2 = 1
    c_ids = BookClassify.objects.filter(c_id=id1).values()
    ids = []
    for i in c_ids:
        ids.append(i['id'])
    b_c1 = BookClassify.objects.filter(c_id__isnull=True)
    b_c2 = BookClassify.objects.filter(c_id__isnull=False)
    b_c_id1 = BookClassify.objects.filter(id=id1)[0]
    b_c_id2 = 0
    if id2 == 'None' or id2 == None:
        books = TBook.objects.filter(book_id__in=set(ids)).values()
        books1 = TBook.objects.filter(book__id__in=set(ids)).values().order_by('dang_price')
    else:
        b_c_id2 = BookClassify.objects.filter(id=id2)[0]
        books = TBook.objects.filter(book_id=id2).values()
        books1 = TBook.objects.filter(book__id__in=set(ids)).values().order_by('dang_price')

    pagtor = Paginator(books, per_page=4)
    page = pagtor.page(num)
    pagtor1 = Paginator(books1, per_page=4)
    page1 = pagtor1.page(num)
    #print(25, id1, id2, books.values(), c_ids, set(ids))
    #print(34, b_c_id1, b_c_id2)
    #print(45, page1, page)
    #print(46, books1)
    request.session['html'] = 'booklist'
    print(57, request.session.get('html'))
    request.session['booklist_id1'] = id1
    request.session['booklist_id2'] = id2
    request.session['num'] = num
    return render(request, 'booklist.html', {'id1': id1, 'id2': id2, 'b_c1': b_c1, 'b_c2': b_c2, 'page': page, 'b_c_id1': b_c_id1, 'b_c_id2': b_c_id2, 'page1': page1, 'user': user, 'state': state})


def books_order(request):
    state = request.GET.get('state')
    #print(51, state)
    if state == '1':
        return HttpResponse('1')
    elif state == '0':
        return HttpResponse('0')

