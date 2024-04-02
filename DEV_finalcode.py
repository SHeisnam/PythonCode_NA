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


    
      
print('Printing the New SNMPv3 credentials infomation \n')
session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator v3 auth sha ' + '$authpass$' + ' priv aes 128 ' + '$privpass$' + ' access 7\n')
# session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator v3 auth sha ' + '$authpass$' + ' priv aes 128 ' + '$privpass$' + '\n')
output = get_output(session)
print(output)




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



###########
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


    
            
print('Delete the Old SNMPv3 credentials infomation \n')
session.send('no snmp-server user ' + '$deleteuser$' +  ' network-operator v3\n')
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



###################
delete-add


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


    
      
print('Delete the Old SNMPv3 credentials infomation \n')
session.send('no snmp-server user ' + '$deleteuser$' +  ' network-operator v3\n')
output = get_output(session)
print(output)




print('Review if the Old SNMPv3 credentials is deleted Or Not\n')
session.send('do show snmp user\n')
output = get_output(session)
print('\n' + output)




print('Update/Add the New SNMPv3 credentials infomation \n')
session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator v3 auth sha ' + '$authpass$' + ' priv aes 128 ' + '$privpass$' + ' access 7\n')
# session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator v3 auth sha ' + '$authpass$' + ' priv aes 128 ' + '$privpass$' + '\n')
output = get_output(session)
print(output)




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


######################
XR - Add


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


    
#snmp-server user srvcnetmonv3 network-operator v3 auth sha clear <PASS1> priv aes 128 clear <PASS2> IPv4 SNMPv3-ACCESS   
print('Update/Add the New SNMPv3 credentials infomation \n')
session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator v3 auth sha clear ' + '$authpass$' + ' priv aes 128 clear ' + '$privpass$' + ' IPv4 SNMPv3-ACCESS\n')
output = get_output(session)
print(output)


    
        
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

################
delete


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


    
            
print('Delete the Old SNMPv3 credentials infomation \n')
session.send('no snmp-server user ' + '$deleteuser$' +  ' network-operator v3\n')
output = get_output(session)
print(output)

    

        
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

#########################################

delete-add 

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


    
      
print('Delete the Old SNMPv3 credentials infomation \n')
session.send('no snmp-server user ' + '$deleteuser$' +  ' network-operator v3\n')
output = get_output(session)
print(output)




print('Review if the Old SNMPv3 credentials is deleted Or Not\n')
session.send('do show snmp user\n')
output = get_output(session)
print('\n' + output)




#snmp-server user srvcnetmonv3 network-operator v3 auth sha clear <PASS1> priv aes 128 clear <PASS2> IPv4 SNMPv3-ACCESS     
print('Update/Add the New SNMPv3 credentials infomation \n')
session.send('snmp-server user ' + '$snmpv3User$' + ' network-operator v3 auth sha clear ' + '$authpass$' + ' priv aes 128 clear ' + '$privpass$' + ' IPv4 SNMPv3-ACCESS\n')
output = get_output(session)
print(output)


    
        
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


############################# NX 

add 

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


#####################
delete

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


    
            
print('Delete the Old SNMPv3 credentials infomation \n')
session.send('no snmp-server user ' + '$deleteuser$' +  '\n')
output = get_output(session)
print(output)



        
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


######################

delete-add 

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


    
            
print('Delete the Old SNMPv3 credentials infomation \n')
session.send('no snmp-server user ' + '$deleteuser$' +  '\n')
output = get_output(session)
print(output)




print('View the list of SNMPv3 Users\n')
session.send('do show snmp user\n')
output = get_output(session)
print('\n' + output)




print('Update/Add the New SNMPv3 credentials infomation \n')
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

################################## F5

add

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




print('Add SNMPv3 Users for F5\n')
session.send('tmsh modify sys snmp users add { ' + '$identSrvAccountUser$' + ' { username ' + '$srvAccount$' + ' auth-protocol sha privacy-protocol des security-level auth-privacy oid-subset .1 auth-password ' + '$authpass$' + ' privacy-password ' + '$privpass$' + ' } }\n')
output = get_output(session)
print(output)




print('Saving the final configuration after adding the srvAccount_the SNMpv3 Users information\n')
session.send('tmsh save sys config\n')
output = get_output(session)
print(output)




print('Printing the SNMPv3 Users information\n')
session.send('tmsh list sys snmp users\n')
output = get_output(session)
print('\n' + output)



session.send('exit\n')
output = get_output(session)
print(output)



client.close()

#######################
delete 

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


    
        
print('Printing the SNMpv3 Users information\n')
session.send('tmsh list sys snmp users\n')
output = get_output(session)
print('\n' + output)




print('Delete SNMPv3 Users for F5\n')
# tmsh modify sys snmp users delete { inetmonv3_1 }
session.send('tmsh modify sys snmp users delete { ' + '$identSrvAccountUser$' + ' }\n')
output = get_output(session)
print('\n' + output)



    
print('Saving the final configuration after deleting the srvAccount_the SNMpv3 Users information\n')
session.send('tmsh save sys config\n')
output = get_output(session)
print('\n' + output)
    
        

print('Printing the SNMpv3 Users information\n')
session.send('tmsh list sys snmp users\n')
output = get_output(session)
print('\n' + output)


    
        
session.send('exit\n')
output = get_output(session)
print(output)



client.close()

##############################

delete-add

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



    
        
print('Printing the SNMpv3 Users information\n')
session.send('tmsh list sys snmp users\n')
output = get_output(session)
print('\n' + output)




print('Delete SNMPv3 Users for F5\n')
# tmsh modify sys snmp users delete { inetmonv3_1 }
session.send('tmsh modify sys snmp users delete { ' + '$identSrvAcctDeleteUser$' + ' }\n')
output = get_output(session)
print('\n' + output)




print('Printing the SNMpv3 Users information\n')
session.send('tmsh list sys snmp users\n')
output = get_output(session)
print('\n' + output)




print('Add SNMPv3 Users for F5\n')
session.send('tmsh modify sys snmp users add { ' + '$identSrvAccountUser$' + ' { username ' + '$srvAccount$' + ' auth-protocol sha privacy-protocol des security-level auth-privacy oid-subset .1 auth-password ' + '$authpass$' + ' privacy-password ' + '$privpass$' + ' } }\n')
output = get_output(session)
print('\n' + output)



    
print('Saving the final configuration after deleting and adding the srvAccount_the SNMpv3 Users information\n')
session.send('tmsh save sys config\n')
output = get_output(session)
print('\n' + output)
    
        


print('Printing the SNMpv3 Users information\n')
session.send('tmsh list sys snmp users\n')
output = get_output(session)
print('\n' + output)


    
        
session.send('exit\n')
output = get_output(session)
print(output)



client.close()



####################

/usr/local/lib/python3.6/site-packages/paramiko/transport.py:32: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography will remove support for Python 3.6.
Connect to remote device #7141 test-devices
  from cryptography.hazmat.backends import default_backend

connect #7141
Attempting to connect to device US-DAL-RIT-OOBACC01 (10.111.129.101).

Device SSH Login:  
Testxxxxx
Device SSH Password:  



Printing the running configuration and review the SNMPv3 setting


show running-config | include snmp

username snmpv3User3 password 5 $5$NPNDCA$PM9b8dQ3JQTD.RW7hsE8dDlfupQ3vO5Yp.eT9zTC0o2  role network-operator
username snmpv3User3 passphrase  lifetime 99999 warntime 14 gracetime 3
snmp-server user xxxxx network-xxxxx auth md5 0x39419a5d9e475c362e6e28b39f5ae416 priv 0x39419a5d9e475c362e6e28b39f5ae416 localizedkey
snmp-server user Testxxxxx priv-15 auth md5 0xe51b3c748e4ddbefc7750b59950497e0 priv 0xe51b3c748e4ddbefc7750b59950497e0 localizedkey
snmp-server user merrickv3 network-operator auth sha 0x69bd684bda3d02ae3dda522eb44447ea989c783d priv aes-128 0x4624066a373a770fad0dc716bb023ed6fd829cb9 localizedkey
snmp-server user snmpv3User3 network-operator auth sha 0x093922a00ec1f6d0a5d441434ea8c2f747fbc457 priv aes-128 0x093922a00ec1f6d0a5d441434ea8c2f747fbc457 localizedkey
snmp-server user srvcritlabv3 network-operator auth sha 0xc061ca5c919f4664df5690d230fa53cfb0a49ea3 priv aes-128 0x436d4005f6ab2df2ac5c5e932e55f753cbb2aad8 localizedkey

US-DAL-RIT-OOBACC01#
View the list of SNMPv3 Users


show snmp user

______________________________________________________________
                  SNMP USERS
______________________________________________________________

User                Auth      Priv(enforce) Groups              acl_filter          
____                ____      _____________ ______              __________          
xxxxx               md5       des(no)       network-xxxxx      
Testxxxxx           md5       des(no)       priv-15            
merrickv3           sha       aes-128(no)   network-operator    
snmpv3User3         sha       aes-128(no)   network-operator    
srvcritlabv3        sha       aes-128(no)   network-operator    
______________________________________________________________
NOTIFICATION TARGET USERS (configured  for sending V3 Inform)
______________________________________________________________

User                          Auth      Priv          
____                          ____      ____          

US-DAL-RIT-OOBACC01#
Getting into the configuration terminal


config t

Enter configuration commands, one per line. End with CNTL/Z.

US-DAL-RIT-OOBACC01(config)#
Printing the New SNMPv3 credentials infomation

snmp-server user snmpv3User5 network-operator auth  sha ****** priv aes-128 ******


US-DAL-RIT-OOBACC01(config)#
View the list of SNMPv3 Users


do show snmp user

______________________________________________________________
                  SNMP USERS
______________________________________________________________

User                Auth      Priv(enforce) Groups              acl_filter          
____                ____      _____________ ______              __________          
xxxxx               md5       des(no)       network-xxxxx      
Testxxxxx           md5       des(no)       priv-15            
merrickv3           sha       aes-128(no)   network-operator    
snmpv3User3         sha       aes-128(no)   network-operator    
snmpv3User5         sha       aes-128(no)   network-operator    
srvcritlabv3        sha       aes-128(no)   network-operator    
______________________________________________________________
NOTIFICATION TARGET USERS (configured  for sending V3 Inform)
______________________________________________________________

User                          Auth      Priv          
____                          ____      ____          

US-DAL-RIT-OOBACC01(config)#
exit


US-DAL-RIT-OOBACC01#
Printing the running configuration and review the SNMPv3 setting


show running-config | include snmp

username snmpv3User3 password 5 $5$NPNDCA$PM9b8dQ3JQTD.RW7hsE8dDlfupQ3vO5Yp.eT9zTC0o2  role network-operator
username snmpv3User3 passphrase  lifetime 99999 warntime 14 gracetime 3
username snmpv3User5 password 5 $5$CEIDAK$7emkTBSwx2fquCxWnxlZLHITu5hf/hu89JCTes9Gmt/  role network-operator
username snmpv3User5 passphrase  lifetime 99999 warntime 14 gracetime 3
snmp-server user xxxxx network-xxxxx auth md5 0x39419a5d9e475c362e6e28b39f5ae416 priv 0x39419a5d9e475c362e6e28b39f5ae416 localizedkey
snmp-server user Testxxxxx priv-15 auth md5 0xe51b3c748e4ddbefc7750b59950497e0 priv 0xe51b3c748e4ddbefc7750b59950497e0 localizedkey
snmp-server user merrickv3 network-operator auth sha 0x69bd684bda3d02ae3dda522eb44447ea989c783d priv aes-128 0x4624066a373a770fad0dc716bb023ed6fd829cb9 localizedkey
snmp-server user snmpv3User3 network-operator auth sha 0x093922a00ec1f6d0a5d441434ea8c2f747fbc457 priv aes-128 0x093922a00ec1f6d0a5d441434ea8c2f747fbc457 localizedkey
snmp-server user snmpv3User5 network-operator auth sha 0x69bd684bda3d02ae3dda522eb44447ea989c783d priv aes-128 0x69bd684bda3d02ae3dda522eb44447ea989c783d localizedkey
snmp-server user srvcritlabv3 network-operator auth sha 0xc061ca5c919f4664df5690d230fa53cfb0a49ea3 priv aes-128 0x436d4005f6ab2df2ac5c5e932e55f753cbb2aad8 localizedkey

US-DAL-RIT-OOBACC01#
View the list of SNMPv3 Users


show snmp user

______________________________________________________________
                  SNMP USERS
______________________________________________________________

User                Auth      Priv(enforce) Groups              acl_filter          
____                ____      _____________ ______              __________          
xxxxx               md5       des(no)       network-xxxxx      
Testxxxxx           md5       des(no)       priv-15            
merrickv3           sha       aes-128(no)   network-operator    
snmpv3User3         sha       aes-128(no)   network-operator    
snmpv3User5         sha       aes-128(no)   network-operator    
srvcritlabv3        sha       aes-128(no)   network-operator    
______________________________________________________________
NOTIFICATION TARGET USERS (configured  for sending V3 Inform)
______________________________________________________________

User                          Auth      Priv          
____                          ____      ____          

US-DAL-RIT-OOBACC01#
exit





Successful snapshot taken.

View new configuration | Compare new configuration with previous

