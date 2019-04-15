import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'University_of_the_West_of_Scotland_U'
    allowed_domains = []
    base_url= 'https://www.uws.ac.uk%s'
    start_urls = []

    C = ['/study/undergraduate/undergraduate-course-search/accounting/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/adult-nursing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/aircraft-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/applied-biomedical-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/applied-bioscience/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/applied-bioscience-zoology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/applied-bioscience-with-forensic-investigation/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/biomedical-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/broadcast-production-tv-radio/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/business-finance/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/business-human-resource-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/business-marketing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/business-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/business-with-english-language/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/chemical-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/chemistry/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/chemistry-with-education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/childhood-studies-2nd-year-entry/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/civil-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/civil-engineering-graduate-apprenticeship/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/commercial-music/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/commercial-sound-production/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/community-education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/computer-animation-arts/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/computer-games-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/computer-games-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/computer-networking/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/computer-aided-design/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/computing-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/criminal-justice-criminal-justice-policing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/cyber-security/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/digital-art-design/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/engineering-design-manufacture/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/engineering-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/english-as-a-second-language/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/environmental-health/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/events-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/filmmaking-screen-writing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/forensic-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/human-resource-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/integrated-health-social-care/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/integrated-health-social-care-with-administration/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/international-business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/international-foundation-programme-business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/it-software-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/journalism-with-the-option-of-sport/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/law/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/law-business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/legal-studies/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/marketing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/maternity-care-assistant/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/mechanical-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/mental-health-nursing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/midwifery/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/music-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/nursing-studies/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/occupational-safety-health/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/performance/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/pharmacy-science-health/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/physics/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/physics-with-education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/physics-with-nuclear-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/professional-health-studies/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/psychology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/social-creative-transformations/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/social-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/social-work/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/society-politics-policy/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/sport-exercise-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/sport-coaching/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/sport-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/sports-coaching-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/technical-theatre-production/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/tourism-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
'/study/undergraduate/undergraduate-course-search/web-mobile-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',]
#     C = ['https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/accounting/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/broadcast-production-tv-radio/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/business-finance/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/business-marketing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/chemistry-with-education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/business-human-resource-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/childhood-studies-2nd-year-entry/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/commercial-music/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/commercial-sound-production/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/adult-nursing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/criminal-justice-criminal-justice-policing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/digital-art-design/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/english-as-a-second-language/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/filmmaking-screen-writing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/events-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/integrated-health-social-care/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/international-business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/journalism-with-the-option-of-sport/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/law/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/law-business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/marketing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/legal-studies/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/integrated-health-social-care-with-administration/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/midwifery/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/performance/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/human-resource-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/physics-with-education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/professional-health-studies/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/mental-health-nursing/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/social-work/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/society-politics-policy/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/psychology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/social-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/social-creative-transformations/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/sport-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/technical-theatre-production/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/sport-coaching/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/tourism-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/business/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/sports-coaching-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/community-education/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/aircraft-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/applied-biomedical-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/applied-bioscience/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/applied-bioscience-with-forensic-investigation/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/biomedical-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/applied-bioscience-zoology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:1,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/business-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/chemistry/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/chemical-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/computer-games-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/civil-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:2,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/computer-games-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/computer-networking/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/computing-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/computer-animation-arts/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/engineering-management/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/cyber-security/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/environmental-health/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/forensic-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:4,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/computer-aided-design/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:3,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/mechanical-engineering/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/occupational-safety-health/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/music-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/pharmacy-science-health/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/physics/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/physics-with-nuclear-technology/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/sport-exercise-science/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:6,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/web-mobile-development/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:7,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',
# 'https://www.uws.ac.uk/study/undergraduate/undergraduate-course-search/nursing-studies/?returnUrl=?%7B%22Keyword%22:%22%22,%22Letter%22:%22%22,%22CourseSubject%22:%7B%22Key%22:%22CourseSubject%22,%22Value%22:%22%22%7D,%22Campus%22:%7B%22Key%22:%22Campus%22,%22Value%22:%5B%22Ayr%22,%22Dumfries%22,%22Hamilton%22,%22Lanarkshire%22,%22London%22,%22Paisley%22,%22New%20College%20Lanarkshire%22%5D%7D,%22StudyMode%22:%7B%22Key%22:%22StudyMode%22,%22Value%22:%5B%5D%7D,%22PageNum%22:5,%22PageSize%22:12,%22SortBy%22:%22Az%22,%22CourseType%22:2771%7D',]
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'University of the West of Scotland'
        try:
            location = response.xpath('//*[@id="course"]/section[1]/div/div/div/div[1]/div/div/div[4]/p[2]').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="course"]/section[1]/div/div/div/div[1]/div/div/div[3]/p[2]').extract()[0]
            department = remove_tags(department)
            department = department.replace('\n\n', '\n')
            department = department.replace('\r\n', '')
            department = department.replace('	', '')
            department = department.replace('  ', '')
            department = department.replace('\n', '')
            department = department.replace('Our Staff', '')
            #print(department)
        except:
            department = ''
            #print(department)


        try:
            degree_name = response.xpath('//*[@id="course"]/section[1]/div/div/div/div[1]/div/div/div[1]/p[2]').extract()[0]
            degree_name = remove_tags(degree_name)
            #degree_name = degree_name.split()[-1]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
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
            programme_en = response.xpath('//*[@id="course"]/section[1]/div/div/h1/span').extract()[0]
            programme_en = remove_tags(programme_en)
            #programme_en = re.findall(' (.*)',programme_en)[0]
            #programme_en = programme_en.replace(degree_name,'')
            programme_en = programme_en.replace('  ','')
            #programme_en = programme_en.replace('\n', '')
            #programme_en = re.findall(('                    '),'')[0]
            #programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="overview"]/div/div/div[2]').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            overview_en = '<div>' + overview_en + '</div>'
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = '9'

            #print(start_date)
        except:
            start_date = ''


        try:
            modules_en = response.xpath('//*[@id="course-details"]/div/div/div/ul[1]|//*[@id="course-details"]/div/section[1]/div').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
            modules_en = modules_en.replace('\n','')
            modules_en = "<div><p>" + modules_en + "</p></div>"
            #print(modules_en)
        except:
            modules_en = 'N/A'
            print(modules_en)



        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="entry-requirements"]/div/div/div').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = "<div>"+rntry_requirements_en+"</div>"
            rntry_requirements_en = rntry_requirements_en.replace('\n\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\r\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('\n', '')
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
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
            ielts_desc = '<p>For applicants whose first language is not English, the University sets a minimum English Language proficiency level. The qualifications below must have been gained within two years of the start of your course. General English language requirements at UWS: International English Language Testing System (IELTS) Academic module (not General Training) overall score 6.0 no sub-test less than 5.5</p>'
            #ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = '6.0'
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            #ielts = re.findall('(\d\.\d)',ielts_desc)[0]
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            ielts_l = '5.5'
            #ielts = re.findall('(\d\.\d)', ielts)[1]
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
            toefl_desc = 'TOEFL IBT*: 78; no sub-test less than: Reading: 17; Listening: 17; Speaking: 17; Writing: 17 * Please note that TOEFL is still acceptable for admission to this programme for both home/EU and international students. For international students, the Home Office has confirmed that the University can choose to use TOEFL to make its own assessment of English language ability for visa applications to degree level courses. We therefore still accept TOEFL tests taken in the last two years for admission to this programme.  '
            #toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = 0

        try:
            toefl = '78'
            #toefl = remove_tags(toefl)

        except:
            toefl = 0

        try:
            toefl_l = 17

        except:
            toefl_l = 0

        try:
            toefl_s = toefl_l
            #toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = 0

        try:
            toefl_r =toefl_l
            #toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = 0

        try:
            toefl_w = toefl_l
            #toefl_w = remove_tags(toefl_w)
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
            career_en = response.xpath('//*[@id="careers"]|//*[@id="career-prospects"]').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ',' ')
            career_en = career_en.replace('\n','')
            career_en = "<div><span>" + career_en + "</span></div>"
            career_en = career_en.replace('                            ','')
            print(career_en)
        except:
            career_en = 'N/A'
            print(career_en)
        try:
            apply_desc_en = '<p>Application for our undergraduate and postgraduate taught courses opens in August each year and runs until course start dates. If you are applying from overseas for undergraduate or postgraduate taught courses, the latest we can process your application is 6 weeks before the course start date. Applications for research degrees may be made at any time.</p>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>Degree certificate(s) in English Academic transcript(s) in English English language proficiency test certificates A signed academic reference on headed paper CV Proof of funding (if required) Passport Visa/CAS statement (if held)</p>'
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
            duration = response.xpath('//*[@id="course"]/section[1]/div/div/div/div[1]/div/div/div[2]/p[2]').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '3' in duration:
                duration = '3'
            elif '4' in duration:
                duration = '4'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '2'
            elif '5' in duration:
                duration = '5'
            elif '6' in duration:
                duration = '6'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = '3'
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
            ib = response.xpath('//*[@id="entry-requirements"]/div/section[1]/div/ul/li[4]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="entry-requirements"]/div/section[1]/div/ul/li[2]').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="course-details-ucas"]/p[2]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="fees-funding"]/div/div[2]/div/div').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('£','')
            tuition_fee = tuition_fee.replace(',','')
            tuition_fee = tuition_fee.replace('*','')
            tuition_fee = tuition_fee.replace(' ','')
            tuition_fee = tuition_fee.replace('\r\n','')
            tuition_fee = tuition_fee.replace('\n','')

            tuition_fee = re.findall('(\d\d\d\d\d)',tuition_fee)[0]

            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0
            #print(tuition_fee)

        try:
            assessment_en = response.xpath('//*[@id="course-details"]/div/section[6]/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            assessment_en = assessment_en.replace('			','')
            assessment_en = assessment_en.replace('		','')
            assessment_en = "<div>"+assessment_en+'</div>'
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