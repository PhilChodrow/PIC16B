from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from re import search

class PagesSpider(CrawlSpider):
    """
    A page crawler for wikipedia.com
    
    When run, this crawler will begin to crawl Wikipedia, starting with the page https://en.wikipedia.org/wiki/Penguin. 
    This crawler attempts to get ALL links on a page, and will keep following links until it reaches the CLOSESPIDER_PAGECOUNT limit specified in settings.py
    """
    
    name = "penguin-crawler"
    allowed_domains = [
        "en.wikipedia.org"
        ]
    
    start_urls = [
        "https://en.wikipedia.org/wiki/Penguin"
    ]
    
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
        ".*Template:.*"
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
                           deny=deny_urls),
             callback = "parse"),
    )
    
    def parse(self, response):
        
        # find the current page
        current = response.url.split("/")[-1]
        
        # extract the href attribute of all links (css element `a`)
        # in the page
        pages = response.css("a::attr(href)").getall()
        
        for page in pages:
            exclude = False
            
            for pattern in self.exclude_patterns:
                if search(pattern, page):
                    exclude = True
            
            if not exclude:
                if page[0:6] == "/wiki/":
                    yield {"source" : current,
                           "target" : page[6:]}
                    
    def parse_start_url(self, response):
        return self.parse(response)