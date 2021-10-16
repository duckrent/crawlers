# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaftieRentOffer(scrapy.Item):
    url = scrapy.Field()
    price = scrapy.Field()
    price_frequency = scrapy.Field()
    address = scrapy.Field()
    number_bedrooms = scrapy.Field()
    number_bedrooms = scrapy.Field()
    number_bathrooms = scrapy.Field()
    property_type = scrapy.Field()
    property_facilities = scrapy.Field()
    entered_date = scrapy.Field()
    number_views = scrapy.Field()
    images = scrapy.Field()
