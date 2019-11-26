from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class DeploymentProcess(db.Model):
    __tablename__ = "deployment_process"
    id = Column(String, primary_key=True)
    deployment_id = Column(String, ForeignKey('deployment.id'))
    process_id = Column(String, ForeignKey('process.id'))
    defaults = Column(Text, default='{}', server_default='{}')

    cpu_allocations = relationship("CpuAllocation", back_populates="deployment_process",
                                  primaryjoin="and_(CpuAllocation.deployment_process_id==DeploymentProcess.id)")
    memory_allocations = relationship("MemoryAllocation", back_populates="deployment_process",
                                     primaryjoin="and_(MemoryAllocation.deployment_process_id==DeploymentProcess.id)")
    deployment = relationship("Deployment", back_populates="deployment_processes")
    proc = relationship("Proc", back_populates="deployment_processes")

    def __repr__(self):
        return self.id


@db.event.listens_for(DeploymentProcess, 'before_update')
@db.event.listens_for(DeploymentProcess, 'before_insert')
def my_before_insert_listener(mapper, connection, deployment_process):
    __update_id__(deployment_process)


def __update_id__(deployment_process):
    deployment_process.id = deployment_process.deployment_id + ':' + deployment_process.process_id
