from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
print('data retrieved ', len(html),'chars')

ifo = json.loads(html)
print(len(ifo))

comments = ifo['comments']
print(len(comments))
sum = 0

for item in comments:
    sum +=item['count']

print(sum)