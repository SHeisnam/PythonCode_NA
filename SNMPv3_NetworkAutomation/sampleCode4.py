from requests import Session
from zeep import Client
from zeep.transports import Transport

session = Session()
session.verify = False
transport = Transport(session=session)
client = Client(
    'https://rhel-nacore1.sac.swinfra.net//soap?wsdl=api.wsdl.wsdl2py',
    transport=transport)
loginResult = client.service.login(parameters={'username':'naadmin', 'password':'0penView#123'})
sesnhdr_type = client.get_element('ns0:list_deviceInputParms')
sesnhdr = sesnhdr_type(sessionid=loginResult.Text)
devices = client.service.list_device(_soapheaders=[sesnhdr], parameters=sesnhdr)
print('\n\n ----------------------------- \n')

for i in devices.ResultSet.Row:
        print(i.hostName + ' ---> '+i.primaryIPAddress)
        params = {
                        "ip":i.primaryIPAddress,
                        "sessionid": loginResult.Text
        }
        device = client.service.show_deviceinfo(parameters=params)
        print('/t/t === >>> '+device.Text)

print('\n\n ----------------------------- \n')