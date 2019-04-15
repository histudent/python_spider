import re

# 仅限于两个分数的，一个总分，一个统一的小分
# 从文本中正则匹配雅思分数进行拆分， 返回一个雅思字典
def get_ielts(ieltsStr):
    ieltDict = {}
    ieltlsrw = re.findall(r"\d\.\d", ieltsStr)
    ieltlsrw = re.findall(r"\d[\d\.]{0,2}\s", ieltsStr)
    ieltlsrw = re.findall(r"\d[\d\.]{0,2}", ieltsStr)
    # print(ieltlsrw)
    if len(ieltlsrw) == 2:
        ieltDict['IELTS'] = ieltlsrw[0].strip()
        ieltDict['IELTS_L'] = ieltlsrw[1].strip()
        ieltDict['IELTS_S'] = ieltlsrw[1].strip()
        ieltDict['IELTS_R'] = ieltlsrw[1].strip()
        ieltDict['IELTS_W'] = ieltlsrw[1].strip()
    elif len(ieltlsrw) == 1:
        ieltDict['IELTS'] = ieltlsrw[0].strip()
        ieltDict['IELTS_L'] = ieltlsrw[0].strip()
        ieltDict['IELTS_S'] = ieltlsrw[0].strip()
        ieltDict['IELTS_R'] = ieltlsrw[0].strip()
        ieltDict['IELTS_W'] = ieltlsrw[0].strip()
    elif len(ieltlsrw) == 5:
        ieltDict['IELTS'] = ieltlsrw[0].strip()
        ieltDict['IELTS_L'] = ieltlsrw[3].strip()
        ieltDict['IELTS_S'] = ieltlsrw[4].strip()
        ieltDict['IELTS_R'] = ieltlsrw[2].strip()
        ieltDict['IELTS_W'] = ieltlsrw[1].strip()
    return ieltDict

# 从文本中正则匹配托福分数进行拆分， 返回一个托福字典
def get_toefl(toeflStr):
    toeflDict = {}
    toefllsrw = re.findall(r"\d\d+", toeflStr)
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

# print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
#                     item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))
# print("item['toefl'] = %s item['toefl_l'] = %s item['toefl_s'] = %s item['toefl_r'] = %s item['toefl_w'] = %s " % (
#                     item['toefl'], item['toefl_l'], item['toefl_s'], item['toefl_r'], item['toefl_w']))
