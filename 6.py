#!/usr/bin/python
#Author: Raj Bindra
from myTables.ConfigTables import TaskMemoryTable
from myTables.ConfigTables import routeinfo
from myTables.ConfigTables import FpcInfoTable
from myTables.ConfigTables import reinfo
from lxml import etree
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import sys
from lxml import etree
from getpass import getpass
from pprint import pprint
import xlwt
devices = open('device_list_test')
devlist = devices.readlines()
user = raw_input('username: ')
passwd = getpass('password: ')
n = 0
book = xlwt.Workbook(encoding="utf-8")
#Start of Sheet1
sheet1 = book.add_sheet("Task Memory")
sheet1.write(0, 0, "Hostname")
sheet1.write(0, 1, "Max Task Memory Used")
sheet1.write(0, 2, "Current Task Memory Used") 
#Start of Sheet2
sheet2 = book.add_sheet("RE Info")
sheet2.write(0, 0, "Hostname")
sheet2.write(0, 1, "Max Task Memory Used")
sheet2.write(0, 2, "Current Task Memory Used")
#Start of Sheet3
sheet3 = book.add_sheet("FPC Info")


#Start of Sheet4
sheet4 = book.add_sheet("Route Tables")


for host in devlist:
    host = host.strip()
    print "Working on %s..." % host
    dev = Device(host,user=user,password=passwd, port=22, gather_facts=False)
    dev.open()
    tm = TaskMemoryTable(dev).get()
#Task Memory Information   
    for item in tm:
        n = n + 1
        sheet1.write(n, 0, host)
        sheet1.write(n, 1, str(item.task_memory_max_avail)+"%")
        sheet1.write(n, 2, str(item.task_memory_in_use_avail)+"%")
        book.save("test.xls")
dev.close()
