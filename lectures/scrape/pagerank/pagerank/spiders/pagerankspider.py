from scrapy.spiders import Spider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import numpy as np


class PageRankSpider(Spider):
    
    name = "pagerank-crawler"
    
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
        
    link_extractor = LinkExtractor(allow="https://en\.wikipedia\.org/wiki/.+",
                                   deny = deny_urls)
    
    visited_pages = set(start_urls)
    
    alpha = 0.15
    
    def parse(self, response):
        self.visited_pages = self.visited_pages.union({response.url})
        source = response.url.split("/")[-1]
        
        # teleport option
        if np.random.rand() < self.alpha:
            
            # seeded PageRank always goes back to the starting page
            link = self.start_urls[0]
            
            # alternatively, go back to a random, previously-visited page 
            # by uncommenting the line below (global PageRank)
            # link = np.random.choice(list(self.visited_pages))
            move_type = "teleport"
            
        # walk option: click a random link on the page  
        else: 
            
            # list of all links on the page, subject to the inclusion and exclusion rules defined above
            links = self.link_extractor.extract_links(response)
            
            # pick a random one
            n = np.random.randint(0, len(links)) 
            link = links[n].url
            move_type = "walk"
        
        # yield data for saving
        yield {
            "source" : source, 
            "target" : link.split("/")[-1],
            "move_type" : move_type
        }
            
        # choose new link
        yield Request(link, callback = self.parse)
        
    def parse_start_url(self, response):
        return self.parse(response)