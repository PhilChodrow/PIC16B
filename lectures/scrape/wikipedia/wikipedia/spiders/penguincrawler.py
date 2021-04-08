from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor

from re import search

class WikipediaSpider(Spider):
    """
    A page crawler for wikipedia.com
    
    When run, this crawler will begin to crawl Wikipedia, starting with the page https://en.wikipedia.org/wiki/Penguin. 
    This crawler attempts to get ALL links on a page, and will keep following links until it reaches the CLOSE_SPIDER_PAGECOUNT limit specified in settings.py. 
    """
    
    name = "penguin-spider"
    
    # only allowed to crawl here
    allowed_domains = [
        "en.wikipedia.org"
        ]
    
    # start with penguins, obviously
    start_urls = [
        "https://en.wikipedia.org/wiki/Penguin"
    ]

    # don't go to any pages with these patterns
    deny_urls = [
        "https://en\.wikipedia\.org/wiki/Wikipedia.*",
        "https://en\.wikipedia\.org/wiki/Main_Page",
        "https://en\.wikipedia\.org/wiki/Free_Content",
        "https://en\.wikipedia\.org/wiki/Talk.*",
        "https://en\.wikipedia\.org/wiki/Portal.*",
        "https://en\.wikipedia\.org/wiki/Special.*",
        "https://en\.wikipedia\.org/wiki/File.*",
        ".*#.*",
        ".*Help:.*",
        ".*Category:.*",
        ".*(identifier).*",
        ".*Template:.*",
        ".*Dictionary.*",
        ".*language.*",
        ".*disambiguation.*"
    ]
    
    # this is a handy gadget that will get all the links on a page
    # for us, except the ones that are denied above. 
    link_extractor = LinkExtractor(allow="https://en\.wikipedia\.org/wiki/.+",
                           deny=deny_urls)
    
    def parse(self, response):
        
        # record the topic of the current page
        current = response.url.split("/")[-1]
        
        # get all the links on the current page
        links = self.link_extractor.extract_links(response)
        
        # for all links on the current page, yield
        # data about them and then yield a request
        # to follow those links. In this case, 
        # yielded data is just the current page
        # and the next page, so we can see what's 
        # connected. 

        for link in links:
            
            yield {"source" : current,
                   "target" : link.url.split("/")[-1]}
            
            yield Request(link.url, callback = self.parse)
        

    def parse_start_url(self, response):
        """
        It's necessary to implement this method in order to 
        ensure that the very first page will have its data 
        recorded. 
        """
        return self.parse(response)