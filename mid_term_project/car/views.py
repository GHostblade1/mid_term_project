import string

from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from car.cart import Cart
import json, random, datetime
from main.models import TUserInfo, TOrder, TOrderitem, TUser

# Create your views here.


def car(request):
    user = request.session.get('user')
    state = '1' if user else '0'
    cart = request.session.get('cart')
    request.session['html'] = 'car_f'
    return render(request, 'car.html', {'cart': cart, 'state': state, 'user': user})


def indent(request):
    user = request.session.get('user')
    state = '1' if user else '0'
    cart = request.session.get('cart')
    if user:
        if cart:
            return render(request, 'indent.html', {'cart': cart, 'state': state, 'user': user})
        else:
            return HttpResponse('<h1>请购买商品</h1>'
                            '<a href="/main/index/">点击跳转到主界面！</a>')
    else:
        return redirect('user:login')

def indent_ok(request):
    try:
        with transaction.atomic():
            user = request.session.get('user')
            state = '1' if user else '0'
            login_state1 = request.POST.get('login_state1')
            print(25, login_state1)
            if login_state1:
                login_user1 = request.POST.get('login_user1')
                ship_man = request.POST.get('ship_man')
                ship_area = request.POST.get('ship_area')
                ship_site = request.POST.get('ship_site')
                ship_postcode = request.POST.get('ship_postcode')
                ship_phone1 = request.POST.get('ship_phone1')
                ship_phone2 = request.POST.get('ship_phone2')
                user_id = TUser.objects.filter(email_addr=login_user1)[0].id
                TUserInfo.objects.create(name=ship_man, addr=ship_site, postalcode=ship_postcode,
                                         phone1=ship_phone1, phone2=ship_phone2, null1=ship_area, user_id=user_id)
                info_id = TUserInfo.objects.filter(name=ship_man, addr=ship_site, postalcode=ship_postcode, phone1=ship_phone1, phone2=ship_phone2, null1=ship_area, user_id=user_id)[0].id
                cart = request.session.get('cart')
                number = random.sample(string.digits, 9)
                number = ''.join(number)
                start_date = datetime.datetime.now().date()
                print(42, number, start_date)
                TOrder.objects.create(number=number, start_time=start_date, user_id=user_id, total=cart.total_price, info_id=info_id)
                order_id = TOrder.objects.filter(number=number, start_time=start_date, user_id=user_id, total=cart.total_price)[0].id
                for i in cart.cart_item:
                    TOrderitem.objects.create(book_id=i.book.id, item_number=i.amount, subtotal=i.book.dang_price*i.amount, order_id=order_id)
                request.session['cart'] = None
                return render(request, 'indent ok.html', {'state': state, 'user': user, 'number': number, 'cart': cart, 'user1': login_user1, 'ship_man': ship_man})
            else:
                request.session['cart'] = None
                return redirect('user:login')
    except:
        print('出现异常！')
        return HttpResponse('<h1>提交订单异常！</h1>'
                            '<a href="/car/indent/">点击跳转到回订单页面！</a>')
def add_book(request):
    id = request.GET.get('id')
    cart = request.session.get('cart')
    if cart is None:
        cart = Cart()
        cart.add_book_toCart(id)
        request.session['cart'] = cart
    else:
        cart.add_book_toCart(id)
        request.session['cart'] = cart
    #print(32, cart.cart_item[0].book.id, cart.cart_item[1].book.id, cart.cart_item[0].amount, cart.cart_item[1].amount)
    return HttpResponse('1')


def update_cart(request):
    id = request.GET.get('id')
    value1 = request.GET.get('value')
    if value1.isdigit():
        value1 = int(value1)
    else:
        value1 = 1
    cart = request.session.get('cart')
    #cart.delete_book(id)
    cart.modify_cart(id, value1)
    request.session['cart'] = cart
    #print('47', value1)
    list = [cart.total_price, cart.save_price, value1]
    str = json.dumps(list)
    #print('cart53', str)
    return HttpResponse(str)


def delete_book_inCart(request):
    #request.session['cart'] = None
    id = request.GET.get('id')
    cart = request.session.get('cart')
    for i in cart.cart_item:
        if i.book.id == int(id):
            i.status = 0
    cart.sums()
    request.session['cart'] = cart
    return redirect('car:car_f')


def red_amount(request):
    id = request.GET.get('id')
    value1 = request.GET.get('value')
    if value1.isdigit():
        value1 = int(value1)
    else:
        value1 = 2
    value1 -= 1
    cart = request.session.get('cart')
    # cart.delete_book(id)
    cart.modify_cart(id, value1)
    request.session['cart'] = cart
    # print('47', value1)
    list = [cart.total_price, cart.save_price, value1]
    str = json.dumps(list)
    #print('cart53', str)
    return HttpResponse(str)


def add_amount(request):
    id = request.GET.get('id')
    value1 = request.GET.get('value')
    if value1.isdigit():
        value1 = int(value1)
    else:
        value1 = 2
    value1 += 1
    cart = request.session.get('cart')
    # cart.delete_book(id)
    cart.modify_cart(id, value1)
    request.session['cart'] = cart
    # print('47', value1)
    list = [cart.total_price, cart.save_price, value1]
    str = json.dumps(list)
    #print('cart53', str)
    return HttpResponse(str)


def recover_book_inCart(request):
    id = request.GET.get('id')
    cart = request.session.get('cart')
    for i in cart.cart_item:
        if i.book.id == int(id):
            i.status = 1
    cart.sums()
    request.session['cart'] = cart
    return redirect('car:car_f')