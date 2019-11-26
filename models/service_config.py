from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class ServiceConfig(db.Model):
    __tablename__ = "service_config"

    id = Column(String, primary_key=True, nullable=False)
    service_id = Column(String, ForeignKey('service.id'), nullable=False)
    name = Column(String(64), nullable=False)
    service_config = Column(Text)
    service = relationship("Service", back_populates="service_configs")


    def __repr__(self):
        return self.id


@db.event.listens_for(ServiceConfig, 'before_update')
@db.event.listens_for(ServiceConfig, 'before_insert')
def my_before_insert_listener(mapper, connection, serviceConfig):
    __update_id__(serviceConfig)


def __update_id__(serviceConfig):
    serviceConfig.id = serviceConfig.service_id + ':' + serviceConfig.name
