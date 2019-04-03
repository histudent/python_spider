# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ScrapyschoolCanadaCollegeSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyschoolCanadaCollegeDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
'''去空格'''
# 对字符串进行循环处理，去除\n\r\t标签，以及行首行尾空格
def clear_space_str(str):
    str = str.replace("\n", "").replace("\r", "").replace('\t', "").replace("  ", "").strip()
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


'''获取雅思/托福'''
import re
# 仅限于两个分数的，一个总分，一个统一的小分
# 从文本中正则匹配雅思分数进行拆分， 返回一个雅思字典
def get_ielts(ieltsStr):
    ieltDict = {}
    ieltlsrw = re.findall(r"\d\.\d", ieltsStr)
    ieltlsrw = re.findall(r"[\d\.]{1,4}", ieltsStr)
    if len(ieltlsrw) >= 2:
        ieltDict['IELTS'] = ieltlsrw[0]
        ieltDict['IELTS_L'] = ieltlsrw[1]
        ieltDict['IELTS_S'] = ieltlsrw[1]
        ieltDict['IELTS_R'] = ieltlsrw[1]
        ieltDict['IELTS_W'] = ieltlsrw[1]
    elif len(ieltlsrw) == 1:
        ieltDict['IELTS'] = ieltlsrw[0]
        ieltDict['IELTS_L'] = ieltlsrw[0]
        ieltDict['IELTS_S'] = ieltlsrw[0]
        ieltDict['IELTS_R'] = ieltlsrw[0]
        ieltDict['IELTS_W'] = ieltlsrw[0]
    return ieltDict

# 从文本中正则匹配托福分数进行拆分， 返回一个托福字典
def get_toefl(toeflStr):
    toeflDict = {}
    toefllsrw = re.findall(r"\d+", toeflStr)
    # print(toefllsrw)
    if len(toefllsrw) >= 2:
        toeflDict['TOEFL'] = toefllsrw[0]
        toeflDict['TOEFL_L'] = toefllsrw[1]
        toeflDict['TOEFL_S'] = toefllsrw[1]
        toeflDict['TOEFL_R'] = toefllsrw[1]
        toeflDict['TOEFL_W'] = toefllsrw[1]
    elif len(toefllsrw) == 1:
        toeflDict['TOEFL'] = toefllsrw[0]
        toeflDict['TOEFL_L'] = toefllsrw[0]
        toeflDict['TOEFL_S'] = toefllsrw[0]
        toeflDict['TOEFL_R'] = toefllsrw[0]
        toeflDict['TOEFL_W'] = toefllsrw[0]
    return toeflDict

'''获取学费'''
# 获取学费当中的最大值
def getTuition_fee(str):
    allfee = re.findall(r'\d+,\d+', str)
    # print(allfee)
    for index in range(len(allfee)):
        fee = allfee[index].split(",")
        allfee[index] = ''.join(fee)
        # print(allfee[index])
    # print(allfee)
    maxfee = 0
    for fee in allfee:
        if int(fee) >= maxfee:
            maxfee = int(fee)
    return maxfee

def getT_fee(str):
    allfee = re.findall(r'\d{5}', str)
    maxfee = 0
    for fee in allfee:
        if int(fee) >= maxfee:
            maxfee = int(fee)
    return maxfee

'''去除标签'''
import re
# 去除标签中的属性和a标签
def remove_class(var):
    # 正则匹配各个标签的属性，然后逐个替换
    var=''.join(var)
    clear_class = re.findall('[\w\-]*=".*?"|[\w\-]*=\'.*?\'', var)
    # print(clear_class)
    for i in clear_class:
        var = var.replace(' ' + i, '')
    for i in clear_class:
        var = var.replace(i, '')
    cc=re.findall('\s{2,}',var)
    for i in cc:
        var = var.replace(i,'')

    # 正则匹配不需要的标签以及内带的内容
    clear_class1 = re.findall('<script[\w\W]*?</script>|<iframe[\w\W]*?</iframe>|<style[\w\W]*?</style>|<svg[\w\W]*?</svg>|<!--[\w\W]*?-->|<button[\w\W]*?</button>|<img.*?>', var)
    for i1 in clear_class1:
        var = var.replace(i1, '')

    #  替换掉没用的标签，有新的发现需要替换的标签，需要大家一致修改
    var = var.replace(' >', '')
    var = var.replace('<meta>', '').replace('<link>', '').replace('<noscript></noscript>', '')
    var = var.replace('<a>', '').replace('</a>', '').replace('> <', '><').replace('> <', '><').replace('> ', '>').replace(' <', '<').strip()
    return var
def clear_duration(var):
    var=''.join(var)
    var=var.replace('One','1').replace('one','1').replace('Two','2').replace('two','2').replace('Three','3').replace('three','3')
    var=var.replace('Four','4').replace('four','4').replace('Five','5').replace('five','5')
    dura=re.findall('\d{1,2}\s*[a-zA-Z]{4,6}',var)
    duration=[]
    duration_per=[]
    for i in dura:
        duration.append(''.join(re.findall('\d+',i)))
        duration_per.append(''.join(re.findall('[a-zA-Z]+',i)))
    if duration==[]:
        return {'duration':None,'duration_per':None}
    try:
        durat=list(map(int,duration))
        dura_min=duration.index(str(min(durat)))
        dura_per=duration_per[dura_min]
        if 'year' in dura_per or 'years'in dura_per or 'Years' in dura_per or 'Year' in dura_per:
            dura_per=1
        elif 'month' in dura_per or 'months' in dura_per or 'Months' in dura_per:
            dura_per=3
        elif 'week' in dura_per or 'weeks' in dura_per or 'Week' in dura_per or 'Weeks' in dura_per or 'taught' in dura_per:
            dura_per=4
        elif 'semesters' in dura_per or 'semester' in dura_per or 'trimesters' in dura_per or 'trimester' in dura_per:
            dura_per=2
        else:
            dura_per=None
        return {'duration':min(durat),'duration_per':dura_per}
    except:
        return {'duration':'','duration_per':''}



def tracslateDate(var):
    var=''.join(var).strip()
    date=re.findall('\d{0,2}\s?[A-Z][a-z]+\s\d{4}',var)
    if date==[]:
        date=re.findall('(September|January|February|March|April|May|June|July|August|October|November|December)',var,re.S)
    if date==[]:
        date=re.findall('(Feb|Apr|Jun|Aug|Oct|Nov|Mar|May|Jul|Jan|Sep|Dec)',var,re.S)
    cout=[]
    for i in date:
        years = ''.join(re.findall('\d{4}',i)).strip()
        day = ''.join(re.findall('[0-3]?[0-9]\s', i)).strip()
        i = i.replace(years,'').strip()
        i = i.replace(day,'').strip()
        if years=='':
            years='2019'
        if years != '':
            i = years + '-' + i
        if day != '':
            i = i + '-' + day
        i = i.strip()
        i = i.replace('January', '1').replace('February', '2').replace('March', '3').replace('April', '4')
        i = i.replace('May', '5').replace('June', '6').replace('July', '7').replace('August', '8')
        i = i.replace('September', '9').replace('October', '10').replace('November', '11').replace('December', '12')
        i = i.replace('Jan', '1').replace('Feb', '2').replace('Mar', '3').replace('Apr', '4')
        i = i.replace('May', '5').replace('Jun', '6').replace('Jul', '7').replace('Aug', '8')
        i = i.replace('Sep', '9').replace('Oct', '10').replace('Nov', '11').replace('Dec', '12')
        cout.append(i)
    return cout