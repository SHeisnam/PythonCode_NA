from Opsware.NAS.Client import NASClient
from Opsware.NAS.Connect import NASConnect
import warnings
import getopt
import socket

host = '10.10.16.12'
user = 'naadmin'
passw = 'naadmin'
port = '8023'

tc_device_ip = '10.10.16.18'
labDevices = [
    '172.16.10.1', '172.16.10.2', '172.16.10.3', '172.16.10.4',
    '172.16.10.5', '10.10.16.18', '10.10.16.19'
]
groups = ['CoreNetwork', 'group1']

prompt = r'\]|\>'
nas = NASClient()

# Login to the NA Proxy Server
res = nas.login(user=user, passw=passw, host=host, port=port)
if not res:
    print("*** error Unable to login to NA:", file=sys.stderr)
    exit(1)

# Configure a global default password rule
res = nas.del_authentication(rulename="GlobalDefault", loc="db")
res = nas.add_authentication(
    loc="db",
    passwd="naadmin",
    snmpro="public",
    enablepasswd="naadmin",
    user="naadmin",
    ruledevicegroup="Inventory",
    rule="GlobalDefault"
)

# Create Devices
def createDevices():
    # Add Lab Devices
    for deviceip in labDevices:
        res = nas.del_device(ip=deviceip)
        res = nas.add_device(ip=deviceip)
        res = nas.discover_driver(ip=deviceip)

# Create the class-defined groups
def createGroups():
    for group in groups:
        res = nas.del_group(name=group, type='device')
        res = nas.add_device_group(
            name=group,
            type="static"
        )

    # No create parent child
    res = nas.del_group(name='pgroup1', type='device')
    res = nas.add_parent_group(name="pgroup1", type="device")

    res = nas.add_group_to_parent_group(
        parent="pgroup1",
        child="group1"
    )

    # Add device memberships
    coreNodes = [
        '172.16.10.1', '172.16.10.2', '172.16.10.3', '172.16.10.4',
        '172.16.10.5'
    ]
    for deviceip in coreNodes:
        res = nas.add_device_to_group(
            group="CoreNetwork",
            ip=deviceip
        )
    res = nas.add_device_to_group(group="group1", ip='10.10.16.18')
    res = nas.add_device_to_group(group="group1", ip='10.10.16.19')

createDevices()
createGroups()

print("Configuration Script completed allow 5 minutes for NA discovery tasks to complete")
