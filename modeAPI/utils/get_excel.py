'''pandas操作excel'''
import pandas as pd

'''读取'''

def readFromExcel(file_path, sheet_name ,row_num):
    df = pd.read_excel(file_path, sheet_name)
    result = df.values[row_num].tolist()
    return result
