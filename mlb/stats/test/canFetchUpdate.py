# -*- coding: utf-8 -*-

import os, os.path, re, datetime, time, robotparser, requests, json

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from openpyxl import Workbook,load_workbook

import getCarDetailInfo


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
urlList = {
    'lotte' : ["https://www.lotterentacar.net/robots.txt", "https://www.lotterentacar.net/kor/longsuccession/getLongSuccessionList.do"]
}

default_save_path = '/Users/elbow/Documents/lotteRent/'
webdriver_path = '/Users/elbow/Documents/webdriver/'
pageTotal = 1
# pagingList = [
#     "goDetail('66하9815','IJB1106');",
#     "goDetail('66하9815','ijb1106');"
# ]
# pagingList = [
#     "goDetail('40하 1985','mnm0313@naver.com');",
#     "goDetail('65하7479','min97571@naver.com');",
#     "goDetail('67하4428','zamduri');",
#     "goDetail('04호1112','nero1997');",
#     "goDetail('64하1923','pjy6325@lycos.co.kr');",
#     "goDetail('18하 8088','myworld57');",
#     "goDetail('67하 9437','skkang@dream-plus.co.kr');",
#     "goDetail('65하8548','0803start');",
#     "goDetail('18호6849','rjckdbong87');",
#     "goDetail('72호 1657','wldmsdkd1350@naver.com');"
# ]
# pagingList = [
#     u"goDetail('9328','so900707@naver.com');"
#     u"goDetail('66\ud558','abukki4');",
#     u"goDetail('03\ud5589000.','leecj1210');",
#     u"goDetail('bmw320d','tissue7587@naver.com');"
#     u"goDetail('50gk7294','trade75');",
#     u"goDetail('71gk9471','CHARMINGJOO');",
#
#     u"goDetail('40\ud5583300','wjdfhr99');",
#     u"goDetail('40\ud5583300','hzz00z@daum.net');",
#     u"goDetail('46\ud6384970','moralman');",
#     u"goDetail('62\ud5584841','yep36@naver.com');",
#     u"goDetail('62\ud6381635','lmj6693');",
#     u"goDetail('50\ud5586758','unicon90');",
#     u"goDetail('54\ud6384281','SEOJIN7866');",
#     u"goDetail('62\ud6384885','begetal');",
#     u"goDetail('62\ud5581857','o1o31339233');",
#     u"goDetail('46\ud6381798','gamja124');",
#     u"goDetail('06\ud5585928','teramin47@naver.com');",
#     u"goDetail('69\ud6388833','tntnem');",
#     u"goDetail('37\ud638 2884','ringosteen@daum.net');",
#
#
#     u"goDetail('46\ud6383262','diawodl2');",
#     u"goDetail('46\ud6383262','sex_sexys@naver.com');",
#     u"goDetail('40\ud638 1436','rla654123');",
#     u"goDetail('40\ud6381436','rla654123');",
#     u"goDetail('64\ud5581398','pomi2000');",
#     u"goDetail('64\ud5581398','realloveljk');",
#     u"goDetail('68\ud5589053','nicewinguy');",
#     u"goDetail('68\ud5589053','DGBUPAY');",
#     u"goDetail('67\ud6381178','dumdum11');",
#     u"goDetail('67\ud6381178','dmstjs785@naver.com');",
# ]
pagingList = [
    # u"goDetail('46\ud6384970','moralman');",
    # u"goDetail('62\ud5584841','yep36@naver.com');",
    u"goDetail('62\ud6381635','lmj6693');",
    # u"goDetail('50\ud5586758','unicon90');",
    # u"goDetail('54\ud6384281','SEOJIN7866');",
    # u"goDetail('62\ud6384885','begetal');",
    # u"goDetail('62\ud5581857','o1o31339233');",
    # u"goDetail('46\ud6381798','gamja124');",
    # u"goDetail('06\ud5585928','teramin47@naver.com');",
]
overLapList = []
imgDownList = [
    u"goDetail('62\ud558 4841','yep36@naver.com');",
    u"goDetail('62\ud638 1635','lmj6693');",
    u"goDetail('54\ud638 4281','SEOJIN7866');",
    u"goDetail('62\ud638 4885','begetal');",
    u"goDetail('62\ud558 1857','o1o31339233');",
    u"goDetail('46\ud638 1798','gamja124');",
    u"goDetail('06\ud558 5928','teramin47@naver.com');",

    u"goDetail('28\ud638 8762','ljh1452');",
    u"goDetail('40\ud5c8 5976','osj2081');",
    u"goDetail('40\ud638 7755','pcroom1990@naver.com');",
    u"goDetail('46\ud638 1798','gamja124');",
    u"goDetail('50\ud558 6731','JUNJIN1189');",
    u"goDetail('50\ud558 6758','unicon90');",
    u"goDetail('54\ud558 3888','dlrndus');",
    u"goDetail('62 \ud6388575','aggupa');",
    u"goDetail('64\ud638 2715','hmjang524@naver.com');",
    u"goDetail('69\ud638 5259','kwon121514');",
    u"goDetail('40\ud558 4590','skyofsiea');",
]
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
# WebDriverWait(ChromeDriver, 10).until(
#     expected_conditions.presence_of_element_located( (By.CSS_SELECTOR, target) )
# )
# return True
def getPageCount():

    # soup = loadHTML(urlList['lotte'][1])
    # last_btn = soup.select('.btn_last')[0].get('onclick')

    # ChromeDriver.get(urlList['lotte'][1])
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
        # print listItem
        for item in listItem :
            pagingList.append(item.get('onclick'))
            # print pagingList

    print 'total pagingList : ', pagingList
    print len(pagingList)
    # for item in pagingList:
    #     print item

def page_has_loaded(driver):
    page_state = driver.execute_script(
        'return document.readyState;'
    )
    return page_state

def getFolder(forderName):
    if not( os.path.isdir( default_save_path + 'carImage/' + forderName ) ):
        # os.makedirs( os.path.join( default_save_path + 'carImage/' + forderName ) )
        # return 'making' + forderName
        # print 'making' + forderName
        print 'create folder'
        return False
    else :
        # return str(os.path.join( default_save_path + forderName ))+' already exsit!!'
        # print str(os.path.join( default_save_path + 'carImage/' + forderName ))+' already exsit!!'
        # print 'already exsit!!'
        return True

def arrayToString(arr) :
    returnStr = ''
    if arr is None or arr is 'Null':
        return 'Null'
    else :
        for idx in range(len(arr)) :
            if ( idx is not 0 ) :
                returnStr += ', '+arr[idx]
            else :
                returnStr += arr[idx]
        return returnStr

def validatorCar(carNumber):
    pattern = re.compile('[a-z|A-Z|ㄱ-]+')
    if len(carNumber.replace(' ','')) != 7 or re.search(pattern, carNumber.encode('utf-8') ) != None:
        print carNumber, ' is not validatorCar'
        return False
    return True

def overLap(carNumber):
    if overLapList.count(carNumber) > 0 :
        print 'overLap carNumber is : ',carNumber
        return True
    else :
        overLapList.append(carNumber)
        return False

def setDownImgList(detail) :
    imgDownList.append(detail)

def downloadImgList():
    imgDriver_options = webdriver.ChromeOptions()
    imgDriver_options.add_argument('application-cache')
    imgDriver_options.add_argument('no-sandbox')
    # imgDriver_options.add_argument('--headless')
    imgDriver = webdriver.Chrome(webdriver_path+'chromedriver', chrome_options=imgDriver_options)

    for idx in range( len(imgDownList) ) :
        imgDriver.get(urlList['lotte'][1])
        if page_has_loaded(imgDriver) == 'complete' :
            if imgDriver.execute_script("return !!window.jQuery;") == False :
                print 'there is no jquery'
                imgDriver.execute_script("scr = document.createElement('script');scr.type=\"text/javascript\";scr.src=\"https://code.jquery.com/jquery-1.12.4.min.js\";document.head.append(scr);")
                time.sleep(3)
            carNumber = imgDownList[idx].split("'")[1]
            print 'carNumber', carNumber
            imgDriver.execute_script(imgDownList[idx])

            if validatorCar(carNumber) is True :
                htmlSource = BeautifulSoup(imgDriver.page_source, 'html.parser')
                if htmlSource.select('#error_wrap') == [] :
                    _carNumber = carNumber.replace(' ','')
                    print '_carNumber', _carNumber
                    if not( os.path.isdir( default_save_path + 'carImage/' + _carNumber ) ):
                        print 'there is not folder'
                        os.makedirs( os.path.join( default_save_path + 'carImage/' + _carNumber ) )
                        saveImage(carNumber, htmlSource)
                    else :
                        print 'there is exsit ', _carNumber
                else :
                    print carNumber, " collecting error page info"
    imgDriver.quit()



def imgLoadCheck(url) :
    try:
        urllib2.urlopen(url)
        return True
    except urllib2.HTTPError, e:
        print e.code
        return False

def saveImage(carNumber, htmlSource):
    print 'saveImage function'
    _carNumber = carNumber.replace(' ','')
    print _carNumber, ' in saveImg function'
    imgSrcList = htmlSource.select('.search_view_left .thumb img')
    # /publish/pcKor/images/common/bg_car_default.png
    for idx in range( len(imgSrcList) ) :
        _url = 'https://www.lotterentacar.net' + imgSrcList[idx].get('src').encode('utf-8')
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
                    os.path.join(default_save_path + 'carImage/' + _carNumber.encode('utf-8'),  imgName), "w"
            ) as f:
                f.write(dr)
                # print("저장되었습니다.")
        except urllib2.HTTPError, e:
            print carNumber, ' is :', e.code

def carInfoSave(argStr):

    try :
        ChromeDriver.get(urlList['lotte'][1])
    except TimeoutException as e:
        print 'when disconnected totalTime is : ', datetime.datetime.now() - startTime
        ChromeDriver.quit()
        # print e

    detail = argStr
    if page_has_loaded(ChromeDriver) == 'complete' :
        carNumber = detail.split("'")[1]
        print 'carNumber', carNumber

        if ChromeDriver.execute_script("return !!window.jQuery;") == False :
            print 'there is no jquery'
            ChromeDriver.execute_script("scr = document.createElement('script');scr.type='text/javascript';scr.src='https://code.jquery.com/jquery-1.12.4.min.js';document.head.append(scr);")
            time.sleep(3)

        if validatorCar(carNumber) is True and overLap(carNumber) is False :
            ChromeDriver.execute_script(detail)
            htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
            if htmlSource.select('#error_wrap') == [] :
                # print 'this page is normal page!!!'

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

                if getFolder( carNumber.replace('.','') ) == False :
                    setDownImgList(detail)
            else :
                print carNumber, " collecting error page info"

# --------------------------------------------------------------------------------------------------------------

ws = None
rowCount = 1

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--dns-prefetch-disable')
prefs = {'disk-cache-size': 4096, 'profile.managed_default_content_settings.images': 2}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('application-cache')
chrome_options.add_argument('no-sandbox')
ChromeDriver = ''

if canFetch(urlList['lotte'][0], urlList['lotte'][1]) :

    startTime =  datetime.datetime.now()

    # ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver', chrome_options=chrome_options)
    # ChromeDriver.set_page_load_timeout(150)
    #
    #
    # try :
    #     ChromeDriver.get(urlList['lotte'][1])
    # except TimeoutException as e:
    #     print 'when disconnected totalTime is : ', datetime.datetime.now() - startTime
    #     ChromeDriver.quit()
    #     print e
    #
    # getPageCount()
    #
    # today = str( datetime.datetime.today().strftime('%Y-%m-%d') )
    # fileName = default_save_path + 'excel/lotteRent-'+ today + '.xlsx'
    # if os.path.exists( fileName ):
    #     wb = load_workbook(fileName)
    # else :
    #     wb = load_workbook(default_save_path + 'excel/basic.xlsx')
    #     ws = wb.active
    #     ws.title = today
    #     rowCount = ws.max_row
    #     print 'first rowCount : ', rowCount
    #
    # for idx in range( len(pagingList) ) :
    #     rowCount = rowCount + 1
    #     carInfoSave(pagingList[idx] )
    #
    # ChromeDriver.quit()

    if len(imgDownList) > 0 :
        downloadImgList()
    print 'imgDownList is :', imgDownList


    endTime =  datetime.datetime.now()
    totalTime = endTime - startTime
    print 'totalTime is : ', totalTime


else :
    # print "can't crawling"
    print loadHTML(urlList['lotte'][1])


