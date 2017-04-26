#for loop with list
my_devices_list=['172.30.108.11', '172.30.108.133', '172.30.108.133', '172.30.108.14', 	'172.30.108.176', '172.30.108.254']
for device in my_devices_list:
	 print ("the current device is: " + device)
#for loop with range

range (2,6)
for i in range (2,6):
	print "set interface xe-0/0/%s unit 0 family Ethernet-switching" %i
#for loop with dictionary

this_is_a_dictionary={'ntp_server': '172.17.28.5', 'hostname': 'LAB-EX-VC-Backbone', 'domain': 'jnpr.net', 'name_server': '195.68.0.1', 'time_zone': 'Europe/Paris'}
for key in this_is_a_dictionary:
	 print key
for key in this_is_a_dictionary:
	 print this_is_a_dictionary[key]
#for loop with file
f=open('list_of_ip.txt')
for line in f:
	print line
f.close()
#for loop with a string
for characters in "whatever":
	print characters

