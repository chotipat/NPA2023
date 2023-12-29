from jinja2 import Environment, FileSystemLoader
import yaml

loader = FileSystemLoader("templates")

env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router-nat.j2")

with open("data/routers-nat.yml") as f:
    router = yaml.safe_load(f)


router_conf = "config/" + router["management_ip"] + "-exercise-nat.txt"
with open(router_conf, "w") as f:
    f.write(template.render(router))
