#!/usr/bin/env python
from bs4 import BeautifulSoup
import dataset
import requests

# connecting to a SQLite database
db = dataset.connect('sqlite:///benfordslaw.db')

alexa_urls = ['http://www.alexa.com/topsites/global;0', 'http://www.alexa.com/topsites/global;1', 'http://www.alexa.com/topsites/global;2', 'http://www.alexa.com/topsites/global;3']

url_prefix = "http://"

website_table = db['website']

for alexa_url in alexa_urls:
    r = requests.get(alexa_url)
    soup = BeautifulSoup(r.content, "lxml")
    
    # get the 25 links from each page
    site_listings = soup.select('.site-listing h2 a')

    for site_listing in site_listings:
        # urls on alexa pages look like <a href="/siteinfo/google.com">google.com</a>, so get
        # the contents and add the http prefix
        url = url_prefix + site_listing.contents[0]
        website_id = website_table.upsert(dict(url=url, doc_size=0), ['url'])
    
    print alexa_url + " is done. \n"

print "Finished! Top 100 URLs should be in the database now."