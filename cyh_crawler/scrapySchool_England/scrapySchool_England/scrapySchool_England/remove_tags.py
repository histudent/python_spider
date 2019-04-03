import re
from scrapySchool_England.clearSpace import clear_same_s
# 去除标签中的属性和a标签
def remove_class(var):
    var=''.join(var)
    #清洗标签
    clear_class=re.findall('[a-zA-Z\-]*=[\'\"].+[\'\"]', var)
    for i in clear_class:
        var=var.replace(' ' + i, '')
    #去除a标签
    var = var.replace('<a>', '').replace('</a>', '')
    #去除注释
    fan_ren_de_biao_qian=re.findall('<!.+>',var)
    for i in fan_ren_de_biao_qian:
        var=var.replace(i,'')
    var=clear_same_s(var)
    return var