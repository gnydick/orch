from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class Deployment(db.Model):
    __tablename__ = "deployment"
    id = Column(String, primary_key=True)
    service_id = Column(String, ForeignKey('service.id'))
    deployment_target_id = Column(String, ForeignKey('deployment_target.id'))
    version = Column(String, nullable=False, default='latest')
    tag = Column(String, nullable=False, default='default')

    defaults = Column(Text, default='{}', server_default='{}')

    deployment_target = relationship("DeploymentTarget", back_populates="deployments")
    service = relationship("Service", back_populates="deployments")
    configs = relationship("Config", back_populates="deployment")
    releases = relationship('Release', back_populates='deployment')
    zones = relationship("Zone", secondary='deployments_zones', back_populates="deployments")
    deployment_processes = relationship("DeploymentProcess", back_populates="deployment")

    def __repr__(self):
        return self.id


@db.event.listens_for(Deployment, 'before_update')
@db.event.listens_for(Deployment, 'before_insert')
def my_before_insert_listener(mapper, connection, deployment):
    __update_id__(deployment)


def __update_id__(deployment):
    deployment.id = deployment.deployment_target_id + ':' + deployment.service_id + ':' + deployment.tag
