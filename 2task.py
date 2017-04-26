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
devices = open('device_list_test')
devlist = devices.readlines()
user = raw_input('username: ')
passwd = getpass('password: ')
for host in devlist:
    host = host.strip()
    print "Working on %s..." % host
    dev = Device(host,user=user,password=passwd, port=22, gather_facts=False)
    dev.open()
    file = open('OUTPUT.txt', 'ab')
    tm = TaskMemoryTable(dev).get()
#Task Memory Information   
    file.write('\n')
    file.write("========================%s-Task Memory-Info==========================" % (host))
    for item in tm:
        file.write('\n')
        file.write("Max Task Memory Used: "+str(item.task_memory_max_avail)+"%")
        file.write("  Current Task Memory Used: "+str(item.task_memory_in_use_avail)+"%")
    re = reinfo(dev).get()
#Routing Engine Information
    file.write('\n')
    file.write("==========================%s-RE-Info=================================" % (host))
    for item in re:
        file.write('\n')
        file.write("RE Slot#: "+item.reslot)
        file.write("  RE Model: "+item.remodel)
        file.write("  Mastership State: "+item.mastership_state)
        file.write("  Memory Utilization: "+item.memory_utilization+"%")
        newcpu = int(item.cpu_idle)
        total = 100
        CPU = total - newcpu
        file.write("  CPU Utilization: " +str(CPU)+"%")
    fp = FpcInfoTable(dev).get()
#FPC Information
    file.write('\n')
    file.write("==========================%s-FPC-Info================================" % (host))
    for item in fp:
        file.write('\n')
        file.write("Slot: "+str(item.slot))
        file.write("  State: "+item.state)
        file.write("  Total Memory: "+str(item.total_memory)+"MB")
        file.write("  Memory-Heap-Utilization: "+str(item.memory)+"%")
#Route Table Information
    file.write('\n')
    file.write("==========================%s-Route-Info==============================" % (host))
    ri = routeinfo(dev).get(table="inet.0")
    for item in ri:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)

    ria = routeinfo(dev).get(table="inet.2")
    for item in ria:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)

    rib = routeinfo(dev).get(table="inet.3")
    for item in rib:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)

    ric = routeinfo(dev).get(table="inet6.0")
    for item in ric:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)

    rid = routeinfo(dev).get(table="bgp.l2vpn.0")
    for item in rid:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)

    rie = routeinfo(dev).get(table="bgp.l3vpn.0")
    for item in rie:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)

    rif = routeinfo(dev).get(table="mpls.0")
    for item in rif:
        file.write('\n')
        file.write("Table Name: "+item.table_name)
        file.write(" Active Routes: "+item.active_route_count)
        file.write(" Total Routes: "+item.total_route_count)
    dev.close()
    print "Done with %s..." % host
file.close()
