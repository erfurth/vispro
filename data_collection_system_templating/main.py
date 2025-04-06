from jinja2 import Template

with open("templates/docker-compose.j2") as f:
    template = Template(f.read())

data_services = [{"name": "ultrasonic"}, {"name": "mcp150"}]

config = template.render(services=data_services, BASE_PORT=8000)

with open("docker-compose.yml", "w") as f:
    f.write(config)
