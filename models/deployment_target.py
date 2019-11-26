from sqlalchemy import *
from sqlalchemy.orm import validates, relationship

from db import db


class DeploymentTarget(db.Model):
    __tablename__ = "deployment_target"

    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    environment_id = Column(String, ForeignKey('environment.id'))
    type = Column(String(64))
    defaults = Column(Text, default='{}', server_default='{}')

    environment = relationship("Environment", back_populates="deployment_targets")
    deployments = relationship("Deployment", back_populates="deployment_target")
    nodegroups = relationship("Nodegroup", back_populates="deployment_target")

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'deployment_target'
    }

    def __repr__(self):
        return self.id


@validates('id')
def validate_name(self, key, value):
    assert value != ''
    return value


class K8sCluster(DeploymentTarget):
    __sti_type__ = 'k8s'
    __mapper_args__ = {
        'polymorphic_identity': __sti_type__
    }

    def __repr__(self):
        return self.id


class CloudFormation(DeploymentTarget):
    __sti_type__ = 'cf'
    __mapper_args__ = {
        'polymorphic_identity': __sti_type__
    }

    def __repr__(self):
        return self.id


@db.event.listens_for(K8sCluster, 'before_update')
@db.event.listens_for(K8sCluster, 'before_insert')
@db.event.listens_for(CloudFormation, 'before_update')
@db.event.listens_for(CloudFormation, 'before_insert')
def my_before_insert_listener(mapper, connection, target):
    __update_id__(target)


def __update_id__(target):
    target.id = target.environment_id + ':' + target.name + ':' + target.__sti_type__
