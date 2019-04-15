import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'York_St_John_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Faccounting--business-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Faccounting--business-management-ba-hons%2F&auth=O5QstWVTMCf8EYFjk2j2MQ&profile=_default&rank=1&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Faccounting--finance-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Faccounting--finance-ba-hons%2F&auth=ASIRm2av15VaujnBbNHuyA&profile=_default&rank=2&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Famerican-studies--film-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Famerican-studies--film-studies-ba-hons%2F&auth=rSr5DlAJgioUfFkZLe4GQg&profile=_default&rank=3&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Famerican-studies--history-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Famerican-studies--history-ba-hons%2F&auth=7sG%2B3G7%2B82aPXNOavvXVfA&profile=_default&rank=4&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Famerican-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Famerican-studies-ba-hons%2F&auth=f2lEe0ur8u42J5ne7ySBDA&profile=_default&rank=5&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fanimation-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fanimation-ba-hons%2F&auth=buSXn3wykih7lD%2FuQXAVHQ&profile=_default&rank=6&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiochemistry-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiochemistry-bsc-hons%2F&auth=ccYnTgxZlbuLA%2BfkqY8qCQ&profile=_default&rank=7&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiology-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiology-bsc-hons%2F&auth=1HulUTZD%2F69dkx28t8ewtw&profile=_default&rank=8&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiomedical-science-bsc-hons-with-placement%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiomedical-science-bsc-hons-with-placement%2F&auth=o1O7j0rnnJiBz3Cc%2FdnX1Q&profile=_default&rank=9&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiomedical-science-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fbiomedical-science-bsc-hons%2F&auth=kqlIkUG9uN0ICEIGjB3h7A&profile=_default&rank=10&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fbsl-and-deaf-studies%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fbsl-and-deaf-studies%2F&auth=J5jm5a048nOwObrMsUJMaQ&profile=_default&rank=11&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-and-economics-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-and-economics-ba-hons%2F&auth=ZTCniz3bRbwl5X0FttNgeA&profile=_default&rank=12&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-degrees-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-degrees-with-foundation-year%2F&auth=CcJhxyNBuUXEO224tD6emA&profile=_default&rank=13&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-information-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-information-management-ba-hons%2F&auth=%2F9FJBf1gfa59L8w3KOuPtQ&profile=_default&rank=14&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-information-technology-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-information-technology-ba-hons%2F&auth=waRMwt7FjF8o9%2FOjq%2B9Rjw&profile=_default&rank=15&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--finance-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--finance-ba-hons%2F&auth=F6Qi7JmNDXXrO6cvbuYJTg&profile=_default&rank=16&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--french-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--french-ba-hons%2F&auth=qboaS5WXkOS5q11t7E5vIQ&profile=_default&rank=17&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--hr-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--hr-management-ba-hons%2F&auth=nArjYqAELI1RIJ7qKVlsyg&profile=_default&rank=18&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--japanese-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--japanese-ba-hons%2F&auth=WMtySdNDTHsBrTVqA1AURA&profile=_default&rank=19&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--spanish-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--spanish-ba-hons%2F&auth=x%2BRH4XwkKfAaFMXJ88B9Tg&profile=_default&rank=20&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--bsl-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management--bsl-ba-hons%2F&auth=d%2FEja4M6wyPFlON7EfII%2Bg&profile=_default&rank=21&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-management-ba-hons%2F&auth=zBaGjADviPTLdpZ3W8kq1w&profile=_default&rank=22&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fbusiness-studies-ba-hons%2F&auth=EeFYk1aMNvhwcghxFzOSKQ&profile=_default&rank=23&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-with-edu-studies%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-with-edu-studies%2F&auth=acHjgrdDCHM5ugVSHYlbKA&profile=_default&rank=24&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-ba-hons%2F&auth=S25d3lkcfqXL%2BDnyGOsGSQ&profile=_default&rank=25&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-with-bsl%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-with-bsl%2F&auth=7B%2Fww9%2B%2BLkzDPNAAd0RVaw&profile=_default&rank=26&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-w-se-need--incl%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fchildren-young-people--families-w-se-need--incl%2F&auth=qxnr3fCNM0b2BiC5174Vqg&profile=_default&rank=27&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fcomputer-science-with-placement-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fcomputer-science-with-placement-bsc-hons%2F&auth=mJtUKblEmGAA2mDQSX9Gog&profile=_default&rank=28&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fcomputer-science-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fcomputer-science-bsc-hons%2F&auth=OmuQ3P6Wlh0u8UghUFtr5Q&profile=_default&rank=29&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fpsychology--counselling%2Fcounselling-coaching--mentoring-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fpsychology--counselling%2Fcounselling-coaching--mentoring-ba-hons%2F&auth=i9enRAXiUdhQvRbOvbYECA&profile=_default&rank=30&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing--english-language-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing--english-language-ba-hons%2F&auth=p8citXq8xr%2BkbjZ3cgyEYA&profile=_default&rank=31&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing--english-literature-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing--english-literature-ba-hons%2F&auth=pvuoUOAp7fvw7pYABOTezA&profile=_default&rank=32&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing--media-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing--media-ba-hons%2F&auth=Z0ZSLG2BbIpME4K2HKeIiw&profile=_default&rank=33&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fcreative-writing-ba-hons%2F&auth=mGlmNNurtfA98V8cB9X9Qw&profile=_default&rank=34&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fcriminology-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fcriminology-ba-hons%2F&auth=1EXzfFHvJ7ZB%2F3kZzSecLw&profile=_default&rank=35&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fcriminology-with-policing-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fcriminology-with-policing-studies-ba-hons%2F&auth=FL42QwXLqCFvTb4HW0Oaig&profile=_default&rank=36&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fdata-science%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fdata-science%2F&auth=VVSlo71ZqdVLqiu1q9C0hQ&profile=_default&rank=37&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdigital-music-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdigital-music-ba-hons%2F&auth=k6S6P6R1HpqGu3I2u6AHBQ&profile=_default&rank=38&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama--comedy-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama--comedy-ba-hons%2F&auth=2wx7o50V6OkOqu8nxzEgmw&profile=_default&rank=39&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama--dance-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama--dance-ba-hons%2F&auth=%2B5O2gv7nbFEae%2BN066yOlg&profile=_default&rank=40&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama--theatre-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama--theatre-ba-hons%2F&auth=1SgqIv6Ik7CxXiYDEVzzog&profile=_default&rank=41&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama-education--community-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fdrama-education--community-ba-hons%2F&auth=eN5riFyo4CVWz5k1LpjjXw&profile=_default&rank=42&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fearly-childhood-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fearly-childhood-studies-ba-hons%2F&auth=jLMJOHdJLJm7PAHIuH%2BgTw&profile=_default&rank=43&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Feconomics--finance-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Feconomics--finance-bsc-hons%2F&auth=xrqGDucELs2ookNxZDdnmg&profile=_default&rank=44&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-degrees-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-degrees-with-foundation-year%2F&auth=yhrDgFk%2Bp2ZxBqKNmL555Q&profile=_default&rank=45&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-studies--sociology-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-studies--sociology-ba-hons%2F&auth=ZaMMji48d1LRM197gLbxEQ&profile=_default&rank=46&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-studies-ba-hons%2F&auth=gjwZwNqw37W3l1onIVLMEA&profile=_default&rank=47&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-studies-w-special-education-need--incl%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Feducation-studies-w-special-education-need--incl%2F&auth=bNQ01HSYNdVgZ7edLq02aw&profile=_default&rank=48&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--bsl-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--bsl-ba-hons%2F&auth=plcVjzpWT2NokV5gj1DE3w&profile=_default&rank=49&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--education-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--education-studies-ba-hons%2F&auth=lcFbVNI2InT2P7f%2F6x2m4g&profile=_default&rank=50&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-language--english-literature-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-language--english-literature-ba-hons%2F&auth=gUxGQU%2FNrL5IJjg%2BJpsVLw&profile=_default&rank=51&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--french-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--french-ba-hons%2F&auth=lT7riy8WFBp7X5j1wKbGpw&profile=_default&rank=52&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--japanese-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--japanese-ba-hons%2F&auth=dG%2F5I25bXN6ar4YcV5I5YA&profile=_default&rank=53&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--linguistics-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--linguistics-ba-hons%2F&auth=HGa4u78RYXdr0jBcDFv5Tg&profile=_default&rank=54&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--spanish-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Fenglish-language--spanish-ba-hons%2F&auth=qF7UFOiK0kA5kzblqXdgZg&profile=_default&rank=55&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--bsl-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--bsl-ba-hons%2F&auth=IDWnZOH39BBgEP3OGThtcg&profile=_default&rank=56&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--education-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--education-studies-ba-hons%2F&auth=kMJB1u%2B6J8YzHyj73F18oA&profile=_default&rank=57&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--film-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--film-studies-ba-hons%2F&auth=XtMqR5g8X5ttJIAdqDRaxw&profile=_default&rank=58&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--french-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--french-ba-hons%2F&auth=nhBXEXWVvhww6dLETjR1GA&profile=_default&rank=59&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--history-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--history-ba-hons%2F&auth=WghQa8OS1Z8dY82oG%2F41sg&profile=_default&rank=60&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--japanese-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--japanese-ba-hons%2F&auth=05m%2FQxGe0TIWnRaq%2FyPakw&profile=_default&rank=61&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--media-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--media-ba-hons%2F&auth=OkquFY5UPyQ5z4fryvIZGA&profile=_default&rank=62&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--spanish-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature--spanish-ba-hons%2F&auth=nb9gLTNr49oyZFFUJ5P40Q&profile=_default&rank=63&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenglish-literature-ba-hons%2F&auth=7n7Uvzf5Z9ZSBo49WyO%2B4Q&profile=_default&rank=64&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenvironmental-geography-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fenvironmental-geography-bsc-hons%2F&auth=dkwr8Vbpi%2FgiPEiNgDKKTw&profile=_default&rank=65&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fevents-and-int-hospitality-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fevents-and-int-hospitality-management-ba-hons%2F&auth=Nm2iGpnin5yb6ec%2FT3U80A&profile=_default&rank=66&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fevents-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fevents-management-ba-hons%2F&auth=%2FtoH7Do%2BJJ61VOYSj0wzhQ&profile=_default&rank=67&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Ffilm-studies--media-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Ffilm-studies--media-ba-hons%2F&auth=eudxYoyCBfLGDVVvamavZA&profile=_default&rank=68&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Ffilm-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Ffilm-studies-ba-hons%2F&auth=7DukMEno%2BMd9VPkfMcisQQ&profile=_default&rank=69&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Ffine-art-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Ffine-art-ba-hons%2F&auth=%2BcgpYfXhUtqk7woPZF%2FfRw&profile=_default&rank=70&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Ffurniture-design-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Ffurniture-design-ba-hons%2F&auth=INTHZLglPu5DyxaSlI8K6w&profile=_default&rank=71&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fgames-design-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fgames-design-ba-hons%2F&auth=OQsVVt0u3T%2Bq8vM5H58iEg&profile=_default&rank=72&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fgames-development-with-placement-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fgames-development-with-placement-bsc-hons%2F&auth=J0TJeuviRc9vvdYmyoVFmQ&profile=_default&rank=73&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fgames-development-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fgames-development-bsc-hons%2F&auth=%2BG%2BMIQ6CVzrwt3FDwKhStQ&profile=_default&rank=74&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fgeography-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fgeography-bsc-hons%2F&auth=9mTHPX11hfLqpdYXpGOArA&profile=_default&rank=75&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fgraphic-design-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fgraphic-design-ba-hons%2F&auth=6wuUExJotEdAwXmlateNtg&profile=_default&rank=76&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhistory-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhistory-ba-hons%2F&auth=NfvMYM9ZEl7BN5IWBF3ANw&profile=_default&rank=77&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-ba-hons%2F&auth=tld6A14n5pz10jXoVXiFoQ&profile=_default&rank=78&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-with-american-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-with-american-studies-ba-hons%2F&auth=JO%2BotV6BcoMaJP62XzNbkw&profile=_default&rank=79&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-with-history-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-with-history-ba-hons%2F&auth=NgMUZSAi5FkvsjffH4uElg&profile=_default&rank=80&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-with-media-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhuman-geography-with-media-studies-ba-hons%2F&auth=p5yNokYuW8LrGBD0hpIozw&profile=_default&rank=81&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhumanities-with-foundation-year-%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fhumanities-with-foundation-year-%2F&auth=EC%2BPfvx%2FCLNB706vT49Atw&profile=_default&rank=82&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fillustration-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fillustration-ba-hons%2F&auth=tQzi6K2Bf5x8TTysw0d2kw&profile=_default&rank=83&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Findependent-music-production-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Findependent-music-production-ba-hons%2F&auth=MDpA0zbNkvcT6t1MiBuo%2BA&profile=_default&rank=84&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Finterior-design-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Finterior-design-ba-hons%2F&auth=LfK%2Fc76m%2BaUi3Hsv%2FN3cWw&profile=_default&rank=85&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Finternational-business-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Finternational-business-management-ba-hons%2F&auth=WiF1KudCp3Ws9zTNwYfomg&profile=_default&rank=86&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Finternational-hospitality-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Finternational-hospitality-management-ba-hons%2F&auth=xiA4aQC3eqJAaMMJFPTueA&profile=_default&rank=87&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fint-tourism-and-hospitality-mgmt-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fint-tourism-and-hospitality-mgmt-ba-hons%2F&auth=LqGfC0qvP1Pwm2W9kkXBNQ&profile=_default&rank=88&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flang--ling-degrees-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flang--ling-degrees-with-foundation-year%2F&auth=Y2eyl79IsfjOpVSLIgqQvg&profile=_default&rank=89&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french--spanish-ba-hons-%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french--spanish-ba-hons-%2F&auth=%2BbtfEPfaywQ4DbOurQZOPg&profile=_default&rank=90&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french-with-bsl-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french-with-bsl-ba-hons%2F&auth=kSGYnTxwHEnhRUuu8QMyLw&profile=_default&rank=91&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french-with-japanese-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french-with-japanese-ba-hons%2F&auth=Dbn7v5UIgB6uwgAk6zgY0Q&profile=_default&rank=92&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french-with-spanish-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-french-with-spanish-ba-hons%2F&auth=69u2pauJdEZBRl9LMgxRZQ&profile=_default&rank=93&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-spanish-with-bsl-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-spanish-with-bsl-ba-hons%2F&auth=QHTWl0NXyk0RiBYb5Tqcnw&profile=_default&rank=94&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-spanish-with-japanese-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flanguages-spanish-with-japanese-ba-hons%2F&auth=6RbG02vJvl3Nc92lQpFzMQ&profile=_default&rank=95&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Flaw-llb-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Flaw-llb-hons%2F&auth=09o2g2vki8jrquk0c0GM9g&profile=_default&rank=96&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flinguistics--tesol-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Flinguistics--tesol-ba-hons%2F&auth=cjxpQ1kd9XJxb7%2BE5v%2F%2FjQ&profile=_default&rank=97&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fmarketing-and-events-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fmarketing-and-events-management-ba-hons%2F&auth=V0pzzceNSATALGcyJvPgBA&profile=_default&rank=98&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fmarketing--int-hospitality-mgmt-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fmarketing--int-hospitality-mgmt-ba-hons%2F&auth=jVN4AwqgKACj00Wj2ipecA&profile=_default&rank=99&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fmarketing-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fmarketing-management-ba-hons%2F&auth=nemipe9q7d6XfDWHYc5bbg&profile=_default&rank=100&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fmathematics-%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fmathematics-%2F&auth=TnM6e0JB%2BZqPLKujFEIoPQ&profile=_default&rank=101&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fmedia-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fmedia-ba-hons%2F&auth=NGTvgr9GUMppBy5HA44YnA&profile=_default&rank=102&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-and-production-degrees-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-and-production-degrees-with-foundation-year%2F&auth=3zK49%2FbMld67wqBLpsqX4w&profile=_default&rank=103&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-production-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-production-ba-hons%2F&auth=2vuL6zMeUqmnQ7ej4BWSLg&profile=_default&rank=104&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-production-film--television-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-production-film--television-ba-hons%2F&auth=9zhngAOLMzmMLcESGppr4g&profile=_default&rank=105&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-production-journalism-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fmedia--production%2Fmedia-production-journalism-ba-hons%2F&auth=SnxEeihicIbEu4aXZrRV9g&profile=_default&rank=106&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-ba-hons%2F&auth=Vb5kkz7j0qKC629Ooy1HzA&profile=_default&rank=107&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-composition-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-composition-ba-hons%2F&auth=oE0Pvf8XAgSLWIGqpMv%2BPg&profile=_default&rank=108&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-production-and-creative-business-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-production-and-creative-business-ba-hons%2F&auth=KKaOWCC%2BVrwPygJq71Z69w&profile=_default&rank=109&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-production-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-production-ba-hons%2F&auth=INGlx%2BCsBnOTWyfONUjL6Q&profile=_default&rank=110&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-education--community-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-education--community-ba-hons%2F&auth=V70%2F%2BubmrZwEDMQzV5T4RQ&profile=_default&rank=111&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-performance-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fperformance%2Fmusic-performance-ba-hons%2F&auth=I7L3SBBkN74mPCuAXSFGcQ&profile=_default&rank=112&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fnutrition-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fnutrition-bsc-hons%2F&auth=g7C7YsdnChjRopXsfPJZ1Q&profile=_default&rank=113&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Foccupational-therapy-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Foccupational-therapy-bsc-hons%2F&auth=nwOp28mN5OU95APJSJBauQ&profile=_default&rank=114&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fphotography-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fphotography-ba-hons%2F&auth=2OYhWVEYdXl9e%2FQ37LxT%2FQ&profile=_default&rank=115&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fphysical-education--sports-coaching-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fphysical-education--sports-coaching-ba-hons%2F&auth=GMuNIbuxTgsmGBEmSnctww&profile=_default&rank=116&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fphysiotherapy-bhsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhealth-sciences%2Fphysiotherapy-bhsc-hons%2F&auth=nbBzLY2gM%2FUIHvtpftXrwQ&profile=_default&rank=117&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fpolice-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fpolice-studies-ba-hons%2F&auth=YB78c4F%2BL7QugLKqZdvscQ&profile=_default&rank=118&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics--history-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics--history-ba-hons%2F&auth=%2BIhyrsQWY3C0XHpXel3uaw&profile=_default&rank=119&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics--war-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics--war-studies-ba-hons%2F&auth=1ETRO3TaTWfrRstXM4AMhg&profile=_default&rank=120&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics-ba-hons%2F&auth=2QqFADDbjfoePaimW3FonA&profile=_default&rank=121&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics-philosophy-and-ethics-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fpolitics-philosophy-and-ethics-ba-hons%2F&auth=jxqF0FyjzXAHOhAWohkcmw&profile=_default&rank=122&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fprimary-education-3---7-years-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fprimary-education-3---7-years-ba-hons%2F&auth=fexdbesePHHzhjDwIGsMdw&profile=_default&rank=123&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fprimary-education-5---11-years-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fprimary-education-5---11-years-ba-hons%2F&auth=NEHFFGWfxTkdJqgLRo9rrw&profile=_default&rank=124&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fproduct-design-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fart--design%2Fproduct-design-ba-hons%2F&auth=K8kFZcwV9bHfCbn1sDZPtg&profile=_default&rank=125&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fpsychology--counselling%2Fpsychology-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fpsychology--counselling%2Fpsychology-bsc-hons%2F&auth=l7%2BNYT9RtS98YRt6PsZOXw&profile=_default&rank=126&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fpsychology--counselling%2Fpsychology-with-counselling-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fpsychology--counselling%2Fpsychology-with-counselling-bsc-hons%2F&auth=CbLaeyS%2BUYB%2Fd7GEC0v31A&profile=_default&rank=127&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Freligion--philosophy%2Freligion--philosophy-degrees-with-foundation-year%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Freligion--philosophy%2Freligion--philosophy-degrees-with-foundation-year%2F&auth=ziBi9oVDLql2xHy%2FbO6b%2Bg&profile=_default&rank=128&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Freligion--philosophy%2Freligion-philosophy--ethics-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Freligion--philosophy%2Freligion-philosophy--ethics-ba-hons%2F&auth=bfVwtISMB1yDrK4ocyuv8Q&profile=_default&rank=129&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsocial-sciences-degrees-with-fy%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsocial-sciences-degrees-with-fy%2F&auth=Ha4P5DqvOngKDIMi33fcJQ&profile=_default&rank=130&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsociology-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsociology-ba-hons%2F&auth=1C8eldkAdb%2FfmYnf3qJylg&profile=_default&rank=131&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsociology-with-criminology-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsociology-with-criminology-ba-hons%2F&auth=r8gQtlY7IKxCErsCVChLGg&profile=_default&rank=132&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsociology-with-police-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsocial-sciences%2Fsociology-with-police-studies-ba-hons%2F&auth=D0Tc%2Bs6EN%2FXQKPeukJC2Ng&profile=_default&rank=133&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fsoftware-engineering-with-placement-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fsoftware-engineering-with-placement-bsc-hons%2F&auth=rKY%2BIrtqtl9g4bEZIxE8Ew&profile=_default&rank=134&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fsoftware-engineering-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fcomputing%2Fsoftware-engineering-bsc-hons%2F&auth=cDuXcRnQPClnFEFz3N%2BBkQ&profile=_default&rank=135&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fsport--exercise-science-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fsport--exercise-science-bsc-hons%2F&auth=vUbEY4VstHp1i3nqFKyO7A&profile=_default&rank=136&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fsport--exercise-therapy-bsc-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fsport--exercise-therapy-bsc-hons%2F&auth=1rbJUF1ZdY9cNfhV%2FBvN7Q&profile=_default&rank=137&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fsport-development--business-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fsport%2Fsport-development--business-management-ba-hons%2F&auth=95KLeySvPbgRdHcEJSDCUg&profile=_default&rank=138&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fsports-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fsports-management-ba-hons%2F&auth=H1Hwv5%2FQ5j%2B5otspY%2Fl%2Bfg&profile=_default&rank=139&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fsports-marketing-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Fsports-marketing-management-ba-hons%2F&auth=1cNxKDwMKFanx%2BiJmFx8xQ&profile=_default&rank=140&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Ftesol--french-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Ftesol--french-ba-hons%2F&auth=arJAr95SzdIK%2Feo%2Bd59gOA&profile=_default&rank=141&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Ftesol--japanese-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Ftesol--japanese-ba-hons%2F&auth=Dljgm9%2B5RtOxNj%2F%2FGZFVqA&profile=_default&rank=142&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Ftesol--spanish-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Flanguages--linguistics%2Ftesol--spanish-ba-hons%2F&auth=Qnq%2FkIBckiV65oj%2Fkpw8Dg&profile=_default&rank=143&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Freligion--philosophy%2Ftheology--religious-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Freligion--philosophy%2Ftheology--religious-studies-ba-hons%2F&auth=RnbZFaugjEm0LEq3J8Qeyg&profile=_default&rank=144&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism--events-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism--events-management-ba-hons%2F&auth=M6sTto%2BtEk9gttGMtJusMw&profile=_default&rank=145&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism-management--marketing-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism-management--marketing-ba-hons%2F&auth=rnYcO27SK6aZJZf6n2OgGQ&profile=_default&rank=146&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism-management--spanish-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism-management--spanish-ba-hons%2F&auth=T9VmXN7suerTtC%2FubukOuA&profile=_default&rank=147&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism-management-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fbusiness%2Ftourism-management-ba-hons%2F&auth=4kS7GcwmbzN9gVzKoYlr1Q&profile=_default&rank=148&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fwar-studies-ba-hons%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Fhumanities%2Fwar-studies-ba-hons%2F&auth=t0ocWbqtUyU7WXtUf9JL3w&profile=_default&rank=149&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fyouth-work-and-community-development%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fundergraduate%2Fcourses%2Feducation%2Fyouth-work-and-community-development%2F&auth=Wo4qCwTrcWVZgNY2y4kphQ&profile=_default&rank=150&query=%21showall+%7CcourseStartDate%3A%22%24%2B%2B+September+2019+%24%2B%2B%22+%7CcourseLevel%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'York St John University'
        try:
            location = response.xpath('//*[@id="section-overview"]/div/div[2]/dl[2]/dd').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('//*[@id="section-overview"]/div/div[2]/dl[7]/dt/a').extract()[0]
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
            degree_name = response.xpath('/html/body/main/article/div[1]/header/div/h1/em').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = degree_name.split()[0]

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
            programme_en = response.xpath('//html/body/main/article/div[1]/header/div/h1/text()').extract()[0]
            programme_en = remove_tags(programme_en)
            #programme_en = re.findall(' (.*)',programme_en)[0]
            programme_en = programme_en.replace(degree_name,'')
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
            overview_en = response.xpath('//*[@id="section-overview"]/div/div[1]/p').extract()[0]
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
            modules_en = response.xpath('//*[@id="level-1"]/div').extract()[0]
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
            rntry_requirements_en = response.xpath('//*[@id="reqs-1"]/div').extract()[0]
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
            ielts_desc = response.xpath('//*[@id="reqs-2"]/div/p').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            ielts = response.xpath('//*[@id="reqs-2"]/div/p').extract()[0]
            ielts =remove_tags(ielts)
            ielts = re.findall('IELTS(.*)',ielts)[0]
            ielts = re.findall('(\d\.\d)',ielts)[0]
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            ielts_l = re.findall('IELTS(.*)',ielts)[1]
            ielts = re.findall('(\d\.\d)', ielts)[1]
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
            career_en = response.xpath('//*[@id="collapseCareerOpportunities"]/div').extract()[0]
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
            apply_desc_en = '<div>You can apply directly to the course via our ‘Apply Now’ links. Please select the variant of the course that you intend to undertake (e.g. full-time or part-time) as the link will take you to a customised form for the specific course. You will need to create a login and password and complete the online form. Please contact two referees in advance of submitting your application as an automated request will go out as soon as you submit, and your application will not be reviewed until both references are in place. Applications for September 2017 entry must be submitted and completed by 6 October 2017.</div>'
            #apply_desc_en = remove_tags(apply_desc_en)
            #apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = ''
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
            duration =  response.xpath('//*[@id="section-overview"]/div/div[2]/dl[4]/dd').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '6' in duration:
                duration = '6'
            elif '5' in duration:
                duration = '5'
            elif '4' in duration:
                duration = '4'
            elif '3' in duration:
                duration = '3'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = '0'
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
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="reqs-1"]/div').extract()[0]
            alevel = remove_tags(alevel)
            alevel = alevel.replace('\r\n', '')
            alevel = alevel.replace('  ', '')
            alevel = alevel.replace('\n', '')
            alevel = alevel.replace('			','')
            alevel = alevel.replace('		','')
            alevel = "<div>"+alevel+'</div>'
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="section-overview"]/div/div[2]/dl[1]/dd').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('///*[@id="section-overview"]/div/div[2]').extract()[0]
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
            assessment_en =  ''
            # assessment_en = remove_tags(assessment_en)
            # assessment_en = assessment_en.replace('\r\n', '')
            # assessment_en = assessment_en.replace('  ', '')
            # assessment_en = assessment_en.replace('\n', '')
            # assessment_en = assessment_en.replace('			','')
            # assessment_en = assessment_en.replace('		','')
            # assessment_en = "<div>"+assessment_en+'</div>'
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
        item["batch_number"] = 2
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
        #yield item


