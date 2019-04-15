# -*- coding: utf-8 -*-

'''去空格'''
# 对字符串进行循环处理，去除\n\r\t标签，以及行首行尾空格
def clear_space_str(str):
    str = str.replace("\n", "").replace("\r", "").replace('\t', "").replace("  ", "").strip()
    return str

# 对列表进行循环处理，去除\n\r\t标签，以及行首行尾空格
def clear_space(templist):
    for i in range(len(templist)):
        templist[i] = clear_space_str(templist[i])

# 去除列表中字符串连续的空格
def clear_lianxu_space(templist):
    clear_space(templist)
    while '' in templist:
        templist.remove('')
    templist1Str = '\n'.join(templist).strip()
    return templist1Str


def clear_space_list(templist):
    for i in range(len(templist)):
        templist[i] = templist[i].replace('\n', " ")
        templist[i] = templist[i].strip(" ")
        templist[i] = templist[i].replace('\r', " ")
        templist[i] = templist[i].replace('\t', " ")
    return templist


'''获取雅思/托福'''
import re
# 仅限于两个分数的，一个总分，一个统一的小分
# 从文本中正则匹配雅思分数进行拆分， 返回一个雅思字典
def get_ielts(ieltsStr):
    ieltDict = {}
    ieltlsrw = re.findall(r"\d\.\d", ieltsStr)
    ieltlsrw = re.findall(r"[\d\.]{1,4}", ieltsStr)
    if len(ieltlsrw) >= 2:
        ieltDict['IELTS'] = ieltlsrw[0]
        ieltDict['IELTS_L'] = ieltlsrw[1]
        ieltDict['IELTS_S'] = ieltlsrw[1]
        ieltDict['IELTS_R'] = ieltlsrw[1]
        ieltDict['IELTS_W'] = ieltlsrw[1]
    elif len(ieltlsrw) == 1:
        ieltDict['IELTS'] = ieltlsrw[0]
        ieltDict['IELTS_L'] = ieltlsrw[0]
        ieltDict['IELTS_S'] = ieltlsrw[0]
        ieltDict['IELTS_R'] = ieltlsrw[0]
        ieltDict['IELTS_W'] = ieltlsrw[0]
    return ieltDict

# 从文本中正则匹配托福分数进行拆分， 返回一个托福字典
def get_toefl(toeflStr):
    toeflDict = {}
    toefllsrw = re.findall(r"\d+", toeflStr)
    # print(toefllsrw)
    if len(toefllsrw) >= 2:
        toeflDict['TOEFL'] = toefllsrw[0]
        toeflDict['TOEFL_L'] = toefllsrw[1]
        toeflDict['TOEFL_S'] = toefllsrw[1]
        toeflDict['TOEFL_R'] = toefllsrw[1]
        toeflDict['TOEFL_W'] = toefllsrw[1]
    elif len(toefllsrw) == 1:
        toeflDict['TOEFL'] = toefllsrw[0]
        toeflDict['TOEFL_L'] = toefllsrw[0]
        toeflDict['TOEFL_S'] = toefllsrw[0]
        toeflDict['TOEFL_R'] = toefllsrw[0]
        toeflDict['TOEFL_W'] = toefllsrw[0]
    return toeflDict

'''获取学费'''
# 获取学费当中的最大值
def getTuition_fee(str):
    allfee = re.findall(r'\d+,\d+', str)
    # print(allfee)
    for index in range(len(allfee)):
        fee = allfee[index].split(",")
        allfee[index] = ''.join(fee)
        # print(allfee[index])
    # print(allfee)
    maxfee = 0
    for fee in allfee:
        if int(fee) >= maxfee:
            maxfee = int(fee)
    return maxfee

def getT_fee(str):
    allfee = re.findall(r'\d{5}', str)
    maxfee = 0
    for fee in allfee:
        if int(fee) >= maxfee:
            maxfee = int(fee)
    return maxfee

'''去除标签'''
import re
# 去除标签中的属性和a标签
def remove_class(var):
    clear_class=re.findall('[a-zA-Z\-]*=".+?"', var)
    for i in clear_class:
        var=var.replace(' ' + i, '')
    var = var.replace('<a>', '').replace('</a>', '')
    return var