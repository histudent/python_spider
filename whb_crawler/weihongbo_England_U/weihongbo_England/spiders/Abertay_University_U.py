import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Abertay_University_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
#     C = ['https://www.abertay.ac.uk/course-search/postgraduate-taught/accounting-and-finance-cima-gateway/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/food-and-drink-innovation/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/international-human-resource-management/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/accounting-finance-for-the-global-energy-sector/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/computer-games-technology/',
# 'https://www.abertay.ac.uk/course-search/english-language-courses/pre-sessional-english-programme/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/professional-masters-in-games-development/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/psychology/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/construction-management/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/counselling/',
# 'https://www.abertay.ac.uk/course-search/postgraduate-taught/ethical-hacking-and-cyber-security/',]

#     C= ['http://search.abertay.ac.uk/s/redirect?rank=1&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Faccounting-and-finance%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Faccounting-and-finance%2F&auth=9YaBamRGJol9DZZqtjVvNg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=2&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Faccounting-and-finance-evening-course%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Faccounting-and-finance-evening-course%2F&auth=VD0MFh6vyfp2KEtBDPknEg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=3&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fbiomedical-science%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fbiomedical-science%2F&auth=7x9zYlak6RTwNP%2Bv%2FtmoIQ&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=4&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fmsci-biomedical-science%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fmsci-biomedical-science%2F&auth=ku2zYgYbyAXdhQqKPKfEwA&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=5&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fbusiness-and-human-resource-management%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fbusiness-and-human-resource-management%2F&auth=bpH7djHdU2YeCFOdkpp2fw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=6&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fbusiness-management%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fbusiness-management%2F&auth=p%2F1DCqaLOkHNx2uTVTwd%2FQ&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=7&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcivil-and-environmental-engineering%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcivil-and-environmental-engineering%2F&auth=uiYCNMF0TLyX%2FZmfsomrNg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=8&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputer-arts%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputer-arts%2F&auth=F6E%2F8NtR6lhABABdVE%2BcIg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=9&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputer-game-applications-development%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputer-game-applications-development%2F&auth=qS2Jzm8QZL0TBWRtMhPfMg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=10&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputer-games-technology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputer-games-technology%2F&auth=ux8PphmBXJfQfkPhdlmHYg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=11&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputing%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcomputing%2F&auth=fnJeFBLYypaW4WbuqZ0R9g&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=12&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcriminology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fcriminology%2F&auth=SFkJWvx2j%2FjUPcqkJdL7kw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=13&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fenvironmental-science-and-technology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fenvironmental-science-and-technology%2F&auth=dvQiT0d09gp6uzonR4ZlBg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=14&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fethical-hacking%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fethical-hacking%2F&auth=UzQAc98lGH%2Boe7J4XjxfaQ&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=15&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Ffitness-nutrition-and-health%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Ffitness-nutrition-and-health%2F&auth=649MHmuJVcTG7%2BmBwRCcpg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=16&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Ffood-and-consumer-science%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Ffood-and-consumer-science%2F&auth=g8weKt8Pa1vPKZ5DufHFeg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=17&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Ffood-nutrition-and-health%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Ffood-nutrition-and-health%2F&auth=JiOHYDdp5iVtWR5GtIMQxQ&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=18&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fforensic-and-analytical-science%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fforensic-and-analytical-science%2F&auth=ucFHVJbx0NK9Bn%2FfyIAekA&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=19&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fforensic-sciences%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fforensic-sciences%2F&auth=lO9azYweyb%2BhNiIdZ93wEw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=20&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fgame-design-and-production%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fgame-design-and-production%2F&auth=Lus2hRXyU9J0p%2FT1rgOAGg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=21&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Flaw%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Flaw%2F&auth=WEilWEIvYM5O7Sm3xvPM7w&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=22&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fmanagement-and-the-games-industry%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fmanagement-and-the-games-industry%2F&auth=NSUoWhIPIdWcNxBsmAgKWw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=23&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fmarketing-and-business%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fmarketing-and-business%2F&auth=fjBv97bWj93PSasFHTx3Ag&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=24&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fnursing-mental-health-nursing%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fnursing-mental-health-nursing%2F&auth=9CFk44f7AXBf8Hd9YhNXpg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=25&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fphysical-activity-and-health%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fphysical-activity-and-health%2F&auth=0miDh4lJTl5rkY92OeCyyA&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=26&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fenglish-language-courses%2Fpre-sessional-english-programme%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fenglish-language-courses%2Fpre-sessional-english-programme%2F&auth=7So8ze8a2wACXHBqZquayQ&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=27&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology%2F&auth=h51zryoFlDv9mKXLhfkEkw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=28&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology-and-counselling%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology-and-counselling%2F&auth=eO3DcBWNEAnAStJbwitHDw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=29&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology-and-forensic-biology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology-and-forensic-biology%2F&auth=KLZa4UbSKzApw7IgCfL4Ag&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=30&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology-and-human-resource-management%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fpsychology-and-human-resource-management%2F&auth=17jUVljJE%2BthCWsQAu6KzQ&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=31&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsocial-science%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsocial-science%2F&auth=YjidEtxV03Mut%2Bj58gyAuw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=32&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsociology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsociology%2F&auth=DoE7GXfnmI0P3BlPcYWfMw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=33&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsound-and-music-for-games%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsound-and-music-for-games%2F&auth=baTxADHD%2BVZllliVFAJaJA&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=34&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-exercise-leading-to-named-routes%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-exercise-leading-to-named-routes%2F&auth=KEvXwAFV20SJiC4mBYQ4vg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=35&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-exercise-science%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-exercise-science%2F&auth=1UoYRSqGQypy06GHlkRqlw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=36&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-management%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-management%2F&auth=YSKC8rfCnRStMIJA3Kf0Jw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=37&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-psychology%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsport-and-psychology%2F&auth=9NZi3%2BGF%2FP1zvYZgMHgaig&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=38&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsports-development-and-coaching%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fsports-development-and-coaching%2F&auth=BNbfqRjkVfyQFt07lVWdQg&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',
# 'http://search.abertay.ac.uk/s/redirect?rank=39&collection=umbraco-courses&url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fstrength-and-conditioning%2F&index_url=https%3A%2F%2Fwww.abertay.ac.uk%2Fcourse-search%2Fundergraduate%2Fstrength-and-conditioning%2F&auth=t5nOWfiyFhbBCE9j8DfQhw&query=%21null+%7CStudyLevels%3A%22%24%2B%2B+Undergraduate+%24%2B%2B%22&profile=_default?return=%3FstudyLevel%3DUndergraduate',]
    C =['https://www.abertay.ac.uk/course-search/undergraduate/accounting-and-finance/',
'https://www.abertay.ac.uk/course-search/undergraduate/msci-biomedical-science/',
'https://www.abertay.ac.uk/course-search/undergraduate/ethical-hacking/',
'https://www.abertay.ac.uk/course-search/undergraduate/computer-arts/',
'https://www.abertay.ac.uk/course-search/undergraduate/criminology/',
'https://www.abertay.ac.uk/course-search/undergraduate/computing/',
'https://www.abertay.ac.uk/course-search/undergraduate/computer-games-technology/',
'https://www.abertay.ac.uk/course-search/undergraduate/computer-game-applications-development/',
'https://www.abertay.ac.uk/course-search/undergraduate/food-and-consumer-science/',
'https://www.abertay.ac.uk/course-search/undergraduate/environmental-science-and-technology/',
'https://www.abertay.ac.uk/course-search/undergraduate/fitness-nutrition-and-health/',
'https://www.abertay.ac.uk/course-search/undergraduate/civil-and-environmental-engineering/',
'https://www.abertay.ac.uk/course-search/undergraduate/biomedical-science/',
'https://www.abertay.ac.uk/course-search/undergraduate/business-and-human-resource-management/',
'https://www.abertay.ac.uk/course-search/undergraduate/forensic-sciences/',
'https://www.abertay.ac.uk/course-search/undergraduate/business-management/',
'https://www.abertay.ac.uk/course-search/undergraduate/forensic-and-analytical-science/',
'https://www.abertay.ac.uk/course-search/undergraduate/food-nutrition-and-health/',
'https://www.abertay.ac.uk/course-search/undergraduate/law/',
'https://www.abertay.ac.uk/course-search/undergraduate/management-and-the-games-industry/',
'https://www.abertay.ac.uk/course-search/undergraduate/nursing-mental-health-nursing/',
'https://www.abertay.ac.uk/course-search/undergraduate/physical-activity-and-health/',
'https://www.abertay.ac.uk/course-search/undergraduate/psychology/',
'https://www.abertay.ac.uk/course-search/undergraduate/game-design-and-production/',
'https://www.abertay.ac.uk/course-search/undergraduate/psychology-and-counselling/',
'https://www.abertay.ac.uk/course-search/undergraduate/psychology-and-forensic-biology/',
'https://www.abertay.ac.uk/course-search/undergraduate/social-science/',
'https://www.abertay.ac.uk/course-search/undergraduate/psychology-and-human-resource-management/',
'https://www.abertay.ac.uk/course-search/undergraduate/sound-and-music-for-games/',
'https://www.abertay.ac.uk/course-search/undergraduate/sociology/',
'https://www.abertay.ac.uk/course-search/undergraduate/sport-and-management/',
'https://www.abertay.ac.uk/course-search/undergraduate/sport-and-exercise-leading-to-named-routes/',
'https://www.abertay.ac.uk/course-search/undergraduate/marketing-and-business/',
'https://www.abertay.ac.uk/course-search/undergraduate/sport-and-psychology/',
'https://www.abertay.ac.uk/course-search/undergraduate/sport-and-exercise-science/',
'https://www.abertay.ac.uk/course-search/undergraduate/sports-development-and-coaching/',
'https://www.abertay.ac.uk/course-search/undergraduate/strength-and-conditioning/',]
    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Abertay University'
        try:
            location = 'Dundee'
            #location = remove_tags(location)
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
            degree_name = response.xpath('/html/body/div[1]/section/div/div/h1/span').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = re.findall('(.* \(.*\))',degree_name)[0]

            #degree_name = re.findall('(.*)\n.*',degree_name)[0]
            #degree_name = re.findall('(.*)                    .*',degree_name)[0]
            #degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            degree_name = degree_name.replace(' ','')
            #print(degree_name)
        except:
            degree_name = 'BA'
            #print(degree_name)

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('/html/body/div[1]/section/div/div/h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en =programme_en.replace('\r\n','')
            programme_en = re.findall('(.*)                                            .*',programme_en)[0]
            programme_en = programme_en.replace('                    ','')

            #print(programme_en)

        except:
            programme_en = 'N/A'
            #print(programme_en)

        try:
            overview_en = response.xpath('/html/body/div[1]/div/div[1]/section[1]/div/div/div[2]').extract()[0]
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
            modules_en = response.xpath('//*[@id="Year1"]/div/div|//*[@id="Year2"]/div|/html/body/div[1]/div/div[1]/section[8]/div').extract()[0]
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
            rntry_requirements_en = response.xpath('//*[@id="entryrequirements"]').extract()[0]
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
            ielts_desc = response.xpath('//*[@id="entry-requirements"]/div/section[2]/div/ul/li').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)

        except:
            ielts_desc = 'N/A'

            #print(ielts_desc)

        try:
            #ielts = '6.5'
            #ielts =remove_tags(ielts)
            #ielts = re.findall('IELTS(.*)',ielts)[0]
            ielts = '6.5'
            #print(ielts)
        except:
            ielts = 0
            #print(ielts)

        try:
            #ielts_l = '5.5'
            ielts_l = '6.0'
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
            apply_desc_en = 'https://www.abertay.ac.uk/courses/postgraduate-taught/request-prospectus/'
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
            duration = response.xpath('/html/body/div[1]/div/div[1]/section[1]/div/div/div[1]/div/div[2]/span').extract()[0]
            #duration = remove_tags(duration)
            duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            if '3' in duration:
                duration = '3'
            elif '2' in duration:
                duration = '2'
            elif '1' in duration:
                duration = '1'
            elif '4' in duration:
                duration = '4'
            elif '5' in duration:
                duration = '5'
            elif '1' in duration:
                duration = '1'
            elif 'two' in duration:
                duration = '2'
            else:
                duration = '3'
            #print(duration)

        except:
            duration = 3
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="EntryToYear1"]/div/table/tbody/tr[5]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="EntryToYear1"]/div/table/tbody/tr[3]/td[2]').extract()[0]
            alevel = remove_tags(alevel)
            #alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('/html/body/div[1]/div/div[1]/section[1]/div/div/div[1]/div/div[4]/span|//*[@id="EntryToYear1"]/div/table/tbody/tr[3]/td[2]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = 'N/A'
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//div/div/div[3]/div/div[2]').extract()[0]
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
            assessment_en = response.xpath('/html/body/div[1]/div/div[1]/section[9]/div').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\r\n', '')
            assessment_en = assessment_en.replace('  ', '')
            assessment_en = assessment_en.replace('\n', '')
            #assessment_en = re.findall('Learning and Assessment(.*)Accreditation',assessment_en)[0]
            assessment_en = "<div><span>" + assessment_en + "</span></div>"
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
        item["batch_number"] = 3
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
        item["assessment_en"] =  assessment_en
        #item["apply_pre"] = ''
        yield item


