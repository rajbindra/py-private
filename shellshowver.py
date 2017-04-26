#/usr/bin/python
#Author: Raj Bindra
import sys
from lxml import etree
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from pprint import pprint
import re
devices = open('device_list1')
devlist = devices.readlines()
user = raw_input('username: ')
passwd = getpass('password: ')
for host in devlist: 
    host = host.strip()
    file = open('shell.txt', 'ab')
    print "Working on %s..." % host 
    dev = Device(host,user=user,password=passwd, port=22)
    ss = StartShell(dev)
    ss.open()
    output =  ss.run('cli -c "show chassis fpc | match Online"')    
#    file.write(output)   
#    file.write('\n              ')
    print output
    ss.close()
#file.close()
