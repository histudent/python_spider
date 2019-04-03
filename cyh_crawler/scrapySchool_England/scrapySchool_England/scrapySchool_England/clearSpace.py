import re
def clear_same_s(strs):
    strs=''.join(strs).replace("\r", "").replace('\t', "")
    fan_ren_de_kong_ge=re.findall('  ',strs)
    if fan_ren_de_kong_ge !=[]:
        for i in fan_ren_de_kong_ge:
            strs=strs.replace(i,'')
    strs=strs.split('\n')
    while '' in strs:
        strs.remove('')
    strs='\n'.join(strs)
    return strs


# 对字符串进行循环处理，去除\n\r\t标签，以及行首行尾空格
def clear_space_str(str):
    str = str.replace("\r", "").replace('\n','').replace('\t', "").strip()
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