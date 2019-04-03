import re

# 去除标签中的属性和a标签,字符串
def remove_class(var):
    clear_class=re.findall('[a-zA-Z\-:]*=".+?"|[a-zA-Z\-:]*=\'.+?\'', var)
    for i in clear_class:
        var=var.replace(' ' + i, '')

    # clear_class = re.findall('[a-zA-Z\-]*=".+?"', var)
    # for i in clear_class:
    #     var = var.replace(' ' + i, '')

    clear_class1 = re.findall('<script>.*?</script>', var)
    for i1 in clear_class1:
        var = var.replace(i1, '')
    var = var.replace('<a>', '').replace('</a>', '').replace('> <', '><').replace('> ', '>').replace(' <', '<').strip()
    return var