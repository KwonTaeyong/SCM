from django.urls import path

from .views import index, order
from .func import newcheck

app_name = 'B2C'

urlpatterns = [
    #인덱스
    path('', index.main, name='index'),

    #주문
    path('order/index', order.order_index, name='order'),
    path('order/orderlist/', order.List_view, name='orderlist'),
    path('order/orderlistEn/', order.orderlistEn, name='orderlistEn'),  # 체크 필요
    path('order/orderlistJeju/', order.orderlistJeju, name='orderlistJeju'),
    path('order/orderlistSauce/', order.orderlistSauce, name='orderlistSauce'),

    path('api/getsabangorder/', order.Update_order, name='getorder'),

    path('orderlistmodal/', order.orderlistmodal, name='orderlistmodal'),
    ## new check 설정
    path('newcheck/set_product/', newcheck.new_set_product, name='newcheck'),
    path('orderlistmodal/', order.orderlistmodal, name='orderlistmodal'),

    path('workorder/', order.work_order, name='workorder'),
    path('release/', order.release_list, name='release'),
    path('workorder/', order.work_order, name='workorder'),

    path('salesreport/', order.salesreport, name='salesreport')

]