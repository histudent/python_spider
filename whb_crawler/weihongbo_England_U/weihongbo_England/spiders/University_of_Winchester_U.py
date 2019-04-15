import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_Winchester_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-accounting-and-finance-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-accounting-and-finance-with-foundation-year%2F&auth=YojsiobnnZJYDAl98QOJIQ&profile=courses&rank=1&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-accounting-and-finance%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-accounting-and-finance%2F&auth=qPiMf6iA5JdqgdS3cNkWTg&profile=courses&rank=2&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-accounting-and-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-accounting-and-management%2F&auth=jensMmarcpaZppj11pQBuQ&profile=courses&rank=3&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-american-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-american-studies%2F&auth=GIA8yh1K1Kl5UZFKNJpDoA&profile=courses&rank=4&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-american-studies-and-history%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-american-studies-and-history%2F&auth=m5h0ImnNRmoKCBnnSrntqg&profile=courses&rank=5&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-american-studies-and-politics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-american-studies-and-politics%2F&auth=9pRZ8hrDJy2EK%2FLBPFaaow&profile=courses&rank=6&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-ancient-classical-and-medieval-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-ancient-classical-and-medieval-studies%2F&auth=Uw1mp0WmLw2dyCxE%2BF4B7Q&profile=courses&rank=7&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-animal-welfare-and-society%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-animal-welfare-and-society%2F&auth=4JkoQ3GQGP87e1XpUB%2BjAw&profile=courses&rank=8&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-anthropology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-anthropology%2F&auth=SPLr4nGCBEAOJq0hMzMcxg&profile=courses&rank=9&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-archaeology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-archaeology%2F&auth=zvP1uqtHCuQrazrcylT9Cw&profile=courses&rank=10&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management-top-up%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management-top-up%2F&auth=i5c%2FtZM9Mrgv%2BE5PbhZz2g&profile=courses&rank=11&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management-with-foundation-year%2F&auth=BVChmtSlhxHqWcbKBrG%2BaA&profile=courses&rank=12&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management%2F&auth=QIaG%2BFgm%2FcYTeF6acYQ6VA&profile=courses&rank=13&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management-with-enterprise-and-innovation%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-business-management-with-enterprise-and-innovation%2F&auth=DQEhn2%2FzPaWPeYDp8x1BGA&profile=courses&rank=14&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-childhood-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-childhood-studies%2F&auth=gp5jWUBgiaCdir9RCQ7hqg&profile=courses&rank=15&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-childhood-youth-and-community-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-childhood-youth-and-community-studies%2F&auth=wZ%2F41bF0kGIPXamhh9cVlw&profile=courses&rank=16&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-choreography-and-dance%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-choreography-and-dance%2F&auth=kRMUbAo5TKrooD369O9xHQ&profile=courses&rank=17&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-classical-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-classical-studies%2F&auth=fCkWGi%2FPGDWya094F9eUiA&profile=courses&rank=18&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-comedy-performance-and-production%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-comedy-performance-and-production%2F&auth=zgKzzxrwJNdXa15HgKT7Uw&profile=courses&rank=19&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-and-professional-writing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-and-professional-writing%2F&auth=2mtwLgHronHKQUlp2MVgjQ&profile=courses&rank=20&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing%2F&auth=bD0WY8%2BP8pqZ9tZU3oafjw&profile=courses&rank=21&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing-and-drama%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing-and-drama%2F&auth=MnlibzhZN62JoSp4TTyjww&profile=courses&rank=22&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing-and-english-literature%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing-and-english-literature%2F&auth=arMDbWopqQ4RKYqvodf1Mw&profile=courses&rank=23&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing-with-english-language-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-creative-writing-with-english-language-studies%2F&auth=6AK7TgctBb18KJqfi2vJNQ&profile=courses&rank=24&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-criminology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-criminology%2F&auth=qf%2FEPrAVJQl4jno2yJEU1g&profile=courses&rank=25&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-criminology-and-sociology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-criminology-and-sociology%2F&auth=RgkQrF9eeBTspWnaaOT9oQ&profile=courses&rank=26&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-dance-performance-young-people%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-dance-performance-young-people%2F&auth=fYWZZ5E1Xu2MnYkurfCVSA&profile=courses&rank=27&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-digital-media-design%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-digital-media-design%2F&auth=TfIgPZeL2jK3efTpQxkB5Q&profile=courses&rank=28&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-digital-media-design-3d-visualisation%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-digital-media-design-3d-visualisation%2F&auth=Dd8i%2F71ScVLK4vML6KQVwA&profile=courses&rank=29&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama%2F&auth=jEknBURHsf1jt9CsmwNARA&profile=courses&rank=30&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama-and-english-literature%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama-and-english-literature%2F&auth=ErY500xx4lUmYgWKfzOZ8A&profile=courses&rank=31&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama-and-performing-arts%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama-and-performing-arts%2F&auth=Gl41v%2BK%2BdwzkFQiJrtkrZQ&profile=courses&rank=32&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama-with-creative-writing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-drama-with-creative-writing%2F&auth=6qvtwjckkNK%2B3J2o%2BMIRrg&profile=courses&rank=33&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-early-childhood%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-early-childhood%2F&auth=%2BdkKcNDHr5GvfmMtq%2FLMgw&profile=courses&rank=34&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-special-and-inclusive-education%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-special-and-inclusive-education%2F&auth=bxPeKeHRGvG04pX%2BnmLskw&profile=courses&rank=35&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies%2F&auth=6lYLGsi1VfOmQ0Y9heZl1Q&profile=courses&rank=36&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-drama%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-drama%2F&auth=7qtrk%2BsvRpaHuYz9YmUdyQ&profile=courses&rank=37&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-english-literature%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-english-literature%2F&auth=CbkkiAZjNRV%2BvQE9rjBrFg&profile=courses&rank=38&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-history%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-history%2F&auth=fAaqA5zsHLRDDJ%2F79kji1w&profile=courses&rank=39&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-mathematics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-studies-and-mathematics%2F&auth=ysmDcgFhhaAYoB7XrGex5Q&profile=courses&rank=40&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-youth-and-community-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-education-youth-and-community-studies%2F&auth=JaAHJInTBdsw33moVmreCQ&profile=courses&rank=41&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-language-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-language-studies%2F&auth=bONMYd59IYX%2B8fNUd%2FzZIA&profile=courses&rank=42&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-language-studies-with-creative-writing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-language-studies-with-creative-writing%2F&auth=NP1tCUo%2B%2BL1z7cNPSfbKKQ&profile=courses&rank=43&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature%2F&auth=bcj%2Bb%2FP%2FOh3uCeGtt9qR7A&profile=courses&rank=44&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-and-film%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-and-film%2F&auth=rQZRDcfkjugnxsEL3Yrtpg&profile=courses&rank=45&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-and-history%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-and-history%2F&auth=9hVoQN%2B4NbCInF4WX%2B8QmQ&profile=courses&rank=46&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-with-creative-writing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-with-creative-writing%2F&auth=XgKkmxZ0lcAB21F3p7zXkg&profile=courses&rank=47&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-with-english-language%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-literature-with-english-language%2F&auth=ASpSDCevNPyJjcVmzaWsIw&profile=courses&rank=48&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-with-american-literature%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-english-with-american-literature%2F&auth=Ym0eBWrC9NLAXqt3Z4SDUA&profile=courses&rank=49&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-event-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-event-management%2F&auth=Dj5ILMIJ6ovB1GM2ucTgyA&profile=courses&rank=50&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-fashion-marketing-and-media%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-fashion-marketing-and-media%2F&auth=RvL1CwO4Bc3kh8uDDznfXA&profile=courses&rank=51&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-and-american-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-and-american-studies%2F&auth=Bj360ow0DNwOxuXKLiQM%2FA&profile=courses&rank=52&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-production%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-production%2F&auth=hUu0WuD4BHXHzv4H9FN4%2BQ&profile=courses&rank=53&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-studies%2F&auth=RrUwqTf1gzRfQMmLAGpmRA&profile=courses&rank=54&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-studies-and-production%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-studies-and-production%2F&auth=wjkX5XIWWmNPfQo6nDz44g&profile=courses&rank=55&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-studies-and-screenwriting%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-film-studies-and-screenwriting%2F&auth=6pNoXAKZPdXgaxo4Ba19ZA&profile=courses&rank=56&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-forensic-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-forensic-studies%2F&auth=nHd2bBs8%2FQLr4EjAw37Sbg&profile=courses&rank=57&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-global-history-and-politics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-global-history-and-politics%2F&auth=JMaYYbY5%2FeTBf2rHGumMWQ&profile=courses&rank=58&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-with-foundation-year%2F&auth=wUymiUj34mE6XnqT3J7k%2Fg&profile=courses&rank=59&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history%2F&auth=0xaCI4ACtolLM6%2F4nqdThg&profile=courses&rank=60&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-and-archaeology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-and-archaeology%2F&auth=nfF5SZ1bTun1jFt599UjBw&profile=courses&rank=61&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-and-the-medieval-world%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-and-the-medieval-world%2F&auth=3VRhXQOslKW3Zw%2FdWj7zRw&profile=courses&rank=62&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-and-the-modern-world%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-history-and-the-modern-world%2F&auth=ehXPgRrXVCz%2FMicGWKP4wQ&profile=courses&rank=63&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-journalism%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-journalism%2F&auth=nduwK0hsRpMILHA%2FmbxvEA&profile=courses&rank=64&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-law-and-business-management-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-law-and-business-management-with-foundation-year%2F&auth=C4oc%2FR9SFKYqbytOo15ZGA&profile=courses&rank=65&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-law-and-business-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-law-and-business-management%2F&auth=U0PSJQhvL%2FMGiIvkjJiuAg&profile=courses&rank=66&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts%2F&auth=flU9TK4lkCtyYbddMhr3FQ&profile=courses&rank=67&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-drama%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-drama%2F&auth=4C4fgmArfuJoDovzD%2B6lSw&profile=courses&rank=68&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-english-literature%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-english-literature%2F&auth=CFQwMpgSYq1vG24LNWxqDw&profile=courses&rank=69&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-history%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-history%2F&auth=Yf09wyXQAdQImhLjei25pQ&profile=courses&rank=70&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-sociology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-liberal-arts-and-sociology%2F&auth=wrB5%2BKmeQeeWcBHObQG1dg&profile=courses&rank=71&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-marketing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-marketing%2F&auth=wggDm%2FniDr33Go6ZA82DYg&profile=courses&rank=72&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-and-communication%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-and-communication%2F&auth=p7pK8KeaslG5QqekWoWMmw&profile=courses&rank=73&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-communication-and-advertising%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-communication-and-advertising%2F&auth=ZE7NG%2F9Css%2BDGCiWBdn33g&profile=courses&rank=74&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-communication-and-journalism%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-communication-and-journalism%2F&auth=UlCEkTCn%2FAIpoqpIs7Qagw&profile=courses&rank=75&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-communication-and-social-media%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-media-communication-and-social-media%2F&auth=k3S3NnYyEB4m7dUTCnyerw&profile=courses&rank=76&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-medieval-history-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-medieval-history-with-foundation-year%2F&auth=3t1RK8lz0%2BOqPujqQelmlw&profile=courses&rank=77&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-modern-history-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-modern-history-with-foundation-year%2F&auth=PqbGti1SRLU1g64CZP7eHg&profile=courses&rank=78&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-music-and-sound-production%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-music-and-sound-production%2F&auth=3kbG%2FNW8kMLKuC3HN8YIRQ&profile=courses&rank=79&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-music-production-and-performance-popular-music%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-music-production-and-performance-popular-music%2F&auth=%2BI19R4Anp4zDolsikOcc0Q&profile=courses&rank=80&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-musical-theatre%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-musical-theatre%2F&auth=iAekMB4P%2FeX9qTtofpfcag&profile=courses&rank=81&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-performing-arts%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-performing-arts%2F&auth=htcSNT9lxOgkPFTHVcpTcQ&profile=courses&rank=82&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-philosophy-politics-and-economics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-philosophy-politics-and-economics%2F&auth=nbP6JQ1BlpjAa%2BXMK%2F3vrg&profile=courses&rank=83&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-philosophy-religion-and-ethics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-philosophy-religion-and-ethics%2F&auth=H9zZGcNGvTb04%2Bz0DMdYAw&profile=courses&rank=84&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-politics-and-global-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-politics-and-global-studies%2F&auth=yNkaYFy5TzoMtU%2FOfHlrFw&profile=courses&rank=85&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-psychology-and-criminology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-psychology-and-criminology%2F&auth=rHxoboDas%2BrNGNmW7GpLPA&profile=courses&rank=86&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-sociology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-sociology%2F&auth=rJ29mS3%2BHU7p14eFd5tT9A&profile=courses&rank=87&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-sports-business-and-marketing%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-sports-business-and-marketing%2F&auth=QZ%2BlkwQY%2FUKm%2B98kcAPbnQ&profile=courses&rank=88&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-sports-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-sports-studies%2F&auth=Fxmc4y%2FeB9ZOGB8OZjWgsg&profile=courses&rank=89&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-theatre-production-arts-and-stage-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-theatre-production-arts-and-stage-management%2F&auth=4xTUoA%2F1p1PDnK5G9T5K8Q&profile=courses&rank=90&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-theology-religion-and-ethics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fba-hons-theology-religion-and-ethics%2F&auth=SMEByBgGb0mCXGSKHUsKow&profile=courses&rank=91&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbed-hons-primary-education-with-recommendation-for-qts-3-years%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbed-hons-primary-education-with-recommendation-for-qts-3-years%2F&auth=tQ2HjUSDRuckDZ5xK2PPsw&profile=courses&rank=92&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbed-hons-primary-education-with-recommendation-for-qts-4-years%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbed-hons-primary-education-with-recommendation-for-qts-4-years%2F&auth=OAiUG50Zzl5iGK0JMQtiOA&profile=courses&rank=93&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-archaeological-practice%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-archaeological-practice%2F&auth=xNrI6uhwvR1f4z%2BgwPHihw&profile=courses&rank=94&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-archaeological-practice-with-professional-placement%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-archaeological-practice-with-professional-placement%2F&auth=UJbyZUKVfRWI08A%2FFOC0NQ&profile=courses&rank=95&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-archaeology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-archaeology%2F&auth=b0PluKy3Fxnk0rH6mzuv2w&profile=courses&rank=96&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-computer-aided-design%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-computer-aided-design%2F&auth=eXGAT0b864Ihr%2BHhV3kEFw&profile=courses&rank=97&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-computer-science%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-computer-science%2F&auth=YNWPIZoiuKSF3mtcN8RweA&profile=courses&rank=98&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-computer-systems-and-networks%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-computer-systems-and-networks%2F&auth=kgMG83jGb26ORvwdWflWxQ&profile=courses&rank=99&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-cyber-security%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-cyber-security%2F&auth=DxKoSroJyTFdTGy3fIsnJg&profile=courses&rank=100&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fapprenticeships%2Fvacancies%2Fbsc-hons-digital-and-technology-solutions-cyber-security-analyst%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fapprenticeships%2Fvacancies%2Fbsc-hons-digital-and-technology-solutions-cyber-security-analyst%2F&auth=P7aKl3IyDl61DplSJLu2tQ&profile=courses&rank=101&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-digital-media-development%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-digital-media-development%2F&auth=Zdkj2AYzZnUPfG5PVnFqSQ&profile=courses&rank=102&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-digital-media-development-3d-environments-game-and-heritage%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-digital-media-development-3d-environments-game-and-heritage%2F&auth=ws17T5f1moH7nlNzSTe9Qw&profile=courses&rank=103&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-economics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-economics%2F&auth=wuZgRZmbO6ZAsDlqMQOeuQ&profile=courses&rank=104&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-economics-and-finance%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-economics-and-finance%2F&auth=LwsmsUxdm%2FyPb%2B833mNUTA&profile=courses&rank=105&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-english-linguistics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-english-linguistics%2F&auth=vVCpXIScbRK1l%2BhZuMxENQ&profile=courses&rank=106&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-english-linguistics-with-forensic-linguistics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-english-linguistics-with-forensic-linguistics%2F&auth=jzZRqrADVNADgp9yzPiXaA&profile=courses&rank=107&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-geography%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-geography%2F&auth=7spGJbWcqN637kWyZoUoVA&profile=courses&rank=108&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-health-community-and-social-care-disability-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-health-community-and-social-care-disability-studies%2F&auth=v4Nl73O4DeS5aBBp3PdB6Q&profile=courses&rank=109&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-health-community-and-social-care-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-health-community-and-social-care-studies%2F&auth=0vekP%2F%2FywF2pWLKEesfa6w&profile=courses&rank=110&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics%2F&auth=4zxkuSb5X6y62HNnLPei0w&profile=courses&rank=111&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-economics%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-economics%2F&auth=0PHVlRYTjY1aBr%2FhL07Apg&profile=courses&rank=112&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-education-studies%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-education-studies%2F&auth=Chiaz4W%2FMHF601qqyBpRiQ&profile=courses&rank=113&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-finance%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-finance%2F&auth=1E44xjLeKAHKTGjGvJB89Q&profile=courses&rank=114&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-mathematics-and-management%2F&auth=1aiNjvGK0av1e9%2FmUNw4cA&profile=courses&rank=115&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-physiotherapy%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-physiotherapy%2F&auth=X3Jd7n8orX9YkMQQvduwNw&profile=courses&rank=116&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychological-science%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychological-science%2F&auth=NIipOg%2Fwj%2BxPa55M%2BTfWVg&profile=courses&rank=117&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychology%2F&auth=wmM7243SnNRSqOdv3ofA7w&profile=courses&rank=118&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychology-and-child-development%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychology-and-child-development%2F&auth=f7H4qrGr7kdpraxpAQLuIA&profile=courses&rank=119&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychology-and-cognition%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-psychology-and-cognition%2F&auth=ERS7VeOitKS8lHksvEj%2BWQ&profile=courses&rank=120&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-social-psychology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-social-psychology%2F&auth=EClt61Wyf2n1ERIcbT1Ycw&profile=courses&rank=121&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-social-work%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-social-work%2F&auth=0NYGYSqdS5y3qeR125wQxA&profile=courses&rank=122&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sport-and-exercise-psychology%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sport-and-exercise-psychology%2F&auth=7aPk2kUP5knOYmzOmfJuBg&profile=courses&rank=123&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sport-and-exercise-science%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sport-and-exercise-science%2F&auth=xzoxKg%2Fk2BLLffTuJBOStw&profile=courses&rank=124&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sport-psychology-and-coaching%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sport-psychology-and-coaching%2F&auth=k8o5c0ykg7xYGQrOGOx%2BbA&profile=courses&rank=125&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sports-coaching%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sports-coaching%2F&auth=awFGvdvYt7hz2HaglxJyXg&profile=courses&rank=126&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sports-coaching-and-performance%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-sports-coaching-and-performance%2F&auth=raEqNvdOewm1MuTi1Zqj3Q&profile=courses&rank=127&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-strength-conditioning-and-fitness%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbsc-hons-strength-conditioning-and-fitness%2F&auth=JQKDByzZnuFTUS44%2BTM%2BYA&profile=courses&rank=128&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fllb-hons-law-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fllb-hons-law-with-foundation-year%2F&auth=hGJwow7eKHavBHvxyaU12w&profile=courses&rank=129&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fllb-hons-law%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fllb-hons-law%2F&auth=uktAejlhModienoCCnUwew&profile=courses&rank=130&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmacc-hons-accounting-and-finance%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmacc-hons-accounting-and-finance%2F&auth=%2F1FqLblo5Ye%2BsQGHye6Idw&profile=courses&rank=131&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmacc-hons-accounting-and-management%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmacc-hons-accounting-and-management%2F&auth=Z9oRk6x0TLiMYoLUzfWu1g&profile=courses&rank=132&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmed-hons-primary-education-with-recommendation-for-qts-4-years%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmed-hons-primary-education-with-recommendation-for-qts-4-years%2F&auth=t%2FaOJh2hDTkAbJC9acd4ew&profile=courses&rank=133&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',
'http://uni-winchester.funnelback.co.uk/s/redirect?collection=winchester-meta&url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmsci-hons-computer-science%2F&index_url=https%3A%2F%2Fwww.winchester.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmsci-hons-computer-science%2F&auth=NZDMol2SmkOVzwWcj2PfLQ&profile=courses&rank=134&query=%21nullquery+%7CcourseType%3A%22%24%2B%2B+undergraduate+%24%2B%2B%22',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of Winchester'
        try:
            location = 'Winchester'
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="bgu-single"]/div/article/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            #department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('//title').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.split()[0]

            #degree_name = re.findall('\((.*)\).*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #degree_name = degree_name.replace(' ','')
            #print(degree_name)
        except:
            degree_name = 'N/A'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//title').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace(' - University of Winchester ','')
            #programme_en = programme_en.split()[1]
            #programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            #programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("\(.*\)(.*)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//body').extract()[0]
            overview_en = remove_tags(overview_en)
            #overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            overview_en = overview_en.replace('  ','')
            overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            overview_en = re.findall('COURSE OVERVIEW(.*)Careers',overview_en)[0]
            overview_en = '<div>' + overview_en + '</div>'

            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = '9,10'

            #print(start_date)
        except:
            start_date = ''


        try:
            #modules_en = response.xpath('//div[4]/div/div/div[1]/div[5]/div/div[2]/p').extract()[0]
            modules_en = response.xpath('//body').extract()[0]
            modules_en = remove_tags(modules_en)
            # overview_en = re.findall('COURSE OVERVIEW(.*)',overview_en)[0]
            modules_en = modules_en.replace('  ', '')
            modules_en = modules_en.replace('\n\n', '\n')
            modules_en = modules_en.replace('\n\n', '')
            modules_en = modules_en.replace('\r\n', '')
            modules_en = modules_en.replace('\n', '')
            modules_en = re.findall('Year 1(.*)in Year 1', modules_en)[0]
            modules_en = '<div>' + modules_en + '</div>'
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//body').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            rntry_requirements_en = re.findall('ENTRY REQUIREMENTS(.*)Visit us',rntry_requirements_en)[0]
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"

            #rntry_requirements_en =rntry_requirements_en.replace('		                        ','')
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = 'N/A'
            #print(rntry_requirements_en)

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            require_chinese_en = ''
        except:
            require_chinese_en = ''
        try:
            ielts_desc = rntry_requirements_en
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            #ielts = '6.5'
            #ielts =remove_tags(ielts)
            ielts = re.findall('(\d\.\d)',ielts_desc)[0]
            #ielts =
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            #ielts_l = '5.5'
            ielts_l = re.findall('(\d\.\d)',ielts_desc)[1]
            #ielts =
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = 0

        try:
            ielts_s = ielts_l

        except:
            ielts_s = ielts_l

        try:
            ielts_r = ielts_l
        except:
            ielts_r = ielts_l

        try:
            ielts_w = ielts_l
        except:
            ielts_w = ielts_l

        try:
            toefl_code = response.xpath('').extract()
            toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = 0

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = 0

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = 0

        try:
            interview_desc_en = response.xpath('//*[@id="entry-requirements-accordion-0"]/div[1]').extract()[0]
            interview_desc_en = remove_tags(interview_desc_en)
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
            interview_desc_en = "<div>" + interview_desc_en + "</div>"
            #print(interview_desc_en)
        except:
            interview_desc_en = 'N/A'
            #print(interview_desc_en)
        try:
            work_experience_desc_en = response.xpath('').extract()
            work_experience_desc_en = remove_tags(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            career_en = response.xpath('//*[@id="section-5"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            #print(career_en)
        except:
            career_en = ''
            #print(career_en)
        try:
            apply_desc_en = '<div>To apply to the University of Winchester for a postgraduate programme you can apply via either method below: UCAS POSTGRADUATE The University of Winchester UCAS institution code is W76 and you can find the relevant course code on the page of the course you are applying for. Once you have submitted your application you will be given a Personal ID number. Please email the following documents (if available at the time of application) to international@winchester.ac.uk  quoting your ID number to complete your application: Evidence of previous academic transcripts and certificates (translated by a verified translator if they are not in English) Evidence of your English Language ability (e.g IELTS – click here for a full list of all accepted tests) An academic reference preferably from your last place of study A copy of your passport and any previous UK visa stamps</div>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>Your previous/ academic qualifications including transcripts Evidence of your English language ability (if applicable) for example, and IELTS certificate A copy of your passport and any previous UK visa stamps (if applicable) A copy of your reference(s) We understand that you may still be waiting to take an English language test or waiting to receive your final exam certificate. Please send us these documents when they are available and/or let us know when we can expect to receive them.</div>'
            #apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        apply_fee = 0


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration = response.xpath('//dl/dd[2]').extract()[0]
            #duration = remove_tags(duration)
            duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '4' in duration:
                duration = '4'
            elif '3' in duration:
                duration = '3'
            elif '2' in duration:
                duration = '6'
            elif '6' in duration:
                duration = '3'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = '1'
            #print(duration)
        except:
            duration = 0
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//body').extract()[0]
            ib = remove_tags(ib)
            ib = ib.replace('\n\n','')
            ib = ib.replace('\n','')
            ib = ib.replace('\r\n','')

            ib = re.findall('International Baccalaureate:(.*points)',ib)[0]

            #print(ib)
        except:
            ib = 'N/A'
            #print(ib)

        try:
            alevel = response.xpath('//body').extract()[0]
            alevel = remove_tags(alevel)
            alevel = alevel.replace('\n\n','')
            alevel = alevel.replace('\r\n','')
            alevel = alevel.replace('\n','')
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            alevel = re.findall('ENTRY REQUIREMENTS(.*Language is required.)',alevel)[0]
            alevel = "<div>" + alevel + "</div>"
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//p[@class = "sub-title"]').extract()[0]
            ucascode = remove_tags(ucascode)
            ucascode = re.findall('UCAS code: (.*)',ucascode)[0]

            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = '12950'
            # tuition_fee = remove_tags(tuition_fee)
            # tuition_fee = tuition_fee.replace('£','')
            # tuition_fee = tuition_fee.replace(',','')
            # tuition_fee = tuition_fee.replace('*','')
            # tuition_fee = tuition_fee.replace(' ','')
            # tuition_fee = tuition_fee.replace('\r\n','')
            # tuition_fee = tuition_fee.replace('\n','')
            #
            # tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)\

        try:
            assessment_en = response.xpath('//body').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\n\n','')
            assessment_en = assessment_en.replace('\r\n','')
            assessment_en = assessment_en.replace('\n','')
            assessment_en = assessment_en.replace('  ',' ')
            assessment_en = re.findall('Assessment(.*)Percentage',assessment_en)[0]
            assessment_en = "<p>" + assessment_en + "</p>"
            #print(assessment_en)

        except:
            assessment_en = 'N/A'
            #print(assessment_en)
        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 1
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = '9'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_l
        item["ielts_r"] = ielts_l
        item["ielts_w"] = ielts_l
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = toefl
        item["toefl_l"] = toefl_l
        item["toefl_s"] = toefl_s
        item["toefl_r"] = toefl_r
        item["toefl_w"] = toefl_w
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 5

        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ib
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        item["assessment_en"] = assessment_en

        #item["apply_pre"] = ''
        yield item


