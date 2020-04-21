import pymysql
from config.conf import *


def get_sql(sql):
    """
    根据传入的sql语句，返回查询的结果
    :param sql: 运行查询的sql语句
    :return: 数据库查询的结果
    """
    pass
    # 调用conf中的数据库参数函数，获取对应的数据库配置信息
    host, port, user, password, database, charset = sql_conf()
    print(host, port, user, password, database, charset)
    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset=charset
    )
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    db.close()
    return data


if __name__ == '__main__':
    id = get_sql("select user_pwd from fanwe_user where user_name = 'cxy2020'; ")
    print(id)
