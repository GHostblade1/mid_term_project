from django.shortcuts import render
from main.models import BookClassify, TBook
# Create your views here.


def index(request):
    user = request.session.get('user')
    state = '1' if user else '0'
    b_c1 = BookClassify.objects.filter(c_id__isnull=True)
    b_c2 = BookClassify.objects.filter(c_id__isnull=False)
    book1 = TBook.objects.all().order_by('-launch_time')
    #print(9, b_c1)
    #print(10, b_c2)
    return render(request, 'index.html', {'b_c1': b_c1, 'b_c2': b_c2, 'book1': book1, 'state': state, 'user': user})
