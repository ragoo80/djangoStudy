# -*- coding: utf-8 -*-
import os

default_save_path = '/Users/elbow/Documents/lotteRent/'

def getFolder(forderName):
    print default_save_path + forderName
    print os.path.isdir( default_save_path + forderName )
    if not( os.path.isdir( default_save_path + forderName ) ):
        os.makedirs( os.path.join( default_save_path + forderName ) )
        return 'making' + forderName
    else :
        return str(os.path.join( default_save_path + forderName ))+' already exsit!!'


def main():
    print getFolder('52호1587')


if __name__ == '__main__':
    main()