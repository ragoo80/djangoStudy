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




# from urllib import urlopen
# import urllib2, urllib
# import requests
#
# def imgLoaded(url) :
# 	req = requests.get(url.decode('utf-8'))
# 	if req.status_code == 200:
# 		print 'img yes'
# 		data = urllib.urlopen(req)
# 		print data
# 		dr = data.read()
# 		print dr
# 	else :
# 		raise Exception("can't load html!!!!!!!!!!!!!!!")
#
# testUrl = 'https://www.lotterentacar.net/atch/upload/getImage.do?atchFileId=20170205teramin47@naver.com06하5928frontImg_V.jpg&fileSepar=succession'
#
# imgLoaded(testUrl)


# --------------------------------------------------------------------------------------------------------------
# 자동차번호 7자리 번호 보다 작거나, 영문 포함
import re
pagingList = [
	# u"goDetail('68\ud5583435','chs1972');",
	u"goDetail('46\ud6385532','park2968@naver.com');",
	u"goDetail('66\ud638','abukki4');",
	u"goDetail('bmw320d','tissue7587@naver.com');",
	u"goDetail('50gk7294','trade75');",
	u"goDetail('44\ud558 4674','6aksmef');",
	u"goDetail('52\ud63813ㅂ8','sdh0328@naver.com');",
	u"goDetail('03하9000.','leecj1210');"
]

# pattern = re.compile('[a-z|A-Z|ㄱ-]+')
# for idx in range(len(pagingList)) :
# 	carNumber = pagingList[idx].split("'")[1]
# 	print carNumber
# 	print len(carNumber)
# 	print re.search(pattern, carNumber.encode('utf-8') )
# 	if len(carNumber) != 7 or re.search(pattern, carNumber.encode('utf-8') ) != None:
# 		print '크롤링에 포함 안시킴 '
# 	else :
# 		print '크롤링에 포함 시킴 '
# 	print '------------------------'


def validatorCar(carNumber):
	pattern = re.compile('[a-z|A-Z|ㄱ-]+')
	if len(carNumber) != 7 or re.search(pattern, carNumber.encode('utf-8') ) != None:
		return False
	return True

for idx in range(len(pagingList)) :
	carNumber = pagingList[idx].split("'")[1].replace('.','')
	print carNumber, len(carNumber)
	if validatorCar(carNumber) is True :
		print 'True 크롤링 포함'
	else :
		print 'True 크롤링 포함안함'