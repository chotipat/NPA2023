from ncclient import manager
import xmltodict

m = manager.connect(
    host="10.0.15.130",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

netconf_filter = """
<filter>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

netconf_reply = m.get(filter=netconf_filter)
netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
    print("Name: {} MAC: {} Input: {} Output {}".format(
                interface["name"],
                interface["phys-address"],
                interface["statistics"]["in-octets"],
                interface["statistics"]["out-octets"]
    )
)
