#!/usr/bin/python
from lxml import etree
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
from myTables.ConfigTables import TaskMemoryTable
# Set device information with IP-address, login user and passwort
dev = Device(host="172.27.0.162", user="rbindra", password="N0c@nd00", gather_facts=False)

# Open connection to the device
dev.open()

tm = TaskMemoryTable(dev).get()
# Print all the information received from device
for item in tm:
    print("---------------------------------------------")
    print("Max Task Memory Used: "+str(item.task_memory_max_avail)+"%")
    print("Current Task Memory Used: "+str(item.task_memory_in_use_avail)+"%")
print("==================================================")

dev.close()
