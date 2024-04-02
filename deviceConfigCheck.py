import base64
import paramiko
import paramiko.transport
import cryptography.hazmat.primitives.ciphers 
import algorithms
import cipher
import modes
import sys
import time

def get_output(session):
            output = ''
            data=''
            time.sleep(1)

            not_done = True
            MAX_RETRY = 5

            while (not_done or MAX_RETRY > 0):
                    if(session.recv_ready()):
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
#device = '#$tc_device_id$'
#sshport = '$tc_proxy_ssh_port$'
device = '#401'
sshport = '8022'
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect('localhost', username='$tc_user_username$', password='$NA_Password$', port=sshport)
client.connect('rhel-nacore1.sac.swinfra.net', username='naadmin', password='0penView#123', port=8022)
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

print('show run\n')
session.send('show run\n')
output = get_output(session)
print('\n' + output)

print('sh \n')
session.send('sh \n')
output = get_output(session)
print('\n' + output)

print('show\n')
session.send('show\n')
output = get_output(session)
print('\n' + output)

print('show \n')
session.send('show \n')
output = get_output(session)
print('\n' + output)

print('show vtp\n')
session.send('show vtp\n')
output = get_output(session)
print('\n' + output)

print('sh snmp\n')
session.send('sh snmp\n')
output = get_output(session)
print('\n' + output)
       
session.send('exit\n')
output = get_output(session)
print(output)

client.close()

    
        