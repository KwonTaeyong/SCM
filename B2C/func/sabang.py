import requests
import xmltodict
import json
from datetime import datetime


def get_order():
    url = 'https://r.sabangnet.co.kr/RTL_API/xml_order_info.html?xml_url=http://222.96.199.9/order.xml'
    res_xml = requests.get(url).content.decode('euc-kr')
    res_dict = xmltodict.parse(res_xml)
    res_json = json.loads(json.dumps(res_dict))
    order_list = res_json['SABANG_ORDER_LIST']['DATA']
    return order_list


def date_trans(date):
    result = None
    if date:
        result = datetime.strptime(date, '%Y%m%d%H%M%S')
    return result

def ref(orderlist):
    with open('ref.json', encoding='utf-8') as json_file:
        ref = json.load(json_file)

    res = []
    for order in orderlist:
        if order['SKU_VALUE'] == None:
            try:
                x = ref[order['PRODUCT_NAME']]
            except:
                continue
        else:
            try:
                x = ref[f"{order['PRODUCT_NAME']} /{order['SKU_VALUE']}"]
            except:
                try:
                    x = ref[f"{order['PRODUCT_NAME']}/ {order['SKU_VALUE']}"]
                except:
                    try:
                        x = ref[f"{order['PRODUCT_NAME']} / {order['SKU_VALUE']}"]
                    except:
                        continue
        order['카테고리'] = x['카테고리']
        order['품목'] = x['품목']
        order['구성품'] = x['구성품']
        order['증정'] = x['증정']

        res.append(order)

    return res


if __name__ == '__main__':
    ref()
