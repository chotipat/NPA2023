from ncclient import manager, xml_
import xml.dom.minidom

m = manager.connect(
    host="10.0.15.130",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

save_config = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""
netconf_reply = m.dispatch(xml_.to_ele(save_config))
print(netconf_reply)