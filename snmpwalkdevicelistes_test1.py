import subprocess

# Define the command to execute
command_template = "/opt/OV/bin/nnmsnmpwalk.ovpl -v 3 -v3u netmonv3 -a SHA -A '0penView#123' -x AES256 -X '0penView#123' {} sysName"

# Define input and output file paths
input_file_path = '/tmp/iplist.txt'
output_file_path = '/tmp/outfile.txt'

# Read IP addresses from the input file
with open(input_file_path, 'r') as file:
    ip_addresses = file.readlines()

# Execute the command for each IP address and write output to the output file
with open(output_file_path, 'w') as outfile:
    for ip_address in ip_addresses:
        ip_address = ip_address.strip()
        command = command_template.format(ip_address)
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            outfile.write(f"Output for IP {ip_address}:\n")
            outfile.write(output)
            outfile.write("\n\n")
        except subprocess.CalledProcessError as e:
            outfile.write(f"Error executing command for IP {ip_address}:\n")
            outfile.write(e.output)
            outfile.write("\n\n")

print("Execution complete. Output written to", output_file_path)
