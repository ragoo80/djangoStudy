# -*- coding: utf-8 -*-

import os

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver

import robotparser, requests, json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
urlList = {
    'lotte' : ["https://www.lotterentacar.net/robots.txt", "https://www.lotterentacar.net/kor/longsuccession/getLongSuccessionList.do"]
}


default_save_path = '/Users/elbow/Documents/lotteRent/'
webdriver_path = '/Users/elbow/Documents/webdriver/'
pageTotal = 0


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
# ChromeDriver = webdriver.Chrome('/Users/elbow/Documents/webdriver/chromedriver', chrome_options=chrome_options)
ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver')
ChromeDriver.implicitly_wait(3)
rp = robotparser.RobotFileParser()


# 차량 정보에서 가져와야 될 정보들 항목
# * 타이틀
# * 월 대여료 - 원 단위 -> 단위 고정
# * 잔여계약 기간 - 개월수, yy-mm
# * 판매자 정보 - 판매자, 이메일, 휴대전화, 지역
# * 차량정보 - 제조사, 차량명, 차량번호, 색상, 차종, 연료, 주행거리(km)
# * 계약정보 - 상태,정비상품, 약정주행거리, 인수가, 보증금, 선납금, 면책금, 추가지원금
# * 옵션 정보 - 편의장치, 안전장치, 기타
# * 차량설명

def canFetch(robotsUrl, loadUrl) :
    rp.set_url(robotsUrl)
    rp.read()
    possible = rp.can_fetch("*", loadUrl)
    return possible

def loadHTML(loadUrl) :
    # way1
    req = requests.get(loadUrl)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    else :
        raise Exception("can't load html!!!!!!!!!!!!!!!")

def getPageCount():
    pageTotal = 73


def carInfoSaveTest():
    ChromeDriver.get(urlList['lotte'][1])
    htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
    carList = htmlSource.select('.img a')
    # print len(carList)
    # print carList[0]
    # print carList[0].get('onclick')

    for idx in range(len(carList)) :
        s = carList[idx].get('onclick')
        splited = s.split("'")
        print splited[1], splited[3]


    # if len(carList) > 0 :
    #     for car in carList :
    #         item = car[0].get('onclick')
    #         splited = item.split("'")
    #         print splited[1], splited[3]
    # else :
    #     print 'carList 항목은 0개 입니다'

    ChromeDriver.quit()


if canFetch(urlList['lotte'][0], urlList['lotte'][1]) :
    # getPageCount()
    carInfoSaveTest()
else :
    print loadHTML(urlList['lotte'][1])



