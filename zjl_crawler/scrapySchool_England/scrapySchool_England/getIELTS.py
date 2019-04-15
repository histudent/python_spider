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