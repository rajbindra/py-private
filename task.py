#!/usr/bin/python
from lxml import etree
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
from myTables.ConfigTables import TaskMemoryTable
import xlwt
# Set device information with IP-address, login user and passwort
dev = Device(host="172.27.0.162", user="rbindra", password="N0c@nd00", gather_facts=False)

# Open connection to the device
dev.open()

tm = TaskMemoryTable(dev).get()
# Print all the information received from device
host="172.27.0.162"
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0, 0, "Hostname")
sheet1.write(0, 1, "Max Task Memory Used")
sheet1.write(0, 2, "Current Task Memory Used")
for item in tm:
    sheet1.write(1, 0, host)
    sheet1.write(1, 1, str(item.task_memory_max_avail))
    sheet1.write(1, 2, str(item.task_memory_in_use_avail))
book.save("test.xls")
dev.close()
