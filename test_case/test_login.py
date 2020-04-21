import requests

url_login = "http://106.12.126.197/fanwe/index.php?ctl=user&act=login"
json = {
    "email": "admin9527",
    "password": "654321q"
}
r_login = requests.post(url=url_login, json=json)
print(r_login.text)
