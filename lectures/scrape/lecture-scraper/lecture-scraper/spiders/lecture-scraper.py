###################################################################
# WEBSCRAPING WITH SCRAPY
###################################################################

# NOTE: This lecture is closely based on the Scrapy Tutorial, available here: 
# https://docs.scrapy.org/en/latest/intro/tutorial.html

# In this lecture, we are going to introduce scrapy, 
# a Python framework for webscraping. We are going to go especially
# slowly through this material, because there are a few key ways 
# in which our workflow for webscraping is going to look 
# very different from usual.  

# - We are going to need to write .py files in a text editor
# - We are going to need to issue some simple terminal commands. 
# - We are going to need to get a little comfortable with HTML, the 
#   fabric of the web. 

# To follow along with this lecture, you'll need to install the
# scrapy package in your PIC16B Anaconda environment. 

###################################################################
# WHAT IS WEBSCRAPING?
###################################################################

# "The web" is a collection of files hosted on a large network of
# communicating servers. *Webscraping* refers to the act of 
# accessing those files and programmatically saving them, or parts 
# of them, to a chosen location (usually your computer). 
# This is often a critical task  when writing projects that require # data from the internet. 

# In these lectures, we'll focus on how to scrape HTML. HTML 
# (HyperText Markup Language) may be fairly said to be the 
# fabric of the internet. Nearly all of the things that you 
# would normally think of as "webpages" are really files 
# written in HTML. A browser like Firefox, Chrome, or Safari is
# just a program for *rendering* HTML in an attractive visual 
# format. Unfortunately, for scraping, we often need to interact
# with raw HTML, which can get messy. Fortunately, the scrapy 
# package gives us some tools with which to do this. 

# Unfortunately, this starts off kind of complicated -- the first
# thing we need to do is to *activate* our Anaconda environment 
# and then create a scrapy "project", both in the terminal. 

# 1. Open a terminal and navigate to the location where you would #    like to make your scrapy project. Then, type: 
# 2. >>> conda activate PIC16B
# 3. >>> scrapy startproject lecture
 
# Now is a good time to fire up your text editor. We would like to 
# make a file called lecturescraper.py in the directory 
# lecture/lecture/spiders

# We are finally ready to write a webscraper.  
 
import scrapy

# Great! We have written one (1) line of Python. 

# Now that we've done our Python programming for the day, let's
# take a quick look at the tutorial website we'll scrape from. 

# http://quotes.toscrape.com/

# We observe that there are a number of quotes, which possess 
# text, authors, and tags. There are multiple pages of 
# these quotes, which are accessed via the "Next" button. 

# For our first scraper, we'll specify two of the several 
# webpages, and just download their HTML. 

# first spider: download all html from specified URLS
# to run in terminal: scrapy crawl quotes

class QuotesSpider(scrapy.Spider):
    
    # this name is used to call different spiders
    # from the terminal 
    name = "quotes"
    
    # the spider will inspect both of these pages
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]
    
    # most important method! Determines what should happen
    # when we find a webpage. This implementation just 
    # saves the HTML in a file. 
    
    def parse(self, response):
        
        # number of the page
        page = response.url.split("/")[-2]
        
        # write the entire webpage to local html
        filename = f"quotes-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)

# A few notes: 

# - Our scraper is a class. 
# - Our scraper subclasses the scrapy.Spider class. I'll use 
#   "scraper" and "Spider" interchangeably from here on out. 
# - The parse method is the most important method in a Spider,
#   and specifies what should happen when the Spider encounters
#   a *response.* A response is an object corresponding to a 
#   webpage; it contains the raw HTML as well as a number of useful
#   attributes and methods for extracting information from the 
#   page. 

###################################################################
# INTERLUDE: THE SCRAPY SHELL
###################################################################
            
# We're going to need to get comfortable thinking of webpages like 
# these as big collections of HTML. Your browser probably has 
# "Developer Tools" or something like that, which allow you to 
# inspect the HTML directly. 

# The Scrapy Shell allows you to experiment with ways to extract 
# information from a selected response. For example: 
# >>> scrapy shell http://quotes.toscrape.com/page/1/

# Let's extract quotes from the HTML using css selectors. 
# Then we'll get quotes and tags. 


###################################################################
# NEXT SPIDER: SAVING DATA
###################################################################

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
        
        # loop through an iterable of quotes
        for quote in response.css("div.quote"):
            
            # extract the text of the quote    
            text = quote.css("span.text::text").get()
            
            # author and tags
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            tags = ",".join(tags)
            
            # yield data. Although it looks like we're just kind of
            # yielding into the void, this data will be saved in 
            # a CSV via our terminal command. 
            yield {
                "text" : text,
                "author": author,
                "tags": tags
            }

###################################################################
# NEXT SPIDER: FOLLOWING LINKS
###################################################################

# So far, we've been able to: 
# - Download HTML from *specified* pages. 
# - Use CSS selectors to obtain data within the HTML. 

# However, we might want to scrape data in a setting in which we 
# don't actually know which pages exist, how many there are, or 
# how they are linked. In these kinds of situations, we need to 
# give our spider some ability to 

# - Find links within the HTML
# - Follow those links, and parse the results.  

# *Finding* the links is not too complicated -- it's just a matter
# of using more CSS selectors (i.e. more messing around in the ) 
# scrapy shell. *Following* the links is more subtle, and involves 
# the concept of *requests*. 

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
        
        # first part of this method is same as before
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
        
        # NEW PART HERE
        # now we need to add logic for *following links*. 
        # After yielding the data (above), we also need to construct and yield a *Request* object with the appropriate URL,
        # and then specifying what should happen when we get there as a *callback*
        
        # find the link to the next page (it's the "next" button)
        # the href is the part of the HTML element that actually contains
        # the hyperlink. 
        next_page = response.css("li.next a").attrib["href"]
        
        if next_page is not None:
            # make the full URL
            next_page = response.urljoin(next_page)
            
            # yield a Request object. Yielding a request causes the Spider to attempt to go to the specified URL. 
            # The callback controls what happens when you get 
            # there. So, this line says: 
            # "go to next_page, and once you get there, do 
            # self.parse again"
            yield scrapy.Request(next_page, callback = self.parse)