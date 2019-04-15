# -*- coding: utf-8 -*-
import scrapy
import re
from scrapySchool_Australian_yan.clearSpace import clear_space, clear_space_str, clear_lianxu_space
from scrapySchool_Australian_yan.getItem import get_item
from scrapySchool_Australian_yan.getTuition_fee import getTuition_fee
from scrapySchool_Australian_yan.items import ScrapyschoolAustralianYanItem
from scrapySchool_Australian_yan.remove_tags import remove_class
from scrapySchool_Australian_yan.getStartDate import getStartDate
from scrapySchool_Australian_yan.getDuration import getIntDuration
from lxml import etree
import requests
from w3lib.html import remove_tags


class TheUniversityOfNewSouthWales_P_handbook2019Spider(scrapy.Spider):
    name = "TheUniversityOfNewSouthWales_P_handbook2019"
    # start_urls = ["https://www.handbook.unsw.edu.au/",]
#     start_urls = ["https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9314?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7318?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5312?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9318?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5306?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7306?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9313?browseByFaculty=FacultyOfArtDesign&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8236?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5275?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8224?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8930?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8942?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7401?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8910?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7960?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8960?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7359?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8143?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7131?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7451?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8151?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5151?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8152?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5148?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7148?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8660?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7543?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8621?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5449?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7320?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8338?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5341?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8037?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5037?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9150?browseByFaculty=FacultyOfLaw&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9201?browseByFaculty=FacultyOfLaw&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5512?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7312?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9012?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9372?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7372?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5372?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7360?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5509?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8901?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5545?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5536?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8741?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/5741?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8095?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8161?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8271?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8717?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8719?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8411?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8416?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8350?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8355?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8625?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7315?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8404?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/7355?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8417?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5499?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7339?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8623?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8233?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8202?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8237?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8234?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8259?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8282?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7327?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8925?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8926?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8203?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8204?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7375?browseByFaculty=FacultyOfArtsAndSocialSciences&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8148?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8121?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7123?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8136?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7127?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8127?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7332?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5132?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8132?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8141?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8131?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7313?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5313?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8313?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8149?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5149?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7149?browseByFaculty=FacultyOfBuiltEnvironment&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8543?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5543?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8059?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5059?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5046?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7335?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8335?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5335?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7343?browseByFaculty=FacultyOfEngineering&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8902?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9041?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8362?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5362?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7362?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9043?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9044?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7367?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9048?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5567?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9051?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9053?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9052?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9058?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9054?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9042?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9370?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5507?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9045?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7368?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9046?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9056?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9040?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9057?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9047?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9059?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9065?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5508?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7379?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9014?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7014?browseByFaculty=FacultyOfMedicine&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7659?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5659?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7433?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7436?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8073?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7440?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5331?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8256?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8257?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5304?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8750?browseByFaculty=FacultyOfScience&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7412?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8412?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8406?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8413?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/5273?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7273?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9273?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8435?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8371?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8361?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8635?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8409?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8415?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7357?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9250?browseByFaculty=UnswBusinessSchool&",
# "https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/7321?browseByFaculty=UnswBusinessSchool&", ]
    # 2019.03.14更新链接
    start_urls = ["https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8224?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8625?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8355?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8404?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8417?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9046?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8136?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8338?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8910?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8901?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/9201?browseByFaculty=FacultyOfLaw&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8313?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8149?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9014?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8151?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8152?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8148?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8095?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8121?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8930?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8942?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8910?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8960?browseByFaculty=FacultyOfArtsAndSocialSciences&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8543?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9051?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8361?browseByFaculty=UnswBusinessSchool&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8059?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8059?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8335?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8335?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8073?browseByFaculty=FacultyOfScience&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9370?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/9065?browseByFaculty=FacultyOfMedicine&",
"https://www.handbook.unsw.edu.au/postgraduate/programs/2019/8037?browseByFaculty=FacultyOfEngineering&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8132?browseByFaculty=FacultyOfBuiltEnvironment&",
"https://www.handbook.unsw.edu.au/Postgraduate/programs/2019/8141?browseByFaculty=FacultyOfBuiltEnvironment&", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


    def parse(self, response):
    #     faculty_urls = response.xpath("//div[@id='tab_OrgUnits']/a/@href").extract()
    #     # print(faculty_urls)
    #     if faculty_urls:
    #         for link in faculty_urls:
    #             url = "https://www.handbook.unsw.edu.au" + link
    #             yield scrapy.Request(url, callback=self.parse_url)
    #
    # def parse_url(self, response):
    #     # print("======================", response.url)
    #     links = response.xpath("//div[@id='singleCoursePostgraduate']//a/@href").extract()
    #     print("links: ", links)
    #     if links:
    #         for link in links:
    #             url = "https://www.handbook.unsw.edu.au" + link.replace("\n", "").strip()
    #             print("url: ", url)
    #             # yield scrapy.Request(url, callback=self.parse_data)
    #
    # def parse_data(self, response):
        item = get_item(ScrapyschoolAustralianYanItem)
        item['university'] = "The University of New South Wales"
        item['url'] = response.url
        item['degree_type'] = 2
        item['teach_time'] = 'coursework'
        print("===========================")
        print(response.url)
        try:
            department = response.xpath("//li[3]//a//text()").extract()
            item['department'] = ''.join(department).strip()
            print("item['department']: ", item['department'])

            location = response.xpath("//div[@role='complementary']//strong[@tabindex='0'][contains(text(),'Campus')]/../p//text()").extract()
            item['location'] = ''.join(location).strip()
            print("item['location']: ", item['location'])

            duration = response.xpath(
                "//div[contains(@role,'complementary')]//strong[contains(@tabindex,'0')][contains(text(),'Typical duration')]/../p//text()").extract()
            clear_space(duration)
            print("duration: ", duration)
            if "Years" in ''.join(duration):
                item['duration'] = ''.join(duration).replace("Years", "").strip()
                item['duration_per'] = 1
            print("item['duration']: ", item['duration'])

            # //div[@id='readMoreToggle1']
            overview_en = response.xpath("//div[@id='readMoreToggle1']/div[1]").extract()
            item['degree_overview_en'] = item['overview_en'] = remove_class(clear_lianxu_space(overview_en))
            print("item['overview_en']: ", item['overview_en'])

            item["rntry_requirements_en"] = None
            rntry_requirements_en = response.xpath("//div[@class='m-accordion-group m-accordion-with-header']//div[@class='m-accordion-body']").extract()
            if rntry_requirements_en:
                item['rntry_requirements_en'] = remove_class(clear_lianxu_space(rntry_requirements_en))
            print("item['rntry_requirements_en']: ", item['rntry_requirements_en'])

            modules_en = response.xpath("//div[@id='structure']/div[position()<last()]").extract()
            if modules_en:
                item['modules_en'] = remove_class(clear_lianxu_space(modules_en))
            print("item['modules_en']: ", item['modules_en'])

            # start_date = response.xpath(
            #     "//section//dt[contains(text(), 'Entry')]/following-sibling::dd[1]//text()").extract()
            # clear_space(start_date)
            # print(len(start_date))
            # print("start_date: ", start_date)
            #
            # tuition_fee = response.xpath(
            #     "//section//dt[contains(text(), 'Estimated first year tuition')]/following-sibling::*[1]//text()").extract()
            # clear_space(tuition_fee)
            # print(len(tuition_fee))
            # print("tuition_fee: ", tuition_fee)
            #
            # careerEle = response.xpath("//section//dl[last()]")
            # print(len(careerEle))
            # print("careerEle: ", careerEle)

            # 学位类型列表
            degree_name = response.xpath("//div[@role='complementary']//p[contains(text(),'Master of')]/text()|//div[@role='complementary']//p[contains(text(),'Juris Doctor')]/text()").extract()
            clear_space(degree_name)
            if len(degree_name) > 0:
                item['degree_name'] = ', '.join(degree_name).replace("-", "").strip()
            else:
                item['degree_name'] = None
            print("item['degree_name']: ", item['degree_name'])

            programme_list = response.xpath('//div[@data-hbui-filter-item="specialisation"]/a/div/p//text()').extract()
            print("programme_list: ", programme_list)

            if item['degree_name'] is None:
                pass
            else:
                if len(programme_list) == 0:
                    programme_en = response.xpath("//span[@data-hbui='module-title']//text()").extract_first(None)
                    print("programmen: ", programme_en)
                    item['programme_en'] = programme_en
                    yield item
                else:
                    for prog in programme_list:
                        item['programme_en'] = prog
                        yield item
        except Exception as e:
            with open(".//scrapySchool_Australian_yan/error/"+item['university']+str(item['degree_type'])+".txt", 'w', encoding="utf-8") as f:
                f.write(str(e) + "\n" + response.url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", response.url)

    def parse_major_detile(self, major_url, item):
        item['url'] = major_url
        print("item['url']_major: ", item['url'])
        data = requests.get(major_url, headers=self.headers_base)
        response = etree.HTML(data.text.replace('<?xml version="1.0" encoding="utf-8"?>', ""))
        # print("===1=", response)
        programme = response.xpath("//div[@class='internalContentWrapper']/h1[1]//text()")
        print("prog ", programme)
        programme_str = ''.join(programme)
        if "-" in programme_str:
            programme_list = programme_str.split("-")
            item['programme_en'] = ''.join(programme_list[:-1]).strip()
        else:
            item['programme_en'] = programme_str
        print("item['programme_en']_major: ", item['programme_en'])

        overview_en = response.xpath("//h2[contains(text(),'Stream Outline')]/../preceding-sibling::*[1]/following-sibling::*[position()<3]|"
                                     "//td[@class='mainInformation']//div[1]")
        overview_en_str = ""
        if len(overview_en) > 0:
            for m in overview_en:
                # print("===", overview_en_str)
                overview_en_str += etree.tostring(m, encoding='unicode',method='html')
        item['overview_en'] = remove_class(clear_lianxu_space([overview_en_str]))
        print("item['overview_en']_major: ", item['overview_en'])

        modules_en = response.xpath(
            "//a[@name='planstructure']/preceding-sibling::*[1]/following-sibling::*[position()<last()-1]|"
            "//table[@class='tabluatedInfo']")
        modules_en_str = ""
        if len(modules_en) > 0:
            for m in modules_en:
                modules_en_str += etree.tostring(m, encoding='unicode',method='html')
        item['modules_en'] = remove_class(clear_lianxu_space([modules_en_str]))
        print("item['modules_en']_major: ", item['modules_en'])

        new_url_list = response.xpath("//table[@class='tabluatedInfo']//tr/td/a/@href")
        return new_url_list