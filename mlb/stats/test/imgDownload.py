# -*- coding: utf-8 -*-

import urllib2

req = urllib2.Request('https://www.lotterentacar.net/atch/upload/getImage.do?atchFileId=20180913015821hyh0401@nate.comfrontImg_V.jpg&fileSepar=succession')
data = urllib2.urlopen(req)
dr = data.read()

with open('avante test.jpg', mode="wb") as f:
    f.write(dr)
    print("저장되었습니다.")
