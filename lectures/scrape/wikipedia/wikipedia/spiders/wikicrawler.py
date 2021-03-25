from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from wikipedia.items import WikipediaItem

from re import search

class PagesSpider(CrawlSpider):
    """
    A page crawler for wikipedia.com
    
    When run, this crawler will show all links on the Wikipedia main page. 
    """
    
    name = "wikipedia_pages"
    allowed_domains = [
        "wikipedia.org"
        ]
    
    start_urls = [
        "https://en.wikipedia.org/wiki/Main_Page"
    ]
    
    exclude_patterns = [
            "\#",
            "File",
            "Wikipedia",
            "Help",
            "Category",
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
                            ".*#.*"
                        ]),
             callback = "parse"),
    )
    
    def parse(self, response):
        
        pages = response.css("a::attr(href)").extract()
        
        for page in pages:
            
            exclude = False
            
            for pattern in self.exclude_patterns:
                if search(pattern, page):
                    exclude = True
            
            if not exclude:
                if "/wiki/" in page:
                    yield {"page" : page[6:]}