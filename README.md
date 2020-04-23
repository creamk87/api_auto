[TOC]



## 一、API接口测试分工

### 1、单独独立完成接口自动化

按照这个架构思维去编写

### 2、几个人完成，我做主导

前期做的事情：

- 需求确定
- 计划的确定
- 人员安排

1. 搭建初步框架出来，告知所有的测试人员，各模块的含义

2. 建立起规则和公共的方法

   比如：公共方法，自己写好，方便其他人调用
              其他人编写公共方法，一定要去说明，需要主导人员认可
              test_case 根据人员按模块划分

### 3、如果只是辅助

1. 了解代码结构，不懂去询问

2. 根据分配的任务，编写对应的测试用例

3. 好的方法，提出改进

   

## 二、模块划分：

### config配置文件

【通用的信息放其中，比如测试接口的 服务器地址 等】
dev环境  sit环境
package

### test_data 测试数据的维护

【测试数据维护较多，单独抽离出来维护】
package

### common 公共的方法

【数据参数化，表格，数据库的操作，后期做密码处理、校验】
package

### test_case pytest框架

【针对每个接口发送请求】
directory

### report 报告

【生成对应的报告  html、xml、allure报告】
directory

### run_case 用例运行模块

【分装运行测试用例的模块】

### log 

生成日志，方便后期的问题定位

### CI/CD 持续集成



## 三、参数化

### 1、函数参数化：

参见  test_case --> test_fore.py

### 2、文件参数化：

文件类型：excel表格，csv文件，txt文件
python也有提供第三方包
一般选择excel表格，进行参数化
参见  test_case --> test_update.py

### 3、数据库参数化：

​    1、部分接口，参数其他方式获取不到，可以采用数据库去获取
​    2、比如：手机验证码信息（手机接收后，数据库中也会保存）

### 4、字典参数化：

​    比如：环境地址
​    参见  config --> conf.py 中服务器环境配置

### 5、列表参数化：

​    比如：数据库连接信息
​    参见  config --> conf.py 中数据库连接配置



## 四、动态关联：

前一个接口返回的结果当后一个接口的请求参数

### cookies

登录时，前一个请求返回的cookies，在后一个接口测试时，可以将该参数填入对应的实参位置

### Response body中的请求数据

#### 	1、txt/html格式的数据提取

#### 	2、json格式数据的提取

​		参见test_fore.py中例子



## 五、断言

```python
assert a 				# 判断xx为真
assert not a 		# 判断xx为假
assert a in b 	# 判断b包含a
assert a == b 	# 判断a等于b
assert a != b 	# 判断a等于b
```

1、返回Http请求的状态码

```python
assert r_login.content.decode("unicode_escape")
```

2、数据库返回的结果断言

```python
assert get_sql("select id from user where id = '24';")
```

​	

## 六、pytest框架

### 1、命名规则

test_开头或 _test结尾

类用Test开头，不能带有 (init) 方法



### 2、安装

pytest包

```bash
pip install pytest
```

python-html报告

```bash
pip install pytest-html
```

allure报告

```bash
pip install allure-pytest
```



### 3、运行用例

run_case --> run_all_case.py

```python
import pytest

# 如何去运行测试用例，test开头的函数即可

if __name__ == '__main__':
    # 单个文件运行，运行添加，对应的文件地址，用相对路径
    pytest.main(["../test_case/test_case_01.py"])

    # 多个文件运行，以列表形式添加
    pytest.main(["../test_case/test_case_01.py", "../test_case/test_case_02.py"])

    # 运行整个目录
    pytest.main(["../test_case"])
```



### 4、pytest传参

​		接口之间的动态关联

​		添加地址接口，需要登录成功返回的cookies值，作为后续接口的参数才能成功添加

​		test_login()	test_add_address() 添加地址函数中会调用 test_login 函数，pytest在运行该文件时，会导致test_login运行两次

```
解决方法：

​	1、将要调用的值，定义为全局变量

​	test_login()函数中添加	

​	global cookies

​	cookies = r_login.cookies 

​	在test_add_address中，调用cookies时，就使用全局变量，调用该参数
```



### 5、生成allure报告



#### 	a、生成html报告

​	"--html=../report/report.html"

#### 	b、生成xml格式的报告

​	"--junitxml=../report/report.xml"	

#### 	c、生成allure格式的报告

​		1、生成allure结果目录，json格式		

​			"--alluredir","../report/reportallure"

​		2、生成allure报告

​			安装allure工具

​			brew install allure

​			安装完成后，输入 allure --version 查看 allure 版本

​			allure generate report/xml -o allure-reports-new/

​			allure generate [json文件路径] -o [allure报告生成路径] --clean

​		

```bash
Mac上需要注意，在本地查看报告时，浏览器偶尔会出现

​		**XMLHttpRequest cannot load file:///问题 Ajax本地跨域问题**

解决方法：

打开terminal终端，cd到谷歌浏览器应用程序下
cd /Applications/Google Chrome.app/Contents/MacOS
sudo mv Google\ Chrome Google.real  # 将原来的chrome启动程序重命名，该名字在后面会用到
vim Google\ Chrome  # 创建Google Chrome文件
添加下面的脚本在文件中：
#!/bin/bash
cd "/Applications/Google Chrome.app/Contents/MacOS"
"/Applications/Google Chrome.app/Contents/MacOS/Google.real" --args --disable-web-security --user-data-dir --enable-file-cookies  --allow-file-access-from-files

添加浏览器启动参数，主要是 --enable-file-cookies  --allow-file-access-from-files 这2个参数，允许浏览器支持本地文件（file协议）ajax请求

重启浏览器即可

```

