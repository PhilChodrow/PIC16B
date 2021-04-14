from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from filedownload.items import FileDownloadItem


class WikipediaImageSpider(Spider):
    
    name = "image-spider"
    
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
    # for us, except the ones that are denied above. Stored as a 
    # class variable of our spider. 
    link_extractor = LinkExtractor(allow="https://en\.wikipedia\.org/wiki/.+", deny=deny_urls)
    
    
    valid_extensions = [".jpg", ".svg"]
    
    def parse_image_page(self, response):
        link_resolutions = [r.attrib["href"] for r in response.css("a.mw-thumbnail-link").css("a")]
        
        if len(link_resolutions) > 1:
            
            res = min(len(link_resolutions), 1)
            url = link_resolutions[res]
            
            if "https:" not in url:
                url = "https:" + url
            
            item = FileDownloadItem()
            item['file_urls'] = [url]
            
            yield item
    
    def parse(self, response):
        
        image_boxes = response.css("div.thumbinner")
        box_contents = image_boxes.css("div.thumbcaption")
        image_links = box_contents.css("a:first-child")
        image_suffixes = [link.attrib["href"] for link in image_links]
        
        prefix = "https://en.wikipedia.org"
        
        image_urls = [prefix + suffix for suffix in image_suffixes]
            
        # yield the items
        for url in image_urls:
            
            yield Request(url, callback = self.parse_image_page)
            
        # follow links to next page
        links = self.link_extractor.extract_links(response)
        
        for link in links: 
            yield Request(link.url, callback = self.parse)
            
            
            

    def parse_start_url(self, response):
        """
        It's necessary to implement this method in order to 
        ensure that the very first page will have its data 
        recorded. 
        """
        return self.parse(response)