import json

import xlrd


def read_txt(filename):
    filepath = "../data/{}".format(filename)
    with open(filepath,mode="r",encoding="utf-8") as f:
       return f.readlines()

def get_txt_data(filename):
    arr=[]
    for data in read_txt(filename):
        # arr.append(tuple(data.strip().split("，")))
        arr.append(tuple(data.strip().split(",")))
    return arr[1:]


def read_json(filename):

    filepath = "../data/"+filename
    #获取文件流 并调用load
    with open(filepath,"r",encoding="utf-8") as f:
        return json.load(f)

def read_excel(filename):
    xls = xlrd.open_workbook("../data/{}".format(filename))
    sheet = xls.sheet_by_index(0)
    list = []
    for r in range(sheet.nrows):
        list.append(tuple(sheet.row_values(r)))
    return list



if __name__ == '__main__':
    #读取txt文件返回列表
    print(read_txt("account.txt"))
    print("*"*50)
    arr = []
    for data in read_txt("account.txt"):
        print(data)
        print(type(data))
        # arr.append(tuple(data.strip().split("，")))
        arr.append(tuple(data.strip().split(",")))


    print(arr[1:])
    print(arr[1:][0][0])
    # print(read_json("login.json"))
    # print(read_excel("data.xlsx"))
