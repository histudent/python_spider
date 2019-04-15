# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/6 10:36'
import re
def tracslateDate(var):
    var=''.join(var).strip()
    date=re.findall('\d{0,2}\s?[A-Z][a-z]+\s\d{0,4}',var)
    cout=[]
    for i in date:
        years = ''.join(re.findall('\d{4}',i)).strip()
        day = ''.join(re.findall('[0-3]?[0-9]\s', i)).strip()
        i = i.replace(years,'').strip()
        i = i.replace(day,'').strip()
        if years != '':
            i = years + '-' + i
        if day != '':
            i = i + '-' + day
        i = i.strip()
        i = i.replace('January', '1').replace('February', '2').replace('March', '3').replace('April', '4')
        i = i.replace('May', '5').replace('June', '6').replace('July', '7').replace('August', '8')
        i = i.replace('September', '9').replace('October', '10').replace('November', '11').replace('December', '12')
        cout.append(i)
    return cout