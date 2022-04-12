import json
import xlrd



def read_json(filename):
    filepath = "../data/"+filename
    #获取文件流 并调用load
    with open(filepath,"r",encoding="utf-8") as f:
        return json.load(f)

def get_socail_excel_data():
    xls = xlrd.open_workbook("../data/data.xlsx")
    sheet = xls.sheet_by_index(0)
    list = []
    for r in range(sheet.nrows):
        list.append(sheet.row_values(r))
    return list

def get_campus_excel_data():
    xls = xlrd.open_workbook("../data/data.xlsx")
    sheet = xls.sheet_by_index(1)
    list = []
    for r in range(sheet.nrows):
        list.append(sheet.row_values(r))
    return list


def get_user():
    xls = xlrd.open_workbook("../data/data.xlsx")
    sheet = xls.sheet_by_index(2)
    list = sheet.col_values(0)
    return list



