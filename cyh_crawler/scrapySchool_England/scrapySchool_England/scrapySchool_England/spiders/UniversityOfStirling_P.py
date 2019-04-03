# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.middlewares import clear_duration
from scrapySchool_England.clearSpace import clear_same_s
class UniversityofstirlingSpider(scrapy.Spider):
    name = 'UniversityOfStirling_P'
    allowed_domains = ['stir.ac.uk']
#     start_urls = ['https://www.stir.ac.uk/courses/pg-taught/']
#     def parse(self, response):
#         urllist=['/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fadvancing-practice%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fadvancing-practice%2F&auth=bw%2BxqjUeydNQrQRPTA7HFQ&profile=_default_preview&rank=4&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-professional-studies%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-professional-studies%2F&auth=R1ye4EVIuUIbBCXdZlPxTw&profile=_default_preview&rank=9&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-msc%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-msc%2F&auth=fqlfkbja3ILJ7zP6C1PYgQ&profile=_default_preview&rank=10&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-mres%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-mres%2F&auth=MvfIMpmU8EL%2BwnoecsjnNQ&profile=_default_preview&rank=11&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-criminology%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-criminology%2F&auth=cKtFtiaLO78BJq5yNBT25A&profile=_default_preview&rank=12&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fsocial-research-statistics-and-social-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fsocial-research-statistics-and-social-research%2F&auth=3a%2FIermQ36%2FaabH8or6OHA&profile=_default_preview&rank=13&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-doctorate%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fapplied-social-research-doctorate%2F&auth=6xBSZgh8whbeOKIglNnZVQ&profile=_default_preview&rank=14&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquatic-food-security%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquatic-food-security%2F&auth=hBLTs2Y9g%2FNXyIfaMsL1wA&profile=_default_preview&rank=16&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquatic-pathobiology%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquatic-pathobiology%2F&auth=Vy1xkzlFTzVxLV%2BkqXGdmg&profile=_default_preview&rank=17&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquatic-veterinary-studies%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquatic-veterinary-studies%2F&auth=Z0C2ZFB2QMGXjPge3QZEZQ&profile=_default_preview&rank=18&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Fbanking-finance%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Fbanking-finance%2F&auth=Dsl9dartO47VGr0Wmhcfyg&profile=_default_preview&rank=19&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Fbehavioural-decision-making-finance%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Fbehavioural-decision-making-finance%2F&auth=QBur%2F67zBEUUU%2BJetvAidw&profile=_default_preview&rank=20&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fbehavioural-science-for-management%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fbehavioural-science-for-management%2F&auth=rq95b7%2BFw0lQCTJejxepmA&profile=_default_preview&rank=21&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Fbig-data%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Fbig-data%2F&auth=41qRHloh0KbdMtXW1FsXGw&profile=_default_preview&rank=22&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Fprofessional-doctorate-big-data-science%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Fprofessional-doctorate-big-data-science%2F&auth=DuthZYpLIk2UWR%2F5mrSD1Q&profile=_default_preview&rank=23&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fbusiness-management-msc%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fbusiness-management-msc%2F&auth=RZLMHpVosLcWn%2BvWmQxvRQ&profile=_default_preview&rank=25&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fbusiness-management-research-methods-mres%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fbusiness-management-research-methods-mres%2F&auth=%2Fa%2FWTYB%2BdATRJNaeWHcoZw&profile=_default_preview&rank=26&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fclinical-doctorates%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fclinical-doctorates%2F&auth=1%2FHO1lxtOYzT9AADt20nhA&profile=_default_preview&rank=30&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fcreative-writing%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fcreative-writing%2F&auth=gKJMI6mrS%2Bk7DSmCD7Thjw&profile=_default_preview&rank=33&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fcriminological-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fcriminological-research%2F&auth=SFAKY6gFwd9HAGp1qyniug&profile=_default_preview&rank=34&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fdata-science-for-business%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fdata-science-for-business%2F&auth=WncqHN%2F3fRDyL0UmkCLw2Q&profile=_default_preview&rank=37&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fdementia-studies%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fdementia-studies%2F&auth=e%2FHu2U8WFoI54mD6dyV1SA&profile=_default_preview&rank=38&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fdigital-media-and-society%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fdigital-media-and-society%2F&auth=Dqns6ipw073ILqrwxQSbeg&profile=_default_preview&rank=40&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fdoctor-of-business-administration%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fdoctor-of-business-administration%2F&auth=N1KshO2jwd1fbPzprC4ipQ&profile=_default_preview&rank=41&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fdiplomacy%2Fdoctor-of-diplomacy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fdiplomacy%2Fdoctor-of-diplomacy%2F&auth=WEjFksdY6%2Bf73USY3Ob3Kg&profile=_default_preview&rank=42&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Fedd-educational-doctorate%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Fedd-educational-doctorate%2F&auth=HmlFEnWfXiKGXrBwzIOYBQ&profile=_default_preview&rank=43&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fearly-years-practice-health-visiting%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fearly-years-practice-health-visiting%2F&auth=cb%2F5G9hgyWgreoUiHohMcQ&profile=_default_preview&rank=44&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Feconomics-for-business-and-policy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Feconomics-for-business-and-policy%2F&auth=bpEUCpIrLFro%2FkYRtAy6Aw&profile=_default_preview&rank=47&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Feducation-studies-and-tesol%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Feducation-studies-and-tesol%2F&auth=CcqznYY7zs1URdb0F8jwJQ&profile=_default_preview&rank=50&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Feducational-leadership-sqh%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Feducational-leadership-sqh%2F&auth=hHTJN81ot%2BLQ6gkmVYBa7Q&profile=_default_preview&rank=51&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Feducational-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Feducational-research%2F&auth=nECekqYJLqP7Q7oYhAlw3Q&profile=_default_preview&rank=52&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fenglish-language-linguistics%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fenglish-language-linguistics%2F&auth=OJgXuWDxccjStLXTIn0dEw&profile=_default_preview&rank=53&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Fenvironment-heritage-policy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Fenvironment-heritage-policy%2F&auth=6ameAaHlbqhfYxT5CSJ%2B5Q&profile=_default_preview&rank=55&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fenvironmental-sciences%2Fenvironmental-management%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fenvironmental-sciences%2Fenvironmental-management%2F&auth=qnUF4pH6JAMtj94JMEq3ZQ&profile=_default_preview&rank=57&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fenvironmental-sciences%2Fenvironmental-management-conservation%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fenvironmental-sciences%2Fenvironmental-management-conservation%2F&auth=uKiH4R%2FAo2kFy8fXGtVM4A&profile=_default_preview&rank=58&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fenvironmental-sciences%2Fenvironmental-management-energy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fenvironmental-sciences%2Fenvironmental-management-energy%2F&auth=rGwJGvrbwuf6NJ7Jzdb6Pg&profile=_default_preview&rank=59&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Fenvironmental-policy-governance%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Fenvironmental-policy-governance%2F&auth=alfovEvTIhJto36PgrVt2g&profile=_default_preview&rank=60&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Ffinance%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Ffinance%2F&auth=JtAEvbdU4oEsfuHOhXctaw&profile=_default_preview&rank=66&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Ffintech%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Ffintech%2F&auth=P6zaoVxsHRJnHf6UU8WnoA&profile=_default_preview&rank=68&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fgender-studies%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fgender-studies%2F&auth=KIZxIFkwW5YacuWMFxtPzA&profile=_default_preview&rank=70&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fglobal-issues-in-gerontology-ageing%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fglobal-issues-in-gerontology-ageing%2F&auth=ehNFlnfvAt3zFBjW6WNNgA&profile=_default_preview&rank=72&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fhealth-psychology%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fhealth-psychology%2F&auth=mLgC5lN5V%2FiiFzUv0xz5TA&profile=_default_preview&rank=73&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fhealth-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fhealth-research%2F&auth=uqPmijNdlnYBHlFZM2te1w&profile=_default_preview&rank=74&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhistory-politics%2Fhistorical-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhistory-politics%2Fhistorical-research%2F&auth=lR81nS3XYUbfaLSeIcEqWQ&profile=_default_preview&rank=76&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fhousing-studies-part-time%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fhousing-studies-part-time%2F&auth=4DLmHhogD0tTX%2FR1eh892g&profile=_default_preview&rank=78&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fhousing-studies-with-internship%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fhousing-studies-with-internship%2F&auth=pZkW3DwtFfOO6VpIOzdKig&profile=_default_preview&rank=79&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fhuman-animal-interaction%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fhuman-animal-interaction%2F&auth=%2F%2FqGzPAiOBu2%2BAKIqBqnZA&profile=_default_preview&rank=80&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmsc-human-resource-management%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmsc-human-resource-management%2F&auth=zYIUNuUn3c60hg9SBSLX2Q&profile=_default_preview&rank=81&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fhumanities%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fhumanities%2F&auth=60R4umqb01LJmWJbRHJxow&profile=_default_preview&rank=83&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Finternational-accounting-finance%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Finternational-accounting-finance%2F&auth=loVXzSFTQkRLqX38HQseLA&profile=_default_preview&rank=85&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Finternational-business%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Finternational-business%2F&auth=1HFzilrkGpGG%2BMH7DKOlBQ&profile=_default_preview&rank=86&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Finternational-conflict-cooperation%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Finternational-conflict-cooperation%2F&auth=Odc8uFscXUeC%2BU6xsAn%2BtQ&profile=_default_preview&rank=87&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Finternational-energy-law-policy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Finternational-energy-law-policy%2F&auth=qhUOonxnTKwzR65z3sO%2BcA&profile=_default_preview&rank=88&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Finternational-human-resource-management%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Finternational-human-resource-management%2F&auth=huvwGRGXU7h%2BS9KQd8j5PA&profile=_default_preview&rank=89&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Finternational-journalism%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Finternational-journalism%2F&auth=ks8wOSZhkaqaAVG897%2BnvQ&profile=_default_preview&rank=90&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Finvestment-analysis%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faccounting-finance-banking-and-economics%2Finvestment-analysis%2F&auth=AegeY2Gi2qMUGtTgEEL0XQ&profile=_default_preview&rank=92&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmanagement-muscat%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmanagement-muscat%2F&auth=Dy2YT%2FoYHrz0Qnu9f68Qmw&profile=_default_preview&rank=98&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Fmanagement-english-language-teaching%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Fmanagement-english-language-teaching%2F&auth=C2UwAX%2F0TP7hnahb5WUhdg&profile=_default_preview&rank=99&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmarketing%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmarketing%2F&auth=IzoM3DwUb2WhckVbQiQkGA&profile=_default_preview&rank=101&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmba%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fmba%2F&auth=F5xPMOjvBZgvRjrJUYvqqw&profile=_default_preview&rank=103&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Fmathematics-and-data-science%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcomputing-and-data-science%2Fmathematics-and-data-science%2F&auth=9q5LRWWoESuNHh%2B%2B6T79LA&profile=_default_preview&rank=105&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fmedia-communications-management-vietnam%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fmedia-communications-management-vietnam%2F&auth=aypZKC7jI0umxrtqv%2Fy69g&profile=_default_preview&rank=106&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fmedia-management%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fmedia-management%2F&auth=jc6Zc4l%2Bpxj7GB8FGd5U1Q&profile=_default_preview&rank=107&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fmedia-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fmedia-research%2F&auth=kWeI5%2Fh4h%2BbF7zrupGzXww&profile=_default_preview&rank=108&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fperformance-coaching%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fperformance-coaching%2F&auth=FFM1n49J40NC2nD%2F7IVfpA&profile=_default_preview&rank=114&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhistory-politics%2Fphilosophy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhistory-politics%2Fphilosophy%2F&auth=0jHUzASM%2BFUH0Is7mcCvTQ&profile=_default_preview&rank=115&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Fprofessional-education-leadership%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Fprofessional-education-leadership%2F&auth=zy7nhR462IFxcL1i99ZMAw&profile=_default_preview&rank=122&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-research-methods-autism-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-research-methods-autism-research%2F&auth=rhgZUk%2B8gRa%2BkJFANJntpA&profile=_default_preview&rank=123&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-bilingualism-research%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-bilingualism-research%2F&auth=FdyWDpnA23F4iIBinE9FEw&profile=_default_preview&rank=124&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-research-methods-child-development%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-research-methods-child-development%2F&auth=h2m02Ik9bveQBO%2FT1kqEbQ&profile=_default_preview&rank=125&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fresearch-methods-cognition-and-neuropsychology%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fresearch-methods-cognition-and-neuropsychology%2F&auth=WyseYv6AsJNWydbhcdh3vA&profile=_default_preview&rank=126&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-evolutionary-psychology%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-evolutionary-psychology%2F&auth=evDzk%2FKW8uLk0uo0ZHQnAQ&profile=_default_preview&rank=127&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-research-methods-general%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-research-methods-general%2F&auth=PaUCVW0X%2BWpzQ8lT6fNYaQ&profile=_default_preview&rank=128&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-perception-and-action%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-perception-and-action%2F&auth=ER5wXD2ualq2KrfTlFBLpw&profile=_default_preview&rank=129&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-psychology-of-faces%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsych-research-methods-psychology-of-faces%2F&auth=cx0kydC75IciC%2BwPlbBKpQ&profile=_default_preview&rank=130&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-therapy-in-primary-care%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychological-therapy-in-primary-care%2F&auth=sVOTJSpFsJkKgG0U6uWTBQ&profile=_default_preview&rank=131&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychology-accredited-conversion-course%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fpsychology%2Fpsychology-accredited-conversion-course%2F&auth=47PFpWQ00foB1jREqeS3ew&profile=_default_preview&rank=133&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fpsychology-of-sport%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fpsychology-of-sport%2F&auth=VlblLV5arJcX7gOUcAm8uw&profile=_default_preview&rank=134&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fpublic-health%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fhealth-sciences-sport%2Fpublic-health%2F&auth=UYS7WSx%2FRUj9YJZLsHTTDg&profile=_default_preview&rank=135&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Fpublic-policy%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Flaw-politics-and-policy%2Fpublic-policy%2F&auth=4L%2F8ywcUmbMr8VCXbXlAYA&profile=_default_preview&rank=136&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fpublishing-studies-mres%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fpublishing-studies-mres%2F&auth=twQvD79yK7WhP3S7fVo8bQ&profile=_default_preview&rank=137&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fpublishing-studies-mlitt%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fpublishing-studies-mlitt%2F&auth=HtIbyKrfsRISABEwsT4Ktg&profile=_default_preview&rank=138&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fscottish-literature%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fscottish-literature%2F&auth=Kl9rUGAUFmscmJPi%2Fk3qxQ&profile=_default_preview&rank=143&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fsocial-enterprise%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fsocial-enterprise%2F&auth=MDs2yV4%2FgkBDolJovMhEpQ&profile=_default_preview&rank=144&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fsocial-work-studies%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsocial-sciences%2Fsocial-work-studies%2F&auth=32ggq40PSSeQ3CL4zyNO7w&profile=_default_preview&rank=146&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fsport-management%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fsport-management%2F&auth=e8IHBViFbIGnu7s7Ig99sw&profile=_default_preview&rank=153&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fsport-nutrition%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fsport%2Fsport-nutrition%2F&auth=dKNOlU5HtstBFV601AO5Ug&profile=_default_preview&rank=154&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fstrategic-communication-public-relations-pfu%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fstrategic-communication-public-relations-pfu%2F&auth=SzIXgwj78CWyFz3qL39lrQ&profile=_default_preview&rank=157&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fstrategic-public-relations%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fstrategic-public-relations%2F&auth=%2FBiRif7UVVcSY4yhIh2cKg&profile=_default_preview&rank=158&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fstrategic-public-relations-communication-mgt%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Fstrategic-public-relations-communication-mgt%2F&auth=UboH28ynZRLUEHN3UY9F4g&profile=_default_preview&rank=159&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fstrategic-sustainable-business%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fbusiness-and-management%2Fstrategic-sustainable-business%2F&auth=gyFLP73XnCqptFHct49TSA&profile=_default_preview&rank=160&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquaculture-sustainable-aquaculture%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Faquaculture%2Faquaculture-sustainable-aquaculture%2F&auth=%2FfVZTzPPqi2BvyBx1rR4ZA&profile=_default_preview&rank=161&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftesol-masters-msc%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftesol-masters-msc%2F&auth=Uc0k4fMe%2BsID%2BIPtKaE9Lw&profile=_default_preview&rank=164&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftesol-online%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftesol-online%2F&auth=bxWODt%2BxaAhIlgOzMFhBgg&profile=_default_preview&rank=165&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftqfe-in-service%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftqfe-in-service%2F&auth=CJagXwDnk1oOYUMdU2X6oA&profile=_default_preview&rank=166&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftqfe-pre-service%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftqfe-pre-service%2F&auth=CxOyzxSiF45sZA4nvD3LNg&profile=_default_preview&rank=167&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Ftelevision-content-development-and-production%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fcommunications-media-culture%2Ftelevision-content-development-and-production%2F&auth=apmHrd9yPI92t93SFKhPQg&profile=_default_preview&rank=168&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftesol-research-phd%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Feducation%2Ftesol-research-phd%2F&auth=khb%2Fbs00CEfbWwW2xa9p9A&profile=_default_preview&rank=169&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fthe-gothic-imagination%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Fthe-gothic-imagination%2F&auth=Pk62eb3nFDRTFEK3FrKDhA&profile=_default_preview&rank=170&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Ftranslation-studies%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Ftranslation-studies%2F&auth=wk0dZy1lMMuCSIDVDmB8nQ&profile=_default_preview&rank=171&query=%21padrenullquery',
# '/s/redirect?collection=stir-courses&url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Ftranslation-studies-with-tesol%2F&index_url=https%3A%2F%2Fwww.stir.ac.uk%2Fcourses%2Fpg-taught%2Fliterature-and-languages%2Ftranslation-studies-with-tesol%2F&auth=bT4neMXSQL%2BV0V4rKbpJeg&profile=_default_preview&rank=172&query=%21padrenullquery',]
#         for i in urllist:
#             fullurl='https://www.stir.ac.uk'+i
#             #专业连接进去后有可能又多个专业详情页的连接
#             programme=response.xpath('//h1/../following-sibling::div/ul/li/a/@href').extract()
#             if programme!=[]:
#                 for j in programme:
#                     programmeurl='https://www.stir.ac.uk'+ j
#                     yield scrapy.Request(programmeurl,callback=self.parse_main)
#             else:
#                 yield scrapy.Request(fullurl,callback=self.parse_main)
    start_urls=['https://www.stir.ac.uk/courses/pg-taught/social-sciences/criminological-research/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquatic-food-security/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/social-research-statistics-and-social-research/',
'https://www.stir.ac.uk/courses/pg-taught/computing-and-data-science/big-data/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/applied-social-research-mres/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/applied-social-research-criminology/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/applied-social-research-msc/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquatic-veterinary-studies/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquatic-pathobiology/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/television-content-development-and-production/',
'https://www.stir.ac.uk/courses/pg-taught/sport/sport-management/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/strategic-communication-public-relations-pfu/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/social-enterprise/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/publishing-studies-mres/',
'https://www.stir.ac.uk/courses/pg-taught/sport/psychology-of-sport/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychology-accredited-conversion-course/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-perception-and-action/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-evolutionary-psychology/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-psychology-of-faces/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/research-methods-cognition-and-neuropsychology/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychological-research-methods-child-development/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-bilingualism-research/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychological-research-methods-autism-research/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/media-communications-management-vietnam/',
'https://www.stir.ac.uk/courses/pg-taught/history-politics/philosophy/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/international-journalism/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/human-animal-interaction/',
'https://www.stir.ac.uk/courses/pg-taught/education/educational-research/',
'https://www.stir.ac.uk/courses/pg-taught/education/education-studies-and-tesol/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/criminological-research/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/creative-writing/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/data-science-for-business/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquatic-food-security/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/marine-biotechnology/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/business-management-msc/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/social-research-statistics-and-social-research/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/business-management-research-methods-mres/',
'https://www.stir.ac.uk/courses/pg-taught/computing-and-data-science/big-data/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/applied-social-research-mres/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/applied-social-research-criminology/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/applied-social-research-msc/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/behavioural-science-for-management/',
'https://www.stir.ac.uk/courses/pg-taught/accounting-finance-banking-and-economics/behavioural-decision-making-finance/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquatic-veterinary-studies/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquatic-pathobiology/',
'https://www.stir.ac.uk/courses/pg-taught/accounting-finance-banking-and-economics/banking-finance/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/translation-studies-with-tesol/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/translation-studies/',
'https://www.stir.ac.uk/courses/pg-taught/education/tesol-masters-msc/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/the-gothic-imagination/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/television-content-development-and-production/',
'https://www.stir.ac.uk/courses/pg-taught/sport/sport-nutrition/',
'https://www.stir.ac.uk/courses/pg-taught/aquaculture/aquaculture-sustainable-aquaculture/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/strategic-public-relations-communication-mgt/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/strategic-sustainable-business/',
'https://www.stir.ac.uk/courses/pg-taught/sport/sport-management/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/strategic-communication-public-relations-pfu/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/social-work-studies/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/scottish-literature/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/social-enterprise/',
'https://www.stir.ac.uk/courses/pg-taught/law-politics-and-policy/public-policy/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/publishing-studies-mlitt/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/publishing-studies-mres/',
'https://www.stir.ac.uk/courses/pg-taught/sport/psychology-of-sport/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychology-accredited-conversion-course/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-perception-and-action/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychological-research-methods-general/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-evolutionary-psychology/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-psychology-of-faces/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/research-methods-cognition-and-neuropsychology/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychological-therapy-in-primary-care/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychological-research-methods-child-development/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psych-research-methods-bilingualism-research/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/psychological-research-methods-autism-research/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/media-communications-management-vietnam/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/media-research/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/media-management/',
'https://www.stir.ac.uk/courses/pg-taught/computing-and-data-science/mathematics-and-data-science/',
'https://www.stir.ac.uk/courses/pg-taught/accounting-finance-banking-and-economics/investment-analysis/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/international-journalism/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/international-human-resource-management/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/mba/',
'https://www.stir.ac.uk/courses/pg-taught/education/management-english-language-teaching/',
'https://www.stir.ac.uk/courses/pg-taught/law-politics-and-policy/international-energy-law-policy/',
'https://www.stir.ac.uk/courses/pg-taught/law-politics-and-policy/international-conflict-cooperation/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/international-business/',
'https://www.stir.ac.uk/courses/pg-taught/accounting-finance-banking-and-economics/international-accounting-finance/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/humanities/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/human-animal-interaction/',
'https://www.stir.ac.uk/courses/pg-taught/social-sciences/housing-studies-with-internship/',
'https://www.stir.ac.uk/courses/pg-taught/history-politics/historical-research/',
'https://www.stir.ac.uk/courses/pg-taught/psychology/health-psychology/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/gender-studies/',
'https://www.stir.ac.uk/courses/pg-taught/computing-and-data-science/fintech/',
'https://www.stir.ac.uk/courses/pg-taught/business-and-management/human-resource-management/',
'https://www.stir.ac.uk/courses/pg-taught/law-politics-and-policy/environmental-policy-governance/',
'https://www.stir.ac.uk/courses/pg-taught/environmental-sciences/environmental-management-energy/',
'https://www.stir.ac.uk/courses/pg-taught/environmental-sciences/environmental-management-conservation/',
'https://www.stir.ac.uk/courses/pg-taught/environmental-sciences/environmental-management/',
'https://www.stir.ac.uk/courses/pg-taught/law-politics-and-policy/environment-heritage-policy/',
'https://www.stir.ac.uk/courses/pg-taught/education/educational-research/',
'https://www.stir.ac.uk/courses/pg-taught/literature-and-languages/english-language-linguistics/',
'https://www.stir.ac.uk/courses/pg-taught/education/education-studies-and-tesol/',
'https://www.stir.ac.uk/courses/pg-taught/accounting-finance-banking-and-economics/economics-for-business-and-policy/',
'https://www.stir.ac.uk/courses/pg-taught/health-sciences-sport/early-years-practice-health-visiting/',
'https://www.stir.ac.uk/courses/pg-taught/communications-media-culture/digital-media-and-society/',]
    start_urls = set(start_urls)
    def parse(self, response):
        item=get_item1(ScrapyschoolEnglandItem1)
        item['university'] = 'University of Stirling'
        item['url'] = response.url
        career = response.xpath('//div[contains(@id,"after-graduate")]').extract()
        item['career_en']=remove_class(career)
        assessment=response.xpath('//a[contains(text(),"Assessment")]/following-sibling::div').extract()
        item['assessment_en']=remove_class(assessment)
        yield item
    def parses(self,response):
        print(response.url)
        item=get_item1(ScrapyschoolEnglandItem1)
        programme = response.xpath('//h1/text()').extract()
        programme = ''.join(programme).strip()
        # print(programme)
        clear_deg=re.findall('[A-Z]{2,}[a-z]*',programme)
        # print(clear_deg)
        if clear_deg!=[]:
            clear_deg=clear_deg[0]
        else:
            clear_deg=''.join(clear_deg).strip()
        programme=programme.replace(clear_deg,'').strip()
        programme=programme.replace('()','').strip()
        # print(programme)

        item['university'] = 'University of Stirling'
        item['url'] = response.url
        item['location'] = 'Stirling'
        item['programme_en'] = programme
        item['teach_type']='taught'

        degree_type = response.xpath('//span[contains(text(),"Award")]/../text()').extract()
        degree_name = ''.join(degree_type).strip()
        # print(degree_type)
        item['degree_name'] = degree_name

        overview = response.xpath('//div[@id="ug-course-tabs__overview"]').extract()
        overview=clear_same_s(overview)
        overview=remove_class(overview)
        # print(overview)
        item['overview_en'] = overview
        entry_requirement = response.xpath( '//div[@id="ug-course-tabs__entry-requirements"]').extract()
        entry_requirement=clear_same_s(entry_requirement)
        entry_requirement=remove_class(entry_requirement)
        # print(entry_requirement)
        item['rntry_requirements'] = entry_requirement
        IELTS = response.xpath('//li[contains(text(),"IELTS")]//text()').extract()
        IELTS = ''.join(IELTS).strip()
        item['ielts_desc'] = IELTS
        TOEFL = response.xpath('//li[contains(text(),"TOEFL")]//text()').extract()
        TOEFL = ''.join(TOEFL).strip()
        item['toefl_desc'] = TOEFL
        IELTSs = re.findall('\d\.\d', IELTS)
        if len(IELTSs)==2:
            item['ielts']=max(IELTSs)
            item['ielts_l'],item['ielts_s'],item['ielts_r'],item['ielts_w']=min(IELTSs),min(IELTSs),min(IELTSs),min(IELTSs)
        TOEFLs=re.findall('\d{2,3}',TOEFL)
        if len(TOEFLs)==2:
            item['toefl']=max(TOEFLs)
            item['toefl_l'],item['toefl_s'],item['toefl_r'],item['toefl_w']=min(TOEFLs),min(TOEFLs),min(TOEFLs),min(TOEFLs)
        tuition_fee = response.xpath('//*[contains(text(),"£")]/text()').extract()
        tuition_fee = getTuition_fee(tuition_fee)
        item['tuition_fee'] = tuition_fee

        modules = response.xpath('//h3[contains(text(),"Modules")]/following-sibling::*//text()').extract()
        modules=clear_same_s(modules)
        modules = remove_class(modules)
        item['modules_en'] = modules

        career = response.xpath('//a[contains(text(),"Employability skills")]/following-sibling::*').extract()
        career=clear_same_s(career)
        career=remove_class(career)
        # print(career)
        item['career_en']=career

        durations = response.xpath('//span[contains(text(),"Duration")]/../text()').extract()
        mode = re.findall('(?i)full', ''.join(durations))
        if mode != []:
            item['teach_time'] = '1'
        else:
            item['teach_time'] = '2'
        duration=clear_duration(durations)['duration']
        duration_per=clear_duration(durations)['duration_per']
        item['duration'] = duration
        item['duration_per'] = duration_per
        # print(item)
        item['tuition_fee_pre'] = '£'

        yield item
        # print(item)
