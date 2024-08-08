import asyncio
from datetime import datetime, timedelta

from asyncua import Client
from asyncua.ua.uatypes import QualifiedName
from asyncua.crypto.security_policies import SecurityPolicyBasic256Sha256

#url = "opc.tcp://10.130.2.195:4840" # ip-eah-opcua-server
url = "opc.tcp://OllisPC:48020"
namespace = "http://www.unifiedautomation.com/DemoServer/"

async def main():
    print(f"Connecting to {url} ... ")
    client = Client(url=url)
    #client.set_user("AUDUSER")
    #client.set_user("root")
    #client.set_password("SUNRISE1")
    await client.set_security(
         SecurityPolicyBasic256Sha256,
         certificate="certificates/eah_mcp_150_cert.der",
         private_key="certificates/eah_mcp_150_private_key.pem"
    )

    async with client as client:
        nsidx = await client.get_namespace_index(namespace)
        print(nsidx) 
        nspace_array = await client.get_namespace_array()
        print(nspace_array)

        # tmp_node = await client.nodes.root.get_child("0:Objects/Server/ServerStatus")
        # tmp_node = client.nodes.root
        # tmp_node = await tmp_node.get_child("0:Objects/4:Demo/4:BoilerDemo/4:Boiler1/4:FillLevelSetPoint")

       
        tmp_node = client.get_node("ns=4;s=Demo.BoilerDemo.Boiler1.HeaterStatus")
        val = await tmp_node.read_data_value()
        print("heater_state: " + str(val))

        print("\n\n")

        tmp_node = client.get_node("ns=4;s=Demo.BoilerDemo.Boiler1.TemperatureSensor.Temperature")
        val = await tmp_node.read_data_value()
        print("heater_temperature: " + str(val))
        
        
        # server_state = await tmp_node.get_value()
        # #print(server_state)

        # path = [QualifiedName("Objects", 0), QualifiedName("Sinumerik",2), QualifiedName("/Axis", 2), QualifiedName("/Axis/Drive", 2), QualifiedName("/Axis/Drive/AA_OFF_MODE",2)]

        # tmp_node = await client.nodes.root.get_child(path)
        # print(datetime.now())
        # val = await tmp_node.read_data_value()
        # print(datetime.now())
        # print(val.SourceTimestamp - timedelta(minutes=11, seconds=11))
        # # value = await tmp_node.get_value()
        # print(value)
        
                
    # answer = await client.connect()
    # print(answer)


if __name__ == "__main__":
    asyncio.run(main())