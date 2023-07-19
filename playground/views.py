from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Min,Max,Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Order

# Create your views here.
def say_hello(request):
    #queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    result = Product.objects.filter(collection__id=1).aggregate(count = Count('id'), min_price = Min('unit_price'))

    return render(request,'hello.html',{'name':'Abdullah' , 'result': result})