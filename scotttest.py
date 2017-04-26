import sys
import os
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import *

dev=Device(host=sys.argv[1], user='rbindra', password='N0c@nd00')
try:
    dev.open()
except Exception as err:
    print( "This device is currently napping. Go to the 'Run' page to wake it up! \n" ), err

print ( "Hostname: " + dev.hostname + "\n" )
#print ( "Model: " + dev.facts['model'] +  "\n" )
#print ( "Version: " + dev.facts['version'] +  "\n" )
#print ( "Serial Number: " + dev.facts['serialnumber'] + "\n" )


table_strings = []
inet = "inet "

test = dev.cli('show interfaces terse')

table_strings = filter(None, test.split('\n'))

print ( "Interfaces: \n" )
print (table_strings[0])


for x in range(len(table_strings)):

    if "bme" in table_strings[x]:
        continue

    if "pf" in table_strings[x]:
        continue

    if "em" in table_strings[x]:
        continue

    if inet in table_strings[x]:
        print (table_strings[x])


dev.close()

