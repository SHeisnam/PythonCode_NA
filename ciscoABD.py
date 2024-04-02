import base64
import paramiko
import sys
import time


def get_output(session):
    output = ''
    data = ''
    time.sleep(1)

    not_done = True
    MAX_RETRY = 5

    while (not_done or MAX_RETRY > 0):
        if (session.recv_ready()):
            data = session.recv(65535).decode('ascii')
            output += data
            if MAX_RETRY < 5:
                MAX_RETRY = 5
        else:
            not_done = False
            MAX_RETRY = MAX_RETRY - 1

    return output


client = paramiko.SSHClient()
client.load_system_host_keys()
device = '#$tc_device_id$'
sshport = '$tc_proxy_ssh_port$'
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('localhost', username='$tc_user_username$', password='$NA_Password$', port=sshport)
transport = client.get_transport()
session = transport.open_session()
session.set_combine_stderr(True)
session.invoke_shell()

get_output(session)

session.send('connect ' + device + '\n')
output = get_output(session)
print(output)

session.send('terminal length 0\n')
output = get_output(session)

print('conf t\n')
session.send('conf t\n')
output = get_output(session)
print('\n' + output)

print('do show run\n')
session.send('do show run\n')
output = get_output(session)
print('\n' + output)

print('do show ip route\n')
session.send('do show ip route\n')
output = get_output(session)
print('\n' + output)

print('do show vlan brief\n')
session.send('do show vlan brief\n')
output = get_output(session)
print('\n' + output)

print('do show ip interface b\n')
session.send('do show ip interface b\n')
output = get_output(session)
print('\n' + output)

print('do show vlan b\n')
session.send('do show vlan b\n')
output = get_output(session)
print('\n' + output)

print('do show vlan brief\n')
session.send('do show vlan brief\n')
output = get_output(session)
print('\n' + output)

print('exit\n')
session.send('exit\n')
output = get_output(session)
print('\n' + output)

session.send('exit\n')
output = get_output(session)
print(output)

client.close()


