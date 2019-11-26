from sqlalchemy import *

from db import db

deps_to_zones = Table('deployments_zones', db.metadata,
                      Column('deployment_id', String, ForeignKey('deployment.id')),
                      Column('zone_id', String, ForeignKey('zone.id'))
                      )

subnets_to_nodegroups = Table('subnets_nodegroups', db.metadata,
                              Column('subnet_id', String, ForeignKey('subnet.id')),
                              Column('nodegroup_id', String, ForeignKey('nodegroup.id'))
                              )
