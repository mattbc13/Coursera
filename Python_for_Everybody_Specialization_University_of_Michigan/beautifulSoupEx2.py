# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

pos = int(input('Link Position: '))
rep = int(input('# of Repitions: '))
count = 0

while count < rep:

# Retrieve all of the anchor tags
  tags = soup('a')
#print(tags[pos])
#for tag in tags:
  #print(tag.get('href', None))
  print(tags[pos-1].get('href', None))
  url = tags[pos-1].get('href', None)
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  count +=1
