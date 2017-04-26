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
book = xlwt.Workbook(encoding="utf-8")
#Start of Sheet1
sheet1 = book.add_sheet("Task Memory")
sheet1.write(0, 0, "Hostname")
sheet1.write(0, 1, "Max Task Memory Used")
sheet1.write(0, 2, "Current Task Memory Used")
#Start of Sheet2
sheet2 = book.add_sheet("RE Info")
sheet2.write(0, 0, "Hostname")
sheet2.write(0, 1, "RE Slot")
sheet2.write(0, 2, "RE Model")
sheet2.write(0, 3, "Mastership State")
sheet2.write(0, 4, "Memory Utilization")
sheet2.write(0, 5, "CPU Utilization")
#Start of Sheet3
sheet3 = book.add_sheet("FPC Info")
sheet3.write(0, 0, "Hostname")
sheet3.write(0, 1, "FPC Slot")
sheet3.write(0, 2, "State")
sheet3.write(0, 3, "Total Memory")
sheet3.write(0, 4, "Memory-Heap-Utilization")
#Start of Sheet4
sheet4 = book.add_sheet("Route Tables")
sheet4.write(0, 0, "Hostname")
sheet4.write(0, 1, "inet.0 Total")
sheet4.write(0, 2, "inet.0 Active")
sheet4.write(0, 3, "inet.2 Total")
sheet4.write(0, 4, "inet.2 Active")
sheet4.write(0, 5, "inet.3 Total")
sheet4.write(0, 6, "inet.3 Active")
sheet4.write(0, 7, "inet6.0 Total")
sheet4.write(0, 8, "inet6.0 Active")
sheet4.write(0, 9, "bgp.l2vpn.0 Total")
sheet4.write(0, 10, "bgp.l2vpn.0 Active")
sheet4.write(0, 11, "bgp.l3vpn.0 Total")
sheet4.write(0, 12, "bgp.l3vpn.0 Active")
sheet4.write(0, 13, "mpls.0 Total")
sheet4.write(0, 14, "mpls.0 Active")
n = 0
for host in devlist:
    host = host.strip()
    print "Working on %s..." % host
    dev = Device(host,user=user,password=passwd, port=22, gather_facts=False)
    dev.open()
    tm = TaskMemoryTable(dev).get()
    re = reinfo(dev).get()
    fp = FpcInfoTable(dev).get()
    ri = routeinfo(dev).get(table="inet.0")
    ria = routeinfo(dev).get(table="inet.2")
    rib = routeinfo(dev).get(table="inet.3")
    ric = routeinfo(dev).get(table="inet6.0")
    rid = routeinfo(dev).get(table="bgp.l2vpn.0")
    rie = routeinfo(dev).get(table="bgp.l3vpn.0")
    rif = routeinfo(dev).get(table="mpls.0")
#Task Memory Information   
    for item in tm:
        n += 1
        sheet1.write(n, 0, host)
        sheet1.write(n, 1, str(item.task_memory_max_avail)+"%")
        sheet1.write(n, 2, str(item.task_memory_in_use_avail)+"%")
        book.save("test.xls")
#RE info
    for item in re:
        n += 1
        sheet2.write(n, 0, host)
        sheet2.write(n, 1, (item.reslot))
        sheet2.write(n, 2, (item.remodel))
        sheet2.write(n, 3, (item.mastership_state))
        sheet2.write(n, 4, (item.memory_utilization)+"%")
        newcpu = int(item.cpu_idle)
        total = 100
        CPU = total - newcpu
        sheet2.write(n, 5, str(CPU)+"%")
        book.save("test.xls")
#fpc info
    for item in fp:
        n += 1 
        sheet3.write(n, 0, host)
        sheet3.write(n, 1, str(item.slot))
        sheet3.write(n, 2, (item.state))
        sheet3.write(n, 3, str(item.total_memory)+"MB")
        sheet3.write(n, 4, str(item.memory)+"%")
        book.save("test.xls")
#inet.0
    for item in ri:
        n += 1
        sheet4.write(n, 0, host)
        sheet4.write(n, 1, item.total_route_count)
        sheet4.write(n, 2, item.active_route_count)
        book.save("test.xls")
#inet.2
    for item in ria:
        sheet4.write(n, 3, item.total_route_count)
        sheet4.write(n, 4, item.active_route_count)
#inet.3
    for item in rib:
        sheet4.write(n, 5, item.total_route_count)
        sheet4.write(n, 6, item.active_route_count)
#inet6.0
    for item in ric:
        sheet4.write(n, 7, item.total_route_count)
        sheet4.write(n, 8, item.active_route_count)
#bgp.l2vpn
    for item in rid:
        sheet4.write(n, 9, item.total_route_count)
        sheet4.write(n, 10, item.active_route_count)
#bgp.l3vpn
    for item in rie:
        sheet4.write(n, 11, item.total_route_count)
        sheet4.write(n, 12, item.active_route_count)
#mpls.0
    for item in rif:
        sheet4.write(n, 13, item.total_route_count)
        sheet4.write(n, 14, item.active_route_count)
        book.save("test.xls")
dev.close()
