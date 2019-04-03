import re

# 获取学费当中的最大值
def getTuition_fee(var):
    var = ''.join(var)
    fee = re.findall('£?\d+,?\d{0,3}', var)
    fee = '-'.join(fee).replace(',', '').replace('£', '')
    fee = fee.split('-')
    try:
        fee = list(map(int, fee))
        fee = max(fee)
        return fee
    except:
        return 0