#!/usr/bin/env python3
import ssl
ssl._create_default_https_context=ssl._create_unverified_context()
import urllib
from time import sleep
url = 'https://hl.cbss.10010.com/image?mode=validate&width=60&height=20&random=0.9268993696075565'
from urllib.request import urlopen
for i in range(30):
    data = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
    f = open("image/"+ str(i)+ '.png', 'wb')
    print('save pic:'+ str(i))
    f.write(data)
    f.close()