#!/usr/bin/env python3
import sys
import getopt
from opsware.nas.connect import Connect

host = 'localhost'
port = '$tc_proxy_telnet_port$'
user = '$tc_user_username$'
passw = '$tc_user_password$'
device = '#$tc_device_id$'
output = []

try:
    opts, args = getopt.getopt(sys.argv[1:], "h:p:u:w:d:", ["host=", "port=", "user=", "pass=", "device="])
except getopt.GetoptError:
    print("Usage: script.py -h <host> -p <port> -u <user> -w <password> -d <device>")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        host = arg
    elif opt == '-p':
        port = arg
    elif opt == '-u':
        user = arg
    elif opt == '-w':
        passw = arg
    elif opt == '-d':
        device = arg

con = Connect(user=user, passw=passw, host=host, port=port)

con.login()
if con.connect(device):
    print("Connected to device: ", device)
else:
    print("Failed to connect to device: ", device)
    sys.exit(1)

con.cmd("terminal length 0")

print("tmsh list sys snmp users")
output = con.cmd("tmsh list sys snmp users")
print("\n".join(output))

print("tmsh save sys config")
output = con.cmd("tmsh save sys config")
print("\n".join(output))

print("tmsh list sys snmp users")
output = con.cmd("tmsh list sys snmp users")
print("\n".join(output))

print("tmsh modify sys snmp users delete indentf_2")
output = con.cmd("tmsh modify sys snmp users delete indentf_2")
print("\n".join(output))

print("tmsh list sys snmp users")
output = con.cmd("tmsh list sys snmp users")
print("\n".join(output))

con.disconnect()

con.logout()
con = None
sys.exit(0)
