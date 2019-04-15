from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapymodule_Rent.clearSpace import clear_space
from scrapymodule_Rent.getItem import get_item
from scrapymodule_Rent.items import ScrapymoduleRentItem
import scrapy
import json, math
import re
import requests
from lxml import etree

class RentAgencyTest(scrapy.Spider):
    name = 'rentAgency'
    start_urls = ["https://www.realestate.com.au/agency/korn-real-estate-campbelltown-rla-255949-ZWYBTV",
"https://www.realestate.com.au/agency/jj-real-estate-sa-leabrook-KSFYVV",
"https://www.realestate.com.au/agency/jinsea-real-estate-kent-town-CVEZXX",
"https://www.realestate.com.au/agency/harcourts-beyond-holland-park-XRHSTR",
"https://www.realestate.com.au/agent/christina-cheng-1411522",
"https://www.realestate.com.au/agency/h-t-brisbane-pty-ltd-brisbane-DQLBQV",
"https://www.realestate.com.au/agency/position-property-services-pty-POTPAD",
"https://www.realestate.com.au/agency/raine-horne-coorparoo-camp-hill-LWMTYY",
"https://www.realestate.com.au/agency/joy-realty-sunnybank-MWJYOA",
"https://www.realestate.com.au/agency/auston-realty-EACHRR",
"https://www.realestate.com.au/agency/jenny-yang-realty-brisbane-city-OMWDMS",
"https://www.realestate.com.au/agency/dpg-property-group-melbourne-CVUSUP",
"https://www.realestate.com.au/agency/hamilton-finley-box-hill-IJMZNK",
"https://www.realestate.com.au/agency/ironfish-real-estate-melbourne-TJCDWC",
"https://www.realestate.com.au/agency/lj-hooker-city-residential-melbourne-RIZTKO",
"https://www.realestate.com.au/agency/aussie-home-real-estate-kew-FEHCRQ",
"https://www.realestate.com.au/agency/justin-james-blackburn-NMAKBJ",
"https://www.realestate.com.au/agency/harcourts-mitcham-LAZDKX",
"https://www.realestate.com.au/agency/ivy-real-estate-docklands-docklands-RIUNYL",
"https://www.realestate.com.au/agency/paragon-real-estate-carlton-RLJTFB",
"https://www.realestate.com.au/agency/royaland-real-estate-melbourne-IJQZJB",
"https://www.realestate.com.au/agency/sweeney-estate-agents-footscray-SWFFOO",
"https://www.realestate.com.au/agency/stockdale-leggo-glen-waverley-XSLGWY",
"https://www.realestate.com.au/agency/matrix-global-melbourne-carlton-LIFYVY",
"https://www.realestate.com.au/agency/harcourts-clayton-XRWCLB",
"https://www.realestate.com.au/agency/wise-earth-property-group-melbourne-QDMMTD",
"https://www.realestate.com.au/agency/paramount-residential-GSHAGI",
"https://www.realestate.com.au/agency/international-equities-carlton-IECCAR",
"https://www.realestate.com.au/agency/ray-white-oakleigh-XRWOAK",
"https://www.realestate.com.au/agency/sea-city-nerang-NTSONF",
"https://www.realestate.com.au/agency/stage-property-east-perth-JUPGAB",
"https://www.realestate.com.au/agency/augurum-property-mt-hawthorn-VPZEJJ",
"https://www.realestate.com.au/agency/century-21-grand-alliance-perth-XRWXND",
"https://www.realestate.com.au/agency/blue-ocean-real-estate-sydney-DVSWJR",
"https://www.realestate.com.au/agency/rma-eastwood-eastwood-RMGCGK",
"https://www.realestate.com.au/agency/callagher-estate-agents-annandale-CAZANN",
"https://www.realestate.com.au/agency/elanda-partners-real-estate-sydney-ZPCAPO",
"https://www.realestate.com.au/agency/everest-realty-pty-ltd-chatswood-ZPCAGW",
"https://www.realestate.com.au/agency/pw-realty-sydney-ODKSDL",
"https://www.realestate.com.au/agency/jif-realty-RCWWKA/",
"https://www.realestate.com.au/agency/anc-real-estate-pyrmont-AIKLIF",
"https://www.realestate.com.au/agency/noble-investment-group-QKQIKF",
"https://www.realestate.com.au/agency/pg-mode-realty-haymarket-PGMHAY",
"https://www.realestate.com.au/agency/ghk-real-estate-NOHFQX",
"https://www.realestate.com.au/agency/sec-property-group-sydney-VPCZGA",
"https://www.realestate.com.au/agency/perfect-living-realty-PYYJPB",
"https://www.realestate.com.au/agency/dragon-australia-sydney-VAZVIJ",
"https://www.realestate.com.au/agency/lj-hooker-chinatown-XLJSYF",
"https://www.realestate.com.au/agency/black-diamondz-property-concierge-sydney-KMXVVK",
"https://www.realestate.com.au/agency/ray-white-residential-sydney-cbd-SOMAZG",
"https://www.realestate.com.au/agency/greencliff-agency-sydney-ABCSYT",
"https://www.realestate.com.au/agency/boutique-property-agents-sydney-GOJVRX",
"https://www.realestate.com.au/agency/century-21-city-quarter-sydney-PXDSHF",
"https://www.realestate.com.au/agency/obsidian-property-sydney-FWTIVL",
"https://www.realestate.com.au/agency/sydney-residential-metro-pty-ltd-sydney-SYVSYD",
"https://www.realestate.com.au/agency/metro-realty-AQFNMV",
"https://www.realestate.com.au/agency/sydney-cove-property-the-rocks-PUHSYD",
"https://www.realestate.com.au/agency/chidiac-realty-wentworth-point-RMRTVE",
"https://www.realestate.com.au/agency/grand-sydney-realty-ultimo-FKKDTB",
"https://www.realestate.com.au/agency/laingsimmons-cbd-surry-hills-sydney-PKNMVT",
"https://www.realestate.com.au/agency/laing-real-estate-elizabeth-bay-XLSELI",
"https://www.realestate.com.au/agency/property-square-realty-sydney-LKUEQQ", ]
    # start_urls = ['https://www.realestate.com.au/agency/sea-city-NTSONF/', "https://www.realestate.com.au/agency/jj-real-estate-sa-leabrook-KSFYVV"]
    # print(len(start_urls))
    # start_urls = list(set(start_urls))
    # print(len(start_urls))

    operatorDict = {'https://www.realestate.com.au/agency/sea-city-nerang-NTSONF': 'Sea & City Australia Investment Pty Ltd', 'https://www.realestate.com.au/agency/korn-real-estate-campbelltown-rla-255949-ZWYBTV': 'Korn Real Estate', 'https://www.realestate.com.au/agency/jj-real-estate-sa-leabrook-KSFYVV': 'JJ Real Estate', 'https://www.realestate.com.au/agency/jinsea-real-estate-kent-town-CVEZXX': 'Jin Sea Real Estate', 'https://www.realestate.com.au/agency/harcourts-beyond-holland-park-XRHSTR': 'Harcourts Beyond Sunnybank & Holland Park', 'https://www.realestate.com.au/agent/christina-cheng-1411522': 'Q&C Management Pty Ltd', 'https://www.realestate.com.au/agency/h-t-brisbane-pty-ltd-brisbane-DQLBQV': 'H&T Brisbane Pty Ltd - Brisbane', 'https://www.realestate.com.au/agency/position-property-services-pty-POTPAD': 'New Techcom Marketing Enterprises Pty Ltd', 'https://www.realestate.com.au/agency/raine-horne-coorparoo-camp-hill-LWMTYY': 'Raine&Horne Coorparoo', 'https://www.realestate.com.au/agency/joy-realty-sunnybank-MWJYOA': 'Joy Realty', 'https://www.realestate.com.au/agency/auston-realty-EACHRR': 'Auston Realty', 'https://www.realestate.com.au/agency/jenny-yang-realty-brisbane-city-OMWDMS': 'Jenny Yang Realty', 'https://www.realestate.com.au/agency/dpg-property-group-melbourne-CVUSUP': 'Dynasty Property', 'https://www.realestate.com.au/agency/hamilton-finley-box-hill-IJMZNK': 'Hamilton Finley Box Hill', 'https://www.realestate.com.au/agency/ironfish-real-estate-melbourne-TJCDWC': 'Ironfish Real Estate - MELBOURNE', 'https://www.realestate.com.au/agency/lj-hooker-city-residential-melbourne-RIZTKO': 'LJ Hooker City Residential', 'https://www.realestate.com.au/agency/aussie-home-real-estate-kew-FEHCRQ': 'Aussie Home', 'https://www.realestate.com.au/agency/justin-james-blackburn-NMAKBJ': 'Justin James Real Estate', 'https://www.realestate.com.au/agency/harcourts-mitcham-LAZDKX': 'Harcourts - Mitcham（City&Boxhill)', 'https://www.realestate.com.au/agency/ivy-real-estate-docklands-docklands-RIUNYL': 'Ivy Real Estate Docklands - DOCKLANDS', 'https://www.realestate.com.au/agency/paragon-real-estate-carlton-RLJTFB': 'Paragon Real Estate', 'https://www.realestate.com.au/agency/royaland-real-estate-melbourne-IJQZJB': 'Royaland', 'https://www.realestate.com.au/agency/sweeney-estate-agents-footscray-SWFFOO': 'Sweeney Estate', 'https://www.realestate.com.au/agency/stockdale-leggo-glen-waverley-XSLGWY': 'Stockdale & Leggo - Glen Waverley', 'https://www.realestate.com.au/agency/matrix-global-melbourne-carlton-LIFYVY': 'Matrix Global- Carlton', 'https://www.realestate.com.au/agency/harcourts-clayton-XRWCLB': 'Harcourts - Clayton', 'https://www.realestate.com.au/agency/wise-earth-property-group-melbourne-QDMMTD': 'Wise Earth', 'https://www.realestate.com.au/agency/paramount-residential-GSHAGI': 'Paramount Residential', 'https://www.realestate.com.au/agency/international-equities-carlton-IECCAR': 'International Equities - CARLTON', 'https://www.realestate.com.au/agency/ray-white-oakleigh-XRWOAK': 'Ray White - Oakleigh', 'https://www.realestate.com.au/agency/stage-property-east-perth-JUPGAB': 'Stage property', 'https://www.realestate.com.au/agency/augurum-property-mt-hawthorn-VPZEJJ': 'Augurum Property', 'https://www.realestate.com.au/agency/century-21-grand-alliance-perth-XRWXND': 'Century 21 Grand Alliance - PERTH', 'https://www.realestate.com.au/agency/blue-ocean-real-estate-sydney-DVSWJR': 'Blue Ocean Real Estate - Sydney', 'https://www.realestate.com.au/agency/rma-eastwood-eastwood-RMGCGK': 'RMA Real Estate', 'https://www.realestate.com.au/agency/callagher-estate-agents-annandale-CAZANN': 'Callagher Estate Agents', 'https://www.realestate.com.au/agency/elanda-partners-real-estate-sydney-ZPCAPO': 'Elanda Partners', 'https://www.realestate.com.au/agency/everest-realty-pty-ltd-chatswood-ZPCAGW': 'Everest Realty', 'https://www.realestate.com.au/agency/pw-realty-sydney-ODKSDL': 'PW Realty', 'https://www.realestate.com.au/agency/jif-realty-RCWWKA': 'JIF Group', 'https://www.realestate.com.au/agency/anc-real-estate-pyrmont-AIKLIF': 'ANC Real Estate - Pyrmont', 'https://www.realestate.com.au/agency/noble-investment-group-QKQIKF': 'Noble Investment Group（Sydney）', 'https://www.realestate.com.au/agency/pg-mode-realty-haymarket-PGMHAY': 'P&G Mode Realty', 'https://www.realestate.com.au/agency/ghk-real-estate-NOHFQX': 'GHK real estate P/L', 'https://www.realestate.com.au/agency/sec-property-group-sydney-VPCZGA': 'SEC property group', 'https://www.realestate.com.au/agency/perfect-living-realty-PYYJPB': 'Perfect Living Realty', 'https://www.realestate.com.au/agency/dragon-australia-sydney-VAZVIJ': 'Dragon Australia PTY Ltd.', 'https://www.realestate.com.au/agency/lj-hooker-chinatown-XLJSYF': 'LJ Hooker Chinatown', 'https://www.realestate.com.au/agency/black-diamondz-property-concierge-sydney-KMXVVK': 'Black Diamondz Property Concierge', 'https://www.realestate.com.au/agency/ray-white-residential-sydney-cbd-SOMAZG': 'Ray White Residential Sydney CBD', 'https://www.realestate.com.au/agency/greencliff-agency-sydney-ABCSYT': 'Greencliff Realty', 'https://www.realestate.com.au/agency/boutique-property-agents-sydney-GOJVRX': 'Boutique Property Agents', 'https://www.realestate.com.au/agency/century-21-city-quarter-sydney-PXDSHF': 'CENTURY 21 City Quarter', 'https://www.realestate.com.au/agency/obsidian-property-sydney-FWTIVL': 'Obsidian Property', 'https://www.realestate.com.au/agency/sydney-residential-metro-pty-ltd-sydney-SYVSYD': 'Sydney Residential\xa0Metro', 'https://www.realestate.com.au/agency/metro-realty-AQFNMV': 'Metro Realty', 'https://www.realestate.com.au/agency/sydney-cove-property-the-rocks-PUHSYD': 'Sydney Cove Property', 'https://www.realestate.com.au/agency/chidiac-realty-wentworth-point-RMRTVE': 'Chidiac Realty Sydney', 'https://www.realestate.com.au/agency/grand-sydney-realty-ultimo-FKKDTB': 'Grand Sydney Realty', 'https://www.realestate.com.au/agency/laingsimmons-cbd-surry-hills-sydney-PKNMVT': 'Laing+Simmons CBD Surry Hills', 'https://www.realestate.com.au/agency/laing-real-estate-elizabeth-bay-XLSELI': 'Laing Real Estate', 'https://www.realestate.com.au/agency/property-square-realty-sydney-LKUEQQ': 'Property Square'}
    cityDict = {'https://www.realestate.com.au/agency/sea-city-nerang-NTSONF': 'Melbourne&The gold coast',
                'https://www.realestate.com.au/agency/korn-real-estate-campbelltown-rla-255949-ZWYBTV': 'Adelaide',
                'https://www.realestate.com.au/agency/jj-real-estate-sa-leabrook-KSFYVV': 'Adelaide',
                'https://www.realestate.com.au/agency/jinsea-real-estate-kent-town-CVEZXX': 'Adelaide',
                'https://www.realestate.com.au/agency/harcourts-beyond-holland-park-XRHSTR': 'Brisbane',
                'https://www.realestate.com.au/agent/christina-cheng-1411522': 'Brisbane',
                'https://www.realestate.com.au/agency/h-t-brisbane-pty-ltd-brisbane-DQLBQV': 'Brisbane',
                'https://www.realestate.com.au/agency/position-property-services-pty-POTPAD': 'Brisbane',
                'https://www.realestate.com.au/agency/raine-horne-coorparoo-camp-hill-LWMTYY': 'Brisbane',
                'https://www.realestate.com.au/agency/joy-realty-sunnybank-MWJYOA': 'Brisbane',
                'https://www.realestate.com.au/agency/auston-realty-EACHRR': 'Brisbane',
                'https://www.realestate.com.au/agency/jenny-yang-realty-brisbane-city-OMWDMS': 'Brisbane',
                'https://www.realestate.com.au/agency/dpg-property-group-melbourne-CVUSUP': 'Melbourne',
                'https://www.realestate.com.au/agency/hamilton-finley-box-hill-IJMZNK': 'Melbourne',
                'https://www.realestate.com.au/agency/ironfish-real-estate-melbourne-TJCDWC': 'Melbourne',
                'https://www.realestate.com.au/agency/lj-hooker-city-residential-melbourne-RIZTKO': 'Melbourne',
                'https://www.realestate.com.au/agency/aussie-home-real-estate-kew-FEHCRQ': 'Melbourne',
                'https://www.realestate.com.au/agency/justin-james-blackburn-NMAKBJ': 'Melbourne',
                'https://www.realestate.com.au/agency/harcourts-mitcham-LAZDKX': 'Melbourne',
                'https://www.realestate.com.au/agency/ivy-real-estate-docklands-docklands-RIUNYL': 'Melbourne',
                'https://www.realestate.com.au/agency/paragon-real-estate-carlton-RLJTFB': 'Melbourne',
                'https://www.realestate.com.au/agency/royaland-real-estate-melbourne-IJQZJB': 'Melbourne',
                'https://www.realestate.com.au/agency/sweeney-estate-agents-footscray-SWFFOO': 'Melbourne',
                'https://www.realestate.com.au/agency/stockdale-leggo-glen-waverley-XSLGWY': 'Melbourne',
                'https://www.realestate.com.au/agency/matrix-global-melbourne-carlton-LIFYVY': 'Melbourne',
                'https://www.realestate.com.au/agency/harcourts-clayton-XRWCLB': 'Melbourne',
                'https://www.realestate.com.au/agency/wise-earth-property-group-melbourne-QDMMTD': 'Melbourne',
                'https://www.realestate.com.au/agency/paramount-residential-GSHAGI': 'Melbourne',
                'https://www.realestate.com.au/agency/international-equities-carlton-IECCAR': 'Melbourne',
                'https://www.realestate.com.au/agency/ray-white-oakleigh-XRWOAK': 'Melbourne',
                'https://www.realestate.com.au/agency/stage-property-east-perth-JUPGAB': 'Perth',
                'https://www.realestate.com.au/agency/augurum-property-mt-hawthorn-VPZEJJ': 'Perth',
                'https://www.realestate.com.au/agency/century-21-grand-alliance-perth-XRWXND': 'Perth',
                'https://www.realestate.com.au/agency/blue-ocean-real-estate-sydney-DVSWJR': 'Sydney',
                'https://www.realestate.com.au/agency/rma-eastwood-eastwood-RMGCGK': 'Sydney',
                'https://www.realestate.com.au/agency/callagher-estate-agents-annandale-CAZANN': 'Sydney',
                'https://www.realestate.com.au/agency/elanda-partners-real-estate-sydney-ZPCAPO': 'Sydney',
                'https://www.realestate.com.au/agency/everest-realty-pty-ltd-chatswood-ZPCAGW': 'Sydney',
                'https://www.realestate.com.au/agency/pw-realty-sydney-ODKSDL': 'Sydney',
                'https://www.realestate.com.au/agency/jif-realty-RCWWKA': 'Sydney',
                'https://www.realestate.com.au/agency/anc-real-estate-pyrmont-AIKLIF': 'Sydney',
                'https://www.realestate.com.au/agency/noble-investment-group-QKQIKF': 'Sydney',
                'https://www.realestate.com.au/agency/pg-mode-realty-haymarket-PGMHAY': 'Sydney',
                'https://www.realestate.com.au/agency/ghk-real-estate-NOHFQX': 'Sydney',
                'https://www.realestate.com.au/agency/sec-property-group-sydney-VPCZGA': 'Sydney',
                'https://www.realestate.com.au/agency/perfect-living-realty-PYYJPB': 'Sydney',
                'https://www.realestate.com.au/agency/dragon-australia-sydney-VAZVIJ': 'Sydney',
                'https://www.realestate.com.au/agency/lj-hooker-chinatown-XLJSYF': 'Sydney',
                'https://www.realestate.com.au/agency/black-diamondz-property-concierge-sydney-KMXVVK': 'Sydney',
                'https://www.realestate.com.au/agency/ray-white-residential-sydney-cbd-SOMAZG': 'Sydney',
                'https://www.realestate.com.au/agency/greencliff-agency-sydney-ABCSYT': 'Sydney',
                'https://www.realestate.com.au/agency/boutique-property-agents-sydney-GOJVRX': 'Sydney',
                'https://www.realestate.com.au/agency/century-21-city-quarter-sydney-PXDSHF': 'Sydney',
                'https://www.realestate.com.au/agency/obsidian-property-sydney-FWTIVL': 'Sydney',
                'https://www.realestate.com.au/agency/sydney-residential-metro-pty-ltd-sydney-SYVSYD': 'Sydney',
                'https://www.realestate.com.au/agency/metro-realty-AQFNMV': 'Sydney',
                'https://www.realestate.com.au/agency/sydney-cove-property-the-rocks-PUHSYD': 'Sydney',
                'https://www.realestate.com.au/agency/chidiac-realty-wentworth-point-RMRTVE': 'Sydney',
                'https://www.realestate.com.au/agency/grand-sydney-realty-ultimo-FKKDTB': 'Sydney',
                'https://www.realestate.com.au/agency/laingsimmons-cbd-surry-hills-sydney-PKNMVT': 'Sydney',
                'https://www.realestate.com.au/agency/laing-real-estate-elizabeth-bay-XLSELI': 'Sydney',
                'https://www.realestate.com.au/agency/property-square-realty-sydney-LKUEQQ': 'Sydney'}

    def parse(self, response):
        print("---", response.url)
        # https://services.realestate.com.au/services/listings/search?query={%22channel%22:%22rent%22,%22page%22:1,%22pageSize%22:12,%22filters%22:{%22agencyIds%22:[%22KSFYVV%22]}}
        # 取得链接最后一个后缀
        templink = response.url.split("-")
        # print(templink[-1])
        page = 1
        url = "https://services.realestate.com.au/services/listings/search?query={%22channel%22:%22rent%22,%22page%22:"+ str(page) +",%22pageSize%22:12,%22filters%22:{%22agencyIds%22:[%22"+templink[-1]+"%22]}}"
        # 供应商名称和对应的城市
        operator = self.operatorDict.get(response.url.strip())
        city = self.cityDict.get(response.url.strip())
        print("operator = ", operator)
        print("city = ", city, "\n===========================")
        yield scrapy.Request(url, callback=self.parse_json, meta={"last": templink[-1], "supplier_name": operator, "city": city})

    # 获得第一页的租房信息列表链接  获得该供应商租房信息的总数量
    def parse_json(self, response):
        urljson = json.loads(response.body)
        # print("urljson: ", urljson)
        totalcount = urljson.get("totalResultsCount")
        print("totalcount: ", totalcount, "--", response.url)
        # 获取供应商名称和城市
        supplier_name= response.meta.get("supplier_name")
        city = response.meta.get("city")
        # 先获取第一页租房信息列表链接
        if totalcount > 0:
            urllinks = urljson.get("tieredResults")[0].get("results")
            for results in urllinks:
                rentUrl = results.get("prettyUrl")
                # print("rentUrl", rentUrl)
                url = "https://www.realestate.com.au/" + rentUrl
                # self.testdetail(url)
                item = get_item(ScrapymoduleRentItem)
                item['supplier_name'] = supplier_name
                item['city'] = city
                self.test(url, item)
                yield item
        # 获得API的后缀参数
        last = response.meta.get("last")
        page = totalcount / 12
        if page.is_integer():
            page = int(page)
            print("page: ", page)
        else:
            page = math.ceil(page)
            print("tmppage: ", page)
        for p in range(1, page + 1):
            url = "https://services.realestate.com.au/services/listings/search?query={%22channel%22:%22rent%22,%22page%22:" + str(
                p) + ",%22pageSize%22:12,%22filters%22:{%22agencyIds%22:[%22" + last + "%22]}}"
            # print(url)
            yield scrapy.Request(url, callback=self.parse_json_url, meta={"supplier_name": supplier_name, "city": city})

    # 获取第二页开始之后的租房列表详情页链接
    def parse_json_url(self, response):
        urldetailejson = json.loads(response.body)
        # print("urldetailejson: ", urldetailejson)
        urllinks = urldetailejson.get("tieredResults")[0].get("results")
        for results in urllinks:
            rentUrl = results.get("prettyUrl")
            # print("rentUrl2", rentUrl)
            url = "https://www.realestate.com.au/" + rentUrl
            # self.testdetail(url)
            item = get_item(ScrapymoduleRentItem)
            item['supplier_name'] = response.meta.get("supplier_name")
            item['city'] = response.meta.get("city")
            self.test(url, item)
            yield item

    def test(self, url, item):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        data = requests.get(url, headers=headers)
        response = etree.HTML(data.text)
        item['country'] = 'Australia'
        # item['city'] = 'Adelaide'
        # item['supplier_name'] = 'Korn Real Estate'
        item['url'] = url
        # print("===========================")
        # print(url)
        # print("item['city']", item['city'])
        # print("item['supplier_name']", item['supplier_name'])
        try:
            # housing_type
            housing_type = response.xpath(
                "//div[@id='listing_info']/ul[@class='info']/li[@class='property_info']/span[@class='propertyType']//text()")
            clear_space(housing_type)
            item['housing_type'] = ''.join(housing_type)
            # print("item['housing_type']: ", item['housing_type'])

            # available_time
            available_time = response.xpath(
                "//div[@id='listing_info_secondary']/div[@class='available_date']/span//text()")
            clear_space(available_time)
            # print("available_time: ", available_time)
            available_timeDict = {"Jan": "01",
                                    "Feb": "02",
                                    "Mar": "03",
                                    "Apr": "04",
                                    "May": "05",
                                    "Jun": "06",
                                    "Jul": "07",
                                    "Aug": "08",
                                    "Sep": "09",
                                    "Oct": "10",
                                    "Nov": "11",
                                    "Dec": "12",}
            if available_time[0] == "Available Now":
                item['available_time'] = 'now'
            else:
                available_timetmp = available_time[0].split(" ")[-1]
                # print(available_timetmp)
                available_timetmp1 = available_timetmp.split("-")
                # print("available_timetmp1: ====", available_timetmp1)
                available_timeResult = "20" + available_timetmp1[-1] + "-" + available_timeDict[available_timetmp1[1]] + "-" + available_timetmp1[0]
                item['available_time'] = available_timeResult
            # print("item['available_time']: ", item['available_time'])

            # house_name    //span[@itemprop='streetAddress']
            # house_name = response.xpath(
            #     "//div[@id='description']/p[@class='title']//text()").extract()
            house_name = response.xpath(
                "//span[@itemprop='streetAddress']//text()")
            clear_space(house_name)
            item['house_name'] = ''.join(house_name)
            # print("item['house_name']: ", item['house_name'])

            # room_type
            room_typeCarspaces = response.xpath(
                "//div[@id='features']/div/div[@class='featureList']/ul[1]/li//text()")
            clear_space(room_typeCarspaces)
            # print("room_typeCarspaces: ", room_typeCarspaces)
            if "Bond:" in room_typeCarspaces:
                depositIndex = room_typeCarspaces.index("Bond:")
                deposit = room_typeCarspaces[depositIndex+1]
                item['deposit'] = deposit
            # print("item['deposit']: ", item['deposit'])

            if item['housing_type'] == "Studio":
                item['room_type'] = 'Studio'
            else:
                room_type = ''
                if "Bedrooms:" in room_typeCarspaces:
                    room_typeIndex1 = room_typeCarspaces.index("Bedrooms:")
                    room_type1 = room_typeCarspaces[room_typeIndex1+1]
                    room_type = room_type1
                if "Bathrooms:" in room_typeCarspaces:
                    room_typeIndex2 = room_typeCarspaces.index("Bathrooms:")
                    room_type2 = room_typeCarspaces[room_typeIndex2+1]
                    room_type = room_type + "-" + room_type2
                item['room_type'] = room_type
            # print("item['room_type']: ", item['room_type'])

            if "Garage Spaces:" in room_typeCarspaces:
                carIndex = room_typeCarspaces.index("Garage Spaces:")
                item['car_spaces'] = room_typeCarspaces[carIndex+1]
            elif "Open Car Spaces:" in room_typeCarspaces:
                carIndex = room_typeCarspaces.index("Open Car Spaces:")
                item['car_spaces'] = room_typeCarspaces[carIndex+1]
            # print("item['car_spaces']: ", item['car_spaces'])


            # lease
            # address
            address = response.xpath(
                "//div[@id='listing_address']/h1/span[@class='detail-address']//text()")
            clear_space(address)
            item['address'] = ','.join(address)
            # print("item['address']: ", item['address'])

            # detaile_address   //div[@id='description']/h3[@class='address']
            detaile_address = response.xpath(
                "//div[@id='description']/h3[@class='address']//text()")
            clear_space(detaile_address)
            item['detaile_address'] = ''.join(detaile_address)
            # print("item['detaile_address']: ", item['detaile_address'])

            opentime = response.xpath("//a[@itemprop='events']//text()")
            opentime = ' '.join(opentime)
            if len(opentime) != 0:
                opentimePrefixx = response.xpath("//div[@id='inspectionTimes']/h3//text()")
                clear_space(opentimePrefixx)
                opentime = ''.join(opentimePrefixx) + opentime
            # print("opentime: ", opentime)
            # supporting_facilities
            housing_introduce = response.xpath(
                "//div[@id='description']/p[@class='body']//text()")
            # //div[@id='description']/p[@class='body']//span/@data-description
            housing_introduce1 = response.xpath(
                "//div[@id='description']/p[@class='body']//span/@data-description")
            # print("housing_introduce1===========: ", housing_introduce1)
            # if '<span data-description="' in housing_introduce:
            #     housing_introduce = ''.join(housing_introduce.split('<span data-description="'))
            #     housing_introduce = ''.join(housing_introduce.split('">...</span>'))
            #     aIndex = housing_introduce.find("<a")
            #     housing_introduce = housing_introduce[:aIndex]
            housing_introduce = opentime + "\n" + '\n'.join(housing_introduce).strip().strip("show more").strip().strip("...") + ''.join(housing_introduce1).replace("<br>", "")
            # 去掉房源介绍中的电话号码
            phonem = re.findall(r"[\d\s]{10,13}", housing_introduce)
            phonem = ''.join(phonem)
            phonem1 = re.findall(r"\d{2}-\d{8}", housing_introduce)
            phonem1 = ''.join(phonem1)
            # print(phonem+" ---- "+phonem1)
            housing_introduce = housing_introduce.replace(phonem, "").replace(phonem1, "")
            item['housing_introduce'] = housing_introduce
            # print("item['housing_introduce']: ", item['housing_introduce'])

            # price
            price = response.xpath(
                "//div[@id='listing_info']/ul[@class='info']/li[@class='price']/p[@class='priceText']//text()")
            clear_space(price)
            item['price'] = ''.join(price)
            # print("item['price']: ", item['price'])

            # isRent
            # postal_code
            # picture
            pictureJs = response.xpath("//script//text()")
            # print("pictureJs: ", pictureJs)
            pictureJsStr = ''.join(pictureJs)
            pictureSrc = re.findall(r'{src:\"[\w\/\.]*jpg\"', pictureJsStr)
            # print("pictureSrc:========== ", pictureSrc)
            # print(len(pictureSrc))
            for index in range(len(pictureSrc)):
                pictureSrc[index] = pictureSrc[index].strip('{src:').strip('"')
                pictureSrc[index] = "https://i3.au.reastatic.net/800x600-resize,extend,r=33,g=40,b=46" + pictureSrc[index]
            # print("pictureSrc:==========11 ", pictureSrc)
            item['picture'] = ';'.join(pictureSrc)
            # print("item['picture']: ", item['picture'])

            # housing_introduce
            # supplier_type
            # supplier_name
            # supplier_name = response.xpath(
            #     "//div[@id='agentInfoExpanded']/div/a/img[@class='logo']/@alt|//div[@id='agentInfoExpanded']/div[1]/text()")
            # clear_space(supplier_name)
            # item['supplier_name'] = ''.join(supplier_name)
            # print("item['supplier_name']: ", item['supplier_name'])

            # supplier_logo //div[@class='branding-banner-content']/a/img[@class='logo']/@src
            supplier_logo = response.xpath(
                "//div[@id='agentInfoExpanded']/div/a/img[@class='logo']/@src")
            clear_space(supplier_logo)
            item['supplier_logo'] = ''.join(supplier_logo)
            # print("item['supplier_logo']: ", item['supplier_logo'])

            # contact_name
            contact_name = response.xpath(
                "//div[@class='agentContactInfo'][1]/p//text()")
            clear_space(contact_name)
            if len(contact_name) != 0:
                item['contact_name'] = contact_name[0]
            # print("item['contact_name']: ", item['contact_name'])

            # contact_phone
            contact_phone = response.xpath(
                "//div[@class='agentContactInfo']/ul/li/text()")
            clear_space(contact_phone)
            if len(contact_phone) != 0:
                item['contact_phone'] = contact_phone[0]
            # print("item['contact_phone']: ", item['contact_phone'])

            # contact_email

            # print(item)
            # yield item
        except Exception as e:
            with open("./error/"+item['supplier_name']+".txt", 'a', encoding="utf-8") as f:
                f.write(str(e) + "\n" + url + "\n========================\n")
            print("异常：", str(e))
            print("报错url：", url)
