import scrapy

# basic version: download all html from specified URLS
# to run: scrapy crawl quotes in terminal

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        
        with open(filename, "wb") as f:
            f.write(response.body)
            

# next evolution: save specified data using css selectors
# command to run and save the data: 
## scrapy crawl quotes2 -o quotes.csv    

class QuotesSpider2(scrapy.Spider):
    name = "quotes2"
    
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            
            text = quote.css("span.text::text").get()
            for char in ['”', '“']:
                text = text.replace(char, '')
            
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            tags = ",".join(tags)
            
            yield {
                "text" : text,
                "author": author,
                "tags": tags
            }
            
# next evolution: save specified data using css selectors
# command to run and save the data: 
## scrapy crawl quotes2 -o quotes.csv    

class QuotesSpider2(scrapy.Spider):
    name = "quotes2"
    
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            
            text = quote.css("span.text::text").get()
            for char in ['”', '“']:
                text = text.replace(char, '')
            
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            tags = ",".join(tags)
            
            # this line looks like it's just yielding dictionaries "into the void"
            # but adding the flag -o quotes.csv when using the scrapy crawl 
            # command results in this being saved to a convenient csv file
            yield {
                "text" : text,
                "author": author,
                "tags": tags
            }
 
# DOWNLOAD ALL THE QUOTES 
# command to run and save the data: 
## scrapy crawl quotes3 -o quotes.csv           
class QuotesSpider3(scrapy.Spider):
    name = "quotes3"
    
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]
    
    def parse(self, response):
        
        # first part of this function is same as before
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            for char in ['”', '“']:
                text = text.replace(char, '')
            
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            tags = ",".join(tags)
            
            yield {
                "text" : text,
                "author": author,
                "tags": tags
            }
            
        # follow links by yielding a *Request* object with the appropriate URL,
        # and then specifying what should happen when we get there as a *callback*
        
        next_page = response.css("li.next a").attrib["href"]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)