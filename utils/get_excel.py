'''pandas操作excel'''
import pandas as pd
from openpyxl import load_workbook
from pandas import DataFrame

'''读取'''


def readFromExcel(file_path, sheet_name, row_num):
    df = pd.read_excel(file_path, sheet_name)
    result = df.values[row_num].tolist()
    return result


'''写入'''


def writeToExcel(file_path, sheet_name, content):
    df1 = DataFrame(pd.read_excel(file_path, sheet_name))
    df2 = df1.append(content, ignore_index=True)
    try:
        df2.to_excel(file_path, index=False)
    except PermissionError as e:
        print('目标excel还没关闭，没法写入！！！')
        raise e


'''删除指定行'''


def delete_row(file_path, num):
    wb = load_workbook(file_path)
    ws = wb.active
    ws.delete_rows(num)
    wb.save(file_path)


'''删除多行'''


def delete_more_rows(file_path, num):
    try:
        for i in range(num, -1, -1):
            delete_row(file_path, i)

    except PermissionError as e:
        print('目标excel还没关闭,没法删除！！！')
        raise e
