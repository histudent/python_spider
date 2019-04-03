import scrapy
import re
from scrapySchool_England_Ben.clearSpace import clear_space, clear_lianxu_space
from scrapySchool_England_Ben.items import ScrapyschoolEnglandBenItem
from scrapySchool_England_Ben.getItem import get_item
from scrapySchool_England_Ben.getDuration import getIntDuration,getTeachTime
from scrapySchool_England_Ben.getStartDate import getStartDate
from scrapySchool_England_Ben.remove_tags import remove_class
from scrapySchool_England_Ben.getIELTS import get_ielts

class UniversityOfStrathclyde_USpider(scrapy.Spider):
    name = "UniversityOfStrathclyde_U"
    # allowed_domains = ['baidu.com']
    url_start = "https://www.strath.ac.uk"
    start_urls = ['https://www.strath.ac.uk/courses/?delivery=attendance&attendance=full-time&level_pgt=false&level_pgr=false']

    def parse(self, response):
        # 获得链接
        contentText = response.text
        taughtUrl = re.findall(r"/courses/undergraduate/.*/", contentText)
        print(len(taughtUrl))
        print(taughtUrl)

        # 更新alevel
#         taughtUrl = ["https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologyhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologyfinance/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologybusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologyeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnology/",
# "https://www.strath.ac.uk/courses/undergraduate/businessadministration/",
# "https://www.strath.ac.uk/courses/undergraduate/business/",
# "https://www.strath.ac.uk/courses/undergraduate/biomolecularsciences/",
# "https://www.strath.ac.uk/courses/undergraduate/biomedicalscience/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingbusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingbusinessenterprise/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingbusinessanalysistechnology/",
# "https://www.strath.ac.uk/courses/undergraduate/accounting/",
# "https://www.strath.ac.uk/courses/undergraduate/biochemistryimmunology/",
# "https://www.strath.ac.uk/courses/undergraduate/biomedicalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/biochemistrymicrobiology/",
# "https://www.strath.ac.uk/courses/undergraduate/biochemistry/",
# "https://www.strath.ac.uk/courses/undergraduate/biomedicalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/appliedchemistrychemicalengineering/",
# "https://www.strath.ac.uk/courses/undergraduate/biochemistrypharmacology/",
# "https://www.strath.ac.uk/courses/undergraduate/architecturalstudies/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingmarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/aero-mechanicalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/accountinghumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/aero-mechanicalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/accountinghospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingmathematicsstatistics/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/accountingfinance/",
# "https://www.strath.ac.uk/courses/undergraduate/sportsengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/sportsengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/sportphysicalactivity/",
# "https://www.strath.ac.uk/courses/undergraduate/spanishmarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/speechlanguagepathology/",
# "https://www.strath.ac.uk/courses/undergraduate/spanishhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/spanishhospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/spanisheducation/",
# "https://www.strath.ac.uk/courses/undergraduate/softwareengineering/",
# "https://www.strath.ac.uk/courses/undergraduate/socialpolicyspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/socialwork/",
# "https://www.strath.ac.uk/courses/undergraduate/spanisheconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/socialpolicyhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/socialpolicyeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/scotsenglishlawclinical/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologysocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologymathematics/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologyhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologyeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologyeducation/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologyspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologycounselling/",
# "https://www.strath.ac.uk/courses/undergraduate/psychologysport/",
# "https://www.strath.ac.uk/courses/undergraduate/productionengineeringmanagementmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/productionengineeringmanagementbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/psychology/",
# "https://www.strath.ac.uk/courses/undergraduate/productdesignengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/prostheticsorthotics/",
# "https://www.strath.ac.uk/courses/undergraduate/productdesignengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/productdesigninnovation/",
# "https://www.strath.ac.uk/courses/undergraduate/primaryeducation/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationspsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationsspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationssocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationsjournalismcreativewriting/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationshumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationseducation/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelationseconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/politicsinternationalrelations/",
# "https://www.strath.ac.uk/courses/undergraduate/physicsmphys/",
# "https://www.strath.ac.uk/courses/undergraduate/physicswithteaching/",
# "https://www.strath.ac.uk/courses/undergraduate/physicsmphyswithadvancedresearch/",
# "https://www.strath.ac.uk/courses/undergraduate/physics/",
# "https://www.strath.ac.uk/courses/undergraduate/philosophypoliticseconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/pharmacy/",
# "https://www.strath.ac.uk/courses/undergraduate/pharmacologymicrobiology/",
# "https://www.strath.ac.uk/courses/undergraduate/pharmacology/",
# "https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithoceanengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithoceanengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithhighperformancemarinevehiclesmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/navalarchitecturewithhighperformancemarinevehiclesbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/navalarchitecturemarineengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/navalarchitecturemarineengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/microbiology/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithmaterialsengineering/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithinternationalstudymeng/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithinternationalstudybeng/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithfinancialmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsstatisticsfinance/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsstatisticseconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/mechanicalengineeringwithaeronautics/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsstatisticsbusinessanalysis/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicswithteaching/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsstatisticsaccounting/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsmmath/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsbsc/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicsphysics/",
# "https://www.strath.ac.uk/courses/undergraduate/marketingpsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/mathematicscomputerscience/",
# "https://www.strath.ac.uk/courses/undergraduate/marketinghospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/marketing/",
# "https://www.strath.ac.uk/courses/undergraduate/marketingbusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/managementmarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/managementhospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/managementbusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/management/",
# "https://www.strath.ac.uk/courses/undergraduate/lawwithfrench/",
# "https://www.strath.ac.uk/courses/undergraduate/lawscotsenglish/",
# "https://www.strath.ac.uk/courses/undergraduate/lawspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/lawwithspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/lawsocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/lawpsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/lawpoliticsinternationalrelations/",
# "https://www.strath.ac.uk/courses/undergraduate/laweducation/",
# "https://www.strath.ac.uk/courses/undergraduate/lawhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/laweconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/law/",
# "https://www.strath.ac.uk/courses/undergraduate/journalismcreativewritingsocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/journalismcreativewritinglaw/",
# "https://www.strath.ac.uk/courses/undergraduate/journalismcreativewritingspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/journalismcreativewritinghumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/journalismcreativewritingeducation/",
# "https://www.strath.ac.uk/courses/undergraduate/journalismcreativewritingeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/internationalbusinesswithamodernlanguage/",
# "https://www.strath.ac.uk/courses/undergraduate/internationalbusiness/",
# "https://www.strath.ac.uk/courses/undergraduate/immunologypharmacology/",
# "https://www.strath.ac.uk/courses/undergraduate/immunologymicrobiology/",
# "https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagementpsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagementhospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagementmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/immunology/",
# "https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagementmarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/humanresourcemanagementbusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/hospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/historyspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/historysocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/historypsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/historylaw/",
# "https://www.strath.ac.uk/courses/undergraduate/historyjournalismcreativewriting/",
# "https://www.strath.ac.uk/courses/undergraduate/historyeducation/",
# "https://www.strath.ac.uk/courses/undergraduate/historyeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/historypoliticsinternationalrelations/",
# "https://www.strath.ac.uk/courses/undergraduate/history/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/historyhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchpoliticsinternationalrelations/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchmarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchsocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchlaw/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchjournalismcreativewriting/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchhospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchpsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/frenchhistory/",
# "https://www.strath.ac.uk/courses/undergraduate/frencheducation/",
# "https://www.strath.ac.uk/courses/undergraduate/forensicanalyticalchemistry/",
# "https://www.strath.ac.uk/courses/undergraduate/frencheconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/financemathematicsstatistics/",
# "https://www.strath.ac.uk/courses/undergraduate/financemarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/financemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/financehumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/financebusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/finance/",
# "https://www.strath.ac.uk/courses/undergraduate/englishlawllb/",
# "https://www.strath.ac.uk/courses/undergraduate/englishspanish/",
# "https://www.strath.ac.uk/courses/undergraduate/englishsocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/englishpsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/englishpoliticsinternationalrelations/",
# "https://www.strath.ac.uk/courses/undergraduate/englishlaw/",
# "https://www.strath.ac.uk/courses/undergraduate/englishhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/englishjournalismcreativewriting/",
# "https://www.strath.ac.uk/courses/undergraduate/english/",
# "https://www.strath.ac.uk/courses/undergraduate/englisheducation/",
# "https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringwithinternationalstudy/",
# "https://www.strath.ac.uk/courses/undergraduate/englishhistory/",
# "https://www.strath.ac.uk/courses/undergraduate/englishfrench/",
# "https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringwithbusinessstudies/",
# "https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/electronicelectricalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/electricalenergysystems/",
# "https://www.strath.ac.uk/courses/undergraduate/electronicdigitalsystems/",
# "https://www.strath.ac.uk/courses/undergraduate/electricalmechanicalengineeringwithinternationalstudy/",
# "https://www.strath.ac.uk/courses/undergraduate/electricalmechanicalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/electricalmechanicalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/educationsport/",
# "https://www.strath.ac.uk/courses/undergraduate/educationsocialservices/",
# "https://www.strath.ac.uk/courses/undergraduate/educationsocialpolicy/",
# "https://www.strath.ac.uk/courses/undergraduate/educationeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/educationhumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/economicsmathematicsstatistics/",
# "https://www.strath.ac.uk/courses/undergraduate/economicsmarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/economicspsychology/",
# "https://www.strath.ac.uk/courses/undergraduate/economicsmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/economicshumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/economicsfinance/",
# "https://www.strath.ac.uk/courses/undergraduate/economicsbusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/economics/",
# "https://www.strath.ac.uk/courses/undergraduate/dataanalytics/",
# "https://www.strath.ac.uk/courses/undergraduate/computersciencemeng/",
# "https://www.strath.ac.uk/courses/undergraduate/computersciencebsc/",
# "https://www.strath.ac.uk/courses/undergraduate/computerelectronicsystemswithinternationalstudy/",
# "https://www.strath.ac.uk/courses/undergraduate/computerelectronicsystemsmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/computerelectronicsystemsbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/civilengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/civilengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/civilenvironmentalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/civilenvironmentalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/chemistrywithteaching/",
# "https://www.strath.ac.uk/courses/undergraduate/chemistrywithdrugdiscovery/",
# "https://www.strath.ac.uk/courses/undergraduate/chemistry/",
# "https://www.strath.ac.uk/courses/undergraduate/chemicalengineeringmeng/",
# "https://www.strath.ac.uk/courses/undergraduate/chemicalengineeringbeng/",
# "https://www.strath.ac.uk/courses/undergraduate/businesslawhospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisemarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisehumanresourcemanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisehospitalitytourismmanagement/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisefinance/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterpriseeconomics/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisebusinessanalysistechnology/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprisebusinesslaw/",
# "https://www.strath.ac.uk/courses/undergraduate/businessenterprise/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologymathematicsstatistics/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologymarketing/",
# "https://www.strath.ac.uk/courses/undergraduate/businessanalysistechnologymanagement/", ]
        for link in taughtUrl:
            url = "https://www.strath.ac.uk" + link
            # url = link
            yield scrapy.Request(url, callback=self.parse_data)
    # def error_back(self, response):
    #     with open("err.txt", "a+") as f:
    #         f.write(response.url+"\n==============")
    def parse_data(self, response):
        item = get_item(ScrapyschoolEnglandBenItem)
        # item['country'] = "England"
        # item["website"] = "https://www.strath.ac.uk/"
        item["university"] = "University of Strathclyde"
        item['url'] = response.url
        # 学位类型
        item['degree_type'] = 1
        item['location'] = "16 Richmond Street, Glasgow, G1 1XQ"
        print("===========================")
        print(response.url)
        try:
            # 学位类型
            degree_type = response.xpath("//main[@id='content']/section[@class='PGtPage']/header[@class='page-summary has-img']/div[@class='wrap']/h1/span/text()").extract()
            item['degree_name'] = ''.join(degree_type).strip()
            print("item['degree_name'] = ", item['degree_name'])

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

            ucascode = response.xpath(
                "//strong[contains(text(),'UCAS code:')]/../text()").extract()
            clear_space(ucascode)
            if len(ucascode) > 0:
                item['ucascode'] = ''.join(ucascode[0]).strip()
            print("item['ucascode']: ", item['ucascode'])

            # 课程长度、开学时间、截止日期
            durationTeachtime = response.xpath("//b[contains(text(),'Study mode and duration')]/../text()").extract()
            clear_space(durationTeachtime)
            print("durationTeachtime: ", durationTeachtime)
            durationTeachtimeStr = ''.join(durationTeachtime)

            duration_list = getIntDuration(durationTeachtimeStr)
            # print(duration_list)
            if len(duration_list) == 2:
                item['duration'] = duration_list[0]
                item['duration_per'] = duration_list[-1]
            # print("item['duration'] = ", item['duration'])
            # print("item['duration_per'] = ", item['duration_per'])

            start_date = response.xpath("//b[contains(text(),'Start date')]/../text()").extract()
            start_date_str = ''.join(start_date).replace(":", "")
            # print("start_date_str = ", start_date_str)
            item['start_date'] = getStartDate(start_date_str)
            if item['start_date'] != "" and item['start_date'] > "06" and "2018" not in item['start_date'] and "2019"  not in item['start_date']:
                item['start_date'] = "2018-" + item['start_date']
            elif item['start_date'] != "" and item['start_date'] <= "06" and "2018" not in item['start_date'] and "2019"  not in item['start_date']:
                item['start_date'] = "2019-" + item['start_date']
            # print("item['start_date'] = ", item['start_date'])


            # 截止日期
            deadline = response.xpath("//b[contains(text(),'Application deadline')]/../text()").extract()
            deadline = ''.join(start_date).replace(":", "").strip()
            # print("deadline = ", deadline)
            item['deadline'] = getStartDate(deadline)
            # print("item['deadline'] = ", item['deadline'])

            # 专业描述
            overview = response.xpath("//article[@id='why-this-course']").extract()
            item['overview_en'] = remove_class(clear_lianxu_space(overview))
            # print("item['overview_en'] = ", item['overview_en'])

            # 课程设置、评估方式
            modules = response.xpath("//h3[contains(text(),'Assessment')]/preceding-sibling::*").extract()
            if len(modules) == 0:
                modules = response.xpath("//h3[contains(text(),'Learning & teaching')]/preceding-sibling::*").extract()
                if len(modules) == 0:
                    modules = response.xpath(
                        "//article[@id='course-content']").extract()
            item['modules_en'] = remove_class(clear_lianxu_space(modules))
            # print("item['modules_en'] = ", item['modules_en'])

            assessment_en = response.xpath(
                "//h3[contains(text(),'Assessment')]/preceding-sibling::*[1]/following-sibling::*").extract()
            if len(assessment_en) == 0:
                assessment_en = response.xpath("//h3[contains(text(),'Learning & teaching')]/preceding-sibling::*[1]/following-sibling::*").extract()
            item["assessment_en"] = remove_class(clear_lianxu_space(assessment_en))
            # print("item['assessment_en'] = ", item['assessment_en'])

            # 学术要求、英语要求
            rntry_requirements = response.xpath("//article[@id='entry-requirements']//text()").extract()
            # item["rntry_requirements"] = clear_lianxu_space(rntry_requirements)
            # print("item['rntry_requirements'] = ", item['rntry_requirements'])

            alevel = response.xpath(
                "//h4[contains(text(),'A Levels')]/following-sibling::p[1]//text()|"
                "//strong[contains(text(),'A Levels')]/..//following-sibling::p[1]//text()").extract()
            if len(alevel) == 0:
                alevel = response.xpath("//*[contains(text(),'A Levels')]/../following-sibling::*[1]//text()").extract()
            clear_space(alevel)
            # print(alevel)
            if len(alevel) > 0:
                item['alevel'] = ''.join(alevel[0]).strip()
            # print("item['alevel'] = ", item['alevel'])
            if len(item['alevel']) > 160:
                item['alevel'] = ''.join(item['alevel'][:161])
            # print("item['alevel']1 = ", item['alevel'])

            item['alevel'] = None
            from lxml import etree
            tmp_html = response.text
            key1 = "<h4>A Levels"
            if key1 not in tmp_html:
                key1 = "<h4><strong>A Levels"
                if key1 not in tmp_html:
                    key1 = "<p><strong>A Levels"
                    if key1 not in tmp_html:
                        key1 = '<h4><span style="font-size: 1em;">A Levels'
                        if key1 not in tmp_html:
                            key1 = '<h4 class="p1">A Levels'
                            if key1 not in tmp_html:
                                key1 = '<p>Year 1 entry<u1:p>'
            key2 = "<h4>International Baccalaureate"
            if key2 not in tmp_html:
                key2 = "<h4><strong>International Baccalaureate"
                if key2 not in tmp_html:
                    key2 = '<p><strong>International Baccalaureate'
                    if key2 not in tmp_html:
                        key2 = '<h4 class="p1">European Baccalaureate'
                        if key2 not in tmp_html:
                            key2 = '<h4 class="p1">International Baccalaureate'
                            if key2 not in tmp_html:
                                key2 = '<h4>IB'
                                if key2 not in tmp_html:
                                    key2 = '<h4><span style="font-size: 1em;">International Baccalaureate'
                                    if key2 not in tmp_html:
                                        key2 = '<h4>HND/HNC</h4>'
            if key1 in tmp_html and key2 in tmp_html:
                # 使用正则匹配需要的标签内容的首尾
                key1_re = re.findall(key1, tmp_html)
                print("key1_re: ", key1_re)
                key2_re = re.findall(key2, tmp_html)
                print("key2_re: ", key2_re)
                # 增加能准确获取的div
                end_html = tmp_html.replace(''.join(key1_re), '<div id="container">' + ''.join(key1_re)).replace(''.join(key2_re), '</div>' + ''.join(key2_re))

                end_html_response = etree.HTML(end_html)
                # 可以使用xpath匹配需要的内容了
                end_content = end_html_response.xpath("//div[@id='container']//text()")
                # 转化成带标签的数据内容
                end_content_str = "".join(end_content).strip()
                # if len(end_content) > 0:
                #     end_content_str = etree.tostring(end_content[0], encoding='unicode', method='html')
                item['alevel'] = end_content_str
            print("item['alevel'] = ", item['alevel'])
            # print(len("36 points overall with 18 at Higher Level, including 6, 5 at Higher Level in two of the following subjects: Biology, Chemistry, Physics, Mathematics, Psychology"))


            ib = response.xpath(
                "//h4[contains(text(),'International Baccalaureate')]/following-sibling::p[1]//text()|"
                "//strong[contains(text(),'International Baccalaureate')]/../following-sibling::p[1]//text()").extract()
            if len(ib) == 0:
                ib = response.xpath("//*[contains(text(),'International Baccalaureate')]/../following-sibling::*[1]//text()").extract()
            clear_space(ib)
            if len(ib) > 0:
                item['ib'] = ''.join(ib[0]).strip()

            if len(item['ib']) > 160:
                item['ib'] = ''.join(item['ib'][:161])
            # print("item['ib'] = ", item['ib'])

            # ielts = response.xpath("//h3[contains(text(),'English language requirements')]/following-sibling::*[position()<4]//text()").extract()
            # print("ielts: ", ielts)
            ielts_re = re.findall(r"IELTS.{1,80}", ''.join(rntry_requirements))
            # print("ielts_re = ", ielts_re)
            item["ielts_desc"] = ''.join(ielts_re)
            # print("item['ielts_desc'] = ", item['ielts_desc'])

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
            # print("item['ielts'] = %s item['ielts_l'] = %s item['ielts_s'] = %s item['ielts_r'] = %s item['ielts_w'] = %s "
            #       %(item['ielts'], item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w']))

            # 学费    //article[@id='fees-and-funding']/ul[3]/li
            tuition_fee = response.xpath("//html//article[@id='fees-and-funding']/*[contains(text(),'International')]/following-sibling::*[1]//text()").extract()
            # print("tuition_fee: ", tuition_fee)
            tuition_fee_re = re.findall(r"£[\d,]+", ''.join(tuition_fee))
            # print(tuition_fee_re)
            if len(tuition_fee_re) > 0:
                item['tuition_fee'] = ''.join(tuition_fee_re[0]).replace("£", "").replace(",", "")
                item['tuition_fee_pre'] = "£"
            # print("item['tuition_fee'] = ", item['tuition_fee'])

            # 就业    //article[@id='careers']
            career = response.xpath("//article[@id='careers']").extract()
            item['career_en'] = remove_class(clear_lianxu_space(career))
            # print("item['career_en'] = ", item['career_en'])

            # //article[@id='apply']
            apply_proces_en = response.xpath("//article[@id='apply']").extract()
            item['apply_proces_en'] = remove_class(clear_lianxu_space(apply_proces_en))
            # print("item['apply_proces_en'] = ", item['apply_proces_en'])

            item['require_chinese_en'] = remove_class(clear_lianxu_space(["""<h2>Entry requirements</h2>
              <h3>Undergraduate</h3>
<p><strong>Undergraduate first year entry (four-year degree programme)</strong>&nbsp;</p>
<p>Huikao 80% on average, and at least 80% in the required subjects.</p>
<p>Provinces with no Huikao: 80% on average over six subjects, including required subjects.</p>
<p><strong>Undergraduate second year entry (three-year degree programme)</strong>&nbsp;</p>
<p>Huikao 80% on average, and at least 80% in the required subjects.</p>
<p>Provinces with no Huikao: 80% on average over six subjects, including required subjects.</p>
<div>Gaokao with at least 525 out of 750, or 70% (If the total mark is not out of 750).</div>"""]))
            yield item
        except Exception as e:
            with open("scrapySchool_England_Ben/error/"+item['university']+str(item['degree_type'])+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================")
            print("异常：", str(e))
            print("报错url：", response.url)



