# Create template stream and dump to a file.
# Python Network Programming Techniques

from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader("jinja2/templates")
environment = Environment(loader=loader)
tpl = environment.get_template("template02.j2")

allowed = ["10.10.0.10", "10.10.0.11", "10.10.0.12"]
disallowed = ["10.10.0.50", "10.10.0.62"]
intf = "ethernet0"

out = tpl.render(allowed=allowed, disallowed=disallowed, intf=intf)
print(out)
