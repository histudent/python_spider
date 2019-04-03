# -*- coding: utf-8 -*-
import scrapy
from scrapySchool_England_U.middlewares import *
from scrapySchool_England_U.items import ScrapyschoolEnglandItem
from urllib.request import urlopen

class DurhamuniversityUSpider(scrapy.Spider):
    name = 'DurhamUniversity_U'
    allowed_domains = ['dur.ac.uk']
    start_urls = ['https://www.dur.ac.uk/courses/all/']

    def parse(self, response):
        urls=['https://www.dur.ac.uk/courses/info/?id=12479&title=Business+and+Management+with+Business+Placement&code=N203&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12240&title=Biological+Sciences&code=C103&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16836&title=Theology+and+Religion+Foundation&code=V616&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12397&title=Theology+and+Religion&code=V614&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11864&title=Sociology+with+Foundation&code=L301&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12288&title=Sport%2C+Exercise+and+Physical+Activity+with+Foundation&code=C604&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12286&title=Sport%2C+Exercise+and+Physical+Activity&code=C603&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11572&title=Sociology&code=L300&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=17140&title=Religion%2C+Society+and+Culture+%28With+Year+Abroad%29&code=V618&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=17139&title=Religion%2C+Society+and+Culture&code=V617&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11593&title=Psychology&code=C800&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12302&title=Archaeology+with+Foundation&code=F403&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16861&title=Psychology+with+Foundation&code=C819&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Anthropology+and+Biology&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12448&title=Politics+with+Year+Abroad&code=L202&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12355&title=Anthropology+with+Foundation&code=L608&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11894&title=Politics+with+Foundation&code=L201&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11671&title=Archaeology+and+Ancient+Civilisations&code=VQ48&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11778&title=Philosophy%2C+Politics+and+Economics&code=VL52&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11879&title=Archaeology+with+Foundation&code=V400&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11602&title=Physics&code=F300&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Anthropology+and+Psychology&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11659&title=Philosophy+and+Politics&code=LV25&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11603&title=Archaeology&code=F400&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11663&title=Philosophy+and+Psychology&code=CV85&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11727&title=Politics&code=L200&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11607&title=Archaeology&code=F402&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11638&title=Philosophy+with+Foundation&code=V501&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12207&title=Anthropology+with+Foundation&code=L603&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11987&title=Physics+with+Foundation&code=F302&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11540&title=Anthropology+and+Sociology&code=LL36&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11734&title=Philosophy+and+Theology&code=VV56&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11537&title=Anthropology+and+Archaeology&code=LF64&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11632&title=Philosophy&code=V500&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12204&title=Anthropology&code=L601&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Psychology+and+Economics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11576&title=Anthropology&code=L602&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11525&title=Ancient%2C+Medieval+and+Modern+History&code=V101&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11533&title=Ancient+History+and+Archaeology&code=VF14&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11528&title=Ancient+History&code=V110&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Philosophy+and+Physics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12226&title=Accounting+and+Finance+with+Study+Abroad&code=N304&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12464&title=Accounting+and+Finance+with+Business+Placement&code=N302&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12470&title=Accounting+and+Management+with+Business+Placement&code=N204&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12202&title=Accounting+and+Management&code=NN42&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11799&title=Accounting+and+Finance&code=NN43&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11868&title=Accounting+and+Finance+with+Foundation&code=NN4H&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12222&title=Accounting+and+Management+with+Study+Abroad&code=N206&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12316&title=Accounting+and+Management+with+Foundation&code=N209&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Mathematics+and+Physics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Natural+Sciences&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12405&title=Music+with+Foundation&code=W301&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Mathematics+and+Psychology&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Mathematics+and+Philosophy&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11535&title=Music&code=W300&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12441&title=Modern+European+Languages+and+History+with+Year+Abroad&code=RV92&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12298&title=Mathematics+with+Foundation&code=G107&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16659&title=Marketing+and+Management+with+Study+Abroad&code=N511&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11549&title=Mathematics&code=G100&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12374&title=Modern+Languages+and+Cultures+with+Year+Abroad&code=R002&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12265&title=Music+and+Philosophy&code=WV53&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16834&title=Marketing+and+Management+with+Foundation&code=N512&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16663&title=Marketing+and+Management+with+Business+Placement&code=N510&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16655&title=Marketing+and+Management&code=N509&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11731&title=Law&code=M101&type=LLB&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11816&code=FF3N',
'https://www.dur.ac.uk/courses/info/?id=12213&code=F644',
'https://www.dur.ac.uk/courses/info/?id=11553&title=Mathematics',
'https://www.dur.ac.uk/courses/info/?id=11814&code=F344',
'https://www.dur.ac.uk/courses/info/?id=12358&title=Liberal+Arts&code=LA01&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11811&code=F301',
'https://www.dur.ac.uk/courses/info/?id=12276&title=Liberal+Arts+with+Foundation&code=LA00&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12279&title=Japanese+Studies+%28with+Year+Abroad%29+with+Foundation&code=T203&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12144&title=International+Relations&code=L250&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12238&title=Japanese+Studies+with+Year+Abroad&code=T202&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12299&title=History+with+Foundation&code=V102&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11522&title=History&code=V100&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11586&title=Health+and+Human+Sciences&code=B991&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11861&title=Health+and+Human+Sciences+with+Foundation&code=L691&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Geography+and+Mathematics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12211&title=Geoscience&code=F643&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11684&title=Geophysics+with+Geology&code=F662&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11872&title=Geology+with+Foundation&code=F602&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11610&title=Geology&code=F600&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Geography+and+Psychology&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11900&title=Geography+with+Foundation&code=F801&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Geography+and+Earth+Sciences&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11619&title=Geography&code=F800&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11876&title=General+Engineering+with+Foundation&code=H104&type=BENG&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11651&title=Geography+with+Foundation&code=L700&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11624&title=Geography&code=L702&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12506&title=Finance+with+Foundation&code=N308&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12321&title=Finance+with+Study+Abroad&code=N307&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12325&title=Finance+with+Business+Placement&code=N306&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12319&title=Finance&code=N305&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11875&title=Primary+Education+with+Foundation&code=X120&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12135&title=Primary+Education&code=X101&type=BAE&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Earth+Sciences+and+Mathematics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Economics+and+Psychology&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Economics+and+Mathematics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11876&title=Engineering+with+Foundation&code=H104&type=BENG&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11499&title=General+Engineering&code=H103&type=BENG&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12193&title=English+with+Foundation&code=Q301&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16337&title=Education+Studies+-+Theology+and+Religion&code=X1V6&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11614&title=Environmental+Geoscience&code=F630&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12253&title=Education+Studies+with+Foundation&code=X301&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11643&title=Education+Studies+-+Sociology&code=XL33&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11547&title=English+Literature&code=Q300&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11780&title=Education+Studies+-+Psychology&code=X1C8&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11772&title=Education+Studies+-+English+Studies&code=X1Q3&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11749&title=Education+Studies+-+Philosophy&code=XV35&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11515&title=English+Literature+and+History&code=QV21&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11622&title=English+Literature+and+Philosophy&code=QV35&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11775&title=Education+Studies+-+History&code=X1V1&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11679&title=Education+Studies+-+Geography&code=X1F8&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11681&title=Education+Studies+-+Music&code=X1W3&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12478&title=Economics+with+Study+Abroad&code=L109&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12413&title=Economics+with+Management+with+Study+Abroad&code=L105&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12421&title=Economics+with+Management+with+Business+Placement&code=L104&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12422&title=Economics+with+Management&code=L103&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11568&title=Economics+with+French&code=L1R1&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11649&title=Economics+with+Foundation&code=L101&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12487&title=Economics+with+Business+Placement&code=L106&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11740&title=Economics+and+Politics&code=LL12&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11562&title=Economics&code=L100&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Chemistry+and+Physics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Computer+Science+and+Physics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Chemistry+and+Mathematics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Computer+Science+and+Mathematics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Chemistry+and+Earth+Sciences&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11882&title=Criminology+with+Foundation&code=L372&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11821&title=Criminology&code=L370&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11886&title=Computer+Science+with+Foundation&code=G402&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11508&title=Computer+Science&code=G400&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11995&title=Combined+Honours+in+Social+Sciences+with+Foundation&code=LV00&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11627&title=Combined+Honours+in+Social+Sciences&code=LMV0&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11997&title=Chemistry+with+Foundation&code=F103&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12274&title=Chinese+Studies+%28with+Year+Abroad%29+with+Foundation&code=T103&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11598&title=Chemistry&code=F100&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=16174&title=Classical+Civilisation&code=Q820&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12259&title=Chinese+Studies+with+Year+Abroad&code=T102&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11787&title=Classics&code=Q801&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12407&title=Classics+with+Foundation&code=Q805&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Business+and+Computer+Science&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Biology+and+Psychology&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Biology+and+Physics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Biology+and+Mathematics&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Biology+and+Earth+Sciences&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Biology+and+Geography&code=CFG0&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12292&title=Business+and+Management+with+Foundation&code=NN21&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12293&title=Biological+Sciences+with+Foundation&code=C104&type=BSC&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12331&title=Business+and+Management&code=N201&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=12220&title=Business+and+Management+with+Study+Abroad&code=N207&type=BA&year=2019',
'https://www.dur.ac.uk/courses/info/?id=11725&title=Biology+and+Chemistry&code=CFG0&type=BSC&year=2019',]
        urls=set(urls)
        for u in urls:
            yield scrapy.Request(u,callback=self.parses,meta={'url':u})
    def parses(self,response):
        item=get_item1(ScrapyschoolEnglandItem)
        item['url']=response.meta['url']
        item['university']='Durham University'

        alevel=response.xpath('//div[@id="admissions"]/*').extract()
        # print(alevel)
        h3bq=response.xpath('//h3[contains(text(),"English Language requirements")]/self::*').extract()
        # print(h3bq)
        if ''.join(h3bq) in alevel:
            alevel=alevel[0:alevel.index(''.join(h3bq))]
            print(alevel)
        else:
            print('rong')
        item['alevel']=remove_class(alevel)
        yield item

    # def parse(self, response):
    #     programme_url = response.xpath('//table[@class="courses"]//a/@href').extract()
    #     for i in programme_url:
    #         fullurl = 'https://www.dur.ac.uk' + i
    #         yield scrapy.Request(fullurl, callback=self.parses)
    # def parses(self, response):
    #     print(response.url)
    #     item = get_item1(ScrapyschoolEnglandItem)
    #     item['university'] = 'Durham University'
    #     item['url'] = response.url
    #     item['location'] = 'Durham'
    #     item['tuition_fee_pre'] = '£'
    #     alevel=response.xpath('//th[contains(text(),"A Level")]/../following-sibling::tr[1]//text()').extract()
    #     alevel=''.join(alevel).strip()
    #     item['alevel']=alevel
    #     ib=response.xpath('//th[contains(text(),"International")]/../following-sibling::tr[1]//text()').extract()
    #     ib=''.join(ib).strip()
    #     item['ib']=ib
    #     ucascode=response.xpath('//th[contains(text(),"UCAS code")]/following-sibling::td/text()').extract()
    #     ucascode=''.join(ucascode).strip()
    #     item['ucascode']=ucascode
    #     programme = response.xpath(
    #         '//div[@id="course"]/div[@class="row-fluid titlebar"]/h1/span[@class="span7 title"]/text()').extract()
    #     programme = ''.join(programme).strip()
    #     # print(programme)
    #     item['programme_en'] = programme
    #     degree_type = response.xpath(
    #         '//div[@id="course"]/div[@class="row-fluid titlebar"]/h1//span[@class="type"]/text()').extract()
    #     degree_type = ''.join(degree_type).strip()
    #     # print(degree_type)
    #     item['degree_name'] = degree_type
    #
    #     duration = response.xpath('//th[contains(text(),"Duration")]/following-sibling::td//text()').extract()
    #     duration = clear_duration(duration)
    #     item['duration'] = duration['duration']
    #     item['duration_per'] = duration['duration_per']
    #     # print(duration)
    #
    #     tuition = response.xpath('//th[contains(text(),"nternational")]/following-sibling::td/text()').extract()
    #     tuition_fee = getTuition_fee(tuition)
    #     # print(tuition_fee)
    #     item['tuition_fee'] = tuition_fee
    #
    #     department = response.xpath('//div[@id="department"]/h3[1]/text()').extract()
    #     department = ' '.join(department)
    #     # print(department)
    #     item['department'] = department
    #
    #     overview = response.xpath('//div[@id="department"]/h5[contains(text(),"verview")]/following-sibling::*').extract()
    #     item['overview_en']=remove_class(overview)
    #
    #     item['ielts'] = '6.5'
    #     item['ielts_l'], item['ielts_s'], item['ielts_r'], item['ielts_w'] = '6.0', '6.0', '6.0', '6.0'
    #     item['toefl'] = '92'
    #     item['toefl_l'], item['toefl_l'], item['toefl_l'], item['toefl_l'] = '23', '23', '23', '23'
    #     item['ielts_desc'] = '6.5 (no component under 6.0)'
    #     item['toefl_desc'] = 'TOEFL iBT (internet based test): 92 (no component under 23)'
    #     # try:
    #     #     modules_url = response.xpath(
    #     #         '//h2[contains(text(),"Course Detail")]/following-sibling::p/a[contains(text(),"here")]/@href').extract()
    #     #     modules_url = ''.join(modules_url)
    #     #     modules_url = 'https://www.dur.ac.uk' + modules_url
    #     #     modules = urlopen(modules_url)
    #     #     moduless = readPDF(modules)
    #     #     # print(moduless)
    #     #     item['modules_en'] = moduless
    #     #     modules.close()
    #     # except:
    #     #     pass
    #     # print(item['modules_en'])
    #
    #     modules=response.xpath('//div[@id="essentials"]').extract()
    #     modules=remove_class(modules)
    #     item['modules_en']=modules
    #
    #     assessment = response.xpath('//div[@id="learning"]').extract()
    #     assessment = remove_class(assessment)
    #     item['assessment_en'] = assessment
    #
    #     rntry = response.xpath('//div[@id="admissions"]').extract()
    #     rntry = remove_class(rntry)
    #     item['require_chinese_en'] = rntry
    #
    #     # item['apply_pre'] = '£'
    #     # item['apply_fee'] = '60'
    #     # item['application_open_date'] = '2018-10-1'
    #     # item['start_date'] = '2019-1,2019-9'
    #
    #     apply_proces = ["<div><h3>Apply Online</h3>",
    #                     "<ul><li>Stage One: Check entry requirements</li>",
    #                     "<li>Stage Two: Complete the application form</li>",
    #                     "<li>Stage Three: We process your application</li>",
    #                     "<li>Stage Four: We communicate a decision</li>",
    #                     "<li>Stage Five: Next steps</li></ul>", ]
    #     apply_proces = '\n'.join(apply_proces)
    #     item['apply_proces_en'] = apply_proces
    #
    #     apply_documents_en = ["<ul><li>Personal details</li>",
    #                           "<li>Your education and qualifications already achieved and details of any qualifications that you are currently studying for, if applicable</li>",
    #                           "<li>The names and addresses of two academic referees</li>",
    #                           "<li>A Personal Statement</li>",
    #                           "<li>Supporting documents (for example, degree certificates / transcripts, English Language evidence if you are not a native English speaker, CV, samples of academic work).</li></ul>", ]
    #     apply_documents_en = '\n'.join(apply_documents_en)
    #     item['apply_documents_en'] = apply_documents_en
    #
    #     apply_desc = [
    #         "<div>The standard minimum entry requirement to study a postgraduate programme at Durham University is normally achievement of an upper second class UK honours degree (2:1) or equivalent qualification and two satisfactory academic references. Full details of qualification equivalencies by country can be found here. For applicants who are not Native English speakers, English language evidence may also be required."
    #         "However, some Academic Departments and programmes have different or additional entry requirements. Therefore, before you apply, it is important to check the appropriate course listing in the courses database or departmental web page to ensure that you meet or are able to meet before the programme commencement date:"
    #         "• The Academic Department and specific programme’s entry requirements and, if applicable, any English language requirements"
    #         "• The financial requirements of the programme you are interested in (including deposit payment, tuition fees and any other associated costs).</div>"]
    #     apply_desc = '\n'.join(apply_desc)
    #     item['apply_desc_en'] = apply_desc
    #
    #     career = response.xpath('//div[@id="opportunities"]').extract()
    #     career = remove_class(career)
    #     item['career_en'] = career
    #
    #     # if degree_type in ['BA', 'BEng', 'BSc']:
    #     #     # print(degree_type)
    #     #     yield item
    #     yield item


