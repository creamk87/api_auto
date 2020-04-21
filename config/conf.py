def server_ip():
    """
    dev_ip  开发环境服务器ip地址
    sit_ip  测试环境服务器ip地址
    :return: 不同环境服务器地址
    """
    dev_ip = "http://127.0.0.1:8000"
    sit_ip = "http://106.12.126.197:8080"
    server_address = {
        "dev_ip": "http://127.0.0.1:8000",
        "sit_ip": "http://106.12.126.197:8080"
    }
    return server_address["dev_ip"]


def sql_conf():
    """
    host  数据库服务器ip地址
    port    数据库连接端口
    user    数据库连接用户名
    password    数据库用户密码
    database    数据库名
    charset 数据库字符编码格式
    :return:
    """
    # host = "106.12.126.197"
    # port = 3306
    # user = "root"
    # password = "Cxy123456@"
    # database = "fanwe"
    # charset = "utf8"
    host, port, user, password, database, charset = ["106.12.126.197", 3306, "root", "Cxy123456@", "fanwe", "utf8"]
    return host, port, user, password, database, charset
