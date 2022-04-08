import requests
import xmltodict
import json

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}
session.headers.update(headers)
url = 'https://r.sabangnet.co.kr/RTL_API/xml_order_info.html?xml_url=http://222.96.199.9/order.xml'


res_xml = session.get(url).content.decode('euc-kr')
res_dict = xmltodict.parse(res_xml)
res_json = json.loads(json.dumps(res_dict))
print(res_json)
# tree = elemTree.fromstring(res_xml)
# print(tree)
