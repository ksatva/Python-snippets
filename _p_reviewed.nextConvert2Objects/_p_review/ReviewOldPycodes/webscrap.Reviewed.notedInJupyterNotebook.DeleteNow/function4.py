#web scraping function
#link_crawler.py2
#function4

import re
from webscrapfunc import *

import urlparse
def link_crawler(seed_url, link_regex):
	#crawl a seed_url following links matched by link_regex
	crawl_queue = [seed_url]
	#keep track which url's have seen before
	seen = set(crawl_queue)
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		#filter for links matching
		for link in get_links(html):
			if re.match(link_regex,link):
				#form absolute link
				link = urlparse.urljoin(seed_url,link)				
				#check if have already seen this link
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)

def get_links(html):
	#return a list of links from html
	#following is a regular expression	
	webpage_regex = re.compile('<a[^>+href=["\'](.*?)["\']',re.IGNORECASE)
	return webpage_regex.findall(html)
