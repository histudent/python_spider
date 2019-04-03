# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import re
import datetime
def clear_long_text(var):
    var=''.join(var).strip()
    var=re.split('\s{2,}',var)
    var=' '.join(var)
    return var

def find_fee_s(var):
    var=''.join(var)
    fee=re.findall('\$\d{0,3},?\d{0,3}',var)
    fee='-'.join(fee).replace(',','').replace('$','')
    fee=fee.split('-')
    try:
        fee=list(map(int,fee))
        fee=max(fee)
        return fee
    except:
        return ''

def find_title(var,longvar):
    try:
        cout=longvar[longvar.index(var):]
        cout=''.join(cout).strip()
        return cout
    except:
        return ''

def index_1(var,text,num):
    try:
        cout=text.index(var)+num
        cout=text[cout]
        return cout
    except:
        return ''

def get_index(title,var,num):
    try:
        index=title.index(var)
        cout=title[index+num].strip()
        return cout
    except:
        return ''




class AustraliaSpiderMiddleware(object):
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


class AustraliaDownloaderMiddleware(object):
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

def get_item(itemClass):
    item=itemClass()
    item['university'] = ""
    item['location'] = ""
    item['major_type1'] = ""
    item['major_type2'] = ""
    item['department'] = ""
    item['degree_type'] = 0
    item['degree_name'] = ""
    item['degree_overview_en'] = ""
    item['degree_overview_cn'] = ""
    item['programme_en'] = ""
    item['programme_cn'] = ""
    item['overview_en'] = ""
    item['overview_cn'] = ""
    item['start_date'] = ""
    item['duration'] = ""
    item['duration_per'] = None
    item['modules_en'] = ""
    item['modules_cn'] = ""
    item['career_en'] = ""
    item['career_cn'] = ""
    item['application_open_date'] = ""
    item['deadline'] = ""
    item['apply_pre'] = ""
    item['apply_fee'] = ""
    item['tuition_fee_pre'] = ""
    item['tuition_fee'] = ""
    item['rntry_requirements_en'] = ""
    item['rntry_requirements_cn'] = ""
    item['degree_requirements'] = ""
    item['major_requirements'] = ""
    item['professional_background'] = ""
    item['average_score'] = ""
    item['ielts_desc'] = ""
    item['ielts'] = ""
    item['ielts_l'] = ""
    item['ielts_s'] = ""
    item['ielts_r'] = ""
    item['ielts_w'] = ""
    item['toefl_code'] = ""
    item['toefl_desc'] = ""
    item['toefl'] = ""
    item['toefl_l'] = ""
    item['toefl_s'] = ""
    item['toefl_r'] = ""
    item['toefl_w'] = ""
    item['china_score_requirements'] = ""
    item['interview_desc_en'] = ""
    item['interview_desc_cn'] = ""
    item['portfolio_desc_en'] = ""
    item['portfolio_desc_cn'] = ""
    item['apply_documents_en'] = ""
    item['apply_documents_cn'] = ""
    item['apply_desc_en'] = ""
    item['apply_desc_cn'] = ""
    item['apply_proces_en'] = ""
    item['apply_proces_cn'] = ""
    item['other'] = ""
    item['url'] = ""
    item['gatherer'] = "cyh"
    item['finishing'] = 0
    item['create_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item['import_status'] = 0
    return item
#清洗课程长度
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
#转换日期
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
        i = i.replace('January', '01').replace('February', '02').replace('March', '03').replace('April', '04')
        i = i.replace('May', '05').replace('June', '06').replace('July', '07').replace('August', '08')
        i = i.replace('September', '09').replace('October', '10').replace('November', '11').replace('December', '12')
        i = i.replace('Jan', '01').replace('Feb', '02').replace('Mar', '03').replace('Apr', '04')
        i = i.replace('May', '05').replace('Jun', '06').replace('Jul', '07').replace('Aug', '08')
        i = i.replace('Sep', '09').replace('Oct', '10').replace('Nov', '11').replace('Dec', '12')
        cout.append(i)
    return cout
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
#清洗标签
def remove_class(var):
    var=''.join(var)
    #清洗标签
    clear_class=re.findall('[a-zA-Z\-]*=[\'\"].+?[\'\"]', var)
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
#获取雅思
def get_ielts(ieltsStr):
    ieltDict = {}
    ieltsStr=''.join(ieltsStr)
    ieltlsrw = re.findall(r"[4-9]\.\d?", ieltsStr)
    ieltlsrw=list(map(float,ieltlsrw))
    if len(ieltlsrw) >= 2:
        ieltDict['IELTS'] = max(ieltlsrw)
        ieltDict['IELTS_L'] = min(ieltlsrw)
        ieltDict['IELTS_S'] = min(ieltlsrw)
        ieltDict['IELTS_R'] = min(ieltlsrw)
        ieltDict['IELTS_W'] = min(ieltlsrw)
    elif len(ieltlsrw) == 1:
        ieltDict['IELTS'] = ieltlsrw[0]
        ieltDict['IELTS_L'] = ieltlsrw[0]
        ieltDict['IELTS_S'] = ieltlsrw[0]
        ieltDict['IELTS_R'] = ieltlsrw[0]
        ieltDict['IELTS_W'] = ieltlsrw[0]
    else:
        return ieltlsrw
    return ieltDict
#获取学费
def getTuition_fee(var):
    var = ' '.join(var)
    fee = re.findall('\d+,?\d{0,3}',var)
    fee = '-'.join(fee).replace(',', '').replace('£', '')
    fee = fee.split('-')
    try:
        fee = list(map(int, fee))
        fee = max(fee)
        return fee
    except:
        return 0
def clear_long_text(text):
    try:
        text = remove_class(text)
        text = text.split('\n')
        text = '<p/><p>'.join(text)
        text = '<div><p>' + text + '</p></div>'
        return text
    except:
        return ''