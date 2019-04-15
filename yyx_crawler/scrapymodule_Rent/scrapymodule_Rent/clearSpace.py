

# 对字符串进行循环处理，去除\n\r\t标签，以及行首行尾空格
def clear_space_str(str):
    str = str.replace("\n", "").replace("\r", "").replace('\t', "").strip()
    return str

# 对列表进行循环处理，去除\n\r\t标签，以及行首行尾空格
def clear_space(templist):
    for i in range(len(templist)):
        templist[i] = clear_space_str(templist[i])

# 去除列表中连续的空格
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