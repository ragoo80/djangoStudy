# -*- coding: utf-8 -*-

# import time
#
# start_time = time.time()
# end_time = start_time + 100000
# print start_time, end_time
# while start_time < end_time:
# 	start_time += .1
# 	print 'time1 : ',  start_time
# else :
# 	print 'time2 : ',  start_time




from urllib import urlopen
import urllib2, urllib
import requests

def imgLoaded(url) :
	req = requests.get(url.decode('utf-8'))
	if req.status_code == 200:
		print 'img yes'
		data = urllib.urlopen(req)
		print data
		dr = data.read()
		print dr
	else :
		raise Exception("can't load html!!!!!!!!!!!!!!!")

testUrl = 'https://www.lotterentacar.net/atch/upload/getImage.do?atchFileId=20170205teramin47@naver.com06하5928frontImg_V.jpg&fileSepar=succession'

imgLoaded(testUrl)