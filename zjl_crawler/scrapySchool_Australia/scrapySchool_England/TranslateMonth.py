# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/4 10:51'
def translate_month(str):
    list_of_months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    # str = str.split()
    for i in range(0,12):
        if list_of_months[i] in str:
            str = int(i+1)
            return str
        else:
            pass

