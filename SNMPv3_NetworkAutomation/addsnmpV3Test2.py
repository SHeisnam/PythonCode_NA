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


    
        
print('Printing the running configuration and review the SNMPv3 setting\n')
session.send('show running-config | include snmp\n')
output = get_output(session)
print('\n' + output)

    
        

print('View the list of SNMPv3 Users\n')
session.send('show snmp user\n')
output = get_output(session)
print('\n' + output)

    
        

print('Getting into the configuration terminal\n')
session.send('config t\n')
output = get_output(session)
print('\n' + output)

    
        

print('Adding new Group--> ps-network-operator for PS lab setup\n')
session.send('snmp-server group ps-network-operator v3 priv\n')
output = get_output(session)
print('\n' + output)

    
        

print('Adding new User psnetwork1 to new Group - ps-network-operator for PS lab setup\n')
session.send('snmp-server user psnetwork1 network-operator v3 auth sha $auth_password priv aes 128 $priv_password access 7\n')
output = get_output(session)
print('\n' + output)




print('Adding new User psnetwork2 to new Group - ps-network-operator for PS lab setup\n')
session.send('snmp-server user psnetwork2 network-operator v3 auth sha 0penView#123 priv aes 128 ssw0rd123P@ access 7\n')
output = get_output(session)
print('\n' + output)




print('View the list of SNMPv3 Users\n')
session.send('do show snmp user\n')
output = get_output(session)
print('\n' + output)

    
        
session.send('exit\n')
output = get_output(session)
print(output)



print('Printing the running configuration and review the SNMPv3 setting\n')
session.send('show running-config | include snmp\n')
output = get_output(session)
print('\n' + output)



print('View the list of SNMPv3 Users\n')
session.send('show snmp user\n')
output = get_output(session)
print('\n' + output)

    
        
session.send('exit\n')
output = get_output(session)
print(output)



client.close()        