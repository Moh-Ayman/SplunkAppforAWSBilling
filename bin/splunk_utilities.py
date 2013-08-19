#!/usr/bin/python
# get_detailed_bill.py
__author__ = 'monk-ee'

"""This module provides some handy utilities
"""
import os
import sys
import calendar
import datetime
import time
from datetime import datetime,timedelta

#path and file stuff
path = os.environ["SPLUNK_HOME"]
appname = 'SplunkAppforAWSBilling'
BILLINGREPORTZIPDIR = os.path.join(path, 'etc', 'apps', appname, 'tmp')
BILLINGREPORTCSVDIR = os.path.join(path, 'etc', 'apps', appname, 'csv')
AWSCONFIGFILE = os.path.join(path, 'etc', 'apps', appname, 'local', 'aws.yaml')
ERRORLOGFILE = os.path.join(path, 'etc', 'apps', appname, 'log', 'detailed_bill_errors.txt')

#time related malarkey for guessing last months billing file name - i mean building
def datefilename():
    dt = datetime.now()
    return dt.strftime("%Y-%m")

def subtract_one_month_datefilename():
    "just a timenow function to minimize code repeats"
    dt = datetime.now()
    dt1 = dt.replace(day=1)
    dt2 = dt1 - timedelta(days=1)
    dt3 = dt2.replace(day=1)
    return dt3.strftime("%Y-%m")

def timenow():
    "just a timenow function to minimize code repeats"
    return time.strftime("%m-%d-%Y %H:%M:%S", time.localtime()) + " " + time.strftime("%z")