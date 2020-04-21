import pymysql
import requests
from common.get_mysql import *

user_id = get_sql("select id from fanwe_user where user_name = 'admin222'; ")
print(user_id)
# 抓包，获取用户信息
url = "http://106.12.126.197/fanwe/m.php"

data = {
    "user_type": 0,
    "user_name": "cxy2020",
    "user_pwd": "b865483fef2ecaf9e348abf03c349240",
    "email": "234234@qq.com",
    "mobile": 18387654321,
    "is_effect": 1,
    "id": "2001054",
    "m": "User",
    "a": "update"
}
cookies = {
    "PHPSESSID": "s5qp20vevdjvhsv99mnbr98gr1"
}

r = requests.post(url=url, data=data, cookies=cookies)
print(r.text)
