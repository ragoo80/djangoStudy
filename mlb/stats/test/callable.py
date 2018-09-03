# -*- coding: utf-8 -*-

def testFunction() :
    print 'testFunction exec'


print '1 : ', callable(eval('testFunction'))
print '2 : ', callable(testFunction)