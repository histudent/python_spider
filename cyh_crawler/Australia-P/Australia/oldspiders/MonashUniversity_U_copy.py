# -*- coding: utf-8 -*-
import scrapy
from Australia.middlewares import *
from Australia.items import AustraliaItem
import requests
from lxml import etree
class MonashuniversityUSpider(scrapy.Spider):
    name = 'MonashUniversity_U'
    start_urls = ['https://www.monash.edu/study/courses/find-a-course?f.Tabs%7CcourseTab=Undergraduate&f.InterestAreas%7CcourseInterestAreas=']
    def parse(self, response):
        pro_url = response.xpath('//h2/a/@title').extract()
        # for i in pro_url:
        #     yield scrapy.Request(i,callback=self.parses)
        programme = response.xpath('//h2/a/text()').extract()
        for url, pro in zip(pro_url, programme):
            pro = pro.strip()
            deg_xpath = '//a[contains(@title,"' + url + '")]/../../following-sibling::span/text()'
            degree_name = response.xpath(deg_xpath).extract()
            degree_name = ''.join(degree_name).strip()
            if  '/' in degree_name or 'Diploma' in degree_name:
                pass
            else:
                # print('下载',response.url)
                yield scrapy.Request(url=url,callback=self.parses)
    def parses(self, response):
        item = get_item(AustraliaItem)
        item['university'] = 'Monash University'
        item['url'] = response.url
        programme = response.xpath('//strong[@class="h1"]/text()').extract()
        programme = ''.join(programme).strip()
        item['programme_en'] = programme
        degree_name = response.xpath('//th[contains(text(),"Qualification")]/following-sibling::td/text()').extract()
        degree_name = ''.join(degree_name)
        if degree_name == '':
            degree_name = 'Bachelor of ' +programme
        item['degree_name'] = degree_name
        location = 'Melbourne'
        item['location'] = location
        start_date = response.xpath('//th[contains(text(),"Start date")]/following-sibling::td/text()').extract()
        start_date = tracslateDate(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        rntry_requirement = response.xpath('//div[@id="entry-requirements-2"]').extract()
        rntry_requirement = remove_class(rntry_requirement)
        item['rntry_requirements_en'] = rntry_requirement
        modules = response.xpath('//div[@id="course-structure-3"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = modules
        degree_overview = response.xpath('//div[@class="course-page__overview-panel standard-course"]').extract()
        degree_overview = remove_class(degree_overview)
        item['degree_overview_en'] = degree_overview
        item['ielts'] = '6.5'
        item['ielts_l'] = '6.0'
        item['ielts_s'] = '6.0'
        item['ielts_r'] = '6.0'
        item['ielts_w'] = '6.0'
        item['toefl'] = '79'
        item['toefl_l'] = '12'
        item['toefl_s'] = '18'
        item['toefl_r'] = '13'
        item['toefl_w'] = '21'
        fee = response.xpath(
            '//strong[contains(text(),"$")]//text()|//p[contains(text(),"Domestic Annual Fee")]//text()').extract()
        tuition_fee = getTuition_fee(fee)
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = 'AUD'
        item[
            'apply_documents_en'] = '<p>When submitting an application, you must attach certified copies of academic qualifications. These include academic transcripts, graduation certificates and grading systems.</p>'
        item['application_open_date'] = '2019-4,2019-9'
        item['deadline'] = '9月开放:2020-3-31;4月开放:2019-8-31'
        item['apply_proces_en'] = remove_class(
            ['<div id="New_Content_Container_988951-988951" role="tablist" class="accordion">',
             '        <section class="panel section1 Step_1_Check_your_eligibility-1 close">',
             '            <h3 class="accTitle" id="Step_1_Check_your_eligibility-1" aria-controls="Step_1_Check_your_eligibility-1" role="tab" aria-expanded="false" data-expanded-by-default="false">',
             '                <a href="#Step_1_Check_your_eligibility-1" rel="1">',
             '                                            Step 1: Check your eligibility',
             '                                    </a>',
             '            </h3>',
             '            <div class="accContent" aria-labelledby="Step_1_Check_your_eligibility-1" aria-hidden="true" role="tabpanel" style="display: none;">',
             '                                    <h2>English language proficiency</h2><p>You&rsquo;ll need sound English language skills for graduate research. Check that you have the relevant <a href="https://www.monash.edu/graduate-research/faqs-and-resources/content/chapter-two/2-2">English language proficiency</a>.</p><h2>Academic qualifications</h2><p>Each level of graduate research requires different academic qualifications. Check that you have the relevant academic qualifications for:</p><ul><li><a href="http://www.monash.edu/graduate-research/faqs-and-resources/masters/chapter-two/2-1">Master&rsquo;s by research</a></li><li><a href="https://www.monash.edu/graduate-research/faqs-and-resources/content/chapter-two/2-1">Doctoral degree</a> (PhD)</li><li><a href="https://www.monash.edu/graduate-research/faqs-and-resources/content/chapter-two/2-1">Higher doctorate</a> &ndash; see also <a href="https://www.monash.edu/__data/assets/pdf_file/0004/170149/appendix-l.pdf">further applicant requirements</a> for higher doctorate</li></ul><p>Also check if there are any <a href="http://www.monash.edu/pubs/handbooks/courses/">additional faculty requirements</a> for the graduate research degree you want to apply for.</p><h2>Scholarships eligibility</h2><p>In addition to the minimum entry requirement, your <a href="https://www.monash.edu/graduate-research/future-students/eligibility2/eligibility">eligibility for a scholarship</a> depends on your circumstances. We award a range of scholarships through a competitive selection process based on your academic record, research output, and research experience.</p>',
             '                            </div>',
             '        </section>',
             '              <section class="panel section2 Step_2_Receive_an_invitation_to_apply -2 ">',
             '            <h3 class="accTitle" id="Step_2_Receive_an_invitation_to_apply-2" aria-controls="Step_2_Receive_an_invitation_to_apply-2" role="tab" aria-expanded="false">',
             '                <a href="#Step_2_Receive_an_invitation_to_apply-2" rel="2">',
             '                                            Step 2: Receive an invitation to apply',
             '                                    </a>',
             '            </h3>',
             '            <div class="accContent" aria-labelledby="Step_2_Receive_an_invitation_to_apply-2" aria-hidden="true" role="tabpanel" style="display: none;">',
             '                                    <p>You need to receive an invitation to apply, before you apply. To receive one, you&rsquo;ll need to complete an expression of interest and/or <a href="http://www.monash.edu/research/people/find">find a supervisor</a> who agrees to supervise your research. This depends on the faculty/institute.</p><p>It may take up to four weeks to receive an invitation, so make sure you start this as soon as you can.</p><p>Find out how to receive your invitation by the faculty/institute:</p><ul><li><a title="Mada how to apply" href="https://www.monash.edu/mada/future-students/how-to-apply/apply-enrol-hdr" target="_blank"><u>Art, Design and Architecture</u></a></li><li><a href="https://arts.monash.edu/graduate-research/application-process" target="_blank"><u>Arts</u></a></li><li><a href="https://www.monash.edu/business/future-students/research-degrees/how-to-apply"><u>Business and Economics</u></a></li><li><a href="http://monash.edu/education/research/degrees/apply" target="_blank"><u>Education</u></a></li><li><a href="http://eng.monash.edu/research/apply" target="_blank"><u>Engineering</u></a></li><li><a title="IT how to apply" href="http://www.infotech.monash.edu.au/research/degrees/prospective-students/how-to-apply.html" target="_blank"><u>Information Technology</u></a></li><li><a title="Law" href="http://www.monash.edu/law/research/hdr/courses" target="_blank"><u>Law</u></a></li><li><a href="http://www.med.monash.edu.au/pgrad/research/faculty_admissionand_howtoapply.html" target="_blank"><u>Medicine, Nursing and Health Sciences</u></a><strong>* </strong></li><li><a href="https://www.monash.edu/pharm/doctoral-program/how-to-apply-for-our-doctoral-program" target="_blank"><u>Pharmacy and Pharmaceutical Sciences</u></a></li><li><a href="https://www.monash.edu/science/research/graduate-research/how-to-apply"><u>Science</u></a></li><li><a title="Miri how to apply" href="https://www.monash.edu/muarc/study-with-us/courses-and-study-programs/pgrad" target="_blank"><u>Monash University Accident Research Centre (MUARC)</u></a></li><li><a title="Msi how to apply" href="http://monash.edu/sustainability-institute/programs-initiatives/postgraduate-research.html" target="_blank"><u>Monash Sustainable Development Institute (MSDI)</u></a></li></ul><p><span style="font-size: 90%;">*If you are applying for the Doctor of Philosophy (Clinical Psychology) or Doctor of Philosophy (Clinical Neuropsychology), you don&rsquo;t need an invitation to apply, find a supervisor, or provide a project proposal before applying. See your application process by the <a href="https://www.monash.edu/medicine/psych/teaching/graduate-programs/clinical-doctoral-programs-admission-process">School of Psychological Sciences</a>.</span></p><h3>Australian Sanctions Compliance Policy</h3><p>If you are an international applicant from a country listed under the Australian government sanctions regime, the <a href="https://www.monash.edu/graduate-research/future-students/apply/sanctions">sanctions compliance policy</a> will affect you.</p>',
             '                            </div>',
             '        </section>',
             '                    <section class="panel section3 Step_3_Prepare_your_documentation-3 ">',
             '            <h3 class="accTitle" id="Step_3_Prepare_your_documentation-3" aria-controls="Step_3_Prepare_your_documentation-3" role="tab" aria-expanded="false">',
             '                <a href="#Step_3_Prepare_your_documentation-3" rel="3">',
             '                                            Step 3: Prepare your documentation',
             '                                    </a>',
             '            </h3>',
             '            <div class="accContent" aria-labelledby="Step_3_Prepare_your_documentation-3" aria-hidden="true" role="tabpanel" style="display: none;">',
             '                                    <p>When completing your application, you will be asked to upload copies of documents which include at least:</p><ul><li>Academic curriculum vitae,</li><li>Academic transcripts,</li><li>Proof of citizenship,</li><li>Proof of meeting the&nbsp;<a href="https://www.monash.edu/graduate-research/faqs-and-resources/content/chapter-two/2-2">English language proficiency</a> requirements,</li><li>Invitation to Apply, and</li><li>Research proposal.</li></ul><p>It is your responsibility to provide all supporting documents. Applications where information or documentation is incomplete may not be considered. You will be asked to submit original or correctly certified documents at enrolment.</p><p>If your documents are in a language other than English, you must provide certified translated copies. We prefer&nbsp;<a href="https://www.naati.com.au" target="_blank" rel="external">NAATI qualified translators</a>.</p>',
             '                            </div>',
             '        </section>',
             '                    <section class="panel section4 Step_4_Submit_your_application-4 ">',
             '            <h3 class="accTitle" id="Step_4_Submit_your_application-4" aria-controls="Step_4_Submit_your_application-4" role="tab" aria-expanded="false">',
             '                <a href="#Step_4_Submit_your_application-4" rel="4">',
             '                                            Step 4: Submit your application',
             '                                    </a>',
             '            </h3>',
             '            <div class="accContent" aria-labelledby="Step_4_Submit_your_application-4" aria-hidden="true" role="tabpanel" style="display: none;">',
             '                                    <p>You are ready to submit your application once you have an invitation to apply and supporting documents.</p><p>If you wish to be considered for a scholarship, simply indicate this on the application form. There is no need to fill out a separate application form.</p><p>See this&nbsp;<a href="http://www.monash.edu/graduate-research/future-students/apply/application/guide">application guide</a> to learn about what you will need to provide in each section of the application process.</p><p style="text-align: left;"><a title="Online application form" class="btn btn--blue" href="https://apps.connect.monash.edu.au/apex/f?p=POSTGRADRESEARCHAPP:PUBLIC_PAGE">Apply here</a></p>',
             '                            </div>',
             '        </section>',
             '                                                                            </div>',
             ])
        major_name = response.xpath('//p[@id="specialisations"]/following-sibling::ul/li/a/text()|//ul[@class="majors"]/li/a/text()').extract()
        major_url = response.xpath('//p[@id="specialisations"]/following-sibling::ul/li/a/@data-href|//ul[@class="majors"]/li/a/@data-href').extract()
        duration=response.xpath('//th[contains(text(),"Duration")]/following-sibling::*//text()').extract()
        duration=''.join(duration).strip()
        mode=re.findall('(?i)full',duration)
        overview = response.xpath('//div[@id="overview-tab-content"]').extract()
        item['overview_en']=remove_class(overview)
        deprtment_url = response.xpath('//p[@id="faculty-link"]/a/@href').extract()
        if deprtment_url != []:
            department = self.getDepartment(deprtment_url[0])
            item['department'] = ''.join(department)
        if mode!=[]:
            dura=re.findall('\d',duration)
            dura=list(map(int,dura))
            item['duration']=min(dura)
            item['duration_per']=1
            if major_url!=[]:
                for j,name in zip(major_url,major_name):
                    majorOverview = self.getMajorOverview(j)
                    majMod=''
                    for mM in majorOverview:
                        majMod+=etree.tostring(mM,method='html',encoding='unicode')
                    majorOverview = remove_class(majMod)
                    item['programme_en'] = name
                    item['overview_en'] = majorOverview
                    print('有专业:',j)
                    # yield item
            else:
                print('无专业:',response.url)
                # yield item
        else:
            print('课程长度为',duration,'只有兼职，不要')

    def getDepartment(self,url):
        depResponse=requests.get(url).content
        depResponse=etree.HTML(depResponse)
        department=depResponse.xpath('//div[@class="content-wrapper"]/h2/text()')
        return department
    def getMajorOverview(self,url):
        try:
            moResponse = etree.HTML(requests.get(url).content)
            mo = moResponse.xpath('//button[contains(text(),"Choose another")]/following-sibling::*')
            return mo
        except:
            return None

