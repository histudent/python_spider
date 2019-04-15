import re

# 去除标签中的属性和a标签
def remove_class(var):
    clear_class=re.findall('[a-zA-Z\-]*=".+?"', var)
    for i in clear_class:
        var=var.replace(' ' + i, '')
    var = var.replace('<a>', '').replace('</a>', '')
    return var