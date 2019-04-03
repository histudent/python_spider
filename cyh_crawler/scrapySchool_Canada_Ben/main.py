# _*_ coding:utf-8 _*_
from scrapy import cmdline

# cmdline.execute('scrapy crawl UniversityofWindsor'.split())
# cmdline.execute('scrapy crawl UniversityofWaterloo'.split())
# cmdline.execute('scrapy crawl UniversityofRegina'.split())
# cmdline.execute('scrapy crawl UniversityofLethbridge'.split())
# cmdline.execute('scrapy crawl UniversityofOttawa'.split())
# cmdline.execute('scrapy crawl AcadiaUniversity'.split())
# cmdline.execute('scrapy crawl UniversityofNewBrunswick'.split())
# cmdline.execute('scrapy crawl BishopUniversity'.split())
# cmdline.execute('scrapy crawl UniversityofVictoria'.split())
# cmdline.execute('scrapy crawl BrandonUniversity'.split())
# cmdline.execute('scrapy crawl TrentUniversity'.split())
# cmdline.execute('scrapy crawl MacEwanUniversity'.split())

from pyecharts import Bar,Pie

Bar = Bar("我是主标题", "我是副标题")
# 用于添加图表的数据和设置各种配置项
is_more_utils=True #可以按右边的下载按钮将图片下载到本地
Bar.add("我是一张表格", ["英国本科", "英研究生", "澳洲本科", "澳研究生"], [111, 222, 333, 444], is_more_utils=True)
# Bar.show_config()  # 打印输出图表的所有配置项
Bar.render('E:\\hooli.html')
