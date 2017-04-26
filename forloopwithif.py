#for loop in a list with if, elif, else
my_devices_list=['172.30.108.11', '172.30.108.133', '172.30.108.133', '172.30.108.14',	'172.30.108.176', '172.30.108.254']
for device in my_devices_list:
 if device =='172.30.108.14':
  print "172.30.108.14 was found."
 elif device =='172.30.108.176':
  print "172.30.108.176 was found."
 else:
  print "go fly a kite"
#for loop in dictionary with if, else
this_is_a_dictionary={'ntp_server': '172.17.28.5', 'hostname': 'LAB-EX-VC-Backbone', 'domain': 'jnpr.net', 	'time_zone': 'Europe/Paris'}
for key in this_is_a_dictionary :
	 if key=='domain':
	  print "the domain is " + this_is_a_dictionary[key]

