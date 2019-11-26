from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class Config(db.Model):
    __tablename__ = "config"
    id = Column(String, primary_key=True)

    config_type_id = Column(String, ForeignKey('config_type.id'))
    deployment_id = Column(String, ForeignKey('deployment.id'))
    name = Column(String, nullable=False)

    tag = Column(String, nullable=False, default='default')
    config = Column(Text)

    config_type = relationship("ConfigType", back_populates="configs")

    deployment = relationship("Deployment", back_populates="configs")

    def __repr__(self):
        return self.deployment.id + ':' + self.config_type.id + ':' + self.name + ':' + self.tag


@db.event.listens_for(Config, 'before_update')
@db.event.listens_for(Config, 'before_insert')
def my_before_insert_listener(mapper, connection, config):
    __update_id__(config)


def __update_id__(config):
    config.id = config.deployment_id + ':' + config.config_type_id + ':' + config.name + ':' + config.tag
