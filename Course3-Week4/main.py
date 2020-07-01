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

url = " http://www.py4e.com/code3/mbox.txt"
html = urlopen(url, context=ctx).read()
print(html)
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
spans = soup('span')
sum = 0
for span in spans:
    # Look at the parts of a tag
    sum = sum + int(span.contents[0])
    #print(span.contents[0])
print(sum)