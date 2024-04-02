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
device = '#1501'
sshport = '8022'
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect('localhost', username='$tc_user_username$', password='$NA_Password$', port=sshport)
client.connect('na1.advantageinc.org', username='awest', password='G0th@mc!ty', port=8022)
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

    
        

print('show running config\n')
session.send('show running config\n')
output = get_output(session)
print('\n' + output)

    
        

print('show running-config\n')
session.send('show running-config\n')
output = get_output(session)
print('\n' + output)

    
        

print('show snmp\n')
session.send('show snmp\n')
output = get_output(session)
print('\n' + output)

    
        

print('show snmp group\n')
session.send('show snmp group\n')
output = get_output(session)
print('\n' + output)
    

    
        
session.send('exit\n')
output = get_output(session)
print(output)

client.close()

    
        