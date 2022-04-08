from django.shortcuts import render, redirect
from ..func import sabang
from ..models import Order_list
from django.core.paginator import Paginator
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q
import re
from django.contrib.auth.decorators import login_required

def order_index(request):
    return render(request, 'B2C/order_index.html')

def List_view(request):
    today = datetime.today()  ## 오늘 시간

    print(request.GET)

    order_list = Order_list.objects.all()

    order_list = order_list.filter(scm_status='주문수집')

    if request.GET.get('orderdate1'):
        order_list = order_list.filter(ORDER_DATE__range=[request.GET.get('orderdate1'), request.GET.get('orderdate2')])

    if request.GET.get('deliverydate'):
        req_date = request.GET.get('deliverydate').replace('-', '')
        order_list = order_list.filter(HOPE_DELV_DATE=req_date)

    if request.GET.get('kw'):
        order_list = order_list.filter(
            Q(MALL_ID__icontains=request.GET.get('kw')) |
            Q(RECEIVE_ADDR__icontains=request.GET.get('kw')) |
            Q(USER_NAME__icontains=request.GET.get('kw')) |
            Q(RECEIVE_NAME__icontains=request.GET.get('kw')) |
            Q(PRODUCT_NAME__icontains=request.GET.get('kw')) |
            Q(SKU_VALUE__icontains=request.GET.get('kw'))
        ).distinct()

    ## 페이징 처리
    input_page = int(request.GET.get('page', 1))
    paginator = Paginator(order_list, '30')
    max_page = paginator.num_pages
    if input_page < 1:
        input_page = 1
    elif input_page > max_page:
        input_page = max_page
    page_obj = paginator.page(input_page)
    start_page = input_page - 4
    if start_page < 1:
        start_page = 1
    end_page = input_page + 4
    if end_page > max_page:
        end_page = max_page
    page_range = paginator.page_range[start_page - 1:end_page]

    context = {
        'order_list': page_obj,
        'page_range': page_range,
        'today': today
    }
    return render(request, 'B2C/order_list.html', context)


def orderlistEn(request):
    if request.POST:
        t_data = Order_list.objects.get(id=request.POST.get('id'))
        x = request.POST
        y = x.dict()
        print(y)

        # t_data.ORDER_DATE = request.POST.get('ORDER_DATE')
        # t_data.MALL_ID = request.POST.get('MALL_ID')
        # t_data.USER_NAME = request.POST.get('USER_NAME')
        # t_data.USER_CEL = request.POST.get('USER_CEL')
        # t_data.RECEIVE_NAME = request.POST.get('RECEIVE_NAME')
        # t_data.RECEIVE_CEL = request.POST.get('RECEIVE_CEL')
        # t_data.RECEIVE_ADDR = request.POST.get('RECEIVE_ADDR')
        # t_data.DELIVERY_METHOD_STR = request.POST.get('DELIVERY_METHOD_STR')
        # t_data.DELV_COST = request.POST.get('DELV_COST')
        # t_data.DELV_MSG = request.POST.get('DELV_MSG')
        # t_data.HOPE_DELV_DATE = request.POST.get('HOPE_DELV_DATE')
        # t_data.P_EA = request.POST.get('P_EA')
        # t_data.PAY_COST = request.POST.get('PAY_COST')
        # t_data.DELIVERY_ID = request.POST.get('DELIVERY_ID')
        # t_data.INVOICE_NO = request.POST.get('INVOICE_NO')
        # t_data.IDX = request.POST.get('IDX')
        # t_data.ORDER_ID = request.POST.get('ORDER_ID')
        # t_data.ORDER_STATUS = request.POST.get('ORDER_STATUS')
        # t_data.memo = request.POST.get('memo')
        # t_data.save()

        return redirect('B2C:orderlistEn')

    ## 정규식 통해서 한글만 리스트로 > 한글이 없거나 빈값이면 영어 이므로 list len = 0
    order_list = Order_list.objects.order_by('-ORDER_DATE')
    enlist = []
    for data in order_list:
        text = data.RECEIVE_ADDR
        if len(re.compile('[가-힣]+').findall(text)) == 0:
            enlist.append(data)

    ## 페이징 처리
    input_page = int(request.GET.get('page', 1))
    paginator = Paginator(enlist, '30')
    max_page = paginator.num_pages
    if input_page < 1:
        input_page = 1
    elif input_page > max_page:
        input_page = max_page
    page_obj = paginator.page(input_page)
    start_page = input_page - 4
    if start_page < 1:
        start_page = 1
    end_page = input_page + 4
    if end_page > max_page:
        end_page = max_page
    page_range = paginator.page_range[start_page - 1:end_page]

    context = {
        'order_list': page_obj,
        'page_range': page_range,
    }

    return render(request, 'B2C/orderlistEn.html', context)


def orderlistJeju(request):
    kw = '제주시'
    order_list = Order_list.objects.order_by('-ORDER_DATE')
    order_list = order_list.filter(RECEIVE_ADDR__icontains=kw)

    ## 페이징 처리
    input_page = int(request.GET.get('page', 1))
    paginator = Paginator(order_list, '10')
    max_page = paginator.num_pages
    if input_page < 1:
        input_page = 1
    elif input_page > max_page:
        input_page = max_page
    page_obj = paginator.page(input_page)
    start_page = input_page - 4
    if start_page < 1:
        start_page = 1
    end_page = input_page + 4
    if end_page > max_page:
        end_page = max_page
    page_range = paginator.page_range[start_page - 1:end_page]

    context = {
        'order_list': page_obj,
        'page_range': page_range,
    }

    return render(request, 'B2C/orderlistJeju.html', context)


def orderlistSauce(request):
    return render(request, 'B2C/orderlistSauce.html')


def Update_order(request):
    order_db = Order_list.objects.all()
    order_list = sabang.get_order()
    for order in order_list:
        if not order_db.filter(IDX=order['IDX']):
            Order_list(
                IDX=order['IDX'],
                ORDER_ID=order['ORDER_ID'],
                MALL_ID=order['MALL_ID'],
                ORDER_STATUS=order['ORDER_STATUS'],
                scm_status="주문수집",
                PAY_COST=order['PAY_COST'],
                ORDER_DATE=sabang.date_trans(order['ORDER_DATE']),
                MALL_PRODUCT_ID=order['MALL_PRODUCT_ID'],
                PRODUCT_NAME=order['PRODUCT_NAME'],
                SKU_VALUE=order['SKU_VALUE'],
                item_id=None,
                item_name=None,
                item_quan=None,
                DELIVERY_METHOD_STR=order['DELIVERY_METHOD_STR'],
                DELV_COST=order['DELV_COST'],
                P_EA=order['P_EA'],
                REG_DATE=sabang.date_trans(order['REG_DATE']),
                ORD_CONFIRM_DATE=sabang.date_trans(order['ORD_CONFIRM_DATE']),
                RTN_DT=sabang.date_trans(order['RTN_DT']),
                CHNG_DT=sabang.date_trans(order['CHNG_DT']),
                DELIVERY_CONFIRM_DATE=sabang.date_trans(order['DELIVERY_CONFIRM_DATE']),
                CANCEL_DT=sabang.date_trans(order['CANCEL_DT']),
                DELIVERY_ID=order['DELIVERY_ID'],
                INVOICE_NO=order['INVOICE_NO'],
                INV_SEND_MSG=order['INV_SEND_MSG'],
                INV_SEND_DM=sabang.date_trans(order['INV_SEND_DM']),
                USER_ID=order['USER_ID'],
                USER_NAME=order['USER_NAME'],
                USER_TEL=order['USER_TEL'],
                USER_CEL=order['USER_CEL'],
                RECEIVE_NAME=order['RECEIVE_NAME'],
                RECEIVE_TEL=order['RECEIVE_TEL'],
                RECEIVE_CEL=order['RECEIVE_CEL'],
                RECEIVE_ZIPCODE=order['RECEIVE_ZIPCODE'],
                RECEIVE_ADDR=order['RECEIVE_ADDR'],
                DELV_MSG=order['DELV_MSG'],
                HOPE_DELV_DATE=order['HOPE_DELV_DATE']
            ).save()

    return redirect('B2C:orderlist')


def Order_list_table(request):
    state = request.GET.get('state')
    order_list = Order_list.objects.all()

    order_list = order_list.filter(scm_status=state)

    context = {
        'order_list': order_list,
    }

    return render(request, 'B2C/order_list_table.html', context)


def orderlistmodal(request):
    req_id = request.GET.get('id')
    data = Order_list.objects.get(id=req_id)
    context = {
        'id': data.id,
        'ORDER_DATE': data.ORDER_DATE,
        'MALL_ID': data.MALL_ID,
        'USER_NAME': data.USER_NAME,
        'USER_CEL': data.USER_CEL,
        'RECEIVE_NAME': data.RECEIVE_NAME,
        'RECEIVE_CEL': data.RECEIVE_CEL,
        'RECEIVE_ADDR': data.RECEIVE_ADDR,
        'DELIVERY_METHOD_STR': data.DELIVERY_METHOD_STR,
        'DELV_COST': data.DELV_COST,
        'DELV_MSG': data.DELV_MSG,
        'HOPE_DELV_DATE': datetime.strptime(data.HOPE_DELV_DATE, '%Y%m%d').date(),
        'PRODUCT_NAME': str(data.PRODUCT_NAME) + str('' if data.SKU_VALUE is None else '/' + data.SKU_VALUE),
        'P_EA': data.P_EA,
        'PAY_COST': data.PAY_COST,
        'DELIVERY_ID': data.DELIVERY_ID,
        'INVOICE_NO': data.INVOICE_NO,
        'IDX': data.IDX,
        'ORDER_ID': data.ORDER_ID,
        'ORDER_STATUS': data.ORDER_STATUS,
        'memo': data.memo
    }

    return JsonResponse(context)


def work_order(request):
    order_db = Order_list.objects.values()
    x = sabang.ref(order_db)

    context = {
        'orderlist': x
    }

    return render(request, 'B2C/work_order.html', context)


def salesreport(request):
    today0 = datetime.now().date()
    today = datetime.today()
    order_list = Order_list.objects.all()
    order_list = order_list.filter(ORDER_DATE__range=[today0, today])
    malllist = []
    for iloc in order_list:
        mall = iloc.MALL_ID
        malllist.append(mall)

    malllist = list(set(malllist))

    cost = dict()
    for iloc in malllist:
        data = order_list.filter(MALL_ID=iloc)
        totalcost = 0
        for iloc2 in data:
            totalcost += iloc2.PAY_COST
        cost[iloc] = totalcost

    context = {
        'today0': today0,
        'cost': cost
    }

    return render(request, 'B2C/salesreport.html', context)


def release_list(request):
    order_db = Order_list.objects.values()
    x = sabang.ref(order_db)

    context = {
        'orderlist': x
    }

    return render(request, 'B2C/release_list.html', context)
