"""
目的，验证多种场景，用户名密码正确，错误，用户名不正确
1、安装xlrd包
2、导xlrd包
3、读取excel文件中数据
4、如果excel中的数据是json格式

"""

import xlrd  # 导入excel表格操作包


def get_excel_row(row):
    """
    读取表格中一行的数据
    :param row: 行号，0表示第一行
    :return: 返回，2，3列的值
    """
    excel = xlrd.open_workbook("../testdata/usermessagexlsx.xlsx")
    table = excel.sheets()[0]
    return table.cell_value(row, 1), table.cell_value(row, 2)


"""
excel = xlrd.open_workbook("../testdata/usermessagexlsx.xlsx")  # 打开excel文件，使用相对路径，不用绝对路径

table = excel.sheets()[0]  # 读取excel文件中的第一页内容，1则表示第二页内容

print("行:", table.nrows)  # 取总的行数
print("列:", table.ncols)  # 取总的列数
print(table.row_values(0))  # 取第一行的数据
print(table.col_values(0))  # 取第一列的数据
print(table.cell_value(1, 1))   # 取第二行，第一列的信息，前面是行，后面是列

# excel文件中的数据需要注意格式，直接写数据，读取出来是浮点数
for i in range(1, table.nrows):
    print(table.row_values(i))

for i in range(1, table.nrows):
    print(table.cell_value(i, 1), table.cell_value(i, 2))
"""
