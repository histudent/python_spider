# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/7/19 9:47'
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
    name = 'TheUniversityofAdelaide_p'
    allowed_domains = ['adelaide.edu.au/']
    start_urls = []
    C= [
        'https://www.adelaide.edu.au/degree-finder/2019/maccg_maccntg.html',
        'https://www.adelaide.edu.au/degree-finder/2019/macfi_macfin.html',
        'https://www.adelaide.edu.au/degree-finder/2019/macma_maccmktg.html',
        'https://www.adelaide.edu.au/degree-finder/2019/maeco_madvecon.html',
        'https://www.adelaide.edu.au/degree-finder/2019/magri_magribus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mappe_mappecon.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mapfn_mappfi.html',
        'https://www.adelaide.edu.au/degree-finder/2019/maie_mainentr.html',
        'https://www.adelaide.edu.au/degree-finder/2019/maie_mainentrol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/maiea_mainentra.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mapm_mapmol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mapm_mapprojmgt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mapmp_mapmpsol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mapmp_mapprojmps.html',
        'https://www.adelaide.edu.au/degree-finder/2019/march_marchcswk.html',
        'https://www.adelaide.edu.au/degree-finder/2019/marts_marts.html',
        'https://www.adelaide.edu.au/degree-finder/2019/macms_macmusst.html',
        'https://www.adelaide.edu.au/degree-finder/2019/maitt_martittc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/maah_mastarth.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mbio_mbioinf.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mbib_mbibiom.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mbiot_mbiotechpb.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mba12_mba12.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mbusl_mbusilaw.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mbusr_mbusrsch.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mclnu_mclinur.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcomm_mcomm.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mclaw_mcomplaws.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcoms_mcmpsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcomi_mcompinnov.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcmgt_mconmgt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcp_mcounpsy.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcs_mcybsec.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mdsc_mdatasc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meduc_meduc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengaero.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengch.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengcivst.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengciven.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengelec.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengelect.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengmechan.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengmecha.html',
        'https://www.adelaide.edu.au/degree-finder/2019/meng_mengmin.html',
        'https://www.adelaide.edu.au/degree-finder/2019/menpm_menvp&mgt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mfin_mfinance.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mfbe_mfbec.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mgeos_mgeostat.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mgfab_mglobfab.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mhep_mhlthecpol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/minen_minentr.html',
        'https://www.adelaide.edu.au/degree-finder/2019/minen_minentrol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mib_mintbus.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mim_mintmgmt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mitd_mintradev.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mlack_mlarchcswk.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mlawc_llmcwk.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mmar_mmareng.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mcomc_mcommk.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mme_mmateng.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mmasc_mmathsci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mmis_mmininvsur.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mmups_mmuspest.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mmupp_mmuspp.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurssc.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscac.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscar.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscbn.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnursccn.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscen.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscic.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscmh.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscon.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscor.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscpn.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mnusc_mnurscrn.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mpen_mpetroleng.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mplan_mplanning.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mpud_mplanud.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mprac_mprofac.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mprop_mproperty.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mpsyc_mclinpsy.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mpsyh_mpsyhealth.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mpohf_mpsychohm.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mph_mpubhlt.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mrsec_mrseco.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mscec_mscecot.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mscpe_mscpetge.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mas_maddstud.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mseng_msofteng.html',
        'https://www.adelaide.edu.au/degree-finder/2019/msusc_msursci.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mtms_mteachm&s.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mvo_mvitoenol.html',
        'https://www.adelaide.edu.au/degree-finder/2019/mwb_mwinbus.html'
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
        programme_en_1 = response.xpath('//*[@id="ua-main-content"]/h2/text()').extract()
        programme_en_1 = ''.join(programme_en_1)
        programme_en = remove_tags(programme_en_1).replace('Master of ','')
        if  '(' in programme_en:
            programme_en = re.findall(r'\((.*)\)',programme_en)[0]
        # print(programme_en)

        #4.degree_type
        degree_type = 2

        #5.degree_name
        degree_name = programme_en_1.split('(')[0].strip() if '(' in programme_en_1 else programme_en_1.strip()
        # print(degree_name)

        #6.teach_time
        teach_time = 'coursework'

        #7.duration #8.duration_per
        duration_list = response.xpath('//*[@id="ua-main-content"]/div[2]/div[3]/span[2]').extract()
        duration_list = ''.join(duration_list)
        duration_list = remove_tags(duration_list)
        duration_list = clear_space_str(duration_list)
        # print(duration_list)
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
        # print(location)
        if '2019/hd' in response.url:
            location = 'North Terrace Campus'
        elif len(location) ==0:
            location = ''
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
            ielts = 7

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
            ielts_r = 6.5
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
            ielts_l = 6.5
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
            ielts_s = 6.5
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
            ielts_w = 6.5
        # print(ielts_w)

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
        # print(toefl, toefl_r, toefl_l, toefl_s, toefl_w,response.url)

        #21.rntry_requirements_en
        rntry_requirements_en = response.xpath('//*[@id="df-acc-admission"]/div[5]/table[3]//tr/td').extract()
        rntry_requirements_en = ''.join(rntry_requirements_en)
        rntry_requirements_en = remove_class(rntry_requirements_en)
        # print(rntry_requirements_en)

        #22.apply_proces_en
        apply_proces_en ='https://international.adelaide.edu.au/admissions/how-to-apply'

        #23.deadline
        if 'Master of Psychology' in programme_en:
            deadline = '2018-10-21,2019-5-1'
        elif 'Master of Viticulture and Oenology' in programme_en:
            deadline = '2018-12-1,2019-4-30'
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

        #28.modules_en
        modules_en = response.xpath("//h4[contains(text(),'Example Study Plan')]/following-sibling::div[1]").extract()
        modules_en = ''.join(modules_en)
        modules_en = remove_class(modules_en)
        # print(modules_en)

        item['university'] = university
        item['url'] = url
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['teach_time'] = teach_time
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
