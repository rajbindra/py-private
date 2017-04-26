#!/usr/bin/python
# -*- coding: utf-8 -*-
from jnpr.junos import Device
from lxml import etree
from pprint import pprint as pp
from jnpr.junos.op.routes import RouteTable
dev = Device(host='172.27.0.165', user='rbindra', password='N0c@nd00', port = 22)
dev.open()
dev.timeout = 30000
file = open('routes.txt', 'ab') 
routes = RouteTable(dev)
RTable = routes.get(table='inet.0')
print routes
#file.write(routes)
#file.write(etree.tostring(RTable))
#routes = dev.rpc.get_route_information(table='inet.0')
#file.write(etree.tostring(routes)) 
dev.close()
