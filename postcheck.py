from jnpr.junos import Device
from jnpr.junos.exception import *          # Various exceptions
from jnpr.junos.utils.config import Config  # to perform configuration
from jnpr.junos.utils.fs import FS          # file operations to check image
from jnpr.junos.utils.start_shell import StartShell

from jnpr.jsnapy import SnapAdmin           #  This is JSNAPy snapshots


from sys  import argv               # for command line parameters
from lxml import etree              # for XML contructs
from getpass import getpass                      # in order to get password without echo
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

myprint ("waiting 10 seconds before taking post snapshot....")
time.sleep(10)
myprint ("gathering snapshot after upgrade....")
snapvalue = js.snap(config_file, "post", dev=dev)

print
myprint ("Comparing pre and post snapshots")
snapvalue = js.check(config_file, "pre", "post", dev=dev)

