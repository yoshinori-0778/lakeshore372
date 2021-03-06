#!/bin/env python
import os
import sys
import datetime

run_script = '/data/code/lakeshore372/lakeshore372_getdata.py'
outdirectory = '/data/he3/temp_log'
#outdirectory = './';
#devlocation  = '169.254.235.124,255.255.0.0,7777';
devlocation = '192.168.10.12,255.255.255.0,7777'
dt = 1

if __name__ == '__main__':

    isTest = False
    if len(sys.argv) > 1:
        isTest = True

    now = datetime.datetime.now()
    isAM = (now.hour < 12)
    nowStr = now.strftime('%Y-%m-%d{}'.format('AM' if isAM else 'PM'))
    outputfilename = '{}/data_{}.dat'.format(outdirectory, nowStr)
    cmd = r'python {} {} {} {}'.format(
        run_script, outputfilename, devlocation, dt)
    print (cmd)
    if not isTest:
        os.system(cmd)

    pass
