import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts
from scrapySchool_England.getDuration import getIntDuration, getTeachTime

class BathSpaUniversity_PSpider(scrapy.Spider):
    name = "BathSpaUniversity_P"
    start_urls = ["https://www.bathspa.ac.uk/courses/course-index-a-z/"]


    def parse(self, response):
        links = response.xpath("//h3[@class='title'][contains(text(),'Postgraduate taught degrees')]/following-sibling::div[1]//a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.bathspa.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)


    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.bathspa.ac.uk/"
        item['university'] = "Bath Spa University"
        item['url'] = response.url
        item['teach_type'] = 'taught'
        # 学位类型
        item['degree_type'] = 2
        print("===========================")
        print(response.url)
        try:
            item['location'] = 'Bath'
            # 专业、学位类型//div[@class='masthead-inner']/div/div[@class='masthead-content']/h1
            programme = response.xpath("//div[@class='masthead-inner']/div/div[@class='masthead-content']/h1//text()").extract()
            item['programme_en'] = ''.join(programme)
            print("item['programme_en']: ", item['programme_en'])

            degree_type = response.xpath("//div[@class='masthead-inner']/div/div[@class='masthead-content']/p[1]//text()").extract()
            item['degree_name'] = ''.join(degree_type)
            # print("item['degree_name']: ", item['degree_name'])
            if item['degree_name'] == "" and "phd" in item['programme_en'].lower() or item['degree_name'] == "" and "doctorate" in item['programme_en'].lower():
                item['degree_name'] = 'phd'
                item['teach_type'] = 'phd'
                # 学位类型
                item['degree_type'] = 3
            # print("item['teach_type']: ", item['teach_type'])
            # print("item['degree_type']: ", item['degree_type'])
            print("item['degree_name']: ", item['degree_name'])

            # //div[@class='content']/div[@class='collapsible-content'][1]/div[2]/div[1]
            overview = response.xpath("//h3[contains(text(),'Overview')]/..").extract()
            if len(overview) == 0:
                overview = response.xpath("//h3[contains(text(),'overview')]/..").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en']: ", item['overview_en'])

            modules = response.xpath("//h3[contains(text(),'Course structure')]/..|//h3[contains(text(),'Course modules')]/..").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en']: ", item['modules_en'])

            assessment_en = response.xpath("//h3[contains(text(),'How will I be assessed?')]/..|//h3[contains(text(),'How will I be taught?')]/..|//h3[contains(text(),'Assessment')]/..").extract()
            item['assessment_en'] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en']: ", item['assessment_en'])

            career = response.xpath("//h3[contains(text(),'Career')]/..|//h3[contains(text(),'career')]/..").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en']: ", item['career_en'])

            feeContent = response.xpath(
                "//h3[contains(text(),'International students full time')]/../div/table[1]//td[contains(text(), '2018/19 entry')]/following-sibling::td//text()").extract()
            clear_space(feeContent)
            # print(feeContent)
            if len(feeContent) > 0:
                item['tuition_fee'] = int(feeContent[0].replace("£", "").replace(",", "").strip())
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee']: ", item['tuition_fee'])
            # print("item['tuition_fee_pre']: ", item['tuition_fee_pre'])

            # //div[@class='content']/div[@class='collapsible-content highlighted']/div[2]/div[2]
            entry_requirements = response.xpath("//div[@class='content']/div[@class='collapsible-content highlighted']//text()").extract()
            clear_space(entry_requirements)
            item['rntry_requirements'] = clear_lianxu_space(entry_requirements)
            # print("item['rntry_requirements']: ", item['rntry_requirements'])

            ieltsList = re.findall(r".{1,60}IELTS.{1,60}", item['rntry_requirements'])
            item['ielts_desc'] =''.join(ieltsList)
            print("item['ielts_desc']: ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s " % (
                    item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            interview_desc_en = response.xpath("//h3[contains(text(),'Interview and portfolio guidance')]/..").extract()
            item['interview_desc_en'] = remove_class(clear_lianxu_space(interview_desc_en))
            # print("item['interview_desc_en']: ", item['interview_desc_en'])

            # https://www.bathspa.ac.uk/international/country-advice/china/
            item['require_chinese_en'] = "<p><strong>Postgraduate</strong></p><ul><li>Normally a Bachelor's degree with honours and a good passing grade from an internationally recognised university or Higher Education institution</li><li>Other international qualifications to an equivalent standard will also be considered.</li></ul> "

            # https://www.bathspa.ac.uk/applicants/how-to-apply/postgraduate/
            item['apply_proces_en'] = remove_class(clear_lianxu_space(["""<div class="content">
      <div data-hash-anchor='<a id="d.en.1289"></a>'></div>
<div class="intro-text">
	<p class="intro">You can apply for one of our taught postgraduate courses online from the webpage for the course you're interested in.</p>
</div><div class="rich-text" >
  <div data-hash-anchor='<a id="d.en.1291"></a>'></div>
    <div>
        <h2>How to apply</h2>
<p>To apply simply hit on the "Apply Now" on the course’s webpage. You'll need to create an online account.</p>
<p>Don’t have time to complete your whole application? Don’t worry, you can save your application and come back to it at anytime.</p>
<p>Entry requirements are listed on the course's webpage. If you don’t hold a first degree you may be required to provide additional evidence to support your application.</p>
<p><a href="/courses/">Search for your course</a></p>
<h3>What do I need?</h3>
<p>As part of the online application you’ll need to upload a variety of documents. This may include:</p>
<ul>
<li>Copy of passport</li>
<li>Qualifications</li>
<li>Portfolio</li>
<li>Previous UK visas (if applicable)</li>
<li>Reference.</li>
</ul>
<h3>Contact us</h3>
<p>Please contact us if you have any questions or concerns:&nbsp;<a href="mailto:admissions@bathspa.ac.uk">admissions@bathspa.ac.uk</a></p>
<p>Phone: +44 (0)1225 876180</p>
<h3>Interviews</h3>
<p>You may be required to attend an interview as part of the selection process for a postgraduate course. This is usually a 30 minute discussion of your experience and any work submitted with the application.</p>
<p>Telephone or Skype interviews can usually be arranged for applicants applying from outside of the UK.</p>
    </div>
</div>
"""]))
            # print("item['apply_proces_en']: ", item['apply_proces_en'])

#             department_dict = {"arts management":"Bath Business School","accounting and finance":"Bath Business School",
# "business and management":"Bath Business School",
# "business and management (accounting)":"Bath Business School",
# "business and management (entrepreneurship)":"Bath Business School",
# "business and management (international business)":"Bath Business School",
# "business and management (marketing)":"Bath Business School",
# "curatorial practice":"Bath School of Art and Design",
# "design (ceramics)":"Bath School of Art and Design",
# "design (fashion and textiles)":"Bath School of Art and Design",
# "fine art":"Bath School of Art and Design",
# "visual communication":"Bath School of Art and Design",
# "children's publishing":"College of Liberal Arts",
# "classical acting":"College of Liberal Arts",
# "composition":"College of Liberal Arts",
# "creative producing":"College of Liberal Arts",
# "creative writing":"College of Liberal Arts",
# "creative writing phd":"College of Liberal Arts",
# "crime and gothic fictions":"College of Liberal Arts",
# "dance":"College of Liberal Arts",
# "directing":"College of Liberal Arts",
# "directing circus":"College of Liberal Arts",
# "environmental humanities":"College of Liberal Arts",
# "environmental management":"College of Liberal Arts",
# "feature filmmaking":"College of Liberal Arts",
# "heritage management":"College of Liberal Arts",
# "intercultural musicology":"College of Liberal Arts",
# "liberal arts":"College of Liberal Arts",
# "literature, landscape and environment":"College of Liberal Arts",
# "music performance":"College of Liberal Arts",
# "performing shakespeare":"College of Liberal Arts",
# "principles of applied neuropsychology":"College of Liberal Arts",
# "scriptwriting":"College of Liberal Arts",
# "songwriting (campus based)":"College of Liberal Arts",
# "songwriting (distance learning)":"College of Liberal Arts",
# "sound (arts)":"College of Liberal Arts",
# "sound (design)":"College of Liberal Arts",
# "sound (production)":"College of Liberal Arts",
# "theatre for young audiences":"College of Liberal Arts",
# "transnational writing":"College of Liberal Arts",
# "travel and nature writing":"College of Liberal Arts",
# "writing for young people":"College of Liberal Arts",
# "counselling and psychotherapy practice":"Institute for Education",
# "education (education studies)":"Institute for Education",
# "education (early childhood studies)":"Institute for Education",
# "education (international education)":"Institute for Education",
# "education (leadership and management)":"Institute for Education",
# "inclusive education":"Institute for Education",
# "professional practice":"Institute for Education",
# "professional practice in higher education":"Institute for Education",
# "teaching english to speakers of other languages":"Institute for Education",
# "specific learning difficulties / dyslexia":"Institute for Education",
# "national award for special educational needs coordination":"Institute for Education",
# "professional doctorate in education":"Institute for Education",
# }
#             item['department'] = department_dict.get(item['programme_en'].lower())
#             print("item['department']: ", item['department'])
            department = response.xpath("//dt[contains(text(),'School')]/following-sibling::dd[1]//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            location = response.xpath("//dt[contains(text(),'Campus or location')]/following-sibling::dd[1]//text()").extract()
            item['location'] = ''.join(location).strip()
            print("item['location']: ", item['location'])

            # duration
            durationMode = response.xpath(
                "//dt[contains(text(),'Course length')]/following-sibling::dd[1]//text()").extract()
            clear_space(durationMode)
            print("durationMode: ", durationMode)
            durationMode = ''.join(durationMode)
            duration_list = getIntDuration(''.join(durationMode))
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            item['teach_time'] = getTeachTime(''.join(durationMode))
            print("item['duration']: ", item['duration'])
            print("item['teach_time']: ", item['teach_time'])
            print("item['duration_per']: ", item['duration_per'])
            item['other'] = durationMode
            yield item
        except Exception as e:
            with open("scrapySchool_England/error/" + item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

