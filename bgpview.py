#!/usr/bin/python
import yaml
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
# Set device information with IP-address, login user and passwort
dev = Device(host="172.27.0.159", user="rbindra", password="N0c@nd00")

# Open connection to the device
dev.open()

# Instead of loading a YAML-file place it within the code
yml = '''
---
bgpoutes:
 rpc: get-route-information
 args:
  protocol: bgp
  extensive: True
 item: route-table/rt
 key: rt-destination
 view: bgpView

bgpView:
 fields:
  as_path: rt-entry/as-path
  rt_destination: rt-destination
  rt_prefix_length: rt-prefix-length
  preference: rt-entry/preference
  community: rt-entry/communities/community
'''

# Load Table and View definitions via YAML into namespace
globals().update(FactoryLoader().load(yaml.load(yml)))

# Catching information from vMX1 through Table/View
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
