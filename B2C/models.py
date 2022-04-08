from django.db import models
from django.contrib.auth.models import User


class Order_list(models.Model):
    IDX = models.CharField(max_length=100, null=True, blank=True)  # 사방넷 주문번호
    ORDER_ID = models.CharField(max_length=100, null=True, blank=True)  # 몰 주문번호
    MALL_ID = models.CharField(max_length=100, null=True, blank=True)  # 몰이름
    ORDER_STATUS = models.CharField(max_length=100)  # 주문상태
    scm_status = models.CharField(max_length=100, null=True, blank=True)  # scm 주문상태
    PAY_COST = models.IntegerField()  # 결제액
    ORDER_DATE = models.DateTimeField(null=True, blank=True)  # 몰 주문일자
    MALL_PRODUCT_ID = models.CharField(max_length=100, null=True, blank=True)   # 몰 상품코드
    PRODUCT_NAME = models.CharField(max_length=100, null=True, blank=True)  # 상품명
    SKU_VALUE = models.CharField(max_length=100, null=True, blank=True)  # 옵션명
    item_id = models.CharField(max_length=100, null=True, blank=True)  # 품번
    item_name = models.CharField(max_length=100, null=True, blank=True)  # 품목
    item_quan = models.IntegerField(null=True, blank=True)  # 품목수량
    DELIVERY_METHOD_STR = models.CharField(max_length=100, null=True, blank=True)  # 배송방법
    DELV_COST = models.IntegerField(null=True, blank=True)  # 배송비
    P_EA = models.IntegerField(null=True, blank=True)  # 총 수량
    REG_DATE = models.DateTimeField(null=True, blank=True)  # 사방 수집일자
    ORD_CONFIRM_DATE = models.DateTimeField(null=True, blank=True)  # 주문 확인 일자
    RTN_DT = models.DateTimeField(null=True, blank=True)  # 반품 완료일자
    CHNG_DT = models.DateTimeField(null=True, blank=True)  # 교환 완료일자
    DELIVERY_CONFIRM_DATE = models.DateTimeField(null=True, blank=True)  # 출고 완료일자
    CANCEL_DT = models.DateTimeField(null=True, blank=True)  # 취소 완료일자
    DELIVERY_ID = models.CharField(max_length=100, null=True, blank=True)  # 택배사 코드
    INVOICE_NO = models.BigIntegerField(null=True, blank=True)  # 송장번호
    INV_SEND_MSG = models.CharField(max_length=100, null=True, blank=True)  # 송장 전송 결과
    INV_SEND_DM = models.DateTimeField(null=True, blank=True)  # 송장 전송일
    USER_ID = models.CharField(max_length=100, null=True, blank=True)  # 주문자 ID
    USER_NAME = models.CharField(max_length=100, null=True, blank=True)  # 주문자 이름
    USER_TEL = models.CharField(max_length=100, null=True, blank=True)  # 주문자 전화
    USER_CEL = models.CharField(max_length=100, null=True, blank=True)  # 주문자 폰
    RECEIVE_NAME = models.CharField(max_length=100, null=True, blank=True)  # 수취인 이름
    RECEIVE_TEL = models.CharField(max_length=100, null=True, blank=True)  # 수취인 전화
    RECEIVE_CEL = models.CharField(max_length=100, null=True, blank=True)  # 수취인 폰
    RECEIVE_ZIPCODE = models.CharField(max_length=10, null=True, blank=True)  # 우편번호
    RECEIVE_ADDR = models.CharField(max_length=100, null=True, blank=True)  # 주소
    DELV_MSG = models.CharField(max_length=100, null=True, blank=True)  # 배송메세지
    HOPE_DELV_DATE = models.CharField(max_length=10, null=True, blank=True)  # 배송희망일
    memo = models.CharField(max_length=10, null=True, blank=True) # 메모