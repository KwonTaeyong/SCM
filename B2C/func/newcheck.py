import this

from django.shortcuts import HttpResponse
from ..models import  Order_list
from django.http import JsonResponse
import re


def new_set_product(request):

    ori_data = Order_list.objects.order_by('-ORDER_DATE')  ## 원본 데이터
    ## 주문리스트-체크필요 > 제주도 badge
    orderlistjeju = ''
    kw_jeju = '제주시'
    if ori_data.filter(RECEIVE_ADDR__icontains=kw_jeju):
        orderlistjeju = '1'
    ## 주문리스트-체크필요 > 영문 badge
    orderlisten = ''
    enlist = []
    for data in ori_data:
        text = data.RECEIVE_ADDR
        if len(re.compile('[가-힣]+').findall(text)) == 0:
            enlist.append(data)
            orderlisten = '1'

    context = {
        'orderlistjeju': orderlistjeju,
        'orderlisten': orderlisten,
    }
    return JsonResponse(context)
