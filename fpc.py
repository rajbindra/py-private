from myTables.ConfigTables import FpcInfoTable
from lxml import etree
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader

# Set device information with IP-address, login user and passwort
dev = Device(host="172.27.0.162", user="rbindra", password="N0c@nd00", gather_facts=False)

# Open connection to the device
dev.open()

fp = FpcInfoTable(dev).get()
# Print all the information received from device
#print("===================RE Info========================")
for item in fp:
    print("---------------------------------------------")
    print("Slot: "+str(item.slot))
    print("State: "+item.state)    
    print("Total Memory: "+str(item.total_memory)+"MB")
    print("Memory-Heap-Utilization: "+str(item.memory)+"%")
#    print("CPU Utilization: " +str(CPU)+"%")
print("==================================================")

dev.close()
