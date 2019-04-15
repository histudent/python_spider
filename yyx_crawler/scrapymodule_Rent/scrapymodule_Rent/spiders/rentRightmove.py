from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapymodule_Rent.clearSpace import clear_space, clear_lianxu_space
from scrapymodule_Rent.getItem import get_item
from scrapymodule_Rent.items import ScrapymoduleRentItem
import scrapy, re
import json, math


class RentRightmoveTest(scrapy.Spider):
    name = 'rentRightmove'
    start_urls = ["https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Bath",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Birmingham",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Bradford",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Brighton+and+Hove",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Bristol",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Cambridge",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Canterbury",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Carlisle",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Chelmsford",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Chester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Chichester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Coventry",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Derby",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Durham",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Ely",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Exeter",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Gloucester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Hereford",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Kingston-upon-Hull",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Lancaster",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Leeds",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Leicester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Lichfield",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Lincoln",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Liverpool",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=City-of-London",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Manchester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Newcastle-upon-Tyne",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Norwich",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Nottingham",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Oxford",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Peterborough",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Plymouth",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Portsmouth",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Preston",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Ripon",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Salford",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Salisbury",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Sheffield",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Southampton",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=St-Albans",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Stoke-on-Trent",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Sunderland",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Truro",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Wakefield",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Wells",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Westminster",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Winchester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Wolverhampton",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=Worcester",
"https://www.rightmove.co.uk/property-to-rent/search.html?searchLocation=York", ]
    # print(len(start_urls))
    # start_urls = list(set(start_urls))
    # print(len(start_urls))

    def parse(self, response):
        # print("------------------------", response.url)
        keys = response.xpath("//input[@id='locationIdentifier']/@value").extract()
        if len(keys) == 0:
            keys = response.xpath("//select[@id='locationIdentifier']/option/@value").extract()
        # print("keys: ", keys)
        # https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=STATION%5E1004&index=0&includeLetAgreed=false
        for key in keys:
            key_list = key.split("^")
            # print("key_list: ", key_list)
            url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier="+key_list[0]+"%5E"+key_list[-1]+"&index=0&includeLetAgreed=false"
            # print("url = ", url)
            yield scrapy.Request(url, callback=self.parse_url)

    # 获得每页链接
    def parse_url(self, response):
        # print("******************"+response.url+"******************")
        # 正则匹配js文件
        option_value_list = re.findall(r'<script>window\.jsonModel\s=\s.*</script>', response.text)
        # print("option_value: ", option_value)
        # 转为字符串
        option_value_str = ''.join(option_value_list).replace("<script>window.jsonModel = ", "").replace("</script>", "").strip()
        # print(option_value_str)
        # 转为json文件，字典形式
        option_value_json = json.loads(option_value_str)
        # print(type(option_value_json))
        # 获得页码index
        pagination_option = option_value_json.get("pagination").get("options")
        # print("pagination: ", pagination_option)
        for page_value in pagination_option:
            index = page_value.get("value")
            url  = response.url.replace("index=0", "index="+index)
            # print("url = ", url)
            yield scrapy.Request(url, callback=self.parse_detail_url)

    def parse_detail_url(self, response):
        # print("====每页链接====", response.url)
        links = response.xpath("//div[@id='l-searchResults']/div/div/div/div[@class='propertyCard-content']/div[@class='propertyCard-section']/div[@class='propertyCard-details']/a[@class='propertyCard-link']/@href").extract()
        # print(links)
        # print(len(links))
        city = response.xpath("//input[@class='input input--full']/@value").extract()
        # print("city: ", city)
        for link in links:
            # print("link: ", link)
            if link != '':
                # print("=-=-=-=-")
                url = "https://www.rightmove.co.uk" + link
                yield scrapy.Request(url, callback=self.parse_data, meta={'city': ''.join(city)})

    def parse_data(self, response):
        item = get_item(ScrapymoduleRentItem)
        print("-------------详情页链接--------------", response.url)
        item['country'] = 'England'
        item['url'] = response.url
        item['city'] = response.meta.get('city')
        print(" item['city']: ", item['city'])
        try:
            '''  房源名称：1 bedroom flat to rent
                位置：Park Street, London
                房租：£3,250 pw
                房源描述：Full description'''
            house_name = response.xpath("//h1[@class='fs-22']//text()").extract()
            clear_space(house_name)
            item['house_name'] = ''.join(house_name).strip()
            print("item['house_name']: ", item['house_name'])

            detaile_address = response.xpath("//address[@class='pad-0 fs-16 grid-25']/text()").extract()
            clear_space(detaile_address)
            item['detaile_address'] = ''.join(detaile_address).strip()
            print("item['detaile_address']: ", item['detaile_address'])

            housing_introduce = response.xpath("//h3[contains(text(),'Full description')]/..//text()").extract()
            item['housing_introduce'] = clear_lianxu_space(housing_introduce)
            print("item['housing_introduce']: ", item['housing_introduce'])

            price = response.xpath("//p[@id='propertyHeaderPrice']//strong/text()").extract()
            clear_space(price)
            item['price'] = ''.join(price).strip()
            print("item['price']: ", item['price'])

            supporting_facilities = response.xpath("//h3[contains(text(),'Key features')]/..//text()").extract()
            # clear_space(supporting_facilities)
            item['supporting_facilities'] = clear_lianxu_space(supporting_facilities)
            # print("item['supporting_facilities']: ", item['supporting_facilities'])

            picture_re = re.findall(r'<meta\sitemprop="contentUrl"\scontent=".+\.((jpg)|(JPG))', response.text)
            # print("picture_re: ", picture_re)
            picture = ''
            for p in picture_re:
                picture += p.replace('<meta itemprop="contentUrl" content="', '').strip() + '; '
            item['picture'] = picture
            print("item['picture']: ", item['picture'])

            yield item
        except Exception as e:
            print("异常：", str(e))
            print("报错url：", response.url)
            with open('./error/'+item['city'] +'.txt', 'a+') as f:
                f.write(str(e) + "\n=====================" + item['url'] + "\n")

