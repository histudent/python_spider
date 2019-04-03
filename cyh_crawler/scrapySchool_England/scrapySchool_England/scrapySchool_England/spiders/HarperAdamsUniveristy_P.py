# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration,tracslateDate
import requests
from lxml import etree

class HarperadamsuniveristyPSpider(scrapy.Spider):
    name = 'HarperAdamsUniveristy_P'
    allowed_domains = ['harper-adams.ac.uk']
    start_urls = []
    base_url = 'https://www.harper-adams.ac.uk/courses/courses.cfm?layout=33&q=&type=postgraduate%20research_degree&title=&area=&yoe=2018%202019&cpd=&max=12&start='
    Title = ['1', '13', '25', '37']
    for i in Title:
        fullurl = base_url + i
        start_urls.append(fullurl)
    def parse(self, response):
        programme_url=response.xpath('//article/a/@href').extract()
        for i in programme_url:
            full_url='https://www.harper-adams.ac.uk'+i
            yield scrapy.Request(full_url,callback=self.parses)

    def parses(self,response):
        # print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        Duration = response.xpath('//h4[contains(text(),"Duration")]/following-sibling::p[1]//text()').extract()
        Duration=''.join(Duration)
        if '1' in Duration:
            item['duration'] = 1
            item['duration_per'] = 1
        if 'full' in Duration:
            item['teach_time'] = 'fulltime'
        else:
            item['teach_time'] = 'parttime'

        StartDate = response.xpath('//*[contains(text(),"Start")]/../text()').extract()
        try:
            StartDate=tracslateDate(StartDate)
            StartDate=','.join(StartDate)
            item["start_date"] = StartDate
        except:
            pass
        Course = response.url.split('/')[-1]
        Course = Course.replace('-', ' ').title()
        EntryRequirements = response.xpath('//div[@id="entry-requirements"]').extract()
        EntryRequirements=remove_class(EntryRequirements)
        EntryRequirements=clear_same_s(EntryRequirements)
        CourseOverview = response.xpath('//div[@id="overview"]').extract()
        CourseOverview=remove_class(CourseOverview)
        CourseOverview=clear_same_s(CourseOverview)
        Career = response.xpath('//div[@id="careers"]').extract()
        # if Career==[]:
        #     print(response.url)
        Career = remove_class(Career)
        Career = clear_same_s(Career)
        Assessment = response.xpath('//div[@id="teaching"]').extract()
        if Assessment==[]:
            print(response.url)
        Assessment = remove_class(Assessment)
        Master = response.xpath('//div[@class="page-heading"]/h2/text()').extract()
        Master = ''.join(Master)
        university = 'Harper Adams University'
        item['ielts'] = '6.0'
        item['ielts_l'] = '5.5'
        item['ielts_s'] = '5.5'
        item['ielts_r'] = '5.5'
        item['ielts_w'] = '5.5'
        item['toefl_r'] = '18'
        item['toefl_l'] = '18'
        item['toefl_s'] = '22'
        item['toefl_w'] = '20'
        item['toefl'] = '80'
        item["university"] = university
        item["programme_en"] = Course
        item["degree_name"] = Master
        item["overview_en"] = CourseOverview
        item["assessment_en"] = Assessment
        item["career_en"] = Career
        item["tuition_fee"] = '12650'
        item['tuition_fee_pre'] = '£'
        item['apply_proces_en'] =remove_class(["<div>",
"    	<div>",
"	        <div>",
"                <div>",
"                    <div>",
"                        <div>",
"                        ",
"                        	<p>Applying for university as an international student is similar to the process that UK students follow, but there are a few extra steps.</p>",
"                            ",
"                            <p>These include:</p>",
"							<ul>",
"                            	<li>Taking an <a>English language test</a></li>",
"								<li>Applying for a <a>visa</a></li>",
"								<li>Attending a pre-sessional course</li>",
"                            </ul>",
"							<p>To understand the general steps for applying to one of courses, take a look at our <a>How to apply</a> pages.</p>",
"                        </div>",
"                    </div><div>",
"                     	<div>    ",
"                            ",
"                         </div>",
"                    </div>",
"                 </div>",
"					",
"			</div>",
"		</div>",
"	</div>",
"    <div>",
"        ",
"        <div>",
"            <div>",
"                <div>",
"                    <div>Before you apply</div>",
"                </div>",
"                <div>",
"                    <div>",
"                        <div>",
"                            <div>",
"                    			<div>",
"                    				<div>",
"                                    	",
"                                        <p>To study on a course at Harper Adams, you'll need to meet the entry requirements listed on the <a>English language requirements</a> and you may need to take an English language test.</p>",
"										<p>Like UK students, if you're applying for one of our undergraduate courses, you'll need to apply through the <a>complete an application form</a>.</p>",
"									</div>",
"                                </div><div>",
"                                    <div>    ",
"                                        ",
"                                     </div>",
"                                </div>",
"                            </div>",
"                        </div>",
"                    </div>",
"                </div>",
"            </div>",
"            <div>",
"                <div>",
"                    <div>After you apply</div>",
"                </div>",
"                <div>",
"                    <div>",
"                        <div>",
"                            <div>",
"                    			<div>",
"                    				<div>",
"                                    	",
"                                        <p>We'll look at your application and decide if you meet the entry requirements. We may ask to interview you. We'll keep you updated about the status of your application by email or post.</p>",
"										<p>If we accept your application, we'll send you either an unconditional or conditional offer. Unconditional offers mean you have been accepted to study on a course without any other requirements. A conditional offer means you'll have to give us some additional information or prove a qualification.</p>",
"									</div>",
"                                </div><div>",
"                                    <div>    ",
"                                        ",
"                                     </div>",
"                                </div>",
"                            </div>",
"                        </div>",
"                    </div>",
"                </div>",
"            </div>",
"            <div>",
"                <div>",
"                    <div>Before you arrive</div>",
"                </div>",
"                <div>",
"                    <div>",
"                        <div>",
"                            <div>",
"                    			<div>",
"                    				<div>",
"                                    	",
"                                        <p>Depending on where you're coming from, you'll need to <a>visa pages</a> to find out more.</p>",
"                                        <p>As part of the visa application process, you may need to submit a Confirmation of Acceptance for Studies (CAS) number or a similar letter that says you've been accepted to study here.</p>",
"                                        <h3>Confirmation of Acceptance for Studies (CAS) number</h3>",
"                                        <p>If you meet all of the conditions of your offer by the deadline printed on your offer letter, we'll give you a Confirmation of Acceptance for Studies (CAS) number. You'll need your CAS number to apply for your visa.</p>",
"                                        <p>Your CAS number is unique to you and your place at Harper Adams. It can't be transferred to any other university. If you decide to withdraw your application, you must let us know so we can cancel your CAS number.</p>",
"                                        <h3>Short-term study visa letters</h3>",
"                                        <p>If you're applying for a course that requires a <a>short-term study visa</a>, and you've met any offer conditions we've set, we'll give you a letter that confirms we've accepted you. You'll need to submit this with your visa application. You may also need to show it when you enter the UK.</p>",
"                                        <h3>Applying for accommodation</h3>",
"                                        <p>You'll need to apply for <a>accommodation</a> before you arrive in the UK. We'll send you details of how to do this along with your offer letter. You'll need to tell the university in advance if you're bringing family to live with you.</p>",
"									</div>",
"                                </div><div>",
"                                    <div>    ",
"                                        ",
"                                     </div>",
"                                </div>",
"                            </div>",
"                        </div>",
"                    </div>",
"                </div>",
"            </div>",
"            <div>",
"                <div>",
"                    <div>When you arrive</div>",
"                </div>",
"                <div>",
"                    <div>",
"                        <div>",
"                            <div>",
"                    			<div>",
"                    				<div>",
"                                    	",
"                                        <p>We'll let you know the date that you need to arrive by in your offer letter. You'll need to make arrangements to travel to the UK and get to Harper Adams by this date.</p>",
"										<p>When you first arrive in the UK, you'll need to go through immigration controls. To help you get through immigration as quickly and easily as possible, you should:</p>",
"                                        <ul>",
"                                            <li>Not arrive before the start date of your visa</li>",
"                                            <li>Make sure you've filled in a landing card (if required) and included details of a UK contact - this can be the university's address or the address of a landlord</li>",
"                                            <li>Have your passport, CAS or offer letter, details of where you'll stay and proof that you have enough money to study here ready to show immigration officers</li>",
"                                            <li>Make sure you know the conditions of your visa, when it expires, and the number of hours you are allowed to work</li>",
"                                            <li>Declare any sums of cash over &euro;10,000 (or equivalent in your currency).</li>",
"                                        </ul>",
"                                        <p>To avoid any issues at immigration, you should not:</p>",
"                                        <ul>",
"                                            <li>Bring food or drink (such as meat, dairy products, fish, eggs, honey, fruit, vegetables or plants) with you.</li>",
"                                            <li>Bring counterfeit goods, firearms, weapons or indecent/obscene material with you.</li>",
"                                        </ul>",
"                                        ",
"                                        <p>More information on travelling through the UK border can be found at <a>www.gov.uk/government/publications/coming-to-the-uk/faster-travel-through-the-uk-border</a></p>",
"									</div>",
"                                </div><div>",
"                                    <div>    ",
"                                        ",
"                                     </div>",
"                                </div>",
"                            </div>",
"                        </div>",
"                    </div>",
"                </div>",
"            </div>",
"            <div>",
"                <div>",
"                    <div>After you arrive</div>",
"                </div>",
"                <div>",
"                    <div>",
"                        <div>",
"                            <div>",
"                    			<div>",
"                    				<div>",
"                                    	",
"                                        <p>On your first day at Harper Adams, you'll need to bring your passport and visa (as well as any certificates or documents we've requested) so we can make a copy for our reference.</p>",
"									</div>",
"                                </div><div>",
"                                    <div>    ",
"                                        ",
"                                     </div>",
"                                </div>",
"                            </div>",
"                        </div>",
"                    </div>",
"                </div>",
"            </div>",])

        item["rntry_requirements"] = EntryRequirements
        item["url"] = response.url
        item['location'] = 'Edgmond'

        modu=response.xpath('//div[@class="tabmenu"]/ul/li/a/@onclick').extract()
        mod=response.xpath('//div[@class="tabmenu"]/ul/li/a/@title').extract()
        print(mod)
        print(modu)
        modules = []
        for i,j in zip(mod,modu):
            if 'M' in i:
                print('要这个专业的课程')
                print(i)
                id=re.findall('\d+',j)
                fullurl='https://www.harper-adams.ac.uk/shared/get-pg-route-modules.cfm?id='+str(id[0])+'&year_of_entry='+str(id[1])+'&route='+str(id[2])
                print(fullurl)
                modre=etree.HTML(requests.get(fullurl).content).xpath('//div[@class="content-section-inner"]')
                ma=''
                for mas in modre:
                    ma+=etree.tostring(mas,method='html',encoding='unicode')
                # parMod=remove_class(ma)
                modules+=ma

                # print(id)
            else:
                modules=''
        # print(modules)
        item['modules_en']=remove_class(modules)


        # print(item)
        yield item