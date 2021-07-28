# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def replaceQuotations(text):
    return text.replace(u"\u201c", '').replace(u"\u201d", '')

def returnCSV(array):
    return ",".join(array)

# Making an item to store Data
# The items file can be used to clean data
class GoodReadsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    text =  scrapy.Field(
        input_processor = MapCompose(replaceQuotations, str.strip),
        output_processor = TakeFirst()
    )
    author =  scrapy.Field(
        input_processor = MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst()
    )
    # remove tags and return a csv instead of an array
    tags =  scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = returnCSV

    )

