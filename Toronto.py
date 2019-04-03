# -*- coding:utf-8 -*-
"""
# @PROJECT: scrapySchool_Canada_Ben
# @Author: admin
# @Date:   2018-12-03 17:35:20
# @Last Modified by:   admin
# @Last Modified time: 2018-12-03 17:35:20
"""

import requests, csv
from lxml import etree
from scrapySchool_Canada_Ben.middlewares import *

urls = ["https://www.utoronto.ca/academics/programs-directory?page=0",
"https://www.utoronto.ca/academics/programs-directory?page=1",
"https://www.utoronto.ca/academics/programs-directory?page=2",
"https://www.utoronto.ca/academics/programs-directory?page=3",
"https://www.utoronto.ca/academics/programs-directory?page=4",
"https://www.utoronto.ca/academics/programs-directory?page=5",
"https://www.utoronto.ca/academics/programs-directory?page=6",
"https://www.utoronto.ca/academics/programs-directory?page=7",
"https://www.utoronto.ca/academics/programs-directory?page=8",
"https://www.utoronto.ca/academics/programs-directory?page=9",
"https://www.utoronto.ca/academics/programs-directory?page=10",
"https://www.utoronto.ca/academics/programs-directory?page=11",
"https://www.utoronto.ca/academics/programs-directory?page=12",
"https://www.utoronto.ca/academics/programs-directory?page=13",
"https://www.utoronto.ca/academics/programs-directory?page=14",]
for url in urls:
    headers_base = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    data = requests.get(url, headers=headers_base)
    response = etree.HTML(data.text)

    major = response.xpath("//div[1]/div[1]/a[1]/h4[1]//text()")
    clear_space(major)
    degree = response.xpath("//div[1]/div[1]/a[1]/p[1]//text()")
    clear_space(degree)
    spe = response.xpath("//div[1]/div[1]/a[1]/p[2]//text()")
    clear_space(spe)
    # campus = response.xpath("//div[1]/div[1]/a[1]/p[3]//text()")
    # clear_space(campus)

    print(major)
    print(len(major))
    print(degree)
    print(len(degree))
    print(spe)
    print(len(spe))
    # print(campus)
    # print(len(campus))
    for i in range(len(major)):
        with open("toronto1.csv", "a+") as f:
            writer = csv.writer(f)
            writer.writerow([major[i], degree[i], spe[i]])
    print("===================")



