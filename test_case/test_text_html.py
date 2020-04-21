"""
text/html 格式数据的提取
51job为例
"""

import requests
import re

url_51 = "https://search.51job.com/list/090200,000000,0000,00,9,99,%25E6%2588%2590%25E9%2583%25BD%2B%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
r_51 = requests.get(url=url_51)
r_51.encoding = "gb2312"
print(r_51.text)
# requests.adapters.DEFAULT_RETRIES = 1
# s = requests.session()
# s.keep_alive = False

# 如果提取text格式数据的信息   用re模块，正则表达式匹配提取
# title="武汉达梦数据库有限公司" href="https://jobs.51job.com/all/co5795688.html">武汉达梦数据库有限公司
url_wh = re.findall('title="武汉达梦数据库有限公司" href="(.+?)">武汉达梦数据库有限公司', r_51.text)
print(url_wh)
r_51_wh = requests.get(url=url_wh[0])
r_51_wh.encoding = "gb2312"
print(r_51_wh.text)
