import scrapy 
from demo_project.items import GoodReadsItem
from scrapy.loader import ItemLoader



class GoodReadsSpider(scrapy.Spider):
    # Identity 
    name = "goodreads"
    
    # Request  (# Must be in a function )
    def start_requests(self):     
        # constants 
        baseURL = "https://www.goodreads.com/quotes"
        yield scrapy.Request(baseURL) 

    # Response (parsing)
    def parse(self, response):
        quoteXPath  = "//div[@class='quote']" # quote xpath
        quoteText = ".//div[@class='quoteText']/text()[1]" # Extracting from the above path as root (. - starts from the current selector)
        quoteAuthor = ".//span[@class='authorOrTitle']"
        quoteTags = ".//div[@class='greyText smallText left']/a"
        for quote in response.selector.xpath(quoteXPath):

            # Using the loader
            loader = ItemLoader(item=GoodReadsItem(), selector = quote, response = response)
            loader.add_xpath('text', quoteText)
            loader.add_xpath('author', quoteAuthor)
            loader.add_xpath('tags', quoteTags)
            yield loader.load_item()

        # Next page link extraction 
        nextPage = "//a[@class='next_page']/@href"
        nextPageLink = response.selector.xpath(nextPage).extract_first()
        if (nextPageLink is not None):
            nextPageURL = response.urljoin(nextPageLink)
            yield scrapy.Request(nextPageURL) 

        
    