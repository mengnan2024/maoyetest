'''pandas操作excel'''
import pandas as pd

'''读取'''

def readFromExcel():
    file_path = r'C:\Users\Administrator\Desktop\新建 XLSX 工作表.xlsx'
    df = pd.read_excel(file_path, sheet_name='订单相关')
    result = df.values[4].tolist()
    return result
