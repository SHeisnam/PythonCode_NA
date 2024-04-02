import subprocess

# Function to get user input with a prompt message
def get_input(prompt):
    return input(prompt)

# Path to the input file containing IP addresses
print("Enter the input file path containing IP addresses: ")
input_file = get_input()

# Path to the output log file
print("Enter the output file where snmpwalk info will be saved: ")
output_file = get_input()

# Prompt the service Account for input
print("Enter the Service Account: ")
serviceAccount = get_input()

# Prompt the authentication protocol pass phrase
print("Enter the Authentication Password: ")
authPassword = get_input()

# Prompt the privacy protocol pass phrase
print("Enter the Privacy Password: ")
privPassword = get_input()

# Command to execute
command = f"/opt/OV/bin/nnmsnmpwalk.ovpl -v 3 -v3u {serviceAccount} -a SHA -A '{authPassword}' -x AES256 -X '{privPassword}'"

print(input_file)
print(output_file)
print(serviceAccount)
print(authPassword)
print(privPassword)

# Check if input file exists
try:
    with open(input_file, 'r') as file:
        ip_addresses = file.readlines()
except FileNotFoundError:
    print(f"Input file {input_file} not found.")
    exit(1)

# Iterate through each IP address in the input file
for ip_address in ip_addresses:
    ip_address = ip_address.strip()  # Remove leading/trailing whitespaces
    # Execute the command for the current IP address and append output to the log file
    print(f"Executing snmpwalk using newly updated Auth-Password && Privacy Password for IP: {ip_address}")
    subprocess.run([command, ip_address, 'sysName'], stdout=open(output_file, 'a'), stderr=subprocess.STDOUT, text=True)
    print(f"SNMPWALK Command executed for IP: {ip_address}")

print(f"SNMPWALK validation script execution is completed. Output logged to {output_file}")
