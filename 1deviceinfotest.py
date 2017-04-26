#!/usr/bin/python
from myTables.ConfigTables import TaskMemoryTable
from myTables.ConfigTables import routeinfo
from myTables.ConfigTables import FpcInfoTable
from myTables.ConfigTables import reinfo
from lxml import etree
import yaml
from getpass import getpass
from jnpr.junos import Device
import sys
from jnpr.junos.factory.factory_loader import FactoryLoader
#Tables are located under the "current directly or the script"/myTables/ConfigTables
#Author: Raj Bindra
# Set device information with IP-address, login user and passwort
dev = Device(host="172.27.0.162", user="rbindra", password="N0c@nd00", gather_facts=False)
host = "172.27.0.162"
# Open connection to the device
dev.open()

ri = routeinfo(dev).get(table="inet.0")
# Print all the information received from device
for item in ri:
    print("===========================ROUTE TABLES==============================")    
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)    
    print("Total Routes: "+item.total_route_count)
print("------------")
ria = routeinfo(dev).get(table="inet.2")
for item in ria:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("------------")
rib = routeinfo(dev).get(table="inet.3")
for item in rib:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("------------")
ric = routeinfo(dev).get(table="inet6.0")
for item in ric:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("------------")
rid = routeinfo(dev).get(table="bgp.l2vpn.0")
for item in rid:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("------------")
rie = routeinfo(dev).get(table="bgp.l3vpn.0")
for item in rie:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("------------")
rif = routeinfo(dev).get(table="mpls.0")
for item in rif:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
tm = TaskMemoryTable(dev).get()
#Task Memory
print("=========================TASK MEMORY INFO===============================")
for item in tm:
    print("Max Task Memory Used: "+str(item.task_memory_max_avail)+"%")
    print("Current Task Memory Used: "+str(item.task_memory_in_use_avail)+"%")
fp = FpcInfoTable(dev).get()
# Print all the information received from device
#FPC Details
print("=============================FPC INFO===================================")
for item in fp:
    print("Slot: "+str(item.slot))
    print("State: "+item.state)
    print("Total Memory: "+str(item.total_memory)+"MB")
    print("Memory-Heap-Utilization: "+str(item.memory)+"%")
re = reinfo(dev).get()
# Print all the information received from device
#Routing Engine information
print"==========================%s-RE-Info=================================" % (host)
for item in re:
    print("RE Slot#: "+item.reslot)
    print("RE Model: "+item.remodel)
    print("Mastership State: "+item.mastership_state)
    print("Memory Utilization: "+item.memory_utilization+"%")
    newcpu = int(item.cpu_idle)
    total = 100
    CPU = total - newcpu
    print("CPU Utilization: " +str(CPU)+"%")
    print("-------------------")
print"=============================================================================="

dev.close()
