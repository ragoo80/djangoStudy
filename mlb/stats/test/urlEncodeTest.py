# -*- coding: utf-8 -*-
import urllib
import os, os.path, re, datetime, time, robotparser, requests, json
import urllib2
from selenium import webdriver
from PIL import Image

# testUrl = 'https://www.lotterentacar.net/atch/upload/getImage.do?atchFileId=20170109ljh145228%ED%98%B8%208762innerImg_V.jpg&fileSepar=succession'
# testUrl = 'https://www.lotterentacar.net/atch/upload/getImage.do?atchFileId=20160810yep36@naver.com62%ED%95%98%204841leftSideImg_V.jpg&fileSepar=succession'
# https://www.lotterentacar.net/atch/upload/getImage.do?atchFileId=20160810yep36@naver.com62%ED%95%98%204841rightSideImg_V.jpg&fileSepar=succession
# print testUrl.strip().replace(' ', '%20')



# default_save_path = '/Users/elbow/Documents/lotteRent/'
# webdriver_path = '/Users/elbow/Documents/webdriver/'
# ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver')



# def imgLoadCheck(url) :
#     try:
#         urllib2.urlopen(url)
#         return True
#     except urllib2.HTTPError, e:
#         print e.code
#         return False
# print imgLoadCheck(testUrl) is True
# if imgLoadCheck(testUrl) is True:
#     try:
#         urllib.urlretrieve(testUrl, "t3.jpg")
#         # ChromeDriver.save_screenshot("screenshot1.png")
#
#         image = Image.open(os.path.join('/Users/elbow/Documents/study/python/django/mlb/stats/test', 't3.jpg'))
#         rgb_image = image.convert('RGB')
#         r, g, b = rgb_image.getpixel((1, 1))
#         newImg = Image.new('RGB', image.size, (r, g, b))
#         newImg.putdata(image.getdata())
#         newImg.save('t3_convert.jpg')
#
#     except Exception as e:
#         print e



# pagingList 배열 저장하여 있을 경우 불러와서 재사용 test
import numpy as np

pagingList = [
    u"goDetail('04\ud638 1250','stereodesk@naver.com');",
    u"goDetail('63\ud6384552','min97571@naver.com');",
    u"goDetail('48\ud5583590','hemster');"
]
default_save_path = '/Users/elbow/Documents/lotteRent/'
scriptPath = default_save_path + 'userScript/'+ 'pagingData.npz'
np.savez(scriptPath, np.array(pagingList))
testLoad = np.load( default_save_path + 'userScript/'+ 'pagingData.npz' )
arrData = testLoad['arr_0']
print len(testLoad['arr_0']) > 0
print len(arrData) > 0


# print len(arrData)
# for item in arrData:
#     print item







