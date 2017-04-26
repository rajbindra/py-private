import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.op.xcvr import XcvrTable
devlist = ['CIR1.Amsterdam2-NH','CIR1.Ashburn-VA']
user = raw_input('username: ')
passwd = getpass('password: ') 
for host in devlist:
    sys.stdout.write('rbindra@%s>show chassis hardware detail' % host)
#    sys.stdout.flush()
    dev = Device(host,user=user,password=passwd, port=22)
    dev.open()
    print dev.cli("show chassis hardware", warning=False)  
    dev.close()
