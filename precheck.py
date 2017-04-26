from jnpr.junos import Device
from jnpr.junos.exception import *          # Various exceptions
from jnpr.junos.utils.config import Config  # to perform configuration
from jnpr.junos.utils.fs import FS          # file operations to check image
from jnpr.junos.utils.start_shell import StartShell

from jnpr.jsnapy import SnapAdmin           #  This is JSNAPy snapshots
from getpass import getpass

from sys  import argv               # for command line parameters
from lxml import etree              # for XML contructs
import time                         # In order to sleep and get time
def myprint(str):

    print (time.strftime(" %H:%M:%S",time.gmtime()) + "  " + str)

host = raw_input('hostname: ')
user = raw_input('username: ')
passwd = getpass('password: ')

print "Working on %s..." % host 
dev = Device(host,user=user,password=passwd, port=22)
try:
    dev.open()
except ConnectError as error:
    print 'Unable to connect: ' , error 
    exit()
dev.timeout=2500

js = SnapAdmin()
config_file = "junos-upgrade.yml"
myprint ("Taking snapshot of states before the upgrade")
snapvalue = js.snap(config_file, "pre", dev=dev)

if snapvalue[0] == None:
    myprint ("*** Error while getting snapshot perhaps config file is not there")
    exit()

