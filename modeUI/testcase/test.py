from modeAPI.case.create_lots_of_orders import DataCombo

from utils import get_excel

file_path = r'C:\Users\Administrator\[AutoTest]import_mode.xlsx'

DataCombo().create_more_order(file_path, 10)
get_excel.delete_more_rows(file_path, 11)
