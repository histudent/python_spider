import re

# 去除标签中的属性和a标签,字符串
def remove_class(var):
    clear_class=re.findall('[a-zA-Z0-9\-_]*=".+?"|[a-zA-Z\-]*=\'.+?\'', var)
    for i in clear_class:
        var=var.replace(' ' + i, '')

    clear_class2 = re.findall('<!--.*-->"', var)
    for i in clear_class2:
        var = var.replace(i, '')

    clear_class1 = re.findall('<script>.*?</script>', var)
    for i1 in clear_class1:
        var = var.replace(i1, '')

    clear_class3 = re.findall('<iframe.*?</iframe>', var)
    for i3 in clear_class3:
        var = var.replace(i3, '')

    clear_class4 = re.findall(
        '<!--[\w\W]*?-->|<button[\w\W]*?</button>|<img.*?>',
        var)
    for i1 in clear_class4:
        var = var.replace(i1, '')
    var = var.replace('<a>', '').replace('</a>', '').replace('> <', '><').replace('> ', '>').replace(' <', '<').replace('<!---->', '').strip()
    return var