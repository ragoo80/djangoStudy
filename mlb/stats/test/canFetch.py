# -*- coding: utf-8 -*-

import os

from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




import robotparser, requests, json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
urlList = {
    'lotte' : ["https://www.lotterentacar.net/robots.txt", "https://www.lotterentacar.net/kor/longsuccession/getLongSuccessionList.do"]
}


default_save_path = '/Users/elbow/Documents/lotteRent/'
webdriver_path = '/Users/elbow/Documents/webdriver/'
pageTotal = 0
teamList = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
# ChromeDriver = webdriver.Chrome('/Users/elbow/Documents/webdriver/chromedriver', chrome_options=chrome_options)
ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver')
ChromeDriver.implicitly_wait(3)
rp = robotparser.RobotFileParser()

def canFetch(robotsUrl, loadUrl) :
    rp.set_url(robotsUrl)
    rp.read()
    possible = rp.can_fetch("*", loadUrl)
    return possible

def TransformEnToKo(name) :
    ChromeDriver.get('https://daum.net')
    ChromeDriver.find_element_by_id('q').send_keys(name)
    ChromeDriver.find_element_by_id('daumSearch').submit()
    return BeautifulSoup(ChromeDriver.page_source, 'html.parser').select('.info_tit > a > b')

def setPlayerList() :
    for teamItem in teamList:
        # print(teamItem['name'])
        # print(teamItem['url'])

        players = loadHTML('http://www.nba.com' + teamItem['url']).select('.nba-player-index__row .nba-player-index__name')
        playerList = []

        for player in players :
            playerInfo = {}
            strName = BeautifulSoup(str(player).replace("<br/>", ' '), "html.parser")
            playerInfo['enName'] = strName.text
            playerInfo['krName'] = '';
            playerList.append(playerInfo)
        with open(os.path.join(BASE_DIR, teamItem['name']+'_player_list.json'), 'w+') as json_file:
            json.dump(playerList, json_file)

def setRentList(soup) :
    for car in soup :
        carInfo = {}
        carInfo['name'] = team.text
        carInfo['url'] = team.get('href')
        teamList.append(teamInfo)

def loadHTML(loadUrl) :
    # way1
    req = requests.get(loadUrl)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup
    else :
        raise Exception("can't load html!!!!!!!!!!!!!!!")

def getPageCount():
    # soup = loadHTML(urlList['lotte'][1])
    # print soup.select('.btn_last')[0].get('onclick')
    # setRentList(soup.select('.team__list a'))
    pageTotal = 73

def getFolder(forderName):
    if not( os.path.isdir( default_save_path + 'carImage/' + forderName ) ):
        os.makedirs( os.path.join( default_save_path + 'carImage/' + forderName ) )
        # return 'making' + forderName
        print 'making' + forderName
    else :
        # return str(os.path.join( default_save_path + forderName ))+' already exsit!!'
        print str(os.path.join( default_save_path + 'carImage/' + forderName ))+' already exsit!!'

def carInfoSaveTest():
    ChromeDriver.get(urlList['lotte'][1])
    ChromeDriver.execute_script("goDetail('63하5477','hyh0401@nate.com')")
    htmlSource = BeautifulSoup(ChromeDriver.page_source, 'html.parser')
    imgSrcList = htmlSource.select('.search_view_left img')

    for src in imgSrcList :
        req = urllib2.Request( 'https://www.lotterentacar.net' + src.get('src') )
        data = urllib2.urlopen(req)
        dr = data.read()
        with open( src.get('alt')+'.jpg', mode="wb" ) as f:
            f.write(dr)
            print("저장되었습니다.")

    ChromeDriver.quit()


if canFetch(urlList['lotte'][0], urlList['lotte'][1]) :
    # print 'can crawling'
    getPageCount()
else :
    # print "can't crawling"
    print loadHTML(urlList['lotte'][1])



