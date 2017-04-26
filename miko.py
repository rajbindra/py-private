#!/usr/bin/python
#Author: Raj Bindra
import paramiko
import sys
from lxml import etree
from getpass import getpass
from pprint import pprint
devices = open('1host')
devlist = devices.readlines()
user = raw_input('username: ')
passwd = getpass('password: ')
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for host in devlist:
    host = host.strip()
    remote_conn_pre.connect(host, username=user, password=passwd, look_for_keys=False, allow_agent=False, port=22)
    remote_conn = remote_conn_pre.invoke_shell()
    out = remote_conn.recv(5000)
    print out
    stdin, stdout, stderr = remote_conn_pre.exec_command('show chassis routing-engine\n')
    print stdout.read()
    stdin, stdout, stderr = remote_conn_pre.exec_command('show version\n')
    print stdout.read()
