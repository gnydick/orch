from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class Nodegroup(db.Model):
    __tablename__ = "nodegroup"
    id = Column(String, primary_key=True)
    deployment_target_id = Column(String, ForeignKey('deployment_target.id'))
    name = Column(String(256))
    cpu_total = Column(Integer)
    memory_total = Column(Float)
    defaults = Column(Text, default='{}', server_default='{}')

    deployment_target = relationship("DeploymentTarget", back_populates="nodegroups")
    subnets = relationship("Subnet", secondary='subnets_nodegroups', back_populates="nodegroups")

    def __repr__(self):
        return self.id


@db.event.listens_for(Nodegroup, 'before_update')
@db.event.listens_for(Nodegroup, 'before_insert')
def my_before_insert_listener(mapper, connection, nodegroup):
    __update_id__(nodegroup)


def __update_id__(nodegroup):
    nodegroup.id = nodegroup.deployment_target.id + ':' + nodegroup.name
