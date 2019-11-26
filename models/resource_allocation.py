

from sqlalchemy import *
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import validates, relationship

from db import db


class ResourceAllocation(db.Model):

    watermarks = ('HIGH', 'LOW')
    watermarks_enum = Enum(*watermarks, name='watermark')

    __tablename__ = "resource_allocation"

    id = Column(String, primary_key=True)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    deployment_process_id = Column(String, ForeignKey('deployment_process.id'))
    type = Column(String(64))
    watermark = db.Column(watermarks_enum)
    UniqueConstraint('deployment_process_id','type','watermark')
    defaults = Column(Text, default='{}', server_default='{}')

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'resource_allocation'
    }

    def __repr__(self):
        return self.id


@validates('id')
def validate_name(self, key, value):
    assert value != ''
    return value


class CpuAllocation(ResourceAllocation):
    __sti_type__ = 'cpu'
    __mapper_args__ = {
        'polymorphic_identity': __sti_type__,

    }

    deployment_process = relationship("DeploymentProcess", back_populates="cpu_allocations")

    def __repr__(self):
        return self.id


class MemoryAllocation(ResourceAllocation):
    __sti_type__ = 'memory'
    __mapper_args__ = {
        'polymorphic_identity': __sti_type__
    }

    deployment_process = relationship("DeploymentProcess", back_populates="memory_allocations")

    def __repr__(self):
        return self.id


@db.event.listens_for(CpuAllocation, 'before_update')
@db.event.listens_for(CpuAllocation, 'before_insert')
@db.event.listens_for(MemoryAllocation, 'before_update')
@db.event.listens_for(MemoryAllocation, 'before_insert')
def my_before_insert_listener(mapper, connection, resource_allocation):
    __update_id__(resource_allocation)


def __update_id__(resource_allocation):
    resource_allocation.id = resource_allocation.deployment_process_id + ':' + resource_allocation.type + ':' + resource_allocation.watermark
    if resource_allocation.__sti_type__ == 'cpu':
        resource_allocation.unit = 'm'
    elif resource_allocation.__sti_type__ == 'memory':
        resource_allocation.unit = 'GiB'
