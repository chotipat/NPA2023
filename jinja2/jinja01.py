# https://ttl255.com/jinja2-tutorial-part-1-introduction-and-variable-substitution/
# Template and data are in this file.
# Simple template. Just one layer.

from jinja2 import Template

template = """hostname {{ hostname }}

no ip domain lookup
ip domain name local.lab
ip name-server {{ name_server_pri }}
ip name-server {{ name_server_sec }}

ntp server {{ ntp_server_pri }} prefer
ntp server {{ ntp_server_sec }}"""

hostname = "core-sw-waw-01"
name_server_pri = "1.1.1.1"
name_server_sec = "8.8.8.8"
ntp_server_pri = "0.pool.ntp.org"
ntp_server_sec = "1.pool.ntp.org"

j2_template = Template(template)
print(
    j2_template.render(
        hostname=hostname,
        name_server_pri=name_server_pri,
        name_server_sec=name_server_sec,
        ntp_server_pri=ntp_server_pri,
        ntp_server_sec=ntp_server_sec,
    )
)
