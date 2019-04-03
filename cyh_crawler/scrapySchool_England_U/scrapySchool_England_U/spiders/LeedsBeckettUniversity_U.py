# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem

class LeedsbeckettuniversityUSpider(scrapy.Spider):
    name = 'LeedsBeckettUniversity_U'
    allowed_domains = ['leedsbeckett.ac.uk']
    start_urls = ['https://courses.leedsbeckett.ac.uk/undergraduate-courses/']
    #补抓
    # def parse(self, response):
    #     item=get_item1(ScrapyschoolEnglandItem)
    #     item['university'] = 'Leeds Beckett University'
    #     item['url'] = response.url
    #     overview=response.xpath('//div[contains(@id,"description")]|//div[contains(@id,"benefits")]').extract()
    #     buyaodelaji=response.xpath('//span[contains(text(),"Visit ")]//text()').extract()
    #     overview=remove_class(overview)
    #     for i in buyaodelaji:
    #         overview=overview.replace(i,'')
    #     item['overview_en']=overview
    #     career=response.xpath('//div[@id="career_tab_2"]').extract()
    #
    #     item['career_en']=remove_class(career)
    #     assessment=response.xpath('//div[@class="teachinglearningtoptext"]').extract()
    #     assessment=remove_class(assessment)
    #     item['assessment_en']=assessment
    #     yield item
    def parse(self, response):
        pro_url=response.xpath('//h3/a/@href').extract()
        for i in pro_url:
            URL = 'https://courses.leedsbeckett.ac.uk' + i
            yield scrapy.Request(url=URL, callback=self.parses)
    def parses(self, response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem)
        item['university'] = 'Leeds Beckett University'
        item['url'] = response.url
        item['location'] = 'Leeds'
        degree_name = response.xpath('//div[@class="course-hero__label"]/text()').extract()
        degree_name = ''.join(degree_name).strip()
        item['degree_name'] = degree_name
        programme = response.xpath('//h1[@class="course-hero__title"]/text()').extract()
        programme = ''.join(programme).strip()
        item['programme_en'] = programme
        department = response.xpath('//div[@class="course-hero__labels"]/a/text()').extract()
        department = ''.join(department)
        item['department'] = department
        start_date = response.xpath('//div[contains(text(),"Start Date")]/following-sibling::div//text()').extract()
        start_date = tracslateDate(start_date)
        start_date = set(start_date)
        start_date = ','.join(start_date)
        item['start_date'] = start_date
        duration = response.xpath('//div[contains(text(),"Duration")]/following-sibling::span//text()').extract()
        duration = clear_duration(duration)
        item['duration'] = duration['duration']
        item['duration_per'] = duration['duration_per']
        overview = response.xpath('//h2[contains(text(),"Overview")]/../following-sibling::div').extract()
        overview = remove_class(overview)
        item['overview_en'] = overview
        rntry = response.xpath('//h2[contains(text(),"Entry Requirements")]/../following-sibling::div').extract()
        rntry = remove_class(rntry)
        item['require_chinese_en'] = rntry
        IELTS = response.xpath('//div[@class="entry-ielts"]/text()').extract()
        ielts = get_ielts(IELTS)
        try:
            if ielts != [] or ielts != {}:
                item['ielts_l'] = ielts['IELTS_L']
                item['ielts_s'] = ielts['IELTS_S']
                item['ielts_r'] = ielts['IELTS_R']
                item['ielts_w'] = ielts['IELTS_W']
                item['ielts'] = ielts['IELTS']
        except:
            pass
        career = response.xpath('//h3[contains(text(),"Careers")]/following-sibling::div').extract()
        career = remove_class(career)
        item['career_en'] = career
        modules = response.xpath('//h5[contains(text(),"Core Modules")]/..').extract()
        if modules==[]:
            modules = response.xpath('//div[@class="course-modules wrap wrap--mobile-pad"]').extract()
        modules = remove_class(modules)
        item['modules_en'] = remove_class(modules)
        fee = response.xpath('//div[contains(text(),"£")]/text()').extract()
        fee = ''.join(fee).strip()
        fee = re.findall('£\d{3,}', fee)
        fee = '-'.join(fee).replace(',', '').replace('£', '')
        fee = fee.split('-')
        try:
            fee = list(map(int, fee))
            fee = max(fee)
            item['tuition_fee'] = fee
        except:
            pass
        item['tuition_fee_pre'] = '£'
        ucascode=response.xpath('//div[contains(text(),"UCAS")]/strong/text()').extract()
        ucascode=set(ucascode)
        ucascode=''.join(ucascode)
        item['ucascode']=ucascode
        ib=response.xpath('//h4[contains(text(),"International Bacca")]/../text()').extract()
        try:
            item['ib'] = ib[0]
        except:
            pass
        apply_desc=['<h3 class="staff-profile__h3">',
'                    <span class="h6">Personal details </span>',
'                                    </h3>',
'                <p><img style="height: 135px; width: 135px; float: left;" alt="Computer Icon" src="/-/media/images/undergraduate/application-page-icons/computer.png?h=175&amp;w=175&amp;la=en&amp;mw=1382&amp;hash=A66BFC94592B6D4FA8205164568B3FE3C1E27F97" />Log in and fill out your personal details such as your name, age and email address.',
'<br clear="all" />',
'<em><strong>Tip</strong>: Add your email address - UCAS will be able to let you know whenever your application is updated online.</em></p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="choose"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Courses </span>',
'                                    </h3>',
'                <p><img src="/-/media/images/undergraduate/application-page-icons/hand.png?h=135&amp;w=135&amp;la=en&amp;mw=1382&amp;hash=535417471A5FFABE65D5D69506848CF55041E7B9" alt="Hand icon" style="height: 135px; width: 135px; float: left; margin-right: 3px;" />Choose your five courses - You don&rsquo;t need to order these in terms of preference, and the universities you have chosen won&rsquo;t see where else you&rsquo;ve applied to.',
'<br clear="all" />',
'<em><strong>Tip</strong>: Applying for deferred entry? Make sure you&rsquo;ve checked that your chosen university accepts deferred entry applications for the course you&rsquo;re interested in.</em></p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="educationhistory"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Education history </span>',
'                                    </h3>',
'                <p><img src="/-/media/images/undergraduate/application-page-icons/book.png?h=135&amp;w=135&amp;la=en&amp;mw=1382&amp;hash=A8E055FA7F8C8BBB2460A91B62F42BB4604C1E6A" alt="Book icon" style="height: 135px; width: 135px; float: left; margin-right: 3px;" />Enter your education history - You must enter all of your qualifications &ndash; whether you have the result or you&rsquo;re still awaiting exams and results.</p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="employmenthistory"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Employment history </span>',
'                                    </h3>',
'                <p><img style="height: 135px; width: 135px; float: left; margin-right: 3px;" alt="Case icon" src="/-/media/images/undergraduate/application-page-icons/case.png?h=135&amp;w=135&amp;hash=087F36CFE2E28657DE5B0035CFE40077BF0DAC95&amp;la=en&amp;mw=1382">Enter your employment history - this includes any paid job whether full-time or part-time.',
'<br clear="all">',
'<em><strong>Tip</strong>: Save the details of any unpaid or voluntary work for your personal statement.</em></p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="personalstatement"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Personal statement </span>',
'                                    </h3>',
'                <p><img alt="Person icon" src="/-/media/images/undergraduate/application-page-icons/person.png?h=150&amp;w=150&amp;la=en&amp;mw=1382&amp;hash=D9900537BD51BA301EF7EBFD6A5B558DF77CA4F1" style="height: 150px; width: 150px; float: left; margin-right: 3px;">Write your personal statement - this is your chance to stand out from the crowd, to show universities why you want to study the course and why they should pick you. Visit <a href=" https://www.ucas.com/ucas/undergraduate/getting-started/when-apply/writing-personal-statement">UCAS for tips</a> on writing the perfect personal statement. Don’t worry if you can’t complete the form in one go – you can always save it and revisit it later.</p>',
'<p><br clear="all">',
'<em><strong>Tip</strong>: If you draft your statement in Word first you can spell check it before you copy it to your application. Attention to details like this can make a difference.</em></p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="checkit"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Check it </span>',
'                                    </h3>',
'                <p><img src="/-/media/images/undergraduate/application-page-icons/qmark.png?h=135&amp;w=135&amp;hash=DC77589B5E89BDF85D1391FA1BBFE7BF4C8ED575&amp;la=en&amp;mw=1382" alt="Question mark icon" style="height: 135px; width: 135px; float: left; margin-right: 3px;">Check it - look back at all of the information you have provided and make any necessary changes. Once you have marked all of the sections as complete you’ll be able to read and agree to the declaration.</p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="getareference"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Get a reference </span>',
'                                    </h3>',
'                <p><img src="/-/media/images/undergraduate/application-page-icons/thumb.png?h=135&amp;w=135&amp;la=en&amp;mw=1382&amp;hash=61BB663541CDEE65A439A7493EE5CBB44D2FDDCF" alt="Thumb icon" style="height: 135px; width: 135px; float: left; margin-right: 3px;" />Get a reference - This is a written recommendation from a teacher, adviser, or professional who knows you academically.</p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="makeyourpayment"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Payments </span>',
'                                    </h3>',
'                <p><img style="height: 135px; width: 135px; float: left; margin-right: 3px;" alt="Money Icon" src="/-/media/images/undergraduate/application-page-icons/money.png?h=135&amp;w=135&amp;hash=54AC884710A5FB104D6CD921B4E4A71EBD9F9C4B&amp;la=en&amp;mw=1382">Make your payment - The fee for applying through UCAS is £24.00 for multiple choices, or £13.00 if you’ve got your heart set on just one choice.',
'<br clear="all">',
'<em><strong>Tip</strong>: Late applications submitted after 30th June 2018 have a fee of £24 and you will automatically be entered in to Clearing</em>.</p>',
'            </div>',
'            <div class="staff-profile cf">',
'                <a name="submityourapplication"></a>',

'                <h3 class="staff-profile__h3">',
'                    <span class="h6">Submit your application </span>',
'                                    </h3>',
'                <p><img style="height: 135px; width: 135px; float: left; margin-right: 3px;" alt="Calendar icon" src="/-/media/images/undergraduate/application-page-icons/calender.png?h=135&amp;w=135&amp;la=en&amp;mw=1382&amp;hash=365B007B1BA899C408D3BEF1409674FA0F6EC50D" />Submit your application to UCAS and await your offers. It&rsquo;s as simple as that.</p>',
'<p><strong>Good luck!</strong></p>',
]
        apply_desc=remove_class(apply_desc)
        item['apply_proces_en']=apply_desc
        apply_d=[' <h2 class="h5" id="what-to-include-in-your-application">What to include in your application</h2>',
'    <div><p>When you have completed your application, you will also need to upload copies of the following documents with your application:</p>',
'<ul>',
'    <li>Academic Certificates.</li>',
'    <li>Evidence of your English language ability (see below).</li>',
'    <li>A photocopy of your passport.</li>',
'    <li>A reference to support your application – either academic or professional.</li>',
'    <li>A completed <a href="/-/media/files/international/agent-consent-form--leeds-beckett-university-final.pdf?la=en" target="_blank">Agent Consent Form</a>&nbsp;(required if you are applying via or with the help of an agent).</li>',
'</ul>',]
        apply_d=remove_class(apply_d)
        item['apply_documents_en']=apply_d

        alevel=response.xpath('//div[@data-attendance="Full-time"]//div[contains(@class,"hidepointsondesktop")]//div[contains(text(),"POINTS REQUIRED")]/preceding-sibling::div/text()').extract()
        # print(alevel)
        if alevel!=[]:
            item['alevel']=alevel[0]+' POINTS REQUIRED'
        # yield item

        
