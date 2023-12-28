from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="10.0.15.130",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

netconf_delete_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback operation="delete">
    <name>1</name>
   </Loopback>
  </interface>
 </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_delete_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

