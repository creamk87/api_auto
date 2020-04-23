"""
参数化演示
"""

import requests
from config.conf import *
from common.get_excel import *

"""
接口自动化测试，有很多环境，比如dev开发环境，sit环境，预发布环境，uat环境
要切换环境，修改配置文件
"""

url_reg = server_ip() + "/register"  # 调用函数，来指定对应的测试ip地址
# 表单数据格式，参数data，数据都是字典去保存
reg_data = {
    "username": "cxy201",
    "password": "123456"
}
# 发送请求，表单格式的数据，用data
r_reg = requests.post(url=url_reg, data=reg_data)
print(r_reg.text)
print(r_reg.status_code)

# 登录接口，数据格式，json格式
url_login = server_ip() + "/login"

"""
# 调取封装的函数，读取数据
username, password = get_excel_row(1)  # 读取第2行的信息，分别传给前面2个参数
json = {
    "username": username,
    "password": password
}
"""
"""
如果excel中的数据为json数据
"""
usermessage = get_excel_row(4)[0]  # 取5行的数据，取第一个数据，保存到usermessage里面  str类型
# 把usermessage转换成字典类型 使用 eval 函数
json = eval(usermessage)
# json格式数据，定义值，也是用字典格式保存  json格式！！！！
r_login = requests.post(url=url_login, json=json)
print(r_login.json())

