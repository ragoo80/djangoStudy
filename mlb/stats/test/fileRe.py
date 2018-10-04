# -*- coding: utf-8 -*-
import os
from os import rename, listdir, path
import unicodedata


defaultPath = '/Users/elbow/Desktop/ren/'
folderList = []
def setFileList():
    # count = 0


    for idx in range(len(folderList)) :
        current = idx
        for item in listdir(folderList[idx]) :
            imgName = unicodedata.normalize('NFC', item)
            idx = imgName.find('이미지'.decode('utf-8'))+3
            newName = 'image'+ imgName[idx:]

            print current
            print unicodedata.normalize('NFC', item), newName
            print folderList[current]+'/'+imgName
            print path.exists(folderList[current]+'/'+imgName)
            print '---------------------------------'

            if path.exists(folderList[current]+'/'+imgName):
                rename( unicodedata.normalize('NFC', folderList[current]+'/'+imgName), folderList[current]+'/'+newName )


# print unicodedata.normalize('NFC', folderList[0]+'/'+test)
# print listdir( unicodedata.normalize('NFC', folderList[0]+'/'+test) )
# print listdir(defaultPath+item)

# print 'test : ', path.exists('/Users/elbow/Desktop/ren/05호2232/테스트이미지22.png')
# print listdir('/Users/elbow/Desktop/ren/05호2232/테스트이미지22.png'.encode('utf-8'))
# print path.exists('/Users/elbow/Desktop/ren/05호2232/테스트이미지22.png')
# print path.exists('/Users/elbow/Desktop/ren//Users/elbow/Desktop/ren/05호2232/테스트이미지1.jpg')


def getFolderName() :
    for folderName in listdir(defaultPath):
        if folderName != '.DS_Store' :
            f = defaultPath+folderName.decode('utf-8')
            f = unicodedata.normalize('NFC', f)
            folderList.append(f)

    # print(folderList)
    setFileList()

getFolderName()






