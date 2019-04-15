# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/18 14:32'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from w3lib.html import remove_tags
from scrapySchool_England.clearSpace import clear_space_str
from lxml import etree
import requests
class TheAustralianNationalUniversitySpider(scrapy.Spider):
    name = 'TheAustralianNationalUniversity_p'
    allowed_domains = ['anu.edu.au/']
    start_urls = []
    C = [
        'https://programsandcourses.anu.edu.au/2019/program/MJD',
        'https://programsandcourses.anu.edu.au/2019/program/7330HJD',
        'https://programsandcourses.anu.edu.au/2019/program/7414XMACCT',
        'https://programsandcourses.anu.edu.au/2019/program/7420XMACTP',
        'https://programsandcourses.anu.edu.au/2019/program/7410XMACTS',
        'https://programsandcourses.anu.edu.au/2019/program/MANTH',
        'https://programsandcourses.anu.edu.au/2019/program/VANTH',
        'https://programsandcourses.anu.edu.au/2019/program/MAAPD',
        'https://programsandcourses.anu.edu.au/2019/program/MAAPO',
        'https://programsandcourses.anu.edu.au/2019/program/VAAPD',
        'https://programsandcourses.anu.edu.au/2019/program/VAAPO',
        'https://programsandcourses.anu.edu.au/2019/program/MADAN',
        'https://programsandcourses.anu.edu.au/2019/program/MAPEC',
        'https://programsandcourses.anu.edu.au/2019/program/7421XMAPFN',
        'https://programsandcourses.anu.edu.au/2019/program/MAESC',
        'https://programsandcourses.anu.edu.au/2019/program/VAESC',
        'https://programsandcourses.anu.edu.au/2019/program/VARSC',
        'https://programsandcourses.anu.edu.au/2019/program/MAHCS',
        'https://programsandcourses.anu.edu.au/2019/program/VAHCS',
        'https://programsandcourses.anu.edu.au/2019/program/MMUAU',
        'https://programsandcourses.anu.edu.au/2019/program/MANPS',
        'https://programsandcourses.anu.edu.au/2019/program/VANPS',
        'https://programsandcourses.anu.edu.au/2019/program/VASTP',
        'https://programsandcourses.anu.edu.au/2019/program/VBIAN',
        'https://programsandcourses.anu.edu.au/2019/program/MBIOT',
        'https://programsandcourses.anu.edu.au/2019/program/VBIOT',
        'https://programsandcourses.anu.edu.au/2019/program/MBADM',
        'https://programsandcourses.anu.edu.au/2019/program/VBADM',
        'https://programsandcourses.anu.edu.au/2019/program/MBINS',
        'https://programsandcourses.anu.edu.au/2019/program/VBINS',
        'https://programsandcourses.anu.edu.au/2019/program/VCLAS',
        'https://programsandcourses.anu.edu.au/2019/program/MCLCH',
        'https://programsandcourses.anu.edu.au/2019/program/7601XMCPSY',
        'https://programsandcourses.anu.edu.au/2019/program/VCOMM',
        'https://programsandcourses.anu.edu.au/2019/program/7706XMCOMP',
        'https://programsandcourses.anu.edu.au/2019/program/VCOMP',
        'https://programsandcourses.anu.edu.au/2019/program/MCRJR',
        'https://programsandcourses.anu.edu.au/2019/program/VCRJR',
        'https://programsandcourses.anu.edu.au/2019/program/MCSRM',
        'https://programsandcourses.anu.edu.au/2019/program/MDEMO',
        'https://programsandcourses.anu.edu.au/2019/program/VDEMO',
        'https://programsandcourses.anu.edu.au/2019/program/MDESN',
        'https://programsandcourses.anu.edu.au/2019/program/VDESN',
        'https://programsandcourses.anu.edu.au/2019/program/VDIGA',
        'https://programsandcourses.anu.edu.au/2019/program/MDHPC',
        'https://programsandcourses.anu.edu.au/2019/program/VDHPC',
        'https://programsandcourses.anu.edu.au/2019/program/MDIPL',
        'https://programsandcourses.anu.edu.au/2019/program/VDIPL',
        'https://programsandcourses.anu.edu.au/2019/program/VEASC',
        'https://programsandcourses.anu.edu.au/2019/program/MECPO',
        'https://programsandcourses.anu.edu.au/2019/program/MECON',
        'https://programsandcourses.anu.edu.au/2019/program/MENCH',
        'https://programsandcourses.anu.edu.au/2019/program/VENCH',
        'https://programsandcourses.anu.edu.au/2019/program/NDSTE',
        'https://programsandcourses.anu.edu.au/2019/program/NELENG',
        'https://programsandcourses.anu.edu.au/2019/program/NMECH',
        'https://programsandcourses.anu.edu.au/2019/program/NENPH',
        'https://programsandcourses.anu.edu.au/2019/program/NENRE',
        'https://programsandcourses.anu.edu.au/2019/program/MEINV',
        'https://programsandcourses.anu.edu.au/2019/program/VEINV',
        'https://programsandcourses.anu.edu.au/2019/program/MENVI',
        'https://programsandcourses.anu.edu.au/2019/program/VENVI',
        'https://programsandcourses.anu.edu.au/2019/program/MEREC',
        'https://programsandcourses.anu.edu.au/2019/program/MEMDV',
        'https://programsandcourses.anu.edu.au/2019/program/MEMOL',
        'https://programsandcourses.anu.edu.au/2019/program/VEMDV',
        'https://programsandcourses.anu.edu.au/2019/program/MENVS',
        'https://programsandcourses.anu.edu.au/2019/program/VENVS',
        'https://programsandcourses.anu.edu.au/2019/program/7418XMFIN',
        'https://programsandcourses.anu.edu.au/2019/program/MFIEC',
        'https://programsandcourses.anu.edu.au/2019/program/MFINM',
        'https://programsandcourses.anu.edu.au/2019/program/MFORE',
        'https://programsandcourses.anu.edu.au/2019/program/VFORE',
        'https://programsandcourses.anu.edu.au/2019/program/MLING',
        'https://programsandcourses.anu.edu.au/2019/program/VLING',
        'https://programsandcourses.anu.edu.au/2019/program/VGLOB',
        'https://programsandcourses.anu.edu.au/2019/program/MHIST',
        'https://programsandcourses.anu.edu.au/2019/program/VHIST',
        'https://programsandcourses.anu.edu.au/2019/program/MINPP',
        'https://programsandcourses.anu.edu.au/2019/program/MIDEC',
        'https://programsandcourses.anu.edu.au/2019/program/MIDNK',
        'https://programsandcourses.anu.edu.au/2019/program/MIMGT',
        'https://programsandcourses.anu.edu.au/2019/program/VIMGT',
        'https://programsandcourses.anu.edu.au/2019/program/MINTR',
        'https://programsandcourses.anu.edu.au/2019/program/VINTR',
        'https://programsandcourses.anu.edu.au/2019/program/VIIMW',
        'https://programsandcourses.anu.edu.au/2019/program/MLLM',
        'https://programsandcourses.anu.edu.au/2019/program/MLEAD',
        'https://programsandcourses.anu.edu.au/2019/program/VLEAD',
        'https://programsandcourses.anu.edu.au/2019/program/MMLCV',
        'https://programsandcourses.anu.edu.au/2019/program/VMGMT',
        'https://programsandcourses.anu.edu.au/2019/program/MMGMTSH',
        'https://programsandcourses.anu.edu.au/2019/program/MMKMT',
        'https://programsandcourses.anu.edu.au/2019/program/VMKMT',
        'https://programsandcourses.anu.edu.au/2019/program/VMASC',
        'https://programsandcourses.anu.edu.au/2019/program/MMECA',
        'https://programsandcourses.anu.edu.au/2019/program/VMECA',
        'https://programsandcourses.anu.edu.au/2019/program/7829XMMDS',
        'https://programsandcourses.anu.edu.au/2019/program/7828XMMDSA',
        'https://programsandcourses.anu.edu.au/2019/program/7316XMMIL',
        'https://programsandcourses.anu.edu.au/2019/program/MMUHS',
        'https://programsandcourses.anu.edu.au/2019/program/VMUHS',
        'https://programsandcourses.anu.edu.au/2019/program/VMUSI',
        'https://programsandcourses.anu.edu.au/2019/program/MNSPO',
        'https://programsandcourses.anu.edu.au/2019/program/VNSPO',
        'https://programsandcourses.anu.edu.au/2019/program/MNEUR',
        'https://programsandcourses.anu.edu.au/2019/program/VNEUR',
        'https://programsandcourses.anu.edu.au/2019/program/MPLSC',
        'https://programsandcourses.anu.edu.au/2019/program/VPLSC',
        'https://programsandcourses.anu.edu.au/2019/program/7413XMPACC',
        'https://programsandcourses.anu.edu.au/2019/program/MPROM',
        'https://programsandcourses.anu.edu.au/2019/program/VPROM',
        'https://programsandcourses.anu.edu.au/2019/program/MPUAD',
        'https://programsandcourses.anu.edu.au/2019/program/MPUBH',
        'https://programsandcourses.anu.edu.au/2019/program/MPUPP',
        'https://programsandcourses.anu.edu.au/2019/program/MPPAU',
        'https://programsandcourses.anu.edu.au/2019/program/MPPUT',
        'https://programsandcourses.anu.edu.au/2019/program/VSCBS',
        'https://programsandcourses.anu.edu.au/2019/program/VSCNS',
        'https://programsandcourses.anu.edu.au/2019/program/VSCPI',
        'https://programsandcourses.anu.edu.au/2019/program/VSCQB',
        'https://programsandcourses.anu.edu.au/2019/program/VSCQT',
        'https://programsandcourses.anu.edu.au/2019/program/7624XMSCO',
        'https://programsandcourses.anu.edu.au/2019/program/NSCBS',
        'https://programsandcourses.anu.edu.au/2019/program/NSCNS',
        'https://programsandcourses.anu.edu.au/2019/program/NSCPI',
        'https://programsandcourses.anu.edu.au/2019/program/NSCQB',
        'https://programsandcourses.anu.edu.au/2019/program/NSCQT',
        'https://programsandcourses.anu.edu.au/2019/program/MSCAU',
        'https://programsandcourses.anu.edu.au/2019/program/MSRES',
        'https://programsandcourses.anu.edu.au/2019/program/VSRES',
        'https://programsandcourses.anu.edu.au/2019/program/MSTAT',
        'https://programsandcourses.anu.edu.au/2019/program/MSTST',
        'https://programsandcourses.anu.edu.au/2019/program/VSTST',
        'https://programsandcourses.anu.edu.au/2019/program/MSTUD',
        'https://programsandcourses.anu.edu.au/2019/program/VSTUD',
        'https://programsandcourses.anu.edu.au/2019/program/MTRAN',
        'https://programsandcourses.anu.edu.au/2019/program/VTRAN',
        'https://programsandcourses.anu.edu.au/2019/program/MVISA',
        'https://programsandcourses.anu.edu.au/2019/program/VVISA'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'The Australian National University'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en_a = response.xpath('//*[@id="top"]/div[6]/div[1]/div[1]/h1/span|//*[@id="top"]/div[5]/div[1]/div[1]/h1/span|//*[@id="top"]/div[7]/div[1]/div[1]/h1/span').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en_a = remove_tags(programme_en_a)
        if ' in ' in programme_en_a:
            programme_en = ''.join(programme_en_a.split(" in ")[-1]).strip()

        elif 'Executive Master of ' in programme_en_a:
            programme_en = programme_en_a.replace('Executive Master of ','')
        elif 'Master of ' in programme_en_a:
            programme_en = programme_en_a.replace('Master of ','')
        else:
            programme_en = programme_en_a
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.teach_time #6.duration #7.duration_per
        teach_time_a = response.xpath("//span[@class='tooltip-area']").extract()
        teach_time_a = ''.join(teach_time_a)
        teach_time_a = remove_tags(teach_time_a)
        teach_time = 1
        if '1.5' in teach_time_a:
            duration = 1.5
        elif '2.5' in teach_time_a:
            duration = 2.5
        elif len(teach_time_a)!=0:
            duration = re.findall('\d',teach_time_a)[0]
        else:
            duration = None
        duration_per = 1
        # print(teach_time)
        # print(duration)

        #8.apply_proces_en
        apply_proces_en = url.replace('2019/program/','2019/program/APPLY/')
        # print(apply_proces_en)

        #9.degree_name
        degree_name = programme_en_a
        if ' in ' in degree_name:
            degree_name = ''.join(degree_name.split(' in ')[0]).strip()
        # print(degree_name)



        #10.department
        department = response.xpath('//*[@id="top"]/div[5]/div[1]/div[1]/div/p/span').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #11.overview_en
        overview_en = response.xpath('//*[@id="introduction"]/p').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #12.rntry_requirements_en
        rntry_requirements_en = response.xpath('//*[@id="admission-and-fees"]/div').extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en).replace('\xa0','')
        # print(rntry_requirements_en)

        #13.tuition_fee
        tuition_fee = response.xpath('//*[@id="indicative-fees__international"]/dl/dd').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = remove_tags(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #14.tuition_fee_pre
        tuition_fee_pre = '$'

        #15.modules_en
        modules_en = response.xpath('//*[@id="study"]//div').extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        #16.ielts 17181920 #21.toefl 22232425
        if 'Ju' in programme_en:
            ielts = 7.0
            ielts_w = 7.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_r = 6.0
            toefl = 110
            toefl_w = 26
            toefl_r = 22
            toefl_s = 22
            toefl_l = 22
        elif 'law' in programme_en:
            ielts = 7.0
            ielts_w = 7.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_r = 6.0
            toefl = 110
            toefl_w = 26
            toefl_r = 22
            toefl_s = 22
            toefl_l = 22
        else:
            ielts = 6.5
            ielts_w = 6.0
            ielts_l = 6.0
            ielts_s = 6.0
            ielts_r = 6.0
            toefl = 80
            toefl_w = 20
            toefl_r = 20
            toefl_s = 18
            toefl_l = 18

        #26.apply_pre
        apply_pre = '$'

        #27.major
        major = response.xpath("//*[contains(text(),'Specialisations')]//following-sibling::div//ul//li//@href").extract()
        # print(major)

        #28.career_en
        career_en = response.xpath("//*[contains(text(),'Career Option')]//following-sibling::*").extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)



        item['university'] = university
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['teach_time'] = teach_time
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['apply_proces_en'] = apply_proces_en
        item['degree_name'] = degree_name
        item['department'] = department
        item['rntry_requirements_en'] = rntry_requirements_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_s'] = ielts_s
        item['ielts_w'] = ielts_w
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_w'] = toefl_w
        item['toefl_s'] = toefl_s
        item['toefl_l'] = toefl_l
        item['toefl_r'] = toefl_r
        item['apply_pre'] = apply_pre
        item['career_en'] = career_en
        if len(major)!=0:
            for i in major:
                url_major = 'https://programsandcourses.anu.edu.au'+str(i)
                headers = {
                    "User-Agent": "Mozilla/5.0. (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
                data = requests.get(url_major, headers=headers)
                response_major = etree.HTML(data.text)
                response_overview = response_major.xpath('//*[@id="introduction"]')
                doc1 = ""
                if len(response_overview) > 0:
                    for a in response_overview:
                        doc1 += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                        doc1 = remove_class(doc1)

                response_modules = response_major.xpath('//*[@id="study"]/div')
                doc = ""
                if len(response_modules) > 0:
                    for a in response_modules:
                        doc += (etree.tostring(a, encoding='unicode', pretty_print=False, method='html'))
                        doc = remove_class(doc)

                response_programme = response_major.xpath('//*[@id="skip-to"]/div[1]/div[1]/h1//text()')
                response_programme = ''.join(response_programme).strip()
                item['overview_en'] = doc1
                item['modules_en'] = doc
                item['url'] = url_major
                item['programme_en'] = response_programme
                yield item
        else:
            item['overview_en'] = overview_en
            item['modules_en'] = modules_en
            item['url'] = url
            item['programme_en'] = programme_en
            yield item

