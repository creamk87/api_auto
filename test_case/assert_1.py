"""
assert a 		# 判断xx为真
assert not a 	# 判断xx为假
assert a in b 	# 判断b包含a
assert a == b 	# 判断a等于b
assert a != b 	# 判断a等于b
"""
from common.get_mysql import *

a = 0
b = 1
assert a, "断言失败，打印后面的信息"

assert b, "断言失败，打印后面的信息，成功便不会打印"

assert a == "a"

# 可断言数据库返回的信息
assert get_sql("select id from user where id = '24';")