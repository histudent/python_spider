# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2019-01-07 11:45:16
# @Last Modified by:   admin
# @Last Modified time: 2019-01-07 11:45:16
"""


import scrapy
import re
from scrapySchool_Canada_Ben.getItem import get_item
from scrapySchool_Canada_Ben.middlewares import *
from scrapySchool_Canada_Ben.items import ScrapyschoolCanadaBenItem
from w3lib.html import remove_tags
from lxml import etree
import requests

class BrockUniversity_ModulesSpider(scrapy.Spider):
    name = "BrockUniversity_Modules"
    start_urls = ["https://brocku.ca/webcal/2018/undergrad/adst.html",
"https://brocku.ca/webcal/2018/undergrad/apli.html",
"https://brocku.ca/webcal/2018/undergrad/bchm.html",
"https://brocku.ca/webcal/2018/undergrad/biol.html",
"https://brocku.ca/webcal/2018/undergrad/biom.html",
"https://brocku.ca/webcal/2018/undergrad/bphy.html",
"https://brocku.ca/webcal/2018/undergrad/btec.html",
"https://brocku.ca/webcal/2018/undergrad/busi.html",
"https://brocku.ca/webcal/2018/undergrad/beco.html",
"https://brocku.ca/webcal/2018/undergrad/cana.html",
"https://brocku.ca/webcal/2018/undergrad/chem.html",
"https://brocku.ca/webcal/2018/undergrad/chil.html",
"https://brocku.ca/webcal/2018/undergrad/chys.html",
"https://brocku.ca/webcal/2018/undergrad/clas.html",
"https://brocku.ca/webcal/2018/undergrad/copf.html",
"https://brocku.ca/webcal/2018/undergrad/comm.html",
"https://brocku.ca/webcal/2018/undergrad/chhe.html",
"https://brocku.ca/webcal/2018/undergrad/cosc.html",
"https://brocku.ca/webcal/2018/undergrad/csbu.html",
"https://brocku.ca/webcal/2018/undergrad/cncc.html",
"https://brocku.ca/webcal/2018/undergrad/csdt.html",
"https://brocku.ca/webcal/2018/undergrad/coop.html",
"https://brocku.ca/webcal/2018/undergrad/digi.html",
"https://brocku.ca/webcal/2018/undergrad/dart.html",
"https://brocku.ca/webcal/2018/undergrad/ersc.html",
"https://brocku.ca/webcal/2018/undergrad/econ.html",
"https://brocku.ca/webcal/2018/undergrad/abed.html",
"https://brocku.ca/webcal/2018/undergrad/edae.html",
"https://brocku.ca/webcal/2018/undergrad/eabo.html",
"https://brocku.ca/webcal/2018/undergrad/edcs.html",
"https://brocku.ca/webcal/2018/undergrad/edbe.html",
"https://brocku.ca/webcal/2018/undergrad/ecis.html",
"https://brocku.ca/webcal/2018/undergrad/ecba.html",
"https://brocku.ca/webcal/2018/undergrad/EIBA.html",
"https://brocku.ca/webcal/2018/undergrad/eibs.html",
"https://brocku.ca/webcal/2018/undergrad/epis.html",
"https://brocku.ca/webcal/2018/undergrad/ecbs.html",
"https://brocku.ca/webcal/2018/undergrad/edgu.html",
"https://brocku.ca/webcal/2018/undergrad/engl.html",
"https://brocku.ca/webcal/2018/undergrad/ensu.html",
"https://brocku.ca/webcal/2018/undergrad/film.html",
"https://brocku.ca/webcal/2018/undergrad/fren.html",
"https://brocku.ca/webcal/2018/undergrad/game.html",
"https://brocku.ca/webcal/2018/undergrad/huma.html",
"https://brocku.ca/webcal/2018/undergrad/geog.html",
"https://brocku.ca/webcal/2018/undergrad/getm.html",
"https://brocku.ca/webcal/2018/undergrad/chsc.html",
"https://brocku.ca/webcal/2018/undergrad/hist.html",
"https://brocku.ca/webcal/2018/undergrad/HILA.html",
"https://brocku.ca/webcal/2018/undergrad/abst.html",
"https://brocku.ca/webcal/2018/undergrad/ints.html",
"https://brocku.ca/webcal/2018/undergrad/iasc.html",
"https://brocku.ca/webcal/2018/undergrad/inpe.html",
"https://brocku.ca/webcal/2018/undergrad/inte.html",
"https://brocku.ca/webcal/2018/undergrad/ital.html",
"https://brocku.ca/webcal/2018/undergrad/kine.html",
"https://brocku.ca/webcal/2018/undergrad/labr.html",
"https://brocku.ca/webcal/2018/undergrad/math.html",
"https://brocku.ca/webcal/2018/undergrad/medi.html",
"https://brocku.ca/webcal/2018/undergrad/mars.html",
"https://brocku.ca/webcal/2018/undergrad/mllc.html",
"https://brocku.ca/webcal/2018/undergrad/musi.html",
"https://brocku.ca/webcal/2018/undergrad/neur.html",
"https://brocku.ca/webcal/2018/undergrad/nurs.html",
"https://brocku.ca/webcal/2018/undergrad/oevi.html",
"https://brocku.ca/webcal/2018/undergrad/phil.html",
"https://brocku.ca/webcal/2018/undergrad/phed.html",
"https://brocku.ca/webcal/2018/undergrad/phys.html",
"https://brocku.ca/webcal/2018/undergrad/pcjp.html",
"https://brocku.ca/webcal/2018/undergrad/poli.html",
"https://brocku.ca/webcal/2018/undergrad/pcul.html",
"https://brocku.ca/webcal/2018/undergrad/psyc.html",
"https://brocku.ca/webcal/2018/undergrad/puhl.html",
"https://brocku.ca/webcal/2018/undergrad/recl.html",
"https://brocku.ca/webcal/2018/undergrad/gens.html",
"https://brocku.ca/webcal/2018/undergrad/sosc.html",
"https://brocku.ca/webcal/2018/undergrad/soci.html",
"https://brocku.ca/webcal/2018/undergrad/spma.html",
"https://brocku.ca/webcal/2018/undergrad/stac.html",
"https://brocku.ca/webcal/2018/undergrad/sclc.html",
"https://brocku.ca/webcal/2018/undergrad/tmgt.html",
"https://brocku.ca/webcal/2018/undergrad/visa.html",
"https://brocku.ca/webcal/2018/undergrad/wise.html", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        item = get_item(ScrapyschoolCanadaBenItem)
        item['school_name'] = "Brock University"
        item['url'] = response.url
        print("===========================")
        print(response.url)

        try:
            major_name_en = response.xpath("//a[@name='sec1']/text()").extract()
            clear_space(major_name_en)
            item['major_name_en'] = ''.join(major_name_en).strip()
            print("item['major_name_en']: ", item['major_name_en'])

            tmp_html = response.text
            find_sec = re.findall(r'<a\sname=\"sec\d+\">', tmp_html)
            # print("find_sec: ", find_sec)
            if len(find_sec) > 0:
                for sec in find_sec:
                    tmp_html = tmp_html.replace(sec, "<a>")
            # find_sec1 = re.findall(r'<a\sname=\"sec\d+\">', tmp_html)
            # print("find_sec1: ", find_sec1)
            # print(tmp_html)
            # modules_key1 = r'<td valign="bottom" colspan="2"><a>BSc with Major'
            # if modules_key1 not in tmp_html:
            #     modules_key1 = r'<td valign="bottom" colspan="2"><a>BA with Major'
            # modules_key2 = r'<td valign="bottom" colspan="2"><a>Pass Program</a></td>'
            #
            # if modules_key1 in tmp_html and modules_key2 in tmp_html:
            #     item['modules_en'] = remove_class(getContentToXpath(tmp_html, modules_key1, modules_key2))
            # print("item['modules_en']: ", item['modules_en'])
            # if item['modules_en'] is None:
            #
            # modules_en = response.xpath("//a[contains(text(), 'Computing and Solid-State Device Technology Co-op')]/../../../following-sibling::*[1]").extract()
            modules_en = response.xpath(
                "//a[contains(text(), 'Pass Program')]/../../preceding-sibling::*[position()<3]|//p[contains(text(),'HEALTH SCIENCES COURSES')]/following-sibling::*"
                "//a[contains(text(), 'Bachelor of Science in Kinesiology Program')]/../../../following-sibling::*[1]").extract()
            print("modules_en:", modules_en)
            if len(modules_en) > 0:
                item['modules_en'] = remove_class(clear_lianxu_space(modules_en)).replace("<div><div><ul><li>Home</li><li>Courses</li><li>Search</li><li>Contents</li><li>Previous Page</li><li>Next Page</li><li>Login</li><li>Printable<br>Version</li></ul></div></div>", "").strip()
            print("item['modules_en']: ", item['modules_en'])
            yield item

        except Exception as e:
            with open("scrapySchool_Canada_Ben/error/" + item['school_name'] + ".txt",
                      'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)