from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from wikipedia.items import WikipediaItem

from re import search

class PagesSpider(CrawlSpider):
    """
    A page crawler for wikipedia.com
    
    When run, this crawler will begin to crawl Wikipedia, starting with the page https://en.wikipedia.org/wiki/Penguin
    """
    
    name = "penguin-crawler"
    allowed_domains = [
        "wikipedia.org"
        ]
    
    start_urls = [
        "https://en.wikipedia.org/wiki/Penguin"
    ]
    
    exclude_patterns = [
            "\#",
            "File",
            "Wikipedia",
            "Help",
            "Category",
            ":"
        ]
        
    rules = (
        Rule(LinkExtractor(allow="https://en\.wikipedia\.org/wiki/.+",
                           deny=[
                            "https://en\.wikipedia\.org/wiki/Wikipedia.*",
                            "https://en\.wikipedia\.org/wiki/Main_Page",
                            "https://en\.wikipedia\.org/wiki/Free_Content",
                            "https://en\.wikipedia\.org/wiki/Talk.*",
                            "https://en\.wikipedia\.org/wiki/Portal.*",
                            "https://en\.wikipedia\.org/wiki/Special.*",
                            "https://en\.wikipedia\.org/wiki/File.*",
                            ".*#.*",
                            ".*Category:.*"
                        ]),
             callback = "parse"),
    )
    
    def parse(self, response):
        
        current = response.url.split("/")[-1]
        
        pages = response.css("a::attr(href)").extract()
        
        for page in pages:
            
            exclude = False
            
            for pattern in self.exclude_patterns:
                if search(pattern, page):
                    exclude = True
            
            if not exclude:
                if page[0:6] == "/wiki/":
                    yield {"source" : current,
                           "page" : page[6:]}
                    
    def parse_start_url(self, response):
        return self.parse(response)