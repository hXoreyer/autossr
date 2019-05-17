#-*-coding:utf-8-*-
import urllib2
import re

def getip():
	url = urllib2.urlopen("http://txt.go.sohu.com/ip/soip")
	text = url.read()
	ip = re.findall(r'\d+.\d+.\d+.\d+',text)
	return ip[0]
