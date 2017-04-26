#!/usr/bin/python
# -*- coding: utf-8 -*-
from jnpr.junos import Device
from lxml import etree
from getpass import getpass
from jnpr.junos.op.xcvr import XcvrTable
import sys
user = raw_input('username: ')
passwd = getpass('password: ')
with open('output.txt', 'a') as fp:
    for hosts in open('device_list1'):
        with Device(host=hosts, user=user, password=passwd, port=22) as dev:
            op = dev.rpc.get_chassis_inventory(detail=True)
            fp.write("user@%s>show chassis hardware detail | display xml"%(hosts))
            fp.write(etree.tostring(op))		
