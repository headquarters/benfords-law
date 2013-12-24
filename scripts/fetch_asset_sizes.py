#!/usr/bin/env python
from bs4 import BeautifulSoup
from urlparse import urljoin
import dataset
import requests

# connecting to a SQLite database
db = dataset.connect('sqlite:///benfordslaw.db')

# table: website(url, file_size)
website_table = db['website']

# table: asset(website_id, type, url, file_size)
asset_table = db['asset']

# get all websites currently in the website table
websites = list(website_table.all())

# debugging: 
#websites = []
#websites.append(website_table.find_one(url="http://t.co"))
#websites.append(website_table.find_one(url="http://twitter.com"))

'''
Sample headers:
    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding:gzip,deflate,sdch
    Accept-Language:en-US,en;q=0.8,de;q=0.6,ja;q=0.4
    Cache-Control:no-cache
    Connection:keep-alive
    Cookie:__utma=263995919.2002225245.1384275498.1384275498.1384275498.1; __utmc=263995919; __utmz=263995919.1384275498.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1; _gauges_unique_day=1; __utma=7744177.1422957692.1386987409.1386987409.1386987409.1; __utmb=7744177.5.10.1387306179; __utmc=7744177; __utmz=7744177.1386987409.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=7744177.1422957692.1386987409.1386987409.1386987409.1; __utmb=7744177.5.10.1387306179; __utmc=7744177; __utmz=7744177.1386987409.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)
    Host:requests.readthedocs.org
    Pragma:no-cache
    Referer:http://requests.readthedocs.org/en/latest/
    User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36
'''
headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip,deflate,sdch', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36' }

for website in websites:
    url = website['url']
    try:
        r = requests.get(url, allow_redirects=True, headers=headers)
        soup = BeautifulSoup(r.content, "lxml")
    
        # get the whole document's size
        doc_size = len(r.content)
        
        website_table.update(dict(url=url, doc_size=doc_size), ['url'])
        
        website_id = website['id']
        
        # get all the external asset tags
        links = soup.find_all('link')
        scripts = soup.find_all('script')
        images = soup.find_all('img')
        
        # maintain list of dictionaries for using with insert_many
        rows = []
    
        # google.com => 301 => 302 => 200
        # print str(r.history)
    
        # loop over all assets and make requests, then read contents for length
        if r.status_code == 200:
            for link in links:
                # will include CSS files and favicons
                if link.get('href'):
                    absolute_href = urljoin(url, link['href'])
                    try:
                        l = requests.get(absolute_href)
                        if l.status_code == 200:
                            link_size = len(l.content)
                            row = dict(website_id=website_id, type="link", url=absolute_href, file_size=link_size)
                            rows.append(row)
                    except requests.exceptions.SSLError as e:
                        print "SSLError exception for " + absolute_href + ": " + str(e) + "\n"
                    except requests.packages.urllib3.exceptions.LocationParseError as e:
                        print "LocationParseError exception for " + absolute_src + ": " + str(e) + "\n"
                    except Exception as e:
                        print "Unexpected error: " + str(e)
            
            for script in scripts:
                # exclude internal scripts since they're part of the document
                if script.get('src'):
                    absolute_src = urljoin(url, script['src'])
                    try:
                        s = requests.get(absolute_src)
                        if s.status_code == 200:
                            script_size = len(s.content)
                            row = dict(website_id=website_id, type="script", url=absolute_src, file_size=script_size)
                            rows.append(row)
                    except requests.exceptions.SSLError as e:
                        print "SSLError exception for " + absolute_src + ": " + str(e) + "\n"
                    except requests.packages.urllib3.exceptions.LocationParseError as e:
                        print "LocationParseError exception for " + absolute_src + ": " + str(e) + "\n"
                    except Exception as e:
                        print "Unexpected error: " + str(e)
        
            for image in images:
                # all images with src attribute
                if image.get('src'):
                    absolute_src = urljoin(url, image['src'])
                    try:
                        i = requests.get(absolute_src)
                        if i.status_code == 200:
                            image_size = len(i.content)
                            row = dict(website_id=website_id, type="image", url=absolute_src, file_size=image_size)
                            rows.append(row)
                    except requests.exceptions.SSLError as e:
                        print "SSLError exception for " + absolute_src + ": " + str(e) + "\n"
                    except requests.packages.urllib3.exceptions.LocationParseError as e:
                        print "LocationParseError exception for " + absolute_src + ": " + str(e) + "\n"
                    except Exception as e:
                        print "Unexpected error: " + str(e)

        asset_table.insert_many(rows)
    except requests.exceptions.ConnectionError as e:
        print "ConnectionError exception for " + url + ": " + str(e) + "\n"
    
    print str(url) + " and its assets are done. \n"
    
print "Finished! All asset sizes should be in the database now."