import requests
import sys
import re
from bs4 import BeautifulSoup

if(len(sys.argv) == 1):
    print "useage: python basics.py http://www.example.com"
else:
    url = sys.argv[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    print "Title:"
    print str(soup.title)[7:-8] + "\n"

    print "Links:"
    for link in soup.find_all("a"):
        x = str(link).split("\"")
        if(len(x[1]) > 2 and not x[1].startswith('#')):
            print x[1]
    print ""

    print "robots"
    page = requests.get(url + "/robots.txt")
    s = page.content
    print s
