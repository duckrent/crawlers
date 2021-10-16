import scrapy
from daftie.items import DaftieRentOffer


class RentSpider(scrapy.Spider):
    name = 'rent'
    allowed_domains = ['daft.ie']
    start_urls = [
            f"https://www.daft.ie/property-for-rent/dublin-city?rentalPrice_from=200&rentalPrice_to=20000&sort=publishDateDesc&pageSize=20&from={20*i}" for i in range(44)
            ]
    current_page = 0

    def parse(self, response):
        offers_links = response.xpath('//main/div[3]/div[1]/ul/li/a')
        for link in offers_links:
            yield response.follow(link, callback=self.parse_detail)

    def parse_detail(self, response):
        yield DaftieRentOffer(
                url = response.url,
                price=response.xpath('/html/body/div[2]/main/div[3]/div[1]/div[1]/div/div[2]/div[1]/p/span/text()').get(),
                address=response.xpath('/html/body/div[2]/main/div[3]/div[1]/div[1]/div/div[2]/h1/text()').get(),
                number_bedrooms=response.xpath('/html/body/div[2]/main/div[3]/div[1]/div[1]/div/div[2]/div[2]/p[1]/text()').re_first('\d+'),
                number_bathrooms=response.xpath('/html/body/div[2]/main/div[3]/div[1]/div[1]/div/div[2]/div[2]/p[2]/text()').re_first('\d+'),
                property_type=response.xpath('/html/body/div[2]/main/div[3]/div[1]/div[1]/div/div[2]/div[2]/p[3]/text()').get(),
                property_facilities=[
                    e.xpath('text()').get()
                    for e in response.css('li.PropertyDetailsList__PropertyDetailsListItem-sc-1cjwtjz-1')],
                entered_date=response.css('div.Statistics__StyledStatsContainer-sc-15tgae4-0:nth-child(1) > div:nth-child(1) > p:nth-child(1)').xpath('text()').get().strip(),
                number_views=response.css('div.Statistics__StyledStatsContainer-sc-15tgae4-0:nth-child(2) > div:nth-child(1) > p:nth-child(1)').xpath('text()').re_first('[\d|,]+'),
                images=[i.attrib['src'] for i in response.xpath('//picture/img') if 'data-testid' in i.attrib]
                )
