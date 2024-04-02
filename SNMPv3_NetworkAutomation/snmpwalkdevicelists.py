import subprocess

# Read the IP list from the file
with open('/tmp/iplist.txt', 'r') as f:
    ip_list = f.read().splitlines()

# SNMP parameters
#snmp_username = 'snmp-poller'
#snmp_auth_password = 'PASSWORD1'
#snmp_priv_password = 'PASSWORD1'

snmp_username = int("Enter the SNMPv3 Username: ")
snmp_auth_password = int("Authentication_Password: ")
snmp_priv_password = int("Privacy_Password: ")



# Iterate over each IP and execute the snmpwalk command
for ip in ip_list:
    snmpwalk_command = [
        'snmpwalk',
        '-v3',
        '-l', 'authPriv',
        '-u', snmp_username,
        '-a', 'SHA',
        '-A', snmp_auth_password,
        '-x', 'AES',
        '-X', snmp_priv_password,
        ip
    ]

    # Execute the command and capture output
    try:
        result = subprocess.run(snmpwalk_command, capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error executing snmpwalk command for IP {ip}: {e}\n"

    # Write output to log file
    with open('/tmp/outfile.txt', 'a') as log_file:
        log_file.write(f"Output for {ip}:\n")
        log_file.write(output)
        log_file.write('\n')