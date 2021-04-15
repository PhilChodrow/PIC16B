from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from filedownload.items import FileDownloadItem


class WikipediaImageSpider(Spider):
    """
    A simple spider class to illustrate scraping while downloading files, in this case images. 
    This spider works as follows. 
    
    - The *crawl* logic is handled by a LinkExtractor. The self.parse() method 
      yields requests (with callbacks) by looping through the output of the 
      LinkExtractor. 
    - The *download* logic is handled by the self.parse_image_page() method,
      which tries to download the lowest-resolution image from a wikipedia image page. 
    
    The location of the files saved, as well as the total number of requests sent, are controlled by settings.py
    """
    
    
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
        """
        This function is called when we get to a wikipedia image page, like this one: 
        
        https://en.wikipedia.org/wiki/Penguin#/media/File:Penguins_walking_-Moltke_Harbour,_South_Georgia,_British_overseas_territory,_UK-8.jpg
        
        It uses css selectors to extract a list of candidate links
        to copies of the image at different resolutions. 
        It then attempts to download the second of these, which is usually 
        the lowest resolution. 
        
        The downloading itself requires that a FileDownloadItem() class be 
        defined in items.py. Downloading is handled by yielding these items. 
        The location to which images are downloaded is controlled by 
        settings.py. 
        """
        
        # get links to images of different resolutions
        link_resolutions = [r.attrib["href"] for r in response.css("a.mw-thumbnail-link").css("a")]
        
        # try to choose the second one
        if link_resolutions:
            
            res = min(len(link_resolutions), 1)
            url = link_resolutions[res]
            
            # for unknown reasons, sometimes the https: prefix gets chopped
            # off, so we need to add it back on
            if "https:" not in url:
                url = "https:" + url
            
            # create and yield a FiledownloadItem() with the specified url. 
            item = FileDownloadItem()
            item['file_urls'] = [url]
            yield item
    
    def parse(self, response):
        
        # DOWNLOAD LOGIC: get urls of image pages
        # note that the resulting URLs are not actually addresses
        # of the images themselves, but rather the Wikipedia 
        # image page, like this one: 
        # https://en.wikipedia.org/wiki/Penguin#/media/File:Penguins_walking_-Moltke_Harbour,_South_Georgia,_British_overseas_territory,_UK-8.jpg
        
        # use css selectors to get the image links within 
        # the wikipedia image thumbnails on the current response
        # experimenting with the scrapy shell is recommended for 
        # understanding what's going on here
        image_boxes = response.css("div.thumbinner")
        box_contents = image_boxes.css("div.thumbcaption")
        image_links = box_contents.css("a:first-child")
        image_suffixes = [link.attrib["href"] for link in image_links]
        prefix = "https://en.wikipedia.org"
        image_urls = [prefix + suffix for suffix in image_suffixes]
        
        
        # once we have all the image page urls in a list, we are going to
        # (a) go to each one and 
        # (b) call self.parse_image_page once we get there. 
        for url in image_urls:    
            yield Request(url, callback = self.parse_image_page)
        
        # NAVIGATION LOGIC: we've seen this before  
    
        links = self.link_extractor.extract_links(response)    
        # if you want to visit every possible page linked
        # for link in links: 
        #     yield Request(link.url, callback = self.parse)
        
        # demonstration which results in more images scraped: only follow
        # the first valid link each time
        yield Request(links[0].url, callback = self.parse)
            
    def parse_start_url(self, response):
        """
        It's necessary to implement this method in order to 
        ensure that the very first page will have its data 
        recorded. 
        """
        return self.parse(response)