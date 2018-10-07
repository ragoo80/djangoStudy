# -*- coding: utf-8 -*-

import os
import os.path
import time

from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

import datetime
from openpyxl import Workbook,load_workbook

import getCarDetailInfo


# http://thiagomarzagao.com/2013/11/16/webscraping-with-selenium-part-4/


import robotparser, requests, json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
urlList = {
    'lotte' : ["https://www.lotterentacar.net/robots.txt", "https://www.lotterentacar.net/kor/longsuccession/getLongSuccessionList.do"]
}


# default_save_path = '/Users/elbow/Documents/lotteRent/'
default_save_path = '/Users/ragoo80/Documents/lotteRent/'
webdriver_path = '/Users/ragoo80/Documents/webdriver/'
pageTotal = 1
# pagingList = [
#     "goDetail('66하9815','IJB1106');",
#     "goDetail('66하9815','ijb1106');"
# ]
pagingList = [u"goDetail('46\ud6385532','park2968@naver.com');", u"goDetail('18\ud5588384','skyminseok');", u"goDetail('69\ud6388833','tntnem');", u"goDetail('57\ud6387542','Gh389001@naver.com');", u"goDetail('65\ud5584181','wolfdog88');", u"goDetail('46\ud5583943','L0620HJ');", u"goDetail('52\ud5584883','tmdwjd101@naver.com');", u"goDetail('14\ud6383314','ahs8888');", u"goDetail('15\ud5581193','start1251');", u"goDetail('40\ud5581846','chicksik@hanmail.net');", u"goDetail('40\ud558 6126','coolmercy');", u"goDetail('57\ud5583843','fffsd432@naver.com');", u"goDetail('65\ud558 7785','ssjjhnhn@nate.com');", u"goDetail('63\ud5587673','kwangsroh');", u"goDetail('72\ud5582334','jsh050216@gmail.com');", u"goDetail('44\ud558 4674','6aksmef');", u"goDetail('68\ud6382325','kyseun1');", u"goDetail('63\ud6381684','junghyun8537');", u"goDetail('04\ud638 9191','dhkim629');", u"goDetail('18\ud6387343','brandy78');", u"goDetail('63\ud6382648','135110');", u"goDetail('40\ud6387798','lionel9020@gmail.com');", u"goDetail('57 \ud638 9023','wnsahsla');", u"goDetail('67\ud5583552','aranjuez11');", u"goDetail('52\ud6381587','silk1020@daum.net');", u"goDetail('44\ud6385509','powsdw77@naver.com');", u"goDetail('63\ud5585477','hyh0401@nate.com');", u"goDetail('52\ud6381069','sk3d3');", u"goDetail('57\ud5584992','iprince7');", u"goDetail('04\ud638 9739','alan0913@naver.com');", u"goDetail('46\ud6383262','sex_sexys@naver.com');", u"goDetail('18\ud6386735','ljh0358');", u"goDetail('63\ud5587628','jhjy0314@nate.com');", u"goDetail('67\ud5589254','ojh4997');", u"goDetail('62\ud6388811','sic781@hanmail.net');", u"goDetail('64\ud5585423','dudnwkdal');", u"goDetail('52\ud5581282','jang7480');", u"goDetail('69\ud6389081','ph___one@nate.com');", u"goDetail('65\ud638 6084','hanth2100');", u"goDetail('14\ud6382170','dmpp');", u"goDetail('52\ud6388181','djsyyyaaa@naver.com');", u"goDetail('67\ud6384400','aembaeng');", u"goDetail('44\ud6385696','eodyd557@naver.com');", u"goDetail('18\ud5586242','kj3003');", u"goDetail('68\ud5585253','dgw1002');", u"goDetail('27\ud6385930','ktk7373');", u"goDetail('67\ud5589080','virgo460@hanmail.net');", u"goDetail('52\ud5587321','iprince7');", u"goDetail('68\ud6386700','bsb92');", u"goDetail('65\ud5582019','kpit');", u"goDetail('40\ud558 5306','osj2081');", u"goDetail('40\ud5586139','JOSK2297');", u"goDetail('65\ud5588233','zzeng911');"]
# pagingList = []

# prefs = {'profile.managed_default_content_settings.images': 2} -> 느림
# chrome_options.add_experimental_option('prefs', prefs) -> 느림

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('application-cache')
ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver', chrome_options=chrome_options)

ChromeDriver.set_page_load_timeout(50)
rp = robotparser.RobotFileParser()



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

# list = ChromeDriver.find_element_by_css_selector('.thumb li')
# html = ChromeDriver.find_element_by_tag_name('html')

def getPageCount():

    # soup = loadHTML(urlList['lotte'][1])
    # last_btn = soup.select('.btn_last')[0].get('onclick')

    ChromeDriver.get(urlList['lotte'][1])
    htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
    last_btn = htmlSource.select('.btn_last')[0].get('onclick')
    start = last_btn.find("(")
    end = last_btn.find(")")
    pageTotal = int( last_btn[ int(start+1):int(end) ] )
    print 'pageTotal is : ', pageTotal


    for idx in range(pageTotal) :
        if ( idx > 0 ) :
            # script = 'goPage(' + str(idx+1) +')'
            # ChromeDriver.execute_script(script)

            script = "document.getElementById('pageIndex').value = %s" % str(idx+1)
            print script
            ChromeDriver.execute_script(script)
            ChromeDriver.execute_script("document.getElementById('frm').action = '/kor/longsuccession/getLongSuccessionList.do'")
            ChromeDriver.execute_script("document.getElementById('frm').submit()")


        htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
        listItem = htmlSource.select('.list_car dt a')
        for item in listItem :
            pagingList.append(item.get('onclick'))

    print 'pagingList : ', pagingList
    # for item in pagingList:
    #     print item


def page_has_loaded():
    page_state = ChromeDriver.execute_script(
        'return document.readyState;'
    )
    return page_state

def getFolder(forderName):
    if not( os.path.isdir( default_save_path + 'carImage/' + forderName ) ):
        os.makedirs( os.path.join( default_save_path + 'carImage/' + forderName ) )
        # return 'making' + forderName
        # print 'making' + forderName
        print 'create folder'
        return False
    else :
        # return str(os.path.join( default_save_path + forderName ))+' already exsit!!'
        # print str(os.path.join( default_save_path + 'carImage/' + forderName ))+' already exsit!!'
        print 'already exsit!!'
        return True


# WebDriverWait(ChromeDriver, 10).until(
#     expected_conditions.presence_of_element_located( (By.CSS_SELECTOR, target) )
# )
# return True

def arrayToString(arr) :
    returnStr = ''
    if arr is None :
        return 'Null'
    else :
        for idx in range(len(arr)) :
            if ( idx is not 0 ) :
                returnStr += ', '+arr[idx]
            else :
                returnStr += arr[idx]
        return returnStr

def imgLoadCheck(url) :
    try:
        urllib2.urlopen(url)
        return True
    except urllib2.HTTPError, e:
        print e.code
        return False

def saveImgage(carNumber, htmlSource):
    imgSrcList = htmlSource.select('.search_view_left .thumb img')
    # /publish/pcKor/images/common/bg_car_default.png
    for idx in range( len(imgSrcList) ) :
        _url = 'https://www.lotterentacar.net' + imgSrcList[idx].get('src')
        try:
            req = urllib2.Request( _url )
            data = urllib2.urlopen(req)
            dr = data.read()
            imgName = ''
            if imgSrcList[idx].get('alt') == '' :
                if imgSrcList[idx].get('src') == '/publish/pcKor/images/common/bg_car_default.png' :
                    imgName = 'bg_car_default.jpg'
                else :
                    imgName = 'image' + str(idx) + '.jpg'
            else :
                # imgName = imgSrcList[idx].get('alt')+str(idx)+'.jpg'
                imgName = 'image'+str(idx)+'.jpg'

            # print imgSrcList[idx].get('alt')
            with open(
                    # '66하9815'-> carNumber.decode('utf-8')
                    # '46\ud6385532'-> carNumber.encode('utf-8')
                    os.path.join(default_save_path + 'carImage/' + carNumber.encode('utf-8'),  imgName), "w"
            ) as f:
                f.write(dr)
                # print("저장되었습니다.")
        except urllib2.HTTPError, e:
            print e.code




def carInfoSaveTest(argStr):
    # try :
    #     ChromeDriver.get(urlList['lotte'][1])
    # except TimeoutException as e:
    #     print e



    detail = argStr
    if page_has_loaded() == 'complete' :
        if pagingList[0] == detail :
            ChromeDriver.execute_script(detail)
        else :
            ChromeDriver.execute_script("scr = document.createElement('script');scr.type=\"text/javascript\";scr.textContent = \"function goDetail(carNumber,userId){$('#carNumber').val(carNumber);$('#userId').val(userId);$('#frm').attr('action','/kor/longsuccession/getLongSuccessionDetail.do').submit();}\";document.head.append(scr);")
            ChromeDriver.execute_script(detail)
            carNumber = detail.split("'")[1].replace(' ','')
            print 'carNumber', detail.split("'")[1].replace(' ','')
            htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
            if htmlSource.select('#error_wrap') == [] :
                # print 'this page is not error page!!!'

                carDetailInfo = getCarDetailInfo.find_detail_info(htmlSource)
                # print carDetailInfo

                ws.cell( rowCount,1,carDetailInfo['basicInfo']['title'] )
                ws.cell( rowCount,2,carDetailInfo['basicInfo']['month_price'] )
                ws.cell( rowCount,3,carDetailInfo['basicInfo']['remain_month'] )
                ws.cell( rowCount,4,carDetailInfo['basicInfo']['date'] )

                ws.cell( rowCount,5,carDetailInfo['saleInfo']['saler'] )
                ws.cell( rowCount,6,carDetailInfo['saleInfo']['email'] )
                ws.cell( rowCount,7,carDetailInfo['saleInfo']['cellphone'] )
                ws.cell( rowCount,8,carDetailInfo['saleInfo']['area'] )

                ws.cell( rowCount,9,carDetailInfo['carInfo']['carMaker'] )
                ws.cell( rowCount,10,carDetailInfo['carInfo']['carName'] )
                ws.cell( rowCount,11,carDetailInfo['carInfo']['carNumber'] )
                ws.cell( rowCount,12,carDetailInfo['carInfo']['color'] )
                ws.cell( rowCount,13,carDetailInfo['carInfo']['kind'] )
                ws.cell( rowCount,14,carDetailInfo['carInfo']['fuel'] )
                ws.cell( rowCount,15,carDetailInfo['carInfo']['distance'] )

                ws.cell( rowCount,16,carDetailInfo['contractInfo']['status'] )
                ws.cell( rowCount,17,carDetailInfo['contractInfo']['product'] )
                ws.cell( rowCount,18,carDetailInfo['contractInfo']['Distance'] )
                ws.cell( rowCount,19,carDetailInfo['contractInfo']['takeOver'] )
                ws.cell( rowCount,20,carDetailInfo['contractInfo']['gurantee'] )
                ws.cell( rowCount,21,carDetailInfo['contractInfo']['advance'] )
                ws.cell( rowCount,22,carDetailInfo['contractInfo']['indemnfication'] )
                ws.cell( rowCount,23,carDetailInfo['contractInfo']['support'] )

                ws.cell( rowCount,24,arrayToString( carDetailInfo['optionInfo']['comfortable'] ))
                ws.cell( rowCount,25,arrayToString( carDetailInfo['optionInfo']['safety'] ))
                ws.cell( rowCount,26,arrayToString( carDetailInfo['optionInfo']['etc'] ))

                ws.cell( rowCount,27,carDetailInfo['desc'] )

                wb.save(fileName)

                # if getFolder( carNumber ) == False :
                #     saveImgage(carNumber, htmlSource)
            else :
                "need collecting error page info"

# --------------------------------------------------------------------------------------------------------------

ws = None
rowCount = 1
if canFetch(urlList['lotte'][0], urlList['lotte'][1]) :

    startTime =  datetime.datetime.now()
    # getPageCount()
    today = str( datetime.datetime.today().strftime('%Y-%m-%d') )
    fileName = default_save_path + 'excel/lotteRent-'+ today + '.xlsx'
    if os.path.exists( fileName ):
        wb = load_workbook(fileName)
    else :
        wb = load_workbook(default_save_path + 'excel/basic.xlsx')
    ws = wb.active
    ws.title = today
    rowCount = ws.max_row
    print 'first rowCount : ', rowCount


    try :
        ChromeDriver.get(urlList['lotte'][1])
    except TimeoutException as e:
        print e
    for idx in range( len(pagingList) ) :
        rowCount = rowCount + 1
        carInfoSaveTest(pagingList[idx] )
    endTime =  datetime.datetime.now()
    totalTime = endTime - startTime
    print 'totalTime is : ', totalTime
    ChromeDriver.quit()

else :
    # print "can't crawling"
    print loadHTML(urlList['lotte'][1])


