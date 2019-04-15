from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapymodule_Rent.clearSpace import clear_space, clear_lianxu_space
from scrapymodule_Rent.getItem import get_item
from scrapymodule_Rent.items import ScrapymoduleRentItem
import scrapy, re, time
import json, math
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class RentOpenRentTest(scrapy.Spider):
    name = 'rentOpenRent'
    start_urls = ["https://www.openrent.co.uk/properties-to-rent/Bath?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Birmingham?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Bradford?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Brighton&Hove?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Bristol?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Cambridge?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Canterbury?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Carlisle?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Chelmsford?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Chester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Chichester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Coventry?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Derby?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Durham?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Ely?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Exeter?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Gloucester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Hereford?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Kingston-upon-Hull?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Lancaster?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Leeds?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Leicester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Lichfield?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Lincoln?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Liverpool?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/City-of-London?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Manchester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Newcastle-upon-Tyne?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Norwich?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Nottingham?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Oxford?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Peterborough?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Plymouth?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Portsmouth?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Preston?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Ripon?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Salford?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Salisbury?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Sheffield?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Southampton?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/St-Albans?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Stoke-on-Trent?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Sunderland?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Truro?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Wakefield?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Wells?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Westminster?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Winchester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Wolverhampton?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/Worcester?isLive=true",
"https://www.openrent.co.uk/properties-to-rent/York?isLive=true",  ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    # def start_requests(self):
    #     driver = webdriver.PhantomJS(
    #         r"C:\Users\DELSK\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    #     print("请求网页中...")
    #     try:
    #         for url in self.start_urls:
    #             driver.get(url)
    #             js1 = "var q=document.documentElement.scrollTop=1000"
    #             driver.execute_script()
    #             # yield scrapy.Request(url, callback=self.parse)
    #     except Exception as e:
    #         print("请求异常：", e)

    def parse(self, response):
        print("*************", response.url, "*************")
        city = response.xpath("//input[@id='searchBox_ByCommute_']/@value").extract()
        links = response.xpath("//div[@id='toggleLetProperties']/preceding-sibling::div//div[@class='lpcc']//div[@class='lpc listingPic']/a/@href").extract()
        print(len(links))
        links = list(set(links))
        print(len(links))
        for link in links:
            url = "https://www.openrent.co.uk" + link
            # yield scrapy.Request(url, callback=self.parse_data, meta={'city': ''.join(city)})


    def parse_data(self, response):
        item = get_item(ScrapymoduleRentItem)
        print("---------------------------", response.url)
        item['country'] = 'England'
        item['url'] = response.url
        item['city'] = response.meta.get('city')
        print("item['city']: ", item['city'])
        try:
            '''   房源名称：2 Bed Flat, Rupert Street, W1D
                位置：Location
                卧室数量：Bedrooms
                卫浴数量：Bathrooms
                最多可容纳人数：Maximum Tenants
                是否包Bill：Bills Included
                房源描述：Description
                价格：Price
                每月租金：Rent PCM
                设施：Features
                是否对学生友好：Student Friendly
                是否对宠物友好：Pets Allowed
                最短租期：Minimum Tenancy
                起租时间：Available From'''
            house_name = response.xpath("//h1[@class='property-title']//text()").extract()
            clear_space(house_name)
            item['house_name'] = ''.join(house_name).strip()
            print("item['house_name']: ", item['house_name'])

            detaile_address = response.xpath("//html//div[@class='card manage-card mb-0']//tr[1]/td[contains(text(),'Location:')]/following-sibling::td[1]//text()").extract()
            clear_space(detaile_address)
            item['detaile_address'] = ''.join(detaile_address).strip()
            print("item['detaile_address']: ", item['detaile_address'])

            housing_introduce = response.xpath("//div[@class='description']//text()").extract()
            item['housing_introduce'] = clear_lianxu_space(housing_introduce)
            # print("item['housing_introduce']: ", item['housing_introduce'])

            price = response.xpath("//strong[contains(text(),'Rent PCM')]/../following-sibling::td[1]//text()").extract()
            clear_space(price)
            item['price'] = ''.join(price).strip()
            print("item['price']: ", item['price'])

            supporting_facilities = response.xpath("//h2[contains(text(),'Features')]/..//text()").extract()
            # clear_space(supporting_facilities)
            item['supporting_facilities'] = clear_lianxu_space(supporting_facilities)
            # print("item['supporting_facilities']: ", item['supporting_facilities'])

            lease = response.xpath("//strong[contains(text(),'Minimum Tenancy')]/../following-sibling::td[1]//text()").extract()
            # clear_space(housing_introduce)
            item['lease'] = clear_lianxu_space(lease)
            print("item['lease']: ", item['lease'])

            available_timeDict = {"January": "01",
                                  "February": "02",
                                  "March": "03",
                                  "April": "04",
                                  "May": "05",
                                  "June": "06",
                                  "July": "07",
                                  "August": "08",
                                  "September": "09",
                                  "October": "10",
                                  "November": "11",
                                  "December": "12", }
            available_time = response.xpath("//strong[contains(text(),'Available From')]/../following-sibling::td[1]//text()").extract()
            available_time = clear_lianxu_space(available_time)
            if available_time == "Today":
                item['available_time'] = "now"
            elif "Months" in available_time:
                item['available_time'] = available_time
            else:
                a_time = available_time.split(" ")
                # print("a_time: ", a_time)
                item['available_time'] = a_time[-1] + "-" + available_timeDict.get(a_time[1].replace(',', '').strip()) + "-" + a_time[0]
            print("item['available_time']: ", item['available_time'])

            picture_list = response.xpath("//div//div[@class='property-thumb']//a[@class='photos thumbnail mfp-image']/@href").extract()
            # print(picture_list)
            for picture in picture_list:
                item['picture'] += picture + "; "
            print("item['picture']: ", item['picture'])

            yield item
        except Exception as e:
            print("异常：", str(e))
            print("报错url：", response.url)
            with open('./error/'+item['city'] +'.txt', 'a+') as f:
                f.write(str(e) + "\n=====================" + item['url'] + "\n")

