from myTables.ConfigTables import TaskMemoryTable
from myTables.ConfigTables import routeinfo
from myTables.ConfigTables import FpcInfoTable
from myTables.ConfigTables import reinfo
from myTables.ConfigTables import bgpoutes 
from lxml import etree
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader

# Set device information with IP-address, login user and passwort
dev = Device(host="172.27.0.162", user="rbindra", password="N0c@nd00", gather_facts=False)

# Open connection to the device
dev.open()

ri = routeinfo(dev).get(table="inet.0")
# Print all the information received from device
for item in ri:
    print("==================================================")    
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)    
    print("Total Routes: "+item.total_route_count)
#    print("Memory Utilization: "+item.memory_utilization+"%")
#    newcpu = int(item.cpu_idle)
#    total = 100
#    CPU = total - newcpu 
#    print("CPU Utilization: " +str(CPU)+"%")
print("==================================================")
ria = routeinfo(dev).get(table="inet.2")
# Print all the information received from device
for item in ria:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("==================================================")
rib = routeinfo(dev).get(table="inet.3")
# Print all the information received from device
for item in rib:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("==================================================")
ric = routeinfo(dev).get(table="inet6.0")
# Print all the information received from device
for item in ric:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("==================================================")
rid = routeinfo(dev).get(table="bgp.l2vpn.0")
# Print all the information received from device
for item in rid:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("==================================================")
rie = routeinfo(dev).get(table="bgp.l3vpn.0")
# Print all the information received from device
for item in rie:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("==================================================")
rif = routeinfo(dev).get(table="mpls.0")
# Print all the information received from device
for item in rif:
    print("Table Name: "+item.table_name)
    print("Active Routes: "+item.active_route_count)
    print("Total Routes: "+item.total_route_count)
print("==================================================")
tm = TaskMemoryTable(dev).get()
# Print all the information received from device
for item in tm:
    print("---------------------------------------------")
    print("Max Task Memory Used: "+str(item.task_memory_max_avail)+"%")
    print("Current Task Memory Used: "+str(item.task_memory_in_use_avail)+"%")
print("==================================================")
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
re = reinfo(dev).get()
# Print all the information received from device
print"==================%s-RE-Info========================" % (host)
for item in re:
    print"---------------------------------------------"
    print("RE Slot#: "+item.reslot)
    print("RE Model: "+item.remodel)
    print("Mastership State: "+item.mastership_state)
    print("Memory Utilization: "+item.memory_utilization+"%")
    newcpu = int(item.cpu_idle)
    total = 100
    CPU = total - newcpu
    print("CPU Utilization: " +str(CPU)+"%")
print"=================================================="
bt = bgpoutes(dev).get()
# Print all the information received from device
print("---------------------------------------------")
print("-----------------BGP Routes------------------")
print("---------------------------------------------")
for item in bt:
    print("-")
    print("Route: "+item.rt_destination+"/"+item.rt_prefix_length)
    print(item.as_path+" // Preference: "+item.preference+" // Community: "+str(item.community))
print("-")
print("---------------------------------------------")

dev.close()
