from main.models import TBook


class CartItem:
    def __init__(self, book, amount):
        self.book = book
        self.amount = amount
        self.status = 1


class Cart:
    def __init__(self):
        self.save_price = 0
        self.total_price = 0
        self.cart_item = []

    def sums(self):
        self.total_price = 0
        self.save_price = 0
        for i in self.cart_item:
            if i.status:
                self.total_price += i.book.dang_price * i.amount
                self.save_price += (i.book.pricing - i.book.dang_price) * i.amount




    def add_book_toCart(self, bookid):
        for i in self.cart_item:
            #print('cart25', type(i.book.id), type(bookid))
            if i.book.id == int(bookid):
                #print('cart27', i.book.id, bookid)
                i.amount += 1
                #print('cart29', i.amount)
                self.sums()
                return None
            else:
                print('cart33', '你大爷的')
        book = TBook.objects.filter(id=bookid)[0]
        self.cart_item.append(CartItem(book, 1))
        #print('cart33', self.cart_item)
        self.sums()

    def modify_cart(self, bookid, amount):
        #print('cart43', bookid, type(bookid), amount, type(amount))
        for i in self.cart_item:
            if i.book.id == int(bookid):
                i.amount = amount
                #print('cart47', i.amount)
        self.sums()

    def delete_book(self, bookid):
        for i in self.cart_item:
            if i.book.id == int(bookid):
                self.cart_item.remove(i)
        self.sums()