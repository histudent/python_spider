import scrapy
import re
from scrapySchool_England.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getDuration import getIntDuration,getTeachTime
from scrapySchool_England.getStartDate import getStartDate
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts

class UniversityOfStrathclyde_RSpider(scrapy.Spider):
    name = "UniversityOfStrathclyde_R"
    # allowed_domains = ['baidu.com']
    url_start = "https://www.strath.ac.uk"
    start_urls = ['https://www.strath.ac.uk/courses/?delivery=attendance&attendance=full-time&level_ug=false&level_pgr=false']

    def parse(self, response):
        # 获得链接
        contentText = response.text
        taughtUrl = re.findall(r"/courses/research/.*/", contentText)
        print(len(taughtUrl))
        print(taughtUrl)

        for link in taughtUrl:
            url = "https://www.strath.ac.uk" + link
            yield scrapy.Request(url, callback=self.parse_data)
    # def error_back(self, response):
    #     with open("err.txt", "a+") as f:
    #         f.write(response.url+"\n==============")
    def parse_data(self, response):
        item = get_item1(ScrapyschoolEnglandItem1)
        # item['country'] = "England"
        # item["website"] = "https://www.strath.ac.uk/"
        item["university"] = "University of Strathclyde"
        item['url'] = response.url
        # 授课方式
        item['teach_type'] = 'phd'
        # 学位类型
        item['degree_type'] = 3
        item['location'] = "16 Richmond Street, Glasgow, G1 1XQ"
        print("===========================")
        print(response.url)
        try:
            # 学位类型
            degree_type = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/span/text()").extract()
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name'] = ", item['degree_name'])

            if "PhD" in item['degree_name']:
                item['teach_type'] = 'phd'
            # 专业名
            programme = response.xpath(
                "//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/text()").extract()
            # print("programme = ", programme)
            item['programme_en'] = ''.join(programme).strip()
            print("item['programme_en'] = ", item['programme_en'])

            if "Engineering" in item['programme_en']:
                item['department'] = "Faculty of Engineering"
            elif "Science" in item['programme_en']:
                item['department'] = "Faculty of Science"
            elif "Business" in item['programme_en'] or "Finance" in item['programme_en'] or "Marketing" in item['programme_en']:
                item['department'] = "Strathclyde Business School"
            print("item['department'] = ", item['department'])

            # 课程长度、开学时间、截止日期
            durationTeachtime = response.xpath("//b[contains(text(),'Study mode and duration')]/../text()").extract()
            clear_space(durationTeachtime)
            # print("durationTeachtime: ", durationTeachtime)
            durationTeachtimeStr = ''.join(durationTeachtime)

            item['teach_time'] = getTeachTime(durationTeachtimeStr)
            duration_list = getIntDuration(durationTeachtimeStr)
            # print(duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])
            # print("item['teach_time'] = ", item['teach_time'])

            start_date = response.xpath("//b[contains(text(),'Start date')]/../text()").extract()
            start_date_str = ''.join(start_date).replace(":", "")
            print("start_date_str = ", start_date_str)
            item['start_date'] = getStartDate(start_date_str)
            if item['start_date'] != "" and item['start_date'] > "06" and "2018" not in item['start_date'] and "2019"  not in item['start_date']:
                item['start_date'] = "2018-" + item['start_date']
            elif item['start_date'] != "" and item['start_date'] <= "06" and "2018" not in item['start_date'] and "2019"  not in item['start_date']:
                item['start_date'] = "2019-" + item['start_date']
            # print("item['start_date'] = ", item['start_date'])


            # 截止日期
            deadline = response.xpath("//b[contains(text(),'Application deadline')]/../text()").extract()
            deadline = ''.join(start_date).replace(":", "").strip()
            print("deadline = ", deadline)
            item['deadline'] = getStartDate(deadline)
            print("item['deadline'] = ", item['deadline'])

            # 专业描述
            overview = response.xpath("//article[@id='research-opportunities']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            print("item['overview_en'] = ", item['overview_en'])

            # 课程设置、评估方式
            modules = response.xpath("//h3[contains(text(),'Learning & teaching')]/preceding-sibling::*").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath("//h3[contains(text(),'Learning & teaching')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item["assessment_en"] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en'] = ", item['assessment_en'])

            # 学术要求、英语要求
            rntry_requirements = response.xpath("//article[@id='entry-requirements']//text()").extract()
            item["rntry_requirements"] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            apply_proces_en = response.xpath("//article[@id='how-can-i-apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            print("item['apply_proces_en'] = ", item['apply_proces_en'])

            apply = response.xpath("//article[@id='how-can-i-apply']//text()").extract()
            clear_space(apply)
            ielts_re = re.findall(r"IELTS.{1,80}", ''.join(apply))
            # print("ielts_re = ", ielts_re)
            item["ielts_desc"] = ''.join(ielts_re)
            print("item['ielts_desc'] = ", item['ielts_desc'])

            ielts_dict = get_ielts(item['ielts_desc'])
            # print(ieltlsrw)
            item['ielts'] = ielts_dict.get('IELTS')
            item['ielts_l'] = ielts_dict.get('IELTS_L')
            item['ielts_s'] = ielts_dict.get('IELTS_S')
            item['ielts_r'] = ielts_dict.get('IELTS_R')
            item['ielts_w'] = ielts_dict.get('IELTS_W')
            if item['ielts'] != None:
                item['ielts'] = item['ielts'].strip('.').strip()
            if item['ielts_l'] != None:
                item['ielts_l'] = item['ielts_l'] .strip('.').strip()
            if item['ielts_s'] != None:
                item['ielts_s'] = item['ielts_s'].strip('.').strip()
            if item['ielts_r'] != None:
                item['ielts_r'] = item['ielts_r'].strip('.').strip()
            if item['ielts_w'] != None:
                item['ielts_w'] = item['ielts_w'] .strip('.').strip()
            print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s "
                  %(item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # 学费    //article[@id='fees-and-funding']/ul[3]/li
            tuition_fee = response.xpath("//html//article[@id='fees-and-funding']/*[contains(text(),'International')]/following-sibling::*[1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£[\d,]+", ''.join(tuition_fee))
            # print(tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = ''.join(tuition_fee_re[0]).replace("£", "").replace(",", "")
                item['tuition_fee_pre'] = "£"
            print("item['tuition_fee'] = ", item['tuition_fee'])


            # 就业    //article[@id='careers']
            career = response.xpath("//article[@id='support-and-development']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            print("item['career_en'] = ", item['career_en'])

            yield item
        except Exception as e:
            with open(item['university'] + str(item['degree_type']) + ".txt", 'a+', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)



