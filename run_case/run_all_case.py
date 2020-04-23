import pytest

# 如何去运行测试用例，test开头的函数即可

if __name__ == '__main__':
    # # 单个文件运行，运行添加，对应的文件地址，用相对路径
    pytest.main(
        ["../test_case/test_case_01.py", "--html", "../report/html/test_result.html", "--self-contained-html", "--alluredir", "../report/xml"])

    # 多个文件运行，以列表形式添加
    # pytest.main(["../test_case/test_case_01.py", "../test_case/test_case_02.py"])

    # # 运行整个目录
    # pytest.main(["../test_case"])
