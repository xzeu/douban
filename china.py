import requests
import re

class BDTB:
    def __init__(self,baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    def getPage(self, pageNUM):
        url = self.baseURL + self.seeLZ + '&pn=' +str(pageNUM)
        response = requests.get(url)
        print(response.text)
        return response

baseURL ='http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)