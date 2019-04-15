# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/19 14:57'
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
class TheUniversityofAdelaideUniversitySpider(scrapy.Spider):
    name = 'TheUniversityofAdelaide_u'
    allowed_domains = ['adelaide.edu.au/']
    start_urls = []
    C = [
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_beha&ss1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behmechs1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behe&es1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behchems1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behcivs1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behenvirs1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behpets1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behmins1.html',
        'https://www.adelaide.edu.au/degree-finder/bscms_bscm&cs.html',
        'https://www.adelaide.edu.au/degree-finder/bfsct_bfoodsct.html',
        'https://www.adelaide.edu.au/degree-finder/benvs_benvs.html',
        'https://www.adelaide.edu.au/degree-finder/2019/binne_binnent.html',
        'https://www.adelaide.edu.au/degree-finder/2019/behpe_behpetrol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bhms_bhlthmsc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bengh_behsofts1.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/hpsya_hbpsycadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barts_bart.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/barta_bartadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcom_bcom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcom_bcom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcom_bcom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcom_bcom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcom_bcom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcom_bcom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcomp_bcmpsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcomp_bcmpsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcomp_bcmpsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcomp_bcmpsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcomp_bcmpsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcmsa_bcmpscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcmsa_bcmpscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcmsa_bcmpscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcmsa_bcmpscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcmsa_bcmpscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blaws_llb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/blang_blang.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmsad_bmathscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmsad_bmathscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmsad_bmathscadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmadv_bmusadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmadv_bmusadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmadv_bmusadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmedi_bmedia.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bdest_bdesignst.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bacc_bacc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bbmgt_bbusmgt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bbusg_bbusglobal.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcofi_bcorpfin.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bca_bcrarts.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bappb_bappbio.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bags_bagricsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bds_bds.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bec_becon.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/beca_beconadv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bfin_bfinint.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bfin_bfin.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bintb_bintbus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bdvst_bdevstud.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bcrim_bcrim.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmktg_bmarketing.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bintr_bintlrel.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmuscv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmasc_bmathsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpsyc_bpsyc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmusicol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmusmpc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmusmpj.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmuth_bmusthtre.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsocs_bsocialsc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsocs_bsocialsc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmuspm.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsocs_bsocialsc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmusmc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsoc_bsociol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bnurs_bnursing.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsoc_bsociol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsoc_bsociol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsoc_bsociol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/boral_boralhlth.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bpm_bprojmgt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscas.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscbiotech.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscab.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscmarine.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscectour.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bmus_bmussonic.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscwcb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bsceg.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscibiomed.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscssap.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bscpv_bscaspv.html',
        'https://www.adelaide.edu.au/degree-finder/2019/hschp_hschp.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscmige.html',
        'https://www.adelaide.edu.au/degree-finder/2019/bsc_bscadv.html'
    ]
    C = set(C)
    for i in C:
        start_urls.append(i)
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)

        #1.university
        university = 'The University of Adelaide'
        # print(university)

        #2.url
        url = response.url
        # print(url)

        #3.programme_en
        programme_en_a = response.xpath('//*[@id="ua-main-content"]/h2/text()').extract()
        programme_en_a = ''.join(programme_en_a)
        programme_en = remove_tags(programme_en_a).replace('Bachelor of','').strip()
        if '(' in programme_en:
            programme_en = re.findall(r'\((.*)\)',programme_en)[0]
        # print(programme_en)

        #programme_en 荣誉年
        # programme_en_a = response.xpath('//*[@id="ua-main-content"]/h2/text()').extract()
        # programme_en_a = ''.join(programme_en_a)
        # programme_en = remove_tags(programme_en_a)
        # if 'Honours Degree of Bachelor of ' in programme_en:
        #     programme_en = programme_en.replace('Honours Degree of Bachelor of ','')
        # elif 'Bachelor of 'in programme_en:
        #     programme_en = programme_en.replace('Bachelor of ','')
        # print(programme_en)


        #4.degree_type
        degree_type = 1

        #5.degree_name
        degree_name = programme_en_a
        # print(degree_name)

        #6.modules_en
        modules_en = response.xpath("//*[contains(text(),'Example Study Plan')]//following-sibling::*").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        if 'table' not in modules_en:
            modules_en = None
        # try:
        #     modules_en_url = response.xpath("//*[contains(text(),'Academic Program Rules')]//following-sibling::div//@href").extract()[-1]
        # except:
        #     modules_en_url = ''
        # # print(modules_en_url,'**********',url)
        # print(modules_en)

        #7.duration #8.duration_per
        duration_list = response.xpath('//*[@id="ua-main-content"]/div[2]/div[3]/span[2]').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        if '1.5'in duration_list:
            duration = 1.5
        else:
            try:
                duration = re.findall('\d',duration_list)[0]
            except:
                duration = None
        duration_per = 1
        # print(duration)
        # print(duration_list)

        #9.location
        location = response.xpath('//*[@id="ua-main-content"]/div[2]/div[1]/span[2]/a').extract()
        location = ''.join(location)
        location = remove_tags(location)
        if '2019/hd' in response.url:
            location = 'North Terrace Campus'
        elif len(location) ==0:
            location = 'Online'
        # print(location)

        #10.overview_en
        overview_en = response.xpath('//*[@id="ua-main-content"]/div[2]/div/div').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        # print(overview_en)

        #11.ielts 12131415
        ielts_list = response.xpath('//*[@id="df-acc-admission"]/div[5]/table[2]//tr[2]/td/table//tr/td').extract()
        # ielts_list = ''.join(ielts_list)
        # ielts_list = remove_tags(ielts_list)
        # print(ielts_list)

        #ielts
        try:
            if '7' in ielts_list[1]:
                ielts = 7
            else:
                try:
                    ielts = re.findall('\d\.\d',ielts_list[1])[0]
                except:
                    ielts = None
        except:
            ielts = 6.5

        #ielts_r
        try:
            if '6.5' in ielts_list[2]:
                ielts_r = 6.5
            else:
                try:
                    ielts_r = re.findall('\d',ielts_list[2])[0]
                except:
                    ielts_r = None
        except:
            ielts_r = 6
        # print(ielts_r)

        #ielts_l
        try:
            if '6.5' in ielts_list[3]:
                ielts_l = 6.5
            else:
                try:
                    ielts_l = re.findall('\d', ielts_list[3])[0]
                except:
                    ielts_l = None
        except:
            ielts_l = 6
        # print(ielts_l)

        # ielts_s
        try:
            if '6.5' in ielts_list[4]:
                ielts_s = 6.5
            else:
                try:
                    ielts_s = re.findall('\d', ielts_list[4])[0]
                except:
                    ielts_s = None
        except:
            ielts_s = 6
        # print(ielts_s)

        # ielts_w
        try:
            if '6.5' in ielts_list[5]:
                ielts_w = 6.5
            else:
                try:
                    ielts_w = re.findall('\d', ielts_list[5])[0]
                except:
                    ielts_w = None
        except:
            ielts_w = 6
        # print(ielts_w)
        # print(ielts,ielts_r,ielts_w,ielts_s,ielts_l)
        #16.toefl 17181920
        toefl_list = response.xpath('//*[@id="df-acc-admission"]/div[5]/table[2]//tr[3]/td/table//tr/td').extract()
        toefl_list = ''.join(toefl_list)
        toefl_list = remove_tags(toefl_list)
        # print(toefl_list)
        try:
            toefl = re.findall('\d+',toefl_list)
            # print(toefl)
            a = toefl[0]
            b = toefl[1]
            c = toefl[2]
            d = toefl[3]
            e = toefl[4]
            toefl = a
            toefl_r = b
            toefl_l = c
            toefl_s = d
            toefl_w = e
        except:
            toefl = 94
            toefl_r = 24
            toefl_l = 24
            toefl_s = 23
            toefl_w = 27
        # print(toefl, toefl_r, toefl_l, toefl_s, toefl_w)

        #21.rntry_requirements_en
        rntry_requirements_en = response.xpath('//*[@id="df-acc-admission"]/div[5]/table[3]//tr/td').extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #22.apply_proces_en
        apply_proces_en ='https://international.adelaide.edu.au/admissions/how-to-apply'

        #23.deadline
        if 'Medicine and  Surgery' in programme_en:
            deadline = '2018-6-30,2019-5-1'
        elif 'Dental Surgery' in programme_en:
            deadline = '2018-6-30,2019-5-1'
        elif 'Oral Health' in programme_en:
            deadline = '2018-6-30,2019-5-1'
        elif 'Nursing' in programme_en:
            deadline = '2018-9-30,2019-5-1'
        elif 'Science (Veterinary Bioscience)' in programme_en:
            deadline = '2018-9-30,2019-5-1'
        else:
            deadline = '2018-12-1,2019-5-1'

        #24.tuition_fee
        tuition_fee = response.xpath('//*[@id="df-acc-fees_scholarships"]/div[5]/table//tr/td[2]').extract()
        tuition_fee = ''.join(tuition_fee)
        tuition_fee = getTuition_fee(tuition_fee)
        # print(tuition_fee)

        #25.tuition_fee_pre
        tuition_fee_pre = '$'

        #26.apply_pre
        apply_pre = '$'

        #27.career_en
        career_en = response.xpath('//*[@id="df-acc-careers_parent"]//following-sibling::*').extract()
        career_en = ''.join(career_en)
        career_en = remove_class(career_en)
        # print(career_en)

        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['location'] = location
        item['overview_en'] = overview_en
        item['ielts'] = ielts
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['ielts_s'] = ielts_s
        item['ielts_l'] = ielts_l
        item['toefl'] = toefl
        item['toefl_r'] = toefl_r
        item['toefl_s'] = toefl_s
        item['toefl_w'] = toefl_w
        item['toefl_l'] = toefl_l
        item['rntry_requirements_en'] = rntry_requirements_en
        item['apply_proces_en'] = apply_proces_en
        item['deadline'] = deadline
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['career_en'] = career_en
        item['apply_pre'] = apply_pre
        item['modules_en'] = modules_en
        yield  item