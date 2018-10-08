# -*- coding: utf-8 -*-

import os
import os.path
import time
import re

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
pagingList = [u"goDetail('48\ud5583590','hemster');", u"goDetail('49\ud5589007','neoxix');", u"goDetail('65\ud5582149','looklook@nate.com');", u"goDetail('64\ud5589061','wndnjs5804');", u"goDetail('68\ud5583435','chs1972');", u"goDetail('46\ud6385532','park2968@naver.com');", u"goDetail('18\ud5588384','skyminseok');", u"goDetail('69\ud6388833','tntnem');", u"goDetail('57\ud6387542','Gh389001@naver.com');", u"goDetail('65\ud5584181','wolfdog88');", u"goDetail('46\ud5583943','L0620HJ');", u"goDetail('52\ud5584883','tmdwjd101@naver.com');", u"goDetail('14\ud6383314','ahs8888');", u"goDetail('15\ud5581193','start1251');", u"goDetail('40\ud5581846','chicksik@hanmail.net');", u"goDetail('40\ud558 6126','coolmercy');", u"goDetail('57\ud5583843','fffsd432@naver.com');", u"goDetail('65\ud558 7785','ssjjhnhn@nate.com');", u"goDetail('63\ud5587673','kwangsroh');", u"goDetail('72\ud5582334','jsh050216@gmail.com');", u"goDetail('44\ud558 4674','6aksmef');", u"goDetail('68\ud6382325','kyseun1');", u"goDetail('63\ud6381684','junghyun8537');", u"goDetail('04\ud638 9191','dhkim629');", u"goDetail('18\ud6387343','brandy78');", u"goDetail('63\ud6382648','135110');", u"goDetail('40\ud6387798','lionel9020@gmail.com');", u"goDetail('57 \ud638 9023','wnsahsla');", u"goDetail('67\ud5583552','aranjuez11');", u"goDetail('52\ud6381587','silk1020@daum.net');", u"goDetail('44\ud6385509','powsdw77@naver.com');", u"goDetail('63\ud5585477','hyh0401@nate.com');", u"goDetail('52\ud6381069','sk3d3');", u"goDetail('57\ud5584992','iprince7');", u"goDetail('04\ud638 9739','alan0913@naver.com');", u"goDetail('46\ud6383262','sex_sexys@naver.com');", u"goDetail('18\ud6386735','ljh0358');", u"goDetail('63\ud5587628','jhjy0314@nate.com');", u"goDetail('67\ud5589254','ojh4997');", u"goDetail('62\ud6388811','sic781@hanmail.net');", u"goDetail('64\ud5585423','dudnwkdal');", u"goDetail('52\ud5581282','jang7480');", u"goDetail('69\ud6389081','ph___one@nate.com');", u"goDetail('65\ud638 6084','hanth2100');", u"goDetail('14\ud6382170','dmpp');", u"goDetail('52\ud6388181','djsyyyaaa@naver.com');", u"goDetail('67\ud6384400','aembaeng');", u"goDetail('44\ud6385696','eodyd557@naver.com');", u"goDetail('18\ud5586242','kj3003');", u"goDetail('68\ud5585253','dgw1002');", u"goDetail('27\ud6385930','ktk7373');", u"goDetail('67\ud5589080','virgo460@hanmail.net');", u"goDetail('52\ud5587321','iprince7');", u"goDetail('68\ud6386700','bsb92');", u"goDetail('65\ud5582019','kpit');", u"goDetail('40\ud558 5306','osj2081');", u"goDetail('40\ud5586139','JOSK2297');", u"goDetail('65\ud5588233','zzeng911');", u"goDetail('04\ud638 2454','Jangbi73@naver.com');", u"goDetail('67\ud5588935','romeo37');", u"goDetail('63\ud6388728','p5411090');", u"goDetail('04\ud638 5684','ccb1020');", u"goDetail('65\ud5586676','mogikkm');", u"goDetail('46\ud6383292','tosoulmate');", u"goDetail('18\ud6387502','chals1129');", u"goDetail('04\ud6385079','okok8630');", u"goDetail('52\ud6381793','okok8630');", u"goDetail('57\ud6383573','goodnk2@naver.com');", u"goDetail('18\ud5581288','ejrwnddlek@naver.com');", u"goDetail('65\ud5587073','eunbi1226');", u"goDetail('52\ud5589582','ADQESW123');", u"goDetail('04\ud6387888','claydoll1980');", u"goDetail('68\ud5583718','bmyong');", u"goDetail('44\ud6388859','raser114@naver.com');", u"goDetail('32\ud6381402','kkkrlawhdghk@naver.com');", u"goDetail('63\ud6388687','dbdnjswhd24@naver.com');", u"goDetail('62\ud6386587','khlion99');", u"goDetail('40\ud5583156','jinkyo_han@naver.com');", u"goDetail('65\ud5586878','wkdrlgns91');", u"goDetail('63\ud558 5001','mje7942@gmail.com');", u"goDetail('18\ud5582622','silverlwh');", u"goDetail('40\ud558 6718','s0188');", u"goDetail('40\ud5583457','shwkdehs89');", u"goDetail('04\ud6387684','hyosook1220');", u"goDetail('04\ud6381379','webtle');", u"goDetail('69\ud6385546','wjdgj963');", u"goDetail('57\ud5584970','happytnr');", u"goDetail('18\ud6388118','lucky7max');", u"goDetail('68\ud6389887','jungwan');", u"goDetail('64\ud558 2239','kkkhhhee@hanmail.net');", u"goDetail('01\ud5586072','byeong158@naver.com');", u"goDetail('63\ud5585991','jhw2553');", u"goDetail('40\ud5586718','s0188');", u"goDetail('57\ud5583058','Aoouoo@naver.com');", u"goDetail('04\ud6385684','ccb1020');", u"goDetail('52\ud6381706','wslcho');", u"goDetail('46\ud6384022','min97571@naver.com');", u"goDetail('40\ud558 1985','mnm0313@naver.com');", u"goDetail('65\ud5587479','min97571@naver.com');", u"goDetail('67\ud5584428','zamduri');", u"goDetail('04\ud6381112','nero1997');", u"goDetail('64\ud5581923','pjy6325@lycos.co.kr');", u"goDetail('18\ud558 8088','myworld57');", u"goDetail('67\ud558 9437','skkang@dream-plus.co.kr');", u"goDetail('65\ud5588548','0803start');", u"goDetail('18\ud6386849','rjckdbong87');", u"goDetail('72\ud638 1657','wldmsdkd1350@naver.com');", u"goDetail('68\ud6382953','oochen14@hanmail.net');", u"goDetail('18\ud5588224','shonon14@naver.com');", u"goDetail('62\ud6388311','wkdgmlwp1@nate.com');", u"goDetail('37\ud6382866','dbswlgns3533@naver.com');", u"goDetail('18\ud5582193','pnu88@naver.com');", u"goDetail('44\ud5583150','tttyuu@naver.com');", u"goDetail('57\ud558 8124','luv22182525@gmail.com');", u"goDetail('64\ud6388000','wodnd6160@naver.com');", u"goDetail('67\ud6387612','ljh0358');", u"goDetail('52\ud6388070','besswil@naver.com');", u"goDetail('46\ud6385775','loveisblue4');", u"goDetail('63\ud638 8556','RUDWNS8235');", u"goDetail('52\ud6388445','josk2297');", u"goDetail('18\ud6389453','josk2297');", u"goDetail('58\ud5583058','Aoouoo@naver.com');", u"goDetail('71\ud5589547','jhm0006');", u"goDetail('18\ud6381028','navy0422');", u"goDetail('46\ud6381016','szss');", u"goDetail('18\ud5582408','cktjdals0228@naver.com');", u"goDetail('69\ud6385418','8067439@naver.com');", u"goDetail('44\ud6381571','wminjung1@naver.com');", u"goDetail('52\ud5589384','dwight3990@naver.com');", u"goDetail('65\ud558 5079','anar798');", u"goDetail('67\ud6381588','SUNOODA');", u"goDetail('46\ud6383149','sexy__8022@naver.com');", u"goDetail('46\ud6385557','zhak369');", u"goDetail('64\ud5581183','JOSK2297');", u"goDetail('68\ud6382891','JOSK2297');", u"goDetail('67\ud5583567','lovelyhee7@naver.com');", u"goDetail('52\ud5581085','p5861498@naver.com');", u"goDetail('64\ud6383035','ohjimin');", u"goDetail('57\ud5583229','qkekwndnjs');", u"goDetail('40\ud5585624','hungry108');", u"goDetail('08\ud6382606','navy0422');", u"goDetail('04\ud6389244','ciw0818@naver.com');", u"goDetail('65\ud5588747','popo010');", u"goDetail('52\ud6381541','vws_mjy1@nate.com');", u"goDetail('52\ud6381567','aijinsong');", u"goDetail('46\ud5589639','woalqp');", u"goDetail('57\ud6385531','c713637');", u"goDetail('64\ud6384597','jjuuaann555');", u"goDetail('63\ud5586365','johyun1202@naver.com');", u"goDetail('65\ud6382497','sirano5b');", u"goDetail('63\ud5586968','gkakdlq79@naver.com');", u"goDetail('65\ud5582113','okhmw@naver.com');", u"goDetail('13\ud6382143','sud123ab');", u"goDetail('68\ud6382895','whtjrqls');", u"goDetail('18\ud6387431','wkrdms09');", u"goDetail('18\ud6384263','yskim6302');", u"goDetail('35\ud6385555','goodday0806@naver.com');", u"goDetail('67\ud5584777','isaiah504@naver.com');", u"goDetail('65\ud6389004','dhromej@naver.com');", u"goDetail('65\ud6386678','terlbo');", u"goDetail('66\ud558 5609','kyss93@naver.com');", u"goDetail('52\ud5585567','rishan777@naver.com');", u"goDetail('46\ud6381071','yoinsuk@naver.com');", u"goDetail('69\ud558 1991 ','emmyal');", u"goDetail('63\ud6381556','cpj2461');", u"goDetail('46\ud5583738','gunface');", u"goDetail('65\ud6382394','gnsdlf0112@naver.com');", u"goDetail('04\ud638 2878','sjlovera');", u"goDetail('63\ud6382845','x4545');", u"goDetail('04\ud6382672','k-sungj');", u"goDetail('67\ud5581360','zxcv6602@hanmail.net');", u"goDetail('57\ud638 5531','c713637');", u"goDetail('40\ud6383548','dywmatkcnsrl');", u"goDetail('52\ud5585113','wavelet');", u"goDetail('52\ud5585023','badboyksw');", u"goDetail('52\ud6388482','gustn8626@nave.com');", u"goDetail('63\ud638 3590','dpfla0725');", u"goDetail('67\ud558 6721','duveen');", u"goDetail('08\ud6381588','BLACK4287');", u"goDetail('62\ud638 4046','yong0935@naver.com');", u"goDetail('64\ud5581398','pomi2000');", u"goDetail('68\ud5585805','super386');", u"goDetail('12\ud6382336','dlrgh06');", u"goDetail('66\ud638 5906','neolkw');", u"goDetail('46\ud5587427','fnie0572@hanmail.net');", u"goDetail('69\ud5581256','mjnh2365@hanmail.net');", u"goDetail('62\ud6381546','kristar427@naver.com');", u"goDetail('18\ud6381699','kijimo77');", u"goDetail('66\ud6386097','qudcjf22');", u"goDetail('67\ud5581371','dlsdyd777@naver.com');", u"goDetail('67\ud6381104','darklode@naver.com');", u"goDetail('40\ud5585046','adsd1323');", u"goDetail('68\ud5589350','bleubird@hotmail.co.kr');", u"goDetail('04\ud638 2602','ertfgyn');", u"goDetail('04\ud638 2599','ertfgyn');", u"goDetail('65\ud5588170','rhkrwhdtjq');", u"goDetail('52\ud5581511','qkrrlduf12@naver.com');", u"goDetail('18\ud5586617','ssun-ey@hanmail.net');", u"goDetail('46\ud6384027','hshhong5733@naver.com');", u"goDetail('40\ud558 3300','wjdfhr99');", u"goDetail('18\ud6387314','qkdrnaks01');", u"goDetail('52\ud638 3306','mooooos');", u"goDetail('63\ud5587856','whg963');", u"goDetail('67\ud6381069','seeit73@dnam.com');", u"goDetail('72\ud5581942','hajehanul');", u"goDetail('36\ud638 3798','ch12oy');", u"goDetail('04\ud6382661','s01089264536');", u"goDetail('67\ud6381119','kimjw4799');", u"goDetail('65\ud6387852','s01089264536');", u"goDetail('65\ud638 9235','milkyj21');", u"goDetail('17\ud5c81004','tkfal1');", u"goDetail('67\ud6386183','pjh6393');", u"goDetail('63\ud6389887','jungwan');", u"goDetail('52\ud5589758','er8000');", u"goDetail('04\ud6383200','minjae987');", u"goDetail('18\ud5582193','hongwoo1729');", u"goDetail('40\ud6383297','hspark3578');", u"goDetail('40\ud558 4582','m101x');", u"goDetail('18\ud638 7246','ug722');", u"goDetail('65\ud5584936','SUNOODA');", u"goDetail('68\ud6388916','mmzzggg');", u"goDetail('69\ud6388811','wwh7942');", u"goDetail('46\ud6385494','wwh7942');", u"goDetail('63\ud638 2936','luv22182525@gmail.com');", u"goDetail('52\ud558 9409','eckogt@naver.com');", u"goDetail('63\ud6384657','shinjs629');", u"goDetail('68\ud5581257','kimyh7495');", u"goDetail('64\ud5589406','inhodad');", u"goDetail('67\ud5586459','soccer1005');", u"goDetail('18\ud5582576','sadda77');", u"goDetail('52\ud5589409','eckogt@naver.com');", u"goDetail('40\ud558 3447','ekvkf0701@naver.com');", u"goDetail('65\ud5581504','KOREKO26');", u"goDetail('67\ud6386857','whgusrhk@hanmail.net');", u"goDetail('67\ud6386321','cool08278@naver.com');", u"goDetail('04\ud6385755','tankdog');", u"goDetail('12\ud6385630','jjangmi4');", u"goDetail('68\ud5581766','dokun2003@naver.com');", u"goDetail('67\ud5589420','lltales');", u"goDetail('63\ud5581263','kgh442@naver.com');", u"goDetail('04\ud6382438','ju0860');", u"goDetail('68\ud6382881','rlwntjd12');", u"goDetail('69\ud6384191','wwh7942');", u"goDetail('18\ud5588735','heehyun68@hotmail.com');", u"goDetail('52\ud5587430','jsb9167');", u"goDetail('18\ud6387102','ljy5183');", u"goDetail('52\ud5581316','kangkizer');", u"goDetail('67\ud6386700','bsb92');", u"goDetail('52\ud6387716','equus224');", u"goDetail('18\ud5588186','jeong_14@naver.com');", u"goDetail('52\ud6381318','sdh0328@naver.com');", u"goDetail('52\ud63813\u31428','sdh0328@naver.com');", u"goDetail('46\ud6381324','teen55@hanmail.net');", u"goDetail('65\ud638 7853','s01089264536');", u"goDetail('63\ud638 3889','skw9632@naver.com');", u"goDetail('12\ud6381337','bssuns');", u"goDetail('62\ud6384046','yong0935@naver.com');", u"goDetail('04\ud6383649','yusiyong');", u"goDetail('63\ud6383419','ohkii2000@naver.com');", u"goDetail('67 \ud558 6459','soccer1005');", u"goDetail('52\ud6383561','jooyong81');", u"goDetail('46\ud5584827','shabboy');", u"goDetail('04\ud6389083','kam0120');", u"goDetail('66\ud5589815','IJB1106');", u"goDetail('68\ud5589195','muhankbw@naver.com');", u"goDetail('08\ud6382767','navy0422');", u"goDetail('65\ud6387969','dhfogus');", u"goDetail('72\ud5582808','kjyung222');", u"goDetail('63\ud5581747','park30320');", u"goDetail('52\ud5589535','nero1997');", u"goDetail('69\ud6384123','pic333');", u"goDetail('04\ud638 5740','dldkdus111');", u"goDetail('72\ud558 1241','brightjw');", u"goDetail('46\ud5583247','emforhs4317');", u"goDetail('52\ud5585199','kse0912');", u"goDetail('67\ud6384754','thouzeau@hanmail.net');", u"goDetail('40\ud6384208','tjsxhl@naver.com');", u"goDetail('18\ud6386908','sukmo3@naver.com');", u"goDetail('66\ud638 8596','JS9117');", u"goDetail('04\ud6385885','kappa123');", u"goDetail('52\ud6381021','jangec1');", u"goDetail('65\ud638 1514','blackburn9@naver.com');", u"goDetail('52\ud5581943','tjsgl12');", u"goDetail('18\ud638 7956','4400gun');", u"goDetail('03\ud5589000.','leecj1210');", u"goDetail('52\ud5581805','ccb1020');", u"goDetail('67\ud5581663','wwh7942');", u"goDetail('52\ud5581597','stylebobo');", u"goDetail('14\ud6382282','sky060928');", u"goDetail('46\ud6381687','bc.tak@lotte.net');", u"goDetail('65\ud6387151','wkdwns8822');", u"goDetail('40\ud6383633','dleoqhr124@naver.com');", u"goDetail('18\ud558 4746','lemuelwj');", u"goDetail('66\ud558 9815','IJB1106');", u"goDetail('66\ud6386197','goeom');", u"goDetail('64\ud6387733','xlsodlwu');", u"goDetail('54\ud5584801','tan2');", u"goDetail('52\ud5584746','wwh7942');", u"goDetail('52\ud5589212','para7822');", u"goDetail('18\ud5586663','jjw7822');", u"goDetail('63\ud6388387','hotston');", u"goDetail('64\ud5581234','speed1037');", u"goDetail('52\ud5587568','jone8888');", u"goDetail('63\ud6383334','hyok73@hanmail.net');", u"goDetail('40\ud558 5976','osj2081');", u"goDetail('69\ud5583275','yyw5662');", u"goDetail('63\ud6382049','doc2231');", u"goDetail('65\ud6382942','jeauk7788');", u"goDetail('66\ud638 8110','BSH614');", u"goDetail('62\ud6384689','puha7942@naver.com');", u"goDetail('63\ud6381852','ccb1020');", u"goDetail('67\ud5584426','nsmnsm');", u"goDetail('40\ud5586615','kimhenney@naver.com');", u"goDetail('67\ud5584320','jrsy124');", u"goDetail('66\ud6386608','tjsdnwlgus@naver.com');", u"goDetail('18\ud5582575','kts3178@naver.com');", u"goDetail('52\ud6389865','hk9500');", u"goDetail('67\ud6381935','bbobbiti@naver.com');", u"goDetail('67\ud6386850','yhkim8');", u"goDetail('52\ud5587408','sbc1976@naver.com');", u"goDetail('65\ud6387853','s01089264536');", u"goDetail('40\ud558 5688','gababala');", u"goDetail('72\ud6381055','SUNWOOK2');", u"goDetail('69\ud5586553','ssinu00');", u"goDetail('40\ud5586451','49031325@qq.com');", u"goDetail('67\ud5584667','DANA915');", u"goDetail('18\ud5581118','mso33@hanmail.net');", u"goDetail('52\ud6388131','KOKOCHO');", u"goDetail('66\ud5589312','MFMAN7');", u"goDetail('18\ud5581288','sdgirl');", u"goDetail('46\ud5581985','sdgirl');", u"goDetail('68\ud5585298','sdgirl');", u"goDetail('62\ud638 9270','Kimsoi');", u"goDetail('04\ud6387716','benfor');", u"goDetail('58\ud5584801','jo123a');", u"goDetail('18\ud5586627','wjswndghk');", u"goDetail('64\ud5589728','wj3526');", u"goDetail('52\ud558 1545','012345young@naver.com');", u"goDetail('66\ud6383769','tifldo1004');", u"goDetail('18\ud5589363','welry@naver.com');", u"goDetail('12\ud6381204','tkfal1');", u"goDetail('67\ud558 3115','rmawogh06');", u"goDetail('46\ud5583855','rainmake1');", u"goDetail('67\ud5581072','notablebs');", u"goDetail('67\ud638 1994','yjk1000');", u"goDetail('62\ud6388286','htg1221');", u"goDetail('46\ud6384691','zamduri');", u"goDetail('14\ud6382097','cgb8739@naver.com');", u"goDetail('18\ud5589757','courage0123@gmail.com');", u"goDetail('64\ud5587900','cookorea');", u"goDetail('52\ud638 9864','him3274@naver.com');", u"goDetail('68\ud5584381','kino774@naver.com');", u"goDetail('40\ud5581338','hhr7877@naver.com');", u"goDetail('52\ud5589204','NANANICA');", u"goDetail('58\ud6381547','tkfal1');", u"goDetail('40\ud5586466','midas922');", u"goDetail('06\ud6383322','mmppdd');", u"goDetail('67\ud6383676','jojae93');", u"goDetail('67\ud5586745','molegole98@naver.com');", u"goDetail('18\ud5586466','sukmo3@naver.com');", u"goDetail('69\ud638 1514','blackburn9@naver.com');", u"goDetail('18\ud5582360','cnddl1115');", u"goDetail('67\ud6386116','akwld01');", u"goDetail('66\ud6388478','ccb1020');", u"goDetail('18\ud5585090','lhg2303');", u"goDetail('40\ud6384161','pic333');", u"goDetail('67\ud5584974','MINWO2771');", u"goDetail('67\ud6386208','PTJ37');", u"goDetail('40\ud638 3018','light876');", u"goDetail('06\ud558 5510','yang4348');", u"goDetail('52\ud5581396','wkdgusdn52');", u"goDetail('63\ud6389591','rlathdms1379@naver.com');", u"goDetail('67\ud5586429','mang2989@naver.com');", u"goDetail('67\ud5584553','show3483@naver.com');", u"goDetail('52\ud5585933','us0412');", u"goDetail('62 \ud638 4787','luv22182525@gmail.com');", u"goDetail('67\ud5586895','kimbin123');", u"goDetail('40\ud5583464','jrsy124');", u"goDetail('68\ud6381419','ibeat');", u"goDetail('71\ud5589473','wetour80');", u"goDetail('46\ud5581578','nmj87');", u"goDetail('67\ud5586889','pjs0403');", u"goDetail('40\ud5585657','blkruss');", u"goDetail('22\ud6389993','seagull78');", u"goDetail('66\ud6386316','CYHS99');", u"goDetail('46\ud558 9728','skyjingga@naver.com');", u"goDetail('68\ud6385805','tittu');", u"goDetail('71\ud5588622','kkoongshil');", u"goDetail('67\ud6383421','hyung0162@naver.com');", u"goDetail('18\ud5586648','ehdxo4710');", u"goDetail('46\ud6384267','SUNWOOK2');", u"goDetail('65\ud6389897','navy0422');", u"goDetail('67\ud6381709','josk2297');", u"goDetail('64\ud558 6993','shaandie');", u"goDetail('68\ud5587117','godbscjswo');", u"goDetail('54\ud5587739','s521999');", u"goDetail('46\ud6381681','sjs826@naver.com');", u"goDetail('66\ud6383326','hjizzang');", u"goDetail('40\ud5581832','taeyoon118@gmail.com');", u"goDetail('67\ud6383974','tae4139');", u"goDetail('50\ud6386850','ssun2003');", u"goDetail('46\ud6383324','song5188');", u"goDetail('52\ud638 1341','bluevox81');", u"goDetail('46\ud5583300','MAANNN');", u"goDetail('27\ud5585959','FLY1250');", u"goDetail('69\ud6385546','hyojunida@naver.com');", u"goDetail('40\ud558 3300','hzz00z@daum.net');", u"goDetail('06\ud6381716','zkftbawhdl5@naver.com');", u"goDetail('63\ud6388998','choiguevara6@gmail.com');", u"goDetail('68\ud6382915','qtp1862@hanmail.net');", u"goDetail('14\ud638 1015','lin64ge@naver.com');", u"goDetail('65\ud6382765','dusd123');", u"goDetail('67\ud5588214','kd591102');", u"goDetail('52\ud6381638','sky790915');", u"goDetail('18\ud5584608','tgbpkm');", u"goDetail('67\ud6381520','thouzeau@hanmail.net');", u"goDetail('40\ud6383650','yhj6420');", u"goDetail('66\ud6386186','bc.tak@lotte.net');", u"goDetail('65\ud6389893','tlsg1emd@naver.com');", u"goDetail('52\ud6381118','glqo');", u"goDetail('69\ud6381087','eymin');", u"goDetail('06\ud6383317','kkj0037');", u"goDetail('68\ud6382061','in1291002@naver.com');", u"goDetail('69\ud6388969','shy1274@hanmail.net');", u"goDetail('62\ud6388987','sweety1975');", u"goDetail('46\ud6383774','nero1997');", u"goDetail('69\ud6385347','cjwndud');", u"goDetail('06\ud5585974','beradin0901');", u"goDetail('68\ud6385715','sed000');", u"goDetail('46\ud5581941','ANDYPAK');", u"goDetail('68\ud6384322','Kimyuran87@yahoo.com');", u"goDetail('67\ud6381178','dumdum11');", u"goDetail('23\ud5c88994','INTERNET77');", u"goDetail('54\ud6387343','majer');", u"goDetail('64\ud5581694','realist7');", u"goDetail('65\ud6387102','heyman12');", u"goDetail('62\ud6385672','sukmo3@naver.com');", u"goDetail('63\ud6384895','hongsj0242@nate.com');", u"goDetail('40\ud5581264','chodp0211');", u"goDetail('06\ud638 2726','ckrns51@naver.com');", u"goDetail('67\ud638 4186','jinsu64');", u"goDetail('67\ud558 8580','hkhhs@naver.com');", u"goDetail('69\ud5581510','sukmo3@naver.com');", u"goDetail('69\ud5581422','kjy9973');", u"goDetail('65\ud6387924','ccabsae79');", u"goDetail('69\ud6383975','dchae1');", u"goDetail('68\ud5584199','choieuro');", u"goDetail('67\ud5581340','binnana');", u"goDetail('52\ud6384205','kimmin2480@naver.com');", u"goDetail('35\ud6383832','recess83');", u"goDetail('46\ud6381983','seraphim0312');", u"goDetail('69\ud5586817','hibyun21@gmail.com');", u"goDetail('67\ud5589578','jhs3511');", u"goDetail('63\ud6388231','a33153305@gmail.com');", u"goDetail('46\ud6385655','chk5150');", u"goDetail('07\ud6382736','jsk6801');", u"goDetail('67\ud6387626','arumdury');", u"goDetail('13\ud5584869','wjdwprhrh');", u"goDetail('64\ud558 1983','megadeth77');", u"goDetail('69\ud638 4077','guswns641@naver.com');", u"goDetail('40\ud6381993','dahea');", u"goDetail('63\ud638 1615','wnsahsla');", u"goDetail('64\ud6383050','39771189');", u"goDetail('63\ud6388304','5691');", u"goDetail('40\ud5585302','pic333');", u"goDetail('46\ud5584647','pic333');", u"goDetail('65\ud6382965','kimdong5087@naver.com');", u"goDetail('69\ud6381234','MINHYEOK003');", u"goDetail('68\ud6381950','jajb486');", u"goDetail('63\ud6388704','jinkwan2004@naver.com');", u"goDetail('40\ud6381163','pshcream');", u"goDetail('46\ud5584069','dhgurrbs@naver.com');", u"goDetail('66\ud5589053','kimms617');", u"goDetail('40\ud638 1436','rla654123');", u"goDetail('40\ud6381436','rla654123');", u"goDetail('69\ud6385418','ljhrose0909@naver.com');", u"goDetail('67\ud6387860','ccb1020');", u"goDetail('46\ud6381819','job8282');", u"goDetail('69\ud5586614','haessal22@naver.com');", u"goDetail('46\ud6384011','MRPSN1');", u"goDetail('64\ud5589503','badam11');", u"goDetail('14\ud5c85036','parkenam@naver.com');", u"goDetail('40\ud5586301','leehyonil');", u"goDetail('68\ud6388777','so1239@naver.com');", u"goDetail('67\ud6386908','sarahkla');", u"goDetail('69\ud5584025','jinlyun');", u"goDetail('69\ud638 5259','kwon121514');", u"goDetail('66\ud5585708','SLSHIN');", u"goDetail('14\ud6382111','sirano5b');", u"goDetail('40\ud6381555','spoto07');", u"goDetail('40\ud5581831','taeyoon118@gmail.com');", u"goDetail('67\ud5581099','SHIN1024D');", u"goDetail('67\ud5588781','cccccccpsh');", u"goDetail('40\ud6381163','ekdnal');", u"goDetail('46\ud6383617','OHYOUNSU');", u"goDetail('69\ud5586702','shinwon2yong@naver.com');", u"goDetail('71\ud5589909','hbj63512');", u"goDetail('40\ud6381321','qlql45');", u"goDetail('12\ud6385815','QOWOTJS123');", u"goDetail('69\ud638 5226','skyofsiea');", u"goDetail('40\ud558 4590','skyofsiea');", u"goDetail('06\ud6382707','solidpupa');", u"goDetail('46\ud6381298','judgeyoo911@daum.net');", u"goDetail('68\ud5583129','ydg2486');", u"goDetail('46\ud6381234','MINHYEOK003');", u"goDetail('40\ud638 1622','archss');", u"goDetail('40\ud5583026','ghtksek2');", u"goDetail('54\ud558 3888','dlrndus');", u"goDetail('46\ud6381176','soo1032116');", u"goDetail('46\ud6381102','scy6658@naver.com');", u"goDetail('68\ud6389731','bob620@daum.net');", u"goDetail('68\ud5581605','ccb1020');", u"goDetail('54\ud5584071','chang8237');", u"goDetail('62\ud638 4885','begetal');", u"goDetail('13\ud5581407','non741');", u"goDetail('50\ud6384462','angel7101');", u"goDetail('14\ud6382799','by1wns');", u"goDetail('69\ud6385431','ratm8410');", u"goDetail('66\ud5582851','cooldog26@naver.com');", u"goDetail('68\ud6381409','pic333');", u"goDetail('40\ud5584563','xoghdska1852@naver.com');", u"goDetail('03\ud5588990','ssi0329@naver.com');", u"goDetail('25\ud6383059','1p1p1p');", u"goDetail('62\ud5581648','SUNOODA');", u"goDetail('62\ud558 1857','o1o31339233');", u"goDetail('40\ud5c8 5976','osj2081');", u"goDetail('71gk9471','CHARMINGJOO');", u"goDetail('64\ud6384865','genergykr');", u"goDetail('68\ud6382872','TIMEOFSOUL');", u"goDetail('67\ud5583013','ccb1020');", u"goDetail('67\ud6381178','dmstjs785@naver.com');", u"goDetail('46\ud5581870','1004hon');", u"goDetail('68\ud5585300','wwestone');", u"goDetail('40\ud5585306','hachis');", u"goDetail('46\ud5581698','koh5663');", u"goDetail('46\ud6384598','alsrnsrl');", u"goDetail('62\ud6388066','donaldte');", u"goDetail('66\ud5589815','ijb1106');", u"goDetail('66\ud5588055','pey40526');", u"goDetail('68\ud5585587','FORMID');", u"goDetail('68\ud5581352','kangdoc@hanmail.net');", u"goDetail('69\ud5584661','Y.gunn@icloud.co.kr');", u"goDetail('46\ud6385435','go0120');", u"goDetail('46\ud638 1798','gamja124');", u"goDetail('62\ud6384759','pmt2001');", u"goDetail('40\ud5583223','spoto07');", u"goDetail('69\ud6388737','happyna517');", u"goDetail('25\ud6383011','OdysseyS2');", u"goDetail('22\ud6384441','kys6991@naver.com');", u"goDetail('64\ud5588165','dnfkgkfkek');", u"goDetail('54\ud5581594','erokangman');", u"goDetail('64\ud5587316','SOLAR31');", u"goDetail('46\ud5584196','sines2392');", u"goDetail('40\ud6383650','bka518');", u"goDetail('68\ud6387811','info@tconcierges.com');", u"goDetail('68\ud6382141','ky93100@gmail.com');", u"goDetail('68\ud6385582','KISSWAR');", u"goDetail('40\ud5581700','sosejibuin@nate.com');", u"goDetail('46\ud6384911','lyh0331@hanmail.net');", u"goDetail('bmw320d','tissue7587@naver.com');", u"goDetail('13\ud5584925','pic333');", u"goDetail('50\ud5584317','st2js');", u"goDetail('14\ud6382715','sirano5b');", u"goDetail('68\ud6384988','ccb1020');", u"goDetail('66\ud6386788','wkdwnsdyd55@naver.com');", u"goDetail('46\ud5584228','tjsalsrn@hanmail.net');", u"goDetail('69\ud6381574','hijkl5367');", u"goDetail('40\ud6381045','pic333');", u"goDetail('06\ud558 5928','teramin47@naver.com');", u"goDetail('68\ud6384658','HAMILCOLOR');", u"goDetail('58\ud5583086','jj6600');", u"goDetail('12\ud6382612','ndy96@naver.com');", u"goDetail('34\ud5581135','WNSGH1118');", u"goDetail('40\ud5581736','victra78');", u"goDetail('40\ud638 7755','pcroom1990@naver.com');", u"goDetail('40\ud6381120','chang8237');", u"goDetail('03\ud5589000','leecj1210');", u"goDetail('40\ud6384100','AUDI10201');", u"goDetail('62\ud6384456','BSH614');", u"goDetail('46\ud6383262','diawodl2');", u"goDetail('68\ud6385009','anse0204');", u"goDetail('28\ud638 8762','ljh1452');", u"goDetail('50\ud6384865','dksrlcjfsla@naver.com');", u"goDetail('69\ud6381029','hunwoo1207');", u"goDetail('46\ud5584602','alswl2966');", u"goDetail('14\ud6382711','pjj0080w');", u"goDetail('69\ud6381910','soya2323');", u"goDetail('62\ud6388899','pic333');", u"goDetail('68\ud6382248','leessang0413');", u"goDetail('46\ud5584312','nsh817');", u"goDetail('54\ud6385766','choungck');", u"goDetail('28\ud6389430','choungck');", u"goDetail('68\ud5589103','R45RT');", u"goDetail('69\ud5585950','rhrlajrdj2@naver.com');", u"goDetail('32\ud6381251','2775793');", u"goDetail('9328','so900707@naver.com');", u"goDetail('69\ud5583951','elf99jp');", u"goDetail('68\ud6388691','whisker95@samsungfire.com');", u"goDetail('03\ud6388653','GFDSA1024');", u"goDetail('73\uc2185173','reeky@naver.com');", u"goDetail('69\ud5583161','GOLFKSS');", u"goDetail('66\ud6383688','ljm611205@naver.com');", u"goDetail('71\ud5588599','steelers2016@naver.com');", u"goDetail('69\ud5584529','dslee777');", u"goDetail('46\ud638 4970','moralman');", u"goDetail('40\ud5581111','SMAILL9401');", u"goDetail('40\ud6384357','rorms@naver.com');", u"goDetail('75\ud5c87128','kthjcom@naver.com');", u"goDetail('70\ud5c83848','pic333');", u"goDetail('35\ud6385399','y880410');", u"goDetail('22\ud5585296','CUTE5786');", u"goDetail('64\ud5587541','qkqh05');", u"goDetail('40\ud5586304','idtaeil@enertopia.fr');", u"goDetail('71\ud5588768','kakemusa79');", u"goDetail('35\ud5587916','fox16012@hanmail.net');", u"goDetail('08\ud6382055','navy0422');", u"goDetail('54\ud5587803','jbnoh1');", u"goDetail('69\ud5584675','gotheee@naver.com');", u"goDetail('64\ud5589172','knk1974');", u"goDetail('69\ud5584481','k7296');", u"goDetail('40\ud5583157','hohojoo70');", u"goDetail('69\ud6385403','ruddms2935@naver.com');", u"goDetail('30\ud6383884','zazanlee');", u"goDetail('66\ud6383611','leeinuk7@naver.com');", u"goDetail('27\ud6383795','icuzoa');", u"goDetail('69\ud6385500','DH9792');", u"goDetail('58\ud6381553','tmddhks153');", u"goDetail('64\ud5587983','JMJH7503');", u"goDetail('64\ud5589863','edydwjs');", u"goDetail('58\ud6383515','MOCOM7777');", u"goDetail('40\ud5581252','ch004');", u"goDetail('05\ud5589863','RCN7STAR');", u"goDetail('58\ud6389884','SECRETHUN');", u"goDetail('66\ud558','abukki4');", u"goDetail('68\ud5584739','na_3224@naver.com');", u"goDetail('68\ud6382210','choice1377@naver.com');", u"goDetail('40\ud6384032','anhs25');", u"goDetail('58\ud6383755','dmepj1');", u"goDetail('40\ud5583628','OHYOUNSU');", u"goDetail('64\ud5586965','my15mail@hanmail.net');", u"goDetail('62\ud5584774','pbong1');", u"goDetail('50\ud6387319','jjh3770@hanmail.net');", u"goDetail('66\ud5586004','minhokee');", u"goDetail('71\ud5589562','mhohonone99');", u"goDetail('66\ud5582390','leeyongbae2.0@naver.com');", u"goDetail('50\ud6381932','yghyuk');", u"goDetail('64\ud5581298','jungwan');", u"goDetail('35\ud6381732','ehfdl2005@nate.com');", u"goDetail('64\ud5586078','radeon330@nate.com');", u"goDetail('68\ud5584983','tnaig49');", u"goDetail('08\ud6382139','popogh8636@naver.com');", u"goDetail('14\ud6382089','kkttvv');", u"goDetail('62\ud6388715','bmbmbm19@naver.com');", u"goDetail('69\ud5581440','dam0');", u"goDetail('27\ud5582995','zine3000');", u"goDetail('25\ud6382650','chriskimkrjp');", u"goDetail('66\ud5582590','jjuya84zz');", u"goDetail('15\ud6389462','mcblazm@naver.com');", u"goDetail('64\ud6384188','sukmo3@naver.com');", u"goDetail('62\ud558 4841','yep36@naver.com');", u"goDetail('06\ud5583254','SJB44');", u"goDetail('66\ud5586048','RACKER97');", u"goDetail('69\ud5586882','baibars1021@gmail.com');", u"goDetail('69\ud6389074','se3214');", u"goDetail('62\ud638 1635','lmj6693');", u"goDetail('68\ud5585885','wlsdld15@naver.com');", u"goDetail('69\ud5581999','dog1377@naver.com');", u"goDetail('68\ud6385093','rjn32607');", u"goDetail('64\ud5585250','lib00');", u"goDetail('58\ud5583093','ceo564');", u"goDetail('22\ud6389843','gomtos@gmail.com');", u"goDetail('66\ud5589719','juknow0264@naver.com');", u"goDetail('69\ud5581067','back2486@naver.com');", u"goDetail('69\ud5581449','kyh859@nate.com');", u"goDetail('66\ud6383599','SW4244');", u"goDetail('62\ud5581302','wwwzzang13');", u"goDetail('68\ud6384751','jin4267');", u"goDetail('69\ud5581176','ogm0284');", u"goDetail('50\ud558 6758','unicon90');", u"goDetail('14\ud6382074','t-plus-g@nate.com');", u"goDetail('50gk7294','trade75');", u"goDetail('35\ud5581717','hyjbbbjsbb');", u"goDetail('13\ud5584800','kyahero');", u"goDetail('62\ud6386374','lleports@naver.com');", u"goDetail('62 \ud6388575','aggupa');", u"goDetail('66\ud6386216','slal1106@naver.com');", u"goDetail('50\ud6387102','AIRLINE99');", u"goDetail('0000','tkatjd0060');", u"goDetail('35\ud6385583','woozzazi@keco.or.kr');", u"goDetail('64\ud5581398','realloveljk');", u"goDetail('66\ud5586066','wnchfhd1');", u"goDetail('71\ud6387427','www.esse2790@naver.com');", u"goDetail('50\ud5581219','dksgmldus92');", u"goDetail('54\ud5583613','poto2848@nate.com');", u"goDetail('62\ud6389030','4264WIN');", u"goDetail('22\ud5586949','aibim');", u"goDetail('68\ud5589053','nicewinguy');", u"goDetail('66\ud6386887','yis0724');", u"goDetail('58\ud5583382','jjj47092');", u"goDetail('62\ud6386088','polarislands@naver.com');", u"goDetail('64\ud6387930','ksjjsk4521');", u"goDetail('66\ud5585692','ky93100@gmail.com');", u"goDetail('62\ud6384319','kevin@bmwhockenheim.com');", u"goDetail('27\ud6383667','jtj011@hanmail.net');", u"goDetail('05\ud6389593','hun8379');", u"goDetail('07\ud6382736','JSK6801');", u"goDetail('62\ud5581165','sukmo3@naver.com');", u"goDetail('35\ud6381745','kts3178');", u"goDetail('68\ud6388862','MADOGI');", u"goDetail('58\ud6385405','pica9000@empal.com');", u"goDetail('14\ud6381495','soohyeonc');", u"goDetail('72\ud6389030','city2040@naver.com');", u"goDetail('25\ud6382705','ahs8888');", u"goDetail('68\ud6384991','woong793');", u"goDetail('68\ud6384633','MASCHANG');", u"goDetail('64\ud638 2715','hmjang524@naver.com');", u"goDetail('68\ud5584966','MOODMAKE');", u"goDetail('50\ud6384958','lhy70042002');", u"goDetail('54\ud6383707','KSSENSE');", u"goDetail('64\ud5585140','hunt911');", u"goDetail('66\ud6383639','dnfl84');", u"goDetail('68\ud6385926','nslee@tstec.co.kr');", u"goDetail('64\ud6387820','sukmo3@naver.com');", u"goDetail('68\ud5584201','FORMID');", u"goDetail('50\ud558 6731','JUNJIN1189');", u"goDetail('62\ud5581109','PIGOO1004');", u"goDetail('66\ud6383284','APOIUY10');", u"goDetail('68\ud5589053','DGBUPAY');", u"goDetail('01\ud5586016','JYKONG');", u"goDetail('54\ud5581019','SUNOODA');", u"goDetail('64\ud5589415','SUNOODA');", u"goDetail('71\ud5588429','KDY120925');", u"goDetail('62\ud5585368','SSC1551');", u"goDetail('62\ud5581515','GOLF470');", u"goDetail('06\ud5583781','BYOUNGI');", u"goDetail('62\ud6388746','KKO02');", u"goDetail('54\ud638 4281','SEOJIN7866');", u"goDetail('55gh5305','HISTORYLEE');", u"goDetail('06\ud5584405','GGUZZI1004');"]

# prefs = {'profile.managed_default_content_settings.images': 2} -> 느림
# chrome_options.add_experimental_option('prefs', prefs) -> 느림

chrome_options = webdriver.ChromeOptions()
prefs = {'disk-cache-size': 4096, 'profile.managed_default_content_settings.images': 2}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('--headless')
chrome_options.add_argument('application-cache')
chrome_options.add_argument('no-sandbox')
# chrome_options.add_argument('--dns-prefetch-disable')
ChromeDriver = webdriver.Chrome(webdriver_path+'chromedriver', chrome_options=chrome_options)

ChromeDriver.set_page_load_timeout(150)
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
        # print listItem
        for item in listItem :
            pagingList.append(item.get('onclick'))
            # print pagingList

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
    if arr is None or arr is 'Null':
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
                    os.path.join(default_save_path + 'carImage/' + carNumber.encode('utf-8'),  imgName), "w"
            ) as f:
                f.write(dr)
                # print("저장되었습니다.")
        except urllib2.HTTPError, e:
            print e.code



def validatorCar(carNumber):
    pattern = re.compile('[a-z|A-Z|ㄱ-]+')
    if len(carNumber) != 7 or re.search(pattern, carNumber.encode('utf-8') ) != None:
        return False
    return True

def carInfoSaveTest(argStr):

    try :
        ChromeDriver.get(urlList['lotte'][1])
    except TimeoutException as e:
        print 'when disconnected totalTime is : ', datetime.datetime.now() - startTime
        ChromeDriver.quit()
        # print e

    detail = argStr
    if page_has_loaded() == 'complete' :
        carNumber = detail.split("'")[1].replace(' ','')
        print 'carNumber', detail.split("'")[1].replace(' ','').replace('.','')
        if validatorCar(carNumber) is True :
            ChromeDriver.execute_script(detail)

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
                    # saveImgage(carNumber, htmlSource)
            else :
                "need collecting error page info"

# --------------------------------------------------------------------------------------------------------------

ws = None
rowCount = 1
if canFetch(urlList['lotte'][0], urlList['lotte'][1]) :

    startTime =  datetime.datetime.now()


    try :
        ChromeDriver.get(urlList['lotte'][1])
    except TimeoutException as e:
        print 'when disconnected totalTime is : ', datetime.datetime.now() - startTime
        ChromeDriver.quit()
        # print e

    getPageCount()

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


