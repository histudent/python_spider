from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapymodule_Rent.clearSpace import clear_space, clear_lianxu_space
from scrapymodule_Rent.getItem import get_item
from scrapymodule_Rent.items import ScrapymoduleRentItem
import scrapy, re


class RentCityRoomRentalsTest(scrapy.Spider):
    name = 'rentCityRoomRentals'
    start_urls = ["https://www.cityroomrentals.co.uk/?s=&city=Manchester&_available_start_date=&_available_end_date=&property_type=&bedrooms=&guests="]
    # print(len(start_urls))
    start_urls = list(set(start_urls))
    # print(len(start_urls))


    def parse(self, response):
        # print("------------", response.url, "------------")
        keys = response.xpath("//select[@id='sidebar-city']/option//text()").extract()
        # print(keys)
        # print(len(keys))
        for key in keys:
            # print(key)
            city = key
            if ' ' in key:
                key = key.split(' ')
                # print('+'.join(key), "====")
                key = '+'.join(key)
            url = response.url.replace('city=Manchester', 'city='+key)
            # print("url = ", url)
            yield scrapy.Request(url, callback=self.parse_url, meta={'city': city})

    def parse_url(self, response):
        # print("***************")
        urls = response.xpath('//html//div[@class="overview-property-container"]/div[1]/div[2]//a/@href').extract()
        # print("====", len(urls))
        urls = list(set(urls))
        # print("=====", len(urls))
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_data, meta={'city': response.meta.get('city')})

    def parse_data(self, response):
        item = get_item(ScrapymoduleRentItem)
        print("==========================================", response.url)
        item['country'] = 'England'
        item['city'] = response.meta.get('city')
        print("item['city']: ", item['city'])
        item['url'] = response.url
        try:
            '''   房源名称：CRESCENT PLACE
                房租：FROM: £ 134.00 WEEKLY
                设施：FEATURES
                房源描述：Description
                位置：63 St Mary's Road
                房型名称：8 BEDROOM SHARED HOUSE ROOM
                起租时间：AVAILABLE FROM 01/08/2018
                租期：TENANCY LENGTH 45 and 51 week'''
            house_name = response.xpath("//div[@class='col-sm-8']/h1//text()").extract()
            clear_space(house_name)
            item['house_name'] = ''.join(house_name).strip()
            print("item['house_name']: ", item['house_name'])

            supporting_facilities = response.xpath("//div[@class='property-features']//text()").extract()
            # clear_space(supporting_facilities)
            item['supporting_facilities'] = clear_lianxu_space(supporting_facilities)
            # print("item['supporting_facilities']: ", item['supporting_facilities'])

            housing_introduce = response.xpath("//div[@id='property-description']//text()").extract()
            clear_space(housing_introduce)
            item['housing_introduce'] = '\n'.join(housing_introduce).strip()
            # print("item['housing_introduce']: ", item['housing_introduce'])

            detaile_address = response.xpath("//i[@class='fa fa-map-marker']/../text()").extract()
            clear_space(detaile_address)
            item['detaile_address'] = ''.join(detaile_address).strip()
            print("item['detaile_address']: ", item['detaile_address'])

            picture_list = response.xpath("//div/div[1]/div[1]/img[1]/@src").extract()
            # print("picture_list: ", picture_list)
            for p in picture_list:
                item['picture'] += p + "; "
            print("item['picture']: ", item['picture'])

            # 房间分为长期出租、短期出租、学生房间    主要以下字段不一样：价格、起租时间、租期、房源类型、房间类型
            # 长期出租
            long_term = response.xpath('//div[@id="property-rooms"]//text()').extract()
            # 短期出租
            short_term = response.xpath("//div[@id='short-term-rooms']/div[@class='room-wrapper']").extract()
            # print("short_term: ", short_term)
            # 学生房间
            student_room = response.xpath('//div[@id="property-student-rooms"]/div[@class="room-wrapper"]').extract()
            if len(long_term) != 0:
                print("==============长期出租")
                price = response.xpath("//div[@id='property-rooms']//div[@class='room-wrapper']//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-5']//text()").extract()
                clear_space(price)
                item['price'] = ' '.join(price).replace('From:', "").strip()
                print("item['price']: ", item['price'])

                available_time = response.xpath('//div[@id="property-rooms"]//div[@class="room-wrapper"]//div[@class="row"]//div[@class="medium-gray-background clearfix"]//div[@class="col-sm-4"]//ul[@class="room-features-list list-unstyled"]//li[@class="room-feature"]/h5[contains(text(),"Available From")]/../following-sibling::li[1]//text()').extract()
                clear_space(available_time)
                available_time = ''.join(available_time).split('/')
                # print(available_time)
                item['available_time'] = available_time[-1] + "-" + available_time[1] + "-" + available_time[0]
                print("item['available_time']: ", item['available_time'])

                # lease = response.xpath("//i[@class='fa fa-map-marker']/../text()").extract()
                # clear_space(lease)
                item['lease'] = 'Long Term'
                print("item['lease']: ", item['lease'])

                housing_type = response.xpath("//div[@id='property-rooms']//div[@class='room-wrapper']//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-3']/h5//text()").extract()
                clear_space(housing_type)
                item['housing_type'] = ''.join(housing_type).strip()
                print("item['housing_type']: ", item['housing_type'])
                yield item

            if len(short_term) != 0:
                print("==============短期出租")
                for div_n in range(1, len(short_term)+1):
                    price = response.xpath(
                        "//div[@id='short-term-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-5']//text()").extract()
                    clear_space(price)
                    item['price'] = ' '.join(price).replace('From:', "").strip()
                    print("item['price']: ", item['price'])

                    available_time = response.xpath(
                        "//div[@id='short-term-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-4']/ul/li[2]//text()").extract()
                    clear_space(available_time)
                    available_time = ''.join(available_time).split('/')
                    # print("available_time ",available_time)
                    item['available_time'] = available_time[-1] + "-" + available_time[1] + "-" + available_time[0]
                    print("item['available_time']: ", item['available_time'])

                    # lease = response.xpath("//i[@class='fa fa-map-marker']/../text()").extract()
                    # clear_space(lease)
                    item['lease'] = 'Short Term'
                    # print("item['lease']: ", item['lease'])

                    housing_type = response.xpath(
                        "//div[@id='short-term-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-3']/h6//text()").extract()
                    clear_space(housing_type)
                    item['housing_type'] = ''.join(housing_type).strip()
                    print("item['housing_type']: ", item['housing_type'])

                    room_type = response.xpath(
                        "//div[@id='short-term-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-3']/h5//text()").extract()
                    clear_space(room_type)
                    item['room_type'] = ''.join(room_type).strip()
                    print("item['room_type']: ", item['room_type'])
                    yield item

            if len(student_room) != 0:
                print("==============学生房间")
                for div_n in range(1, len(student_room)+1):
                    print("***************第" + str(div_n) + "房***************")
                    price = response.xpath(
                        "//div[@id='property-student-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-5']//text()").extract()
                    clear_space(price)
                    item['price'] = ' '.join(price).replace('From:', "").strip()
                    print("item['price']: ", item['price'])

                    available_time = response.xpath(
                        "//div[@id='property-student-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-4']/ul/li[2]//text()").extract()
                    clear_space(available_time)
                    available_time = ''.join(available_time).split('/')
                    # print("available_time ",available_time)
                    item['available_time'] = available_time[-1] + "-" + available_time[1] + "-" + available_time[0]
                    print("item['available_time']: ", item['available_time'])

                    lease = response.xpath("//div[@id='property-student-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-4']/ul/li[6]/text()").extract()
                    clear_space(lease)
                    item['lease'] = ''.join(lease).strip()
                    print("item['lease']: ", item['lease'])

                    housing_type = response.xpath(
                        "//div[@id='property-student-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-3']/h6//text()").extract()
                    clear_space(housing_type)
                    item['housing_type'] = ''.join(housing_type).strip()
                    print("item['housing_type']: ", item['housing_type'])

                    room_type = response.xpath(
                        "//div[@id='property-student-rooms']//div[@class='room-wrapper']["+str(div_n)+"]//div[@class='row']//div[@class='medium-gray-background clearfix']//div[@class='col-sm-3']/h5//text()").extract()
                    clear_space(room_type)
                    item['room_type'] = ''.join(room_type).strip()
                    print("item['room_type']: ", item['room_type'])
                    yield item

        except Exception as e:
            print("异常：", str(e))
            print("报错url：", response.url)
            # with open('../error/'+item['city'] +'.txt', 'a+') as f:
            #     f.write(str(e) + "\n=====================" + item['url'] + "\n")

