import requests

url_login = "http://106.12.126.197/fanwe/index.php?ctl=user&act=dologin&fhash=NzJhAtKoEQnHhpxPckXrIjZMvsoqljRTFhreiFIdMNoRKfrnGL"
data_login = {
    "email": "admin9527",
    "user_pwd": "654321q",
    "ajax": 1
}
r_login = requests.post(url=url_login, data=data_login)
print(r_login.content.decode("unicode_escape"))
