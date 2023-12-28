# Load template file. Data is in this file.
# Simple template. Just one layer.

from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader("jinja2/templates")
environment = Environment(loader=loader)
tpl = environment.get_template("template01.j2")
data = {
    "hostname": "core-sw-waw-01",
    "name_server_pri": "1.1.1.1",
    "name_server_sec": "8.8.8.8",
    "ntp_server_pri": "0.pool.ntp.org",
    "ntp_server_sec": "1.pool.ntp.org",
}

out = tpl.render(data)
print(out)
