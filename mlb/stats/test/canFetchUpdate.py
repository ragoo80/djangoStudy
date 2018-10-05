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
# from openpyxl import Workbook,load_workbook

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
# pagingList = [
#     "goDetail('04호 9191','dhkim629');",
#     "goDetail('06하 5928','teramin47@naver.com');",
#     "goDetail('13하4869','wjdwprhrh');",
#     "goDetail('28호 8762','ljh1452');",
#     "goDetail('35호3832','recess83');",
#     "goDetail('40하 4590','skyofsiea');",
#     "goDetail('40허 5976','osj2081');",
#     "goDetail('40호 7755','pcroom1990@naver.com');",
#     "goDetail('46호 1798','gamja124');",
#     "goDetail('50하 6731','JUNJIN1189');",
#     "goDetail('50하 6758','unicon90');",
#     "goDetail('54하 3888','dlrndus');",
#     "goDetail('54호 4281','SEOJIN7866');",
#     "goDetail('62하 4841','yep36@naver.com');",
#     "goDetail('62호 1635','lmj6693');",
#     "goDetail('62호 4885','begetal');",
#     "goDetail('62 호8575','aggupa');",
#     "goDetail('64호 2715','hmjang524@naver.com');",
#     "goDetail('69호 5259','kwon121514');"
# ]

pagingList = [
    "goDetail('40하 1985','mnm0313@naver.com');",
    "goDetail('65하7479','min97571@naver.com');",
    "goDetail('67하4428','zamduri');",
    "goDetail('04호1112','nero1997');",
    "goDetail('64하1923','pjy6325@lycos.co.kr');",
    "goDetail('18하 8088','myworld57');",
    "goDetail('67하 9437','skkang@dream-plus.co.kr');",
    "goDetail('65하8548','0803start');",
    "goDetail('18호6849','rjckdbong87');",
    "goDetail('72호 1657','wldmsdkd1350@naver.com');",
    "goDetail('68호2953','oochen14@hanmail.net');",
    "goDetail('18하8224','shonon14@naver.com');",
    "goDetail('62호8311','wkdgmlwp1@nate.com');",
    "goDetail('37호2866','dbswlgns3533@naver.com');",
    "goDetail('18하2193','pnu88@naver.com');",
    "goDetail('44하3150','tttyuu@naver.com');",
    "goDetail('57하 8124','luv22182525@gmail.com');",
    "goDetail('64호8000','wodnd6160@naver.com');",
    "goDetail('67호7612','ljh0358');",
    "goDetail('52호8070','besswil@naver.com');",
    "goDetail('46호5775','loveisblue4');",
    "goDetail('63호 8556','RUDWNS8235');",
    "goDetail('52호8445','josk2297');",
    "goDetail('18호9453','josk2297');",
    "goDetail('58하3058','Aoouoo@naver.com');",
    "goDetail('71하9547','jhm0006');",
    "goDetail('18호1028','navy0422');",
    "goDetail('46호1016','szss');",
    "goDetail('18하2408','cktjdals0228@naver.com');",
    "goDetail('69호5418','8067439@naver.com');",
    "goDetail('44호1571','wminjung1@naver.com');",
    "goDetail('52하9384','dwight3990@naver.com');",
    "goDetail('65하 5079','anar798');",
    "goDetail('67호1588','SUNOODA');",
    "goDetail('46호3149','sexy__8022@naver.com');",
    "goDetail('46호5557','zhak369');",
    "goDetail('64하1183','JOSK2297');",
    "goDetail('68호2891','JOSK2297');",
    "goDetail('67하3567','lovelyhee7@naver.com');",
    "goDetail('52하1085','p5861498@naver.com');",
    "goDetail('64호3035','ohjimin');",
    "goDetail('57하3229','qkekwndnjs');",
    "goDetail('40하5624','hungry108');",
    "goDetail('08호2606','navy0422');",
    "goDetail('04호9244','ciw0818@naver.com');",
    "goDetail('65하8747','popo010');",
    "goDetail('52호1541','vws_mjy1@nate.com');",
    "goDetail('52호1567','aijinsong');",
    "goDetail('46하9639','woalqp');",
    "goDetail('57호5531','c713637');",
    "goDetail('64호4597','jjuuaann555');",
    "goDetail('63하6365','johyun1202@naver.com');",
    "goDetail('65호2497','sirano5b');",
    "goDetail('63하6968','gkakdlq79@naver.com');",
    "goDetail('65하2113','okhmw@naver.com');",
    "goDetail('13호2143','sud123ab');",
    "goDetail('68호2895','whtjrqls');",
    "goDetail('18호7431','wkrdms09');",
    "goDetail('18호4263','yskim6302');",
    "goDetail('35호5555','goodday0806@naver.com');",
    "goDetail('67하4777','isaiah504@naver.com');",
    "goDetail('65호9004','dhromej@naver.com');",
    "goDetail('65호6678','terlbo');",
    "goDetail('66하 5609','kyss93@naver.com');",
    "goDetail('52하5567','rishan777@naver.com');",
    "goDetail('46호1071','yoinsuk@naver.com');",
    "goDetail('69하 1991 ','emmyal');",
    "goDetail('63호1556','cpj2461');",
    "goDetail('46하3738','gunface');",
    "goDetail('65호2394','gnsdlf0112@naver.com');",
    "goDetail('04호 2878','sjlovera');",
    "goDetail('63호2845','x4545');",
]
# prefs = {'profile.managed_default_content_settings.images': 2} -> 느림
# chrome_options.add_experimental_option('prefs', prefs) -> 느림

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('application-cache')
ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver', chrome_options=chrome_options)

ChromeDriver.set_page_load_timeout(20)
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
            with open(
                    os.path.join(default_save_path + 'carImage/' + carNumber.decode('utf-8'),  imgName), "w"
            ) as f:
                f.write(dr)
                # print("저장되었습니다.")
        except urllib2.HTTPError, e:
            print e.code




def carInfoSaveTest(argStr):
    try :
        ChromeDriver.get(urlList['lotte'][1])
    except TimeoutException as e:
        print e

    detail = argStr
    if page_has_loaded() == 'complete' :
        ChromeDriver.execute_script(detail)
        if page_has_loaded() == 'complete' :
            carNumber = detail.split("'")[1].replace(' ','')
            print 'carNumber', detail.split("'")[1].replace(' ','')
            htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
            if htmlSource.select('#error_wrap') == [] :
                # print 'this page is not error page!!!'
                # carDetailInfo = getCarDetailInfo.find_detail_info(htmlSource)
                # print carDetailInfo

                # 차량 사진 없을 경우
                if ( getFolder( carNumber ) == False ) :
                    saveImgage(carNumber, htmlSource)
            else :
                "need collecting error page info"

# --------------------------------------------------------------------------------------------------------------


rowCount = 1
if canFetch(urlList['lotte'][0], urlList['lotte'][1]) :
    startTime =  datetime.datetime.now()
    for idx in range( len(pagingList) ) :
        carInfoSaveTest(pagingList[idx] )
    endTime =  datetime.datetime.now()
    totalTime = endTime - startTime
    print 'totalTime is : ', totalTime
    ChromeDriver.quit()

else :
    # print "can't crawling"
    print loadHTML(urlList['lotte'][1])


