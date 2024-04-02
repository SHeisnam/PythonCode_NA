import base64
import paramiko
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
snmpv3User = '$tc_device_snmpv3_username$'
authpass = '$tc_device_snmpv3_password$'
privpass = '$tc_device_snmpv3_encryption$'


device = '#301'
sshport = '8022'
snmpv3User = 'snmpV3User'
authpass = 'authpass'
privpass = 'privpass'


client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect('localhost', username='$tc_user_username$', password='$NA_Password$', port=sshport)
client.connect('rhel-nacore1.sac.swinfra.net', username='naadmin', password='0penView#123', port=8022)
transport = client.get_transport()
session = transport.open_session()
session.set_combine_stderr(True)
session.invoke_shell()

get_output(session)


print('Connect to remote device ' + device + ' test-devices\n')
session.send('connect ' + device + '\n')
output = get_output(session)
print(output)

print('Printing the New SNMPv3 credentials information \n')
commands = [
    'config t',
    'snmp-server user ' + snmpv3User + ' network-operator v3 auth sha ' + authpass + ' priv aes 128 ' + privpass + ' access 7',
    'exit'
]

for cmd in commands:
    session.send(cmd + '\n')
    output = get_output(session)
    print(output)


print('View the list of SNMPv3 Users\n')
session.send('show snmp user\n')
output = get_output(session)
print('\n' + output)

    
        
session.send('exit\n')
output = get_output(session)
print(output)

client.close()
