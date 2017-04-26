from lxml import etree
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader

# Set device information with IP-address, login user and passwort
host="172.27.0.162"
dev = Device(host="172.27.0.162", user="rbindra", password="N0c@nd00", gather_facts=False)

# Open connection to the device
dev.open()

# Instead of loading a YAML-file place it within the code
yml = '''
---
reinfo:
 rpc: get-route-engine-information
 item: route-engine
 key: slot
 view: REView

REView:
 fields:
  reslot: slot
  mastership_state: mastership-state
  memory_utilization: memory-buffer-utilization
  cpu_idle: cpu-idle
  remodel: model
'''

# Load Table and View definitions via YAML into namespace
globals().update(FactoryLoader().load(yaml.load(yml)))

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

dev.close()
