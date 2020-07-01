import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/comments_694448.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('count:', len(info['comments']))

sum = 0
for item in info['comments']:
  sum = sum + int(item['count'])
print(sum)