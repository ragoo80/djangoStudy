# -*- coding: utf-8 -*-

import os, re

pattern = re.compile(r'\s+')

def NoneCheck(txt):
    if txt == '' or txt == ',000' :
        return 'Null'
    else :
        return txt


def delBlank(txt):
    txt = txt.encode('utf-8')
    txt = re.sub(pattern, '', txt)
    txt = txt.replace('\r','').replace('\n','').replace('km','').replace('만원','')
    return txt

def commaCheck(thUnit) :
    thUnit = thUnit.encode('utf-8')
    thUnit = re.sub(pattern, '', thUnit)
    thUnit = thUnit.replace('\r','').replace('\n','').replace('km','').replace('만원','')
    if (thUnit != '0') and (thUnit != '') :
        if (thUnit.count(',') == 0) and (len(thUnit) < 4) :
            thUnit += ',000'
    return thUnit


def find_detail_info(htmlSource):
    # print 'from canFetch htmlSource is :', htmlSource

    carInfo = {}
    carInfo['basicInfo'] = {}
    # carInfo['basicInfo']['title'] = htmlSource.select_one('h2').text
    carInfo['basicInfo']['title'] = htmlSource.select('h2')[0].text

    carInfo['basicInfo']['month_price'] = commaCheck( htmlSource.find_all('span', string='월 대여료')[0].find_next_sibling().text )
    carInfo['basicInfo']['remain_month'] = htmlSource.select_one('#remainMonth').text
    carInfo['basicInfo']['date'] = htmlSource.select_one('.term .date').text

    # 판매자 정보
    carInfo['saleInfo'] = {}
    carInfo['saleInfo']['saler'] = htmlSource.find_all('th', string='판매자')[0].find_next_sibling().text
    carInfo['saleInfo']['email'] = htmlSource.find_all('th', string='이메일')[0].find_next_sibling().text
    carInfo['saleInfo']['cellphone'] = htmlSource.find_all('th', string='휴대전화')[0].find_next_sibling().text
    carInfo['saleInfo']['area'] = htmlSource.find_all('th', string='지역')[0].find_next_sibling().text
    # 차량 정보
    carInfo['carInfo'] = {}
    carInfo['carInfo']['carMaker'] = htmlSource.find_all('th', string='제조사')[0].find_next_sibling().text
    carInfo['carInfo']['carName'] = htmlSource.find_all('th', string='차량명')[0].find_next_sibling().text
    carInfo['carInfo']['carNumber'] = htmlSource.find_all('th', string='차량번호')[0].find_next_sibling().text.replace(' ','')
    carInfo['carInfo']['color'] = htmlSource.find_all('th', string='색상')[0].find_next_sibling().text
    carInfo['carInfo']['kind'] = htmlSource.find_all('th', string='차종')[0].find_next_sibling().text
    carInfo['carInfo']['fuel'] = htmlSource.find_all('th', string='연료')[0].find_next_sibling().text
    carInfo['carInfo']['distance'] = commaCheck( htmlSource.find_all('th', string='주행거리')[0].find_next_sibling().text )
    # 계약 정보
    carInfo['contractInfo'] = {}
    carInfo['contractInfo']['status'] = delBlank( htmlSource.find_all('th', string='상태')[0].find_next_sibling().text )
    carInfo['contractInfo']['product'] = delBlank( htmlSource.find_all('th', string='정비상품')[0].find_next_sibling().text )
    carInfo['contractInfo']['Distance'] = delBlank( htmlSource.find_all('th', string='약정주행거리')[0].find_next_sibling().text )
    carInfo['contractInfo']['takeOver'] = NoneCheck( commaCheck( htmlSource.find_all('th', string='인수가')[0].find_next_sibling().text ))
    carInfo['contractInfo']['gurantee'] = NoneCheck( commaCheck( htmlSource.find_all('th', string='보증금')[0].find_next_sibling().text ))
    carInfo['contractInfo']['advance'] = NoneCheck( commaCheck( htmlSource.find_all('th', string='선납금')[0].find_next_sibling().text ))
    carInfo['contractInfo']['indemnfication'] = NoneCheck( commaCheck( htmlSource.find_all('th', string='면책금')[0].find_next_sibling().text ))
    carInfo['contractInfo']['support'] = NoneCheck( commaCheck( htmlSource.find_all('th', string='추가지원금')[0].find_next_sibling().text ))


    # 옵션정보 - 편의 장치
    comfortable = htmlSource.select('.option_info .txt_list')[0].select('.check')
    carInfo['optionInfo'] = {}
    if len(comfortable) is 0 :
        # print 'comfortable is None'
        carInfo['optionInfo']['comfortable'] = None
    else :
        carInfo['optionInfo']['comfortable'] = []
        for item in comfortable :
            # print 'comfortable item is : ', item.text
            carInfo['optionInfo']['comfortable'].append(item.text)

    # 옵션정보 - 안전 장치
    safety = htmlSource.select('.option_info .txt_list')[1].select('.check')
    if len(safety) is 0 :
        # print 'safety is None'
        carInfo['optionInfo']['safety'] = None
    else :
        carInfo['optionInfo']['safety'] = []
        for item in safety :
            # print 'safety item is : ', item.text
            carInfo['optionInfo']['safety'].append(item.text)

    # 옵션정보 - 기타
    etc = htmlSource.select('.option_info .txt_list')[2].select('.check')
    if len(etc) is 0 :
        # print 'safety is None'
        carInfo['optionInfo']['etc'] = None
    else :
        carInfo['optionInfo']['etc'] = []
        for item in etc :
            # print 'etc item is : ', item.text
            carInfo['optionInfo']['etc'].append(item.text)

    # 차량 설명
    carInfo['desc'] = htmlSource.find_all('h3', string="차량 설명")[0].find_next_sibling().text
    # print carInfo

    return carInfo