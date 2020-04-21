"""
获取json格式数据
"""

import requests

url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%88%90%E9%83%BD%E4%B8%9C,ICW&ts=%E5%8C%97%E4%BA%AC%E5%8C%97,VAP&date=2020-04-21&flag=N,N,Y"
headers = {
    "Cookie": "JSESSIONID=DC2529A47172CCD718D7C5675B7F03FD; BIGipServerotn=4141285642.50210.0000; RAIL_EXPIRATION=1587712708162; RAIL_DEVICEID=g0yvDk9dHvrOxw4fVfYl3Ms8ght-gKsW1d0Xsnxy72eey5ljYYJndMM5sJncYMSm3RVReGvXBMqTbhb8CKJeVIZtbHJWmaKVXC_-wksHagLGGpQFtzXPgFSJk0XQ-dkkQIXV6YDpw8mHf9c7n8AmbfwUGWTA8veR; BIGipServerpassport=803733770.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u6210%u90FD%u4E1C%2CICW; _jc_save_toStation=%u5317%u4EAC%u5317%2CVAP; _jc_save_fromDate=2020-04-21; _jc_save_toDate=2020-04-21; _jc_save_wfdc_flag=dc"
}
r = requests.get(url=url, headers=headers)
# 返回的是json格式数据
print(r.json)
