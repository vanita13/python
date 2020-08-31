# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
for i in range(7):
    tags = soup('a')
    j=0
    for tag in tags:
        # Look at the parts of a tag
        if j==17:
            url1 = tag.get('href', None)
            content = tag.contents[0]

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            html = urlopen(url1, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
        j+=1
print(content)
