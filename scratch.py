#!/usr/bin/env python

import json
from string import Template

from db import db
from models import *

s = db.session
dep_id = 'int:orch:orch:orch:default'
dep = s.query(Deployment).get(dep_id)
zones = dep.zones
env = dep.environment
service = dep.service
stack = service.stack
application = stack.application

settings = {}

##### inheritance order for default values
# provider
# region
# environment
# application
# stack
# service
# service_configs
# deployment


prov_dict = json.loads(s.query(Provider).get('aws').defaults)
region_dict = json.loads(s.query(Region).get('aws:us-east-1').defaults)
env_dict = json.loads(env.defaults)
app_dict = json.loads(application.defaults)
stack_dict = json.loads(stack.defaults)
service_dict = json.loads(service.defaults)
deployment_dict = json.loads(dep.defaults)

settings.update(prov_dict)
settings.update(region_dict)
settings.update(env_dict)
settings.update(app_dict)
settings.update(stack_dict)
settings.update(service_dict)

for mod in service.service_configs:
    settings.update(json.loads(mod.defaults))

settings.update(deployment_dict)

monolithic_results = ''


class MyTemplate(Template):
    delimiter = 'π'


for conf in dep.configs:
    tmpl = MyTemplate(conf.config)
    filled_tmpl = tmpl.safe_substitute(settings)
    monolithic_results += filled_tmpl + '\n\n'

for mod in service.service_configs:
    tmpl = MyTemplate(mod.service_config)
    filled_tmpl = tmpl.safe_substitute(settings)
    monolithic_results += filled_tmpl + '\n\n'

print(monolithic_results)
