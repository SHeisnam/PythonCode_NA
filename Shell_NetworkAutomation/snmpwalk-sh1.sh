#!/bin/bash

# Path to the input file containing IP addresses
input_file="/tmp/iplist.txt"

# Path to the output log file
output_file="/tmp/outfile.txt"

# Command to execute
command="/opt/OV/bin/nnmsnmpwalk.ovpl -v 3 -v3u netmonv3 -a SHA -A '0penView#123' -x AES256 -X '0penView#123'"

# Check if input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found."
    exit 1
fi

# Iterate through each IP address in the input file
while IFS= read -r ip_address; do
    # Execute the command for the current IP address and append output to the log file
    echo "Executing command for IP: $ip_address"
    $command "$ip_address" sysName >> "$output_file" 2>&1
    echo "Command executed for IP: $ip_address"
done < "$input_file"

echo "Script execution completed. Output logged to $output_file"
