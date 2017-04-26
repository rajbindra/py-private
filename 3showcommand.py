#!/usr/bin/python
#Author: Raj Bindra
import sys
from lxml import etree
from getpass import getpass
from jnpr.junos import Device
from pprint import pprint
devices = open('device_list1')
devlist = devices.readlines()
user = raw_input('username: ')
passwd = getpass('password: ')
for host in devlist: 
    host = host.strip()
    print "Working on %s..." % host 
    dev = Device(host,user=user,password=passwd, port=22)
    dev.open()
    file = open(host, 'ab')    
    output = dev.cli("show chassis fpc", format='text', warning=False)
    file.write("\n%s"% (host))
    file.write('\n')
    file.write(output)   
    file.write('\n              ')
    #dev.close()
file.close()
