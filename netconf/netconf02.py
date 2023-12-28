from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="10.0.15.130",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

ugly_netconf_reply = m.get_config(source="running")
beautiful_netconf_reply = xml.dom.minidom.parseString(ugly_netconf_reply.xml).toprettyxml()
print(beautiful_netconf_reply)
