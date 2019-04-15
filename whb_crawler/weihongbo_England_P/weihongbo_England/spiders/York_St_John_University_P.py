import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'York_St_John_University_P'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2F3d-design--technologies-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2F3d-design--technologies-msc%2F&auth=VetEWzd76PHJaHSI91Altg&profile=_default&rank=1&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Famerican-studies-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Famerican-studies-ma%2F&auth=jAQFJ0UM5fQVKUvxpyY7aA&profile=_default&rank=2&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Fapplied-linguistics-tesol-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Fapplied-linguistics-tesol-ma%2F&auth=rrkHTwa6hyoO1jsobL414g&profile=_default&rank=3&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Fapplied-linguistics-translation-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Fapplied-linguistics-translation-ma%2F&auth=kJlNKxpfSbVazHqXav0IoA&profile=_default&rank=4&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fapplied-theatre-ma-%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fapplied-theatre-ma-%2F&auth=QkY6OEF8bFJyeQc5A79JAA&profile=_default&rank=5&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Fclinical-linguistics-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Fclinical-linguistics-msc%2F&auth=zzhw0PQMaTXS6806Q3Y%2BLQ&profile=_default&rank=6&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcommunity-music-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcommunity-music-ma%2F&auth=4bJZUtwfVlfzI7JXBvpuXg&profile=_default&rank=7&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcontemporary-literature-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcontemporary-literature-ma%2F&auth=Sbmz9%2Bx5Lx8qevNzmDWXsA&profile=_default&rank=8&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Ftheology--religion-studies%2Fcontemporary-religion-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Ftheology--religion-studies%2Fcontemporary-religion-ma%2F&auth=KVKNPvHHtpwBFTktTcTfdQ&profile=_default&rank=9&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fcounselling%2Fcounselling-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fcounselling%2Fcounselling-ma%2F&auth=t6mdGhjoH2FW8IZdx%2BZU2A&profile=_default&rank=10&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcreative-writing-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcreative-writing-ma%2F&auth=rDvDnTRDdb7h5zTRAqYP5g&profile=_default&rank=11&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcreative-writing-mfa%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcreative-writing-mfa%2F&auth=oif1sTfFoRwhP3adeWKGUg&profile=_default&rank=12&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcyber-security-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fcyber-security-msc%2F&auth=MSck68NQ4JM8lrHAGd1nFw&profile=_default&rank=13&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education%2F&auth=wrGX7KNL6zVuAzBriZyz1w&profile=_default&rank=14&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-early-childhood%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-early-childhood%2F&auth=nJo38EbyaChgKo0UTqC60A&profile=_default&rank=15&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-mentoring%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-mentoring%2F&auth=hBXQeAV4U1XoV9uhRalkbQ&profile=_default&rank=16&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-post-compulsory-education%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-post-compulsory-education%2F&auth=X6VAJ%2BEGTQYwMgYmLzPULw&profile=_default&rank=17&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-research-engaged-setting%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fma-education-research-engaged-setting%2F&auth=dCGJz5EG3VTjFEFJemgyfQ&profile=_default&rank=18&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fexecutive-mba%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fexecutive-mba%2F&auth=FZ9TJrkdr1lbIykcrR22mA&profile=_default&rank=19&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Ffinance-mba%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Ffinance-mba%2F&auth=7ic7KuYW6Nc8CFmtsDjgJQ&profile=_default&rank=20&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Ffine-art-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Ffine-art-ma%2F&auth=Tf4Tl7T9l7qw30znl62KwQ&profile=_default&rank=21&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fhistory-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fhistory-ma%2F&auth=fEKyAIRwCdVMl%2BKNvpOIWA&profile=_default&rank=22&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fhuman-resource-management-mba%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fhuman-resource-management-mba%2F&auth=QeedN74KDBJCiHOCaPTvOg&profile=_default&rank=23&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fillustration-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fillustration-ma%2F&auth=AFGAJXYCzSNHYHcYRa8sWg&profile=_default&rank=24&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Finternational-business-management-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Finternational-business-management-msc%2F&auth=%2FXk3851fgyIJmgr5%2Fjmy5w&profile=_default&rank=25&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Finternational-history-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Finternational-history-ma%2F&auth=xo%2FB5mm0K4CIVnoqZoCH0w&profile=_default&rank=26&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Finternational-marketing-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Finternational-marketing-msc%2F&auth=obBwWU8sgcvvHSCjN3e4zg&profile=_default&rank=27&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Flanguage--linguistics-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Flanguages--linguistics%2Flanguage--linguistics-ma%2F&auth=ePXMQmHSYD67DcTYxd70pQ&profile=_default&rank=28&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fleadership--management-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fleadership--management-msc%2F&auth=ajueYLZcEmOsLIp%2F%2BInSPQ&profile=_default&rank=29&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fprofessional-health--social-care%2Fleadership-in-health--social-care-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fprofessional-health--social-care%2Fleadership-in-health--social-care-msc%2F&auth=8xbKLU9r1rvnvtsXYReBcg&profile=_default&rank=30&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fmaster-of-business-administration-mba%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fbusiness--management%2Fmaster-of-business-administration-mba%2F&auth=bPx7T4TNQ1rmZO5rhvBTVQ&profile=_default&rank=31&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fmusic-composition-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fmusic-composition-ma%2F&auth=8KXF6TnK5Ky1t1av8121pA&profile=_default&rank=32&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fmusic-production-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fmusic-production-ma%2F&auth=W%2BCD2BgeLNgyca1vF9u7xg&profile=_default&rank=33&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fot-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fot-msc%2F&auth=W0gz52GqGNHwi43C9ZFx%2FA&profile=_default&rank=34&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fphotography-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fphotography-ma%2F&auth=BLjNfIIQM7%2BgGBLv6Ma%2Fng&profile=_default&rank=35&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fprofessional-health--social-care%2Fphysiotherapy-pre-registration-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fprofessional-health--social-care%2Fphysiotherapy-pre-registration-msc%2F&auth=pVO4STkLcbF5ZDStQT%2FZFw&profile=_default&rank=36&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fprimary-education-pgce-school-direct%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fprimary-education-pgce-school-direct%2F&auth=uCJ1Y1hZZNPjIQBrqqNLBw&profile=_default&rank=37&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fprimary-education-university-centred-pgce%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fprimary-education-university-centred-pgce%2F&auth=xb%2Bat82clI8ud8T6sAiMOg&profile=_default&rank=38&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fpsychology%2Fprofessional-doctorate-in-counselling-psychology-%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fpsychology%2Fprofessional-doctorate-in-counselling-psychology-%2F&auth=SGjXJvWU1SWqyc6ZH8a%2B2w&profile=_default&rank=39&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fprofessional-health--social-care%2Fprofessional-health--social-care-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fprofessional-health--social-care%2Fprofessional-health--social-care-msc%2F&auth=hD%2F5FF8SSOQgSg8UL20WRQ&profile=_default&rank=40&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fpsychology%2Fpsychology-of-child--adolescent-development-msc%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Fpsychology%2Fpsychology-of-child--adolescent-development-msc%2F&auth=JOYia7uXszNIzh39xpqrnw&profile=_default&rank=41&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fsecondary-education-pgce-school-direct%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fsecondary-education-pgce-school-direct%2F&auth=EN2liltr%2Bw8%2Fgqmmw9RGBA&profile=_default&rank=42&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fsecondary-education-re-pgce%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Feducation%2Fsecondary-education-re-pgce%2F&auth=Mpr0K%2BOVdpPJSNds5Tw2Og&profile=_default&rank=43&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Ftheatre--performance-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Ftheatre--performance-ma%2F&auth=DCOcG1C0zPoEhBb797ORFg&profile=_default&rank=44&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fvirtual-and-augmented-reality-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fvirtual-and-augmented-reality-ma%2F&auth=KM%2F2vGD0uaE5E4EN3es7Tg&profile=_default&rank=45&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',
'https://yorksj.funnelback.co.uk/s/redirect?collection=yorksj-meta&url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanities--performance%2Fvisual-communication-ma%2F&index_url=https%3A%2F%2Fwww.yorksj.ac.uk%2Fstudy%2Fpostgraduate%2Fcourses%2Farts-humanites--performance%2Fvisual-communication-ma%2F&auth=gqCGVj3cxTkmudm6ccIxkw&profile=_default&rank=46&query=%21showall+%7CcourseLevel%3A%22%24%2B%2B+Postgraduate+Taught+%24%2B%2B%22+%7CcourseAttendance%3A%22%24%2B%2B+Full-time+%24%2B%2B%22',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'York St John University'
        try:
            location = response.xpath('//*[@id="section-overview"]/div/div[2]/dl[1]/dd').extract()[0]
            location = remove_tags(location)
            #print(location)
        except:
            location = 'N/A'
            #print(location)
        try:
            department = response.xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/p[2]/a[3]/strong').extract()[0]
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
            degree_overview_en = remove_tags(degree_overview_en,keep=('div','p','ul','li','span'))
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
            overview_en = response.xpath('//*[@id="section-overview"]/div/div[1]').extract()[0]
            overview_en = remove_tags(overview_en,keep=('div','p','ul','li','span'))
            overview_en = overview_en.replace('  ','')
            #overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','')
            overview_en = overview_en.replace('\r\n','')
            overview_en = overview_en.replace('\n','')
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = 'N/A'
            #print(overview_en)


        try:
            start_date = response.xpath('//*[@id="section-overview"]/div/div[2]').extract()[0]
            start_date = remove_tags(start_date)
            if 'January' in start_date:
                start_date = '1'
            else:
                start_date = '9'
            print(start_date)
        except:
            start_date = '9'
            print(start_date)



        try:
            modules_en = response.xpath('//*[@id="level-1"]/div').extract()[0]
            modules_en = remove_tags(modules_en,keep=('div','p','ul','li','span'))
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('	','')
            modules_en = modules_en.replace('  ','')
            modules_en = modules_en.replace('\n','')
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
            ielts = response.xpath('//*[@id="reqs-2"]/div').extract()[0]
            ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            ielts = re.findall('(\d\.\d)',ielts)[0]
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            #ielts_l = re.findall('IELTS(.*)',ielts)[1]
            ielts_l = response.xpath('//*[@id="reqs-2"]/div').extract()[0]
            ielts_l = re.findall('(\d\.\d)', ielts_l)[1]
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
            interview_desc_en = remove_tags(interview_desc_en,keep=('div','p','ul','li','span'))
            interview_desc_en = interview_desc_en.replace('\n\n', '\n')
            interview_desc_en = interview_desc_en.replace('\r\n', '')
            interview_desc_en = interview_desc_en.replace('	', '')
            interview_desc_en = interview_desc_en.replace('  ', '')
            interview_desc_en = interview_desc_en.replace('\n', '')
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
            career_en = remove_tags(career_en,keep=('div','p','ul','li','span'))
            career_en = career_en.replace('\r\n','')
            career_en = career_en.replace('  ','')
            career_en = career_en.replace('\n','')
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
            duration =  response.xpath('//*[@id="section-overview"]/div/div[2]/dl[3]/dd').extract()[0]
            duration = remove_tags(duration)
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '1' in duration:
                duration = '1'
            elif '2' in duration:
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
            alevel = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div/table[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'CC'
            #print(alevel)
        try:
            ucascode = response.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]').extract()[0]
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
            teach_time = response.xpath('//*[@id="section-overview"]/div/div[2]').extract()[0]
            teach_time = remove_tags(teach_time)
            if 'full' in teach_time:
                teach_time = 'fulltime'
            elif 'Full' in teach_time:
                teach_time = 'fulltime'
            else:
                teach_time = 'parttime'
            print(teach_time)
        except:
            teach_time = 'N/A'
            print(teach_time)

        teach_type = 'taught'

        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 2
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
        #item["alevel"] = alevel
        #item["ib"] = ib
        #item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        #item["apply_pre"] = ''
        item["teach_time"] = teach_time
        item["teach_type"] = teach_type
        item["assessment_en"] = ''
        yield item