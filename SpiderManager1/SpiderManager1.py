from bs4 import BeautifulSoup
import re
import urllib2
import urllib

def getHtml(url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
        return html

def getActiveUrl(self):
        para = {"id":"162518"}
        data=urllib.urlencode(para)
        request = urllib2.Request(url,data)
        response=urllib2.urlopen(request)
        html=response.read()
        return html

def getImge(html):
        soup=BeautifulSoup(html,"lxml")
        imgs=soup.find_all("img")
        for img in imgs:
            print img["src"]

html=getHtml("https://movie.douban.com/")
getImge(html)