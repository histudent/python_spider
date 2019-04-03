import re

# 仅限于两个分数的，一个总分，一个统一的小分
# 从文本中正则匹配雅思分数进行拆分， 返回一个雅思字典
def get_ielts(ieltsStr):
    ieltDict = {}
    ieltsStr=''.join(ieltsStr)
    ieltlsrw = re.findall(r"[4-9]\.?\d?", ieltsStr)
    ieltlsrw=list(map(float,ieltlsrw))
    if len(ieltlsrw) == 2:
        ieltDict['IELTS'] = max(ieltlsrw)
        ieltDict['IELTS_L'] = min(ieltlsrw)
        ieltDict['IELTS_S'] = min(ieltlsrw)
        ieltDict['IELTS_R'] = min(ieltlsrw)
        ieltDict['IELTS_W'] = min(ieltlsrw)
    elif len(ieltlsrw) == 1:
        ieltDict['IELTS'] = ieltlsrw[0]
        ieltDict['IELTS_L'] = ieltlsrw[0]
        ieltDict['IELTS_S'] = ieltlsrw[0]
        ieltDict['IELTS_R'] = ieltlsrw[0]
        ieltDict['IELTS_W'] = ieltlsrw[0]
    else:
        return ieltlsrw
    return ieltDict

# 从文本中正则匹配托福分数进行拆分， 返回一个托福字典
def get_toefl(toeflStr):
    toeflDict = {}
    toeflStr=''.join(toeflStr)
    toefllsrw = re.findall(r"\d{1,3}", toeflStr)
    # print(toefllsrw)
    toefllsrw=list(map(int,toefllsrw))
    if len(toefllsrw) == 2:
        toeflDict['TOEFL'] = max(toefllsrw)
        toeflDict['TOEFL_L'] = min(toefllsrw)
        toeflDict['TOEFL_S'] = min(toefllsrw)
        toeflDict['TOEFL_R'] = min(toefllsrw)
        toeflDict['TOEFL_W'] = min(toefllsrw)
    elif len(toefllsrw) == 1:
        toeflDict['TOEFL'] = toefllsrw[0]
        toeflDict['TOEFL_L'] = toefllsrw[0]
        toeflDict['TOEFL_S'] = toefllsrw[0]
        toeflDict['TOEFL_R'] = toefllsrw[0]
        toeflDict['TOEFL_W'] = toefllsrw[0]
    else:
        return toefllsrw
    return toeflDict