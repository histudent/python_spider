# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_same_s
from scrapySchool_England.middlewares import clear_duration,tracslateDate
class NewmanuniversityPSpider(scrapy.Spider):
    name = 'NewmanUniversity_P'
    allowed_domains = ['newman.ac.uk']
    start_urls = ['https://www.newman.ac.uk/study-level/postgraduate/page/1']
    def parse(self, response):
        print(response.url)
        pro_url=response.xpath('//div[@class="constrain"]/article//a/@href').extract()
        for i in pro_url:
            yield scrapy.Request(i,callback=self.parse_main)
        next_page=response.xpath('//a[contains(text(),"Next")]/@href').extract()
        if next_page!=[]:
            next_page_url=next_page[0]
            yield scrapy.Request(next_page_url,callback=self.parse)
    def parse_main(self,response):
        item=get_item1(ScrapyschoolEnglandItem1)
        print(response.url)
        item['url'] = response.url
        item['university'] = 'Newman University'
        item['location'] = 'Birmingham'
        programme=response.xpath('//h1[@class="feature"]/text()').extract()
        programme=''.join(programme).strip()
        # print(programme)
        degree_name=response.xpath('//h1[@class="feature"]/following-sibling::h4/text()').extract()
        degree_name=''.join(degree_name).strip()
        # print(degree_name)
        item['programme_en'] = programme
        mode=re.findall('(?i)full',degree_name)
        if mode!=[]:
            item['teach_time']='1'
        else:
            item['teach_time']= '2'
        degree_name=re.findall('\s\(?[A-Z]{2}.*',programme)
        # print(degree_name)
        degree_name=''.join(degree_name).replace(')','').replace('(','').strip()
        item['degree_name'] = degree_name

        duration=response.xpath('//span[contains(text(),"Year")]/preceding-sibling::*/text()').extract()
        duration=''.join(duration)
        item['duration']=duration
        item['duration_per'] = '1'

        overview=response.xpath('//div[@class="overview_slider__wrapper"]').extract()
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview

        rntry=response.xpath('//h2[contains(text(),"equirements")]/..').extract()
        rntry=remove_class(rntry)
        # print(rntry)
        item['rntry_requirements'] = rntry

        modules=response.xpath('//div[@class="modules_years padded"]//li/div/h5').extract()
        modules=remove_class(modules)
        item['modules_en']=modules

        fee=response.xpath('//p[contains(text(),"£")]/text()').extract()
        tuition_fee=getTuition_fee(fee)
        if tuition_fee==2018:
            tuition_fee=0
        item['tuition_fee']=tuition_fee
        item['tuition_fee_pre'] = '£'
        item['ielts'] = '6.5'

        item['start_date'] = '2019-9'

        apply_preces = [
            '<div  class="asset-wrapper asset aid-921 asset-accordion"><ul class="accordion accordion--clear">',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a1" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a1-panel">',
            '        Step 1 – searching for courses and providers      </h2>',
            '      <div id="accordion-a1-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a1" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>You can use UCAS Progress to look for opportunities in your area. There are lots of courses that you can look through, find out more details and which providers they are delivered at. It is a good idea to think about and research the courses you might enjoy and what type of provider you would like to go to e.g. a college or work-based learning provider etc. You will also be able to find out how far you will need to travel to get there.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a2" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a2-panel">',
            '        Step 2 – saving courses to your favourites page      </h2>',
            '      <div id="accordion-a2-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a2" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>While you are searching you can save courses that you like the look of on your unique favourites’ page. This means that when you sign&nbsp;back in they will be saved there and you don’t have to search around the site for them again. You can favourite as many courses as you would like to at any time. You have also got the ability to save providers so if you like the look of a place you can save it without saving any courses.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a3" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a3-panel">',
            '        Step 3 – completing your profile      </h2>',
            '      <div id="accordion-a3-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a3" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>You can start completing your profile at any time and it is a good idea to do this as soon as you can so you are ready to start making applications. There are five sections that you need to fill out which are:</p>',
            '<ol>',
            '  <li class="bullet-purple bullet-purple">Personal information (e.g. school details, support needs etc)</li>',
            '  <li class="bullet-purple bullet-purple">Qualifications (ability to add any subjects that you are working towards or have completed already)</li>',
            '  <li class="bullet-purple bullet-purple">Work history (if you have any work experience or currently have a part time job you can add it here)</li>',
            '  <li class="bullet-purple bullet-purple">Personal statement (gives you a chance to tell the provider that you are applying to a bit about yourself)</li>',
            '  <li class="bullet-purple bullet-purple">Contact details (allows you to add your contact details e.g. mobile number and email and keep them up-to-date throughout the application process).</li>',
            '</ol>',
            '<p>You can save these sections at any stage and when you have finished can mark as complete. All five sections need to be completed before you can start an application.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a4" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a4-panel">',
            '        Step 4 – making an application      </h2>',
            '      <div id="accordion-a4-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a4" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>Before you can make an application you need to have saved the courses that you would like to apply for and completed all of the sections of your profile. When you are ready click the applications tab on your toolbar and select ‘start a new application’. You will then be able to select the provider you want to apply to and the courses you want to study from the list that you saved as favourites.</p>',
            '<p>This will then put your application into the ‘Not sent’ category. You can then click the blue ‘view’ button and check over your application before you send it. When you are happy you can click ‘submit your application’. If you have not completed all of your profile you will then see a message saying ‘awaiting profile completion’ and you will need to go back and complete all of the sections of your profile before you can send your application. You can send applications to as many providers as you feel is right for you.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a5" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a5-panel">',
            '        Step 5 – course preferencing       </h2>',
            '      <div id="accordion-a5-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a5" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>This must be completed before your application can be submitted. When you have saved the course you would like to apply for, and have completed your profile, select the ‘applications’ tab and click ‘Start a new application’. After choosing the provider you would like to apply to, you are asked to ‘Change the order of your chosen courses’.</p>',
            '<p>You have the ability to move the courses up and down so you can show which is your first choice, second choice etc. Click the blue button ‘Confirm course preference order’ when you have finished.&nbsp;</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a6" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a6-panel">',
            '        Step 6 – application in progress      </h2>',
            '      <div id="accordion-a6-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a6" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>As your application progresses you will be able to see what is happening at every stage by signing back in to UCAS Progress and selecting the ‘Applications Tab’.</p>',
            '<p>When you have sent your application it will move from the ‘Not sent’ column to the second stage ‘In Progress’ and your application will be marked as ‘Submitted’.</p>',
            '<p>When the provider receives your application they will acknowledge this and send you a message saying they have received it which will be marked as ‘Acknowledged’.</p>',
            '<p>You will then see any offers that you receive on this page as well. If you change your mind about your application at any time through the process you can send a message to the provider and either change the courses you are applying for or details on your form.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a7" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a7-panel">',
            '        Step 7 – offer preferencing      </h2>',
            '      <div id="accordion-a7-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a7" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>Provider preferencing enables you to put your applications in the order in which you would like to go to them e.g. first choice, second choice etc. When you start making applications, the first application automatically becomes your first choice provider. When you make any more applications you then have the ability to change your preference. You can do this by going to your applications and then clicking the blue button ‘Change the order of your choices’, or using the ‘Change’ link against the provider.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '      <li class="accordion__child">',
            '      <h2 id="accordion-a8" data-accordion-trigger class="accordion__toggle" tabindex="0" role="button" aria-expanded="false" aria-controls="accordion-a8-panel">',
            '        Step 8 – receiving offers and making choices      </h2>',
            '      <div id="accordion-a8-panel" class="accordion__inner" data-accordion-state="collapsed" aria-labelledby="accordion-a8" aria-hidden="true" role="region">',
            '        <div class="accordion__inner-wrapper">',
            '          <p>If a provider makes you an offer you will see this on your applications page. You can receive conditional and unconditional offers through the system and if there are any conditions these will be visible. You have then got the option to accept or decline the offer. You can accept as many offers as you would like to. When you have accepted an offer that application will move into the last column and be marked as ‘accepted’.</p>',
            '<p>If they don’t want to make you an offer, they will mark your application as <strong>unsuccessful</strong>. Alternatively, they may return your application for you to make changes, or to add alternative courses, before they decide to make you an offer.</p>',
            '        </div>',
            '      </div>',
            '    </li>',
            '  </ul>',
            '</div>', ]
        apply_preces = remove_class(apply_preces)
        # print(apply_preces)
        item['apply_proces_en'] = apply_preces

        apply_d = ['<ol>',
                   '  <li class="bullet-purple bullet-purple">Personal information (e.g. school details, support needs etc)</li>',
                   '  <li class="bullet-purple bullet-purple">Qualifications (ability to add any subjects that you are working towards or have completed already)</li>',
                   '  <li class="bullet-purple bullet-purple">Work history (if you have any work experience or currently have a part time job you can add it here)</li>',
                   '  <li class="bullet-purple bullet-purple">Personal statement (gives you a chance to tell the provider that you are applying to a bit about yourself)</li>',
                   '  <li class="bullet-purple bullet-purple">Contact details (allows you to add your contact details e.g. mobile number and email and keep them up-to-date throughout the application process).</li>',
                   '</ol>', ]
        apply_d = remove_class(apply_d)
        item['apply_documents_en'] = apply_d

        # print(item)
        yield item



