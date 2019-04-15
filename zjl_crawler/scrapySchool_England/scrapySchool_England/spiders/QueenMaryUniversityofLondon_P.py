# _*_ coding:utf-8 _*_
__author__ = 'zjl'
__date__ = '2018/6/27 11:05'
import scrapy,json
import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapySchool_England.getItem import get_item1
from scrapySchool_England.getTuition_fee import getTuition_fee
from scrapySchool_England.items import ScrapyschoolEnglandItem1
from scrapySchool_England.remove_tags import remove_class
from scrapySchool_England.getIELTS import get_ielts, get_toefl
from scrapySchool_England.clearSpace import clear_space_str
from w3lib.html import remove_tags
class QueenMaryUniversityofLondonSpider(scrapy.Spider):
    name = 'QueenMaryUniversityofLondon_P'
    allowed_domains = ['qmul.ac.uk/']
    start_urls = []
    C= [
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121541.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121456.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200926.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200928.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/149585.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121462.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121436.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/126325.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121395.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/126327.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121410.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121525.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121539.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172939.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172474.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172473.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121421.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/182317.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121399.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159406.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159404.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159410.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159407.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159405.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159403.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159408.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/159409.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/177439.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/177441.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/162978.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/162977.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/177440.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/177438.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/163459.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/163458.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121379.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121771.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121366.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121550.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/170655.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/170657.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121382.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/138397.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/137562.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121473.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121354.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/166611.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121547.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121458.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121543.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121461.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/179968.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201202.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201193.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121377.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121738.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121548.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/148633.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121386.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/137236.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/189578.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/145314.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121446.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/176787.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121469.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121454.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121471.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/177122.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/191766.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121476.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121383.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121353.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121428.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121374.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/137235.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121464.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/137241.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/124845.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/124844.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200661.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121430.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121559.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121409.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121453.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121766.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188820.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121572.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121362.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200617.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200621.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200901.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/123996.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121429.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188817.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121512.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201481.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/155455.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/155454.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121371.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/191500.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121495.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121419.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121494.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121527.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121973.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/155742.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121974.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121773.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121348.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/143983.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/149526.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/187915.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/176965.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/190834.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200393.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/190833.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121432.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/190832.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121403.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/122494.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121370.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188749.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121481.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/165305.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/164936.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121523.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121435.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188748.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121415.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188746.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/167125.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188747.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121404.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121423.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121522.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121356.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121770.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/155314.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/155316.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/155315.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121358.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/142363.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/173148.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/173074.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121507.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/181164.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/171298.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200892.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172350.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121407.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172349.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121364.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121763.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121418.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/126476.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121540.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/189901.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201461.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121467.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/170654.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121549.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/170656.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121381.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201462.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121498.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121503.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/189577.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121360.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/189573.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200620.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200622.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200616.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200619.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200618.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200187.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121363.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121384.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121361.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121466.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/199288.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/199287.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121389.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121443.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121479.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121983.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121534.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121417.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121375.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172940.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121478.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121345.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121346.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201369.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/168693.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/168692.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/168690.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/168691.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121493.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121788.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121472.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201214.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121475.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/200392.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/143463.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121447.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121460.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/149026.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/149160.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121422.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188750.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/126163.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121359.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121505.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121502.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/143462.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/191573.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121532.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121553.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121444.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/149157.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/178913.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121560.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121412.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121394.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121414.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/138996.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/125762.html',
        'http://www.qmul.ac.uk/undergraduate/coursefinder/courses/200173.html',
        'http://www.qmul.ac.uk/undergraduate/coursefinder/courses/200172.html',
        'http://www.qmul.ac.uk/undergraduate/coursefinder/courses/200174.html',
        'http://www.qmul.ac.uk/undergraduate/coursefinder/courses/199074.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/149158.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121401.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/189574.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121344.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/201464.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121976.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121482.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188751.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/151798.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/151300.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121350.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/145693.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/188745.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121427.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121535.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121426.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/199124.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/199123.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/172941.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121463.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121342.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/151302.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/151301.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/164872.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/191253.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/195382.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121950.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121465.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/137233.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/178781.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/129308.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/137238.html',
        'http://www.qmul.ac.uk/postgraduate/taught/coursefinder/courses/121536.html'
    ]
    for i in C:
        start_urls.append(i)
    #取列表页
    # for i in range(1,271,10):
    #     base_url = 'http://search.qmul.ac.uk/s/search.html?collection=queenmary-coursefinder-pg&query=&f.Mode%7CM=full+time&sort=title&start_rank='+ str(i)
    #     start_urls.append(base_url)
    # def parse(self, response):
    #     pass
    #     item = get_item1(ScrapyschoolEnglandItem1)
    #     url = response.xpath('//*[@id="search-results"]/li/div[1]/div[1]/div[2]/h4/a/@title').extract()
    def parse(self, response):
        pass
        item = get_item1(ScrapyschoolEnglandItem1)
        #1.university
        university = 'Queen Mary University of London'


        #2.location
        location = 'London'


        #3.department
        department = response.xpath('//*[@id="count"]/article/div/aside/p[3]/a[1]').extract()
        department = ''.join(department)
        department = remove_tags(department)
        # print(department)

        #4.programme_en
        programme_en = response.xpath('//*[@id="count"]/article/header/h1').extract()
        programme_en = ''.join(programme_en)
        programme_en = remove_class(programme_en)
        programme_en = remove_tags(programme_en)
        # print(programme_en)

        #5.degree_type
        degree_type = 2

        #6.degree_name  7.duration  8.duration_per
        try:
            degree_name = response.xpath('//*[@id="count"]/article/header/h2').extract()
            degree_name = ''.join(degree_name)
            degree_name = remove_tags(degree_name)
            #print(degree_name)
            duration = re.findall('\(.*\)',degree_name)
            duration = ''.join(duration)
            duration = duration.replace('(','')
            duration = duration.replace(')','')
            if 'months' in duration:
                duration = re.findall('\d',duration)[0]
                duration_per = 3
            else:
                duration = re.findall('\d',duration)[0]
                duration_per = 1
            # print('duration:',duration)
            # print('duration_per:',duration_per)
            if duration in degree_name:
                degree_name = degree_name.replace(duration,'')
                degree_name = degree_name.replace('(','')
                degree_name = degree_name.replace(')', '')
                degree_name = degree_name.split()[0]
            else:
                degree_name = 'N/A'
            # print(degree_name)
        except:
            degree_name = 'N/A'
            duration = None
            duration_per = 1

        #9.overview_en
        overview_en = response.xpath('//*[@id="first"]').extract()
        overview_en = ''.join(overview_en)
        overview_en = remove_class(overview_en)
        start = overview_en.find('Overview')
        end = overview_en.find('Why study')
        overview_en= overview_en[start: end]
        overview_en = clear_space_str(overview_en)
        # print(overview_en)

        #10.teach_time
        teach_time = 'full time'

        #11.modules_en
        try:
            modules_en = response.xpath('//*[@id="second"]').extract()
            modules_en = ''.join(modules_en)
            modules_en = remove_class(modules_en)
            if 'For more information contact' in modules_en:
                start = modules_en.find('Structure')
                end = modules_en.find('For more information contact')
                modules_en = modules_en[start:end]
                modules_en = clear_space_str(modules_en)
            else:
                modules_en = modules_en
            # print(modules_en)
        except:
            modules_en = 'N/A'

        #12.assessment_en
        try:
            assessment_en = response.xpath('//*[@id="fourth"]').extract()
            assessment_en = ''.join(assessment_en)
            assessment_en = remove_class(assessment_en)
            assessment_en = clear_space_str(assessment_en)
            # print(assessment_en)
        except:
            assessment_en = 'N/A'

        #13.career_en
        try:
            career_en = response.xpath('//*[@id="sixth"]').extract()
            career_en = ''.join(career_en)
            career_en = remove_class(career_en)
            career_en = clear_space_str(career_en)
            # print(career_en)
        except:
            career_en = 'N/A'

        #14.tuition_fee
        try:
            tuition_fee1 = response.xpath('//*[@id="fifth"]/p[2]/text()').extract()
            tuition_fee1 = ''.join(tuition_fee1)
            tuition_fee1 = remove_tags(tuition_fee1)
            tuition_fee1 = re.findall('\d{1,3},\d{3}', tuition_fee1)
            if tuition_fee1 == []:
                tuition_fee = response.xpath('//*[@id="fifth"]/p[1]/text()').extract()
                tuition_fee = ''.join(tuition_fee)
                tuition_fee = remove_tags(tuition_fee)
                tuition_fee = re.findall('\d{1,3},\d{3}', tuition_fee)[0]
                # print(tuition_fee)
            else:
                tuition_fee = tuition_fee1[0]
            tuition_fee = tuition_fee.replace(',','')
            # print(tuition_fee)
        except:
            tuition_fee = 0

        #15.tuition_fee_pre
        tuition_fee_pre = '£'

        #16.entry_requirements
        try:
            entry_requirements_list = response.xpath('//*[@id="third"]').extract()
            entry_requirements_list = ''.join(entry_requirements_list)
            entry_requirements_list = remove_class(entry_requirements_list)
            # entry_requirements_list = remove_tags(entry_requirements_list)
            if 'International applicants' in entry_requirements_list:
                start = entry_requirements_list.find('Entry requirements')
                mid = entry_requirements_list.find('International applicants')
                end = entry_requirements_list.find('For more information')
                entry_requirements = entry_requirements_list[start:mid]
                other = entry_requirements_list[mid:end]
            else:
                entry_requirements = entry_requirements_list
                other = 'N/A'
            if 'mso-fareast-language:EN-US' in entry_requirements:
                start = entry_requirements.findall('Entry requirements')
                end = 'Normal'
                entry_requirements = entry_requirements[start:end]
            else:
                entry_requirements = entry_requirements
            entry_requirements = clear_space_str(entry_requirements)
            other = clear_space_str(other)
            # print(entry_requirements)
            #print(other)
        except:
            entry_requirements = 'N/A'
            other = 'N/A'

        #17.雅思
        if department == 'School of Business and Management':
            ielts=7
            ielts_l=5.5
            ielts_s=5.5
            ielts_r=5.5
            ielts_w=6
            toefl=100
            toefl_l=17
            toefl_s=20
            toefl_r=18
            toefl_w=21
        elif department =='School of English and Drama':
            ielts = 7
            ielts_l = 7
            ielts_s = 7
            ielts_r = 7
            ielts_w = 7
            toefl = 100
            toefl_l = 22
            toefl_s = 25
            toefl_r = 24
            toefl_w = 27
        elif department =='School of Geography':
            ielts = 7
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department=='School of History':
            ielts = 7
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department =='School of Languages, Linguistics and Film':
            ielts = 7
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 7
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 27
        elif department=='School of Law':
            ielts = 7
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 7
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        elif department =='School of Politics and International Relations':
            ielts = 7
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6.5
            toefl = 100
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 24
        else:
            ielts = 6.5
            ielts_l = 5.5
            ielts_s = 5.5
            ielts_r = 5.5
            ielts_w = 6
            toefl = 92
            toefl_l = 17
            toefl_s = 20
            toefl_r = 18
            toefl_w = 21
        # print(ielts,ielts_l,ielts_r,ielts_s,ielts_w)

        url = response.url
        apply_documents_en = 'You must provide the following supporting documentation: Completed application form  Degree transcripts. Please provide a transcript of your degree(s). If you have not yet completed your degree please provide a transcript of your results achieved to date  If your degree was from a UK university, please upload a transcript of your marks for each year If your degree was from an overseas institution, you should supply a transcript of your marks for each year of your studies and a copy of your degree certificate together with a certified translation if the document is not in English. Please note that original documentation will be required before you enrol. International applicants are also advised to include high school transcripts Please provide the contact details of two referees on your application, at least one reference must be from an academic referee who is in a position to comment on the standard of your academic work and suitability for postgraduate level study. Where appropriate, a second referee can provide comment on your professional experience. Your academic referee(s) may already have provided you with a reference that you can use to support any application for study or research that you make. We call these ‘open’ references. Open references will normally only be accepted if they are written on headed paper, provided as a colour copy of the original, and provide the referee’s work contact details. If you have open references, please upload these at the time of application If you do not have open reference, we will contact your referee(s) via email to supply a reference, preferably electronically. Please note, we can only accept references provided by email if it is sent from a university or company email address. References from a personal email address such as Yahoo or Hotmail are not acceptable. Your referee(s) can also supply a paper reference in response to the reference request email your referee will receive. Paper reference forms should be endorsed by an appropriate institution/company stamp or on official institution/company letterhead, and should be provided as a scanned colour copy of the original. Curriculum Vitae (CV)/ Resume This list of documents may vary slightly from course to course, so you will need to check the guidance notes and academic school website for the programme that you are applying for.  Although not mandatory, you are encouraged to send in the following documents in support of your application:  Statement of purpose  Your statement of purpose should explain why you want to study your chosen programme and how it will help your life and career. This should typically be one side of A4 paper. IELTS/TOEFL certificate (if applicable) International applicants should provide evidence of English language ability: IELTS, TOEFL, or other acceptable proof. Please see the international students section for more details.'
        require_chinese_en = 'Taught degrees (MSc/MA: one year) For entry onto our masters level courses students should normally have achieved: Four-year bachelors degree from 211 or 985 University with 75%+ average Four-year bachelors degree from non-211 University within top 300 with average 80%+ The usual entrance requirement to a taught masters degree is a four-year bachelors degree from a 211 University. However, all applications are considered on an individual basis and students may be admitted to masters programmes with a lower level degree if they have work experience relevant to the degree applied for. Students with a three-year diploma (dazhuan) from a recognised institution may apply for the Pre-Masters Graduate Diploma, a year-long course which will gain them access to a masters programme.Research degree (MPhil/PhD: three years) For entry onto our research degree courses students should normally have a masters degree from a recognised university.'
        apply_fee = 0
        apply_pre = '£'
        item['apply_fee']  = apply_fee
        item['apply_pre']  = apply_pre
        item['require_chinese_en'] = require_chinese_en
        item['apply_documents_en'] = apply_documents_en
        item['university'] = university
        item['location'] = location
        item['department'] = department
        item['programme_en'] = programme_en
        item['degree_type'] = degree_type
        item['degree_name'] = degree_name
        item['duration'] = duration
        item['duration_per'] = duration_per
        item['overview_en'] = overview_en
        item['teach_time'] = teach_time
        item['modules_en'] = modules_en
        item['assessment_en'] = assessment_en
        item['career_en'] = career_en
        item['tuition_fee'] = tuition_fee
        item['tuition_fee_pre'] = tuition_fee_pre
        item['rntry_requirements'] = entry_requirements
        item['ielts'] = ielts
        item['ielts_l'] = ielts_l
        item['ielts_s'] = ielts_s
        item['ielts_r'] = ielts_r
        item['ielts_w'] = ielts_w
        item['toefl'] = toefl
        item['toefl_l'] = toefl_l
        item['toefl_s'] = toefl_s
        item['toefl_r'] = toefl_r
        item['toefl_w'] = toefl_w
        item['url'] = url
        yield item