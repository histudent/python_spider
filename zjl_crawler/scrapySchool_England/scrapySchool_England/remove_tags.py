import re

# 去除标签中的属性和a标签
def remove_class(var):
    # 正则匹配各个标签的属性，然后逐个替换
    clear_class = re.findall('[\w\-]*=".*?"|[\w\-]*=\'.*?\'', var)
    # print(clear_class)
    for i in clear_class:
        var = var.replace(' ' + i, '')
    for i in clear_class:
        var = var.replace(i, '')

    # 正则匹配不需要的标签以及内带的内容
    clear_class1 = re.findall('<script[\w\W]*?</script>|<iframe[\w\W]*?</iframe>|<style[\w\W]*?</style>|<svg[\w\W]*?</svg>|<!--[\w\W]*?-->|<button[\w\W]*?</button>|<img.*?>', var)
    for i1 in clear_class1:
        var = var.replace(i1, '')

    #  替换掉没用的标签，有新的发现需要替换的标签，需要大家一致修改
    var = var.replace(' >', '')
    var = var.replace('<meta>', '').replace('<link>', '').replace('<noscript></noscript>', '')
    var = var.replace('<a>', '').replace('</a>', '').replace('> <', '><').replace('> <', '><').replace('> ', '>').replace(' <', '<').strip()
    return var