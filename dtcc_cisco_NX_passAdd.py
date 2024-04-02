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
device = '#$tc_device_id$'
sshport = '$tc_proxy_ssh_port$'



client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('localhost', username='$NA_User$', password='$NA_Password$', port=sshport)
transport = client.get_transport()
session = transport.open_session()
session.set_combine_stderr(True)
session.invoke_shell()

get_output(session)

print('Connect to remote device ' + device + ' test-devices\n')
session.send('connect ' + device + '\n')
output = get_output(session)
print(output)

session.send('$device_user$\n')
output = get_output(session)
print(output)
session.send('$device_password$\n')
output = get_output(session)
print(output)
session.send('terminal length 0\n')
output = get_output(session)


print('Getting into the configuration terminal\n')
session.send('config t\n')
output = get_output(session)
print('\n' + output)


    
            
print('Printing the New SNMPv3 credentials infomation \n')
session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator auth sha ' + '$authpass$' + ' priv aes-128 ' + '$privpass$' + '\n')
output = get_output(session)
print(output)




print('View the list of SNMPv3 Users\n')
session.send('do show snmp user\n')
output = get_output(session)
print('\n' + output)

    
        
session.send('exit\n')
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
