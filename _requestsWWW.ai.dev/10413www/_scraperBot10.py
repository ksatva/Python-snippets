"""
The Ethical Scraper

I, the web scraper will live by the following principles:

    If you have a public API that provides the data I’m looking for, I’ll use it and avoid scraping all together.
    I will always provide a User Agent string that makes my intentions clear and provides a way for you to contact me with questions or concerns.
    I will request data at a reasonable rate. I will strive to never be confused for a DDoS attack.
    I will only save the data I absolutely need from your page. If all I need it OpenGraph meta-data, that’s all I’ll keep.
    I will respect any content I do keep. I’ll never pass it off as my own.
    I will look for ways to return value to you. Maybe I can drive some (real) traffic to your site or credit you in an article or post.
    I will respond in a timely fashion to your outreach and work with you towards a resolution.
    I will scrape for the purpose of creating new value from the data, not to duplicate it.

https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01
avoid scraping all together
always provide a User Agent string
only save the data I absolutely need from your page. 
     If all I need it OpenGraph meta-data

"""
import requests
from bs4 import BeautifulSoup as bs
import re


""" creating BS object for entire website (--first lines)
url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
wdata = requests.get(url)

wdata_content = wdata.content
soup = bs(wdata_content)
"""




"""
#for all links (article +other)
for link in soup.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])
"""



"""
#for only article links
for link in soup.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print(link.attrs['href'])
"""




""" RANDOM WALK THROUGH A WEBSITE
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    url = 'https://en.wikipedia.org' + articleUrl
    wdata = requests.get(url)

    wdata_content = wdata.content
    soup = bs(wdata_content)
    return soup.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
	newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)
	links = getLinks(newArticle)
    """




pages = set()
def getLinks(pageUrl):
    url = 'https://en.wikipedia.org' + pageUrl
    wdata = requests.get(url)

    wdata_content = wdata.content
    soup = bs(wdata_content)

    for link in soup.findAll("a",href=re.compile("^(/wiki/")):
    	if 'href' in link.attrs:
    		if link.attrs['href'] not in pages:
    			#we have encountered a new page
    			newPage = link.attrs['href']
    			print(newPage)
    			pages.add(newPage)
    			getLinks(newPage)

 getLinks("")

