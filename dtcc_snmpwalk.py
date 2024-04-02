#!/usr/bin/env python3

import subprocess

# Path to the input file containing IP addresses
input_file = input("Enter the input file path containing IP addresses: ")

# Path to the output log file
output_file = input("Enter the output file where SNMPWALK info will be saved: ")

# Prompt for the service Account input
serviceAccount = input("Enter the Service Account: ")

# Prompt for the authentication protocol pass phrase
authPassword = input("Enter the Authentication Password: ")

# Prompt for the privacy protocol pass phrase
privPassword = input("Enter the Privacy Password: ")

# Main CLI to test SNMPWALK to each IP address listed in the input file
command = f"/opt/OV/bin/nnmsnmpwalk.ovpl -v 3 -v3u {serviceAccount} -a SHA -A {authPassword} -x AES -X {privPassword}"

print("Making sure the data are stored as variables ")
print(input_file)
print(output_file)
print(serviceAccount)
print(authPassword)
print(privPassword)

# Check if input file exists, else exit with error message
try:
    with open(input_file, 'r') as f:
        ip_addresses = f.readlines()
except FileNotFoundError:
    print(f"The given input file '{input_file}' not found. Provide the correct input file path and re-execute the script.")
    exit(1)

# Iteration process through each IP address in the input file and test the SNMPWALK for each IP address
with open(output_file, 'w') as f_out:
    for ip_address in ip_addresses:
        ip_address = ip_address.strip()  # Remove leading/trailing whitespaces
        # Execute the command for the current IP address
        try:
            result = subprocess.run([command, ip_address, 'sysName'], capture_output=True, text=True, check=True)
            value = result.stdout.splitlines()[0].split(':')[-1].strip()
            f_out.write(f"PASSED | {ip_address} | is a Compliance Device | Hostname = {value} | SNMPWALK is responding\n")
        except subprocess.CalledProcessError as e:
            f_out.write(f"FAILED | {ip_address} | is NOT a Compliance Device | Hostname is unable to resolve | SNMPWALK is NOT responding\n")

print("SNMPWALK validation script execution is completed. Output logged to", output_file)
