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
cookies
    登录时，前一个请求返回的cookies，在后一个接口测试时，可以将该参数填入对应的实参位置
body中的请求数据

### 1、txt/html格式的数据提取

​    