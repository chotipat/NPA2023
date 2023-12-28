# Create template stream and dump to a file.

from jinja2 import Environment, FileSystemLoader
import yaml

loader = FileSystemLoader("jinja2/templates")
environment = Environment(loader=loader)
tpl = environment.get_template("template05.j2")

with open("jinja2/data/data01.yml") as f:
    router = yaml.safe_load(f)

out = tpl.render(router)
print(out)
