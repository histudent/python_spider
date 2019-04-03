from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapymodule_Rent.clearSpace import clear_space, clear_lianxu_space
from scrapymodule_Rent.getItem import get_item
from scrapymodule_Rent.items import ScrapymoduleRentItem
import scrapy, re


class RentZooplaTest(CrawlSpider):
    name = 'rentZoopla'
    start_urls = ["https://www.zoopla.co.uk/to-rent/property/Bath?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Birmingham?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Bradford?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Hove?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Bristol?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Cambridge?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Canterbury?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Carlisle?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Chelmsford?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Chester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Chichester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Coventry?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Derby?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Durham?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Ely?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Exeter?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Gloucester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Hereford?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Kingston-upon-Hull?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Lancaster?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Leeds?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Leicester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Lichfield?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Lincoln?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Liverpool?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/City-of-London?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Manchester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Newcastle-upon-Tyne?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Norwich?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Nottingham?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Oxford?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Peterborough?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Plymouth?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Portsmouth?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Preston?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Ripon?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Salford?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Salisbury?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Sheffield?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Southampton?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/St-Albans?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Stoke-on-Trent?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Sunderland?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Truro?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Wakefield?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Wells?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Westminster?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Winchester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Wolverhampton?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/Worcester?identifier=bath&q=Bath&radius=0&page_size=100&pn=1",
"https://www.zoopla.co.uk/to-rent/property/York?identifier=bath&q=Bath&radius=0&page_size=100&pn=1", ]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='paginate bg-muted']/child::a[last()]")), follow=True, callback='parse_url'),
    )
    def parse_url(self, response):
        print("------------", response.url, "------------")
        city = response.xpath("//span[@class='maps-area-name']/b/text()").extract()
        # print(city)
        links = response.xpath("//div[@id='content']/ul[@class='listing-results clearfix js-gtm-list']/li/div[@class='listing-results-wrapper']/div[@class='listing-results-right clearfix']/a[@class='listing-results-price text-price']/@href").extract()
        # print(len(links))
        links = list(set(links))
        # print(len(links))
        for link in links:
            url = "https://www.zoopla.co.uk" + link
            yield scrapy.Request(url, callback=self.parse_data, meta={'city': ''.join(city)})

    def parse_data(self, response):
        item = get_item(ScrapymoduleRentItem)
        print("==========================================", response.url)
        item['country'] = 'England'
        item['url'] = response.url
        item['city'] = response.meta.get('city')
        print("item['city']: ", item['city'])
        try:
            '''   房源名称：2 bed flat to rent
                房源地址：Princes Court, Brompton Road SW3
                每周价格：£3,250
                每月价格：£3,250
                房源描述：Property description
                图片：照片
                房间设施：Property features
                平面图：Floorplan
                立即可租：Available immediately
                有家具：Furnished'''
            house_name = response.xpath("//h2[@class='listing-details-h1']//text()").extract()
            clear_space(house_name)
            item['house_name'] = ''.join(house_name).strip()
            print("item['house_name']: ", item['house_name'])

            detaile_address = response.xpath("//div[@class='listing-details-address']/h2//text()").extract()
            clear_space(detaile_address)
            item['detaile_address'] = ''.join(detaile_address).strip()
            print("item['detaile_address']: ", item['detaile_address'])

            price = response.xpath("//div[@class='listing-details-price text-price']//strong/span//text()").extract()
            clear_space(price)
            item['price'] = ''.join(price).replace('(', "").replace(')', '').strip()
            print("item['price']: ", item['price'])

            housing_introduce = response.xpath("//h3[contains(text(),'Property description')]/..//text()").extract()
            # clear_space(housing_introduce)
            item['housing_introduce'] = clear_lianxu_space(housing_introduce)
            # print("item['housing_introduce']: ", item['housing_introduce'])

            picture_re = re.findall(r'<meta\sproperty="og:image"\scontent=".+\.jpg', response.text)
            # print("picture_re: ", picture_re)
            picture = ''
            for p in picture_re:
                picture += p.replace('<meta property="og:image" content="', '').strip() + '; '
            item['picture'] = picture
            print("item['picture']: ", item['picture'])

            supporting_facilities = response.xpath("//h3[contains(text(),'Property features')]/..//text()").extract()
            # clear_space(supporting_facilities)
            item['supporting_facilities'] = clear_lianxu_space(supporting_facilities)
            # print("item['supporting_facilities']: ", item['supporting_facilities'])

            yield item
        except Exception as e:
            print("异常：", str(e))
            print("报错url：", response.url)
            with open('./error/'+item['city'] +'.txt', 'a+') as f:
                f.write(str(e) + "\n=====================" + item['url'] + "\n")

