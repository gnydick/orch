from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class Domain(db.Model):
    __tablename__ = "domain"

    id = Column(String, primary_key=True)
    environment_id = Column(String, ForeignKey('environment.id'))
    name = Column(String, nullable=False)
    defaults = Column(Text, default='{}', server_default='{}')

    environment = relationship("Environment", back_populates="domains")
    networks = relationship("Network", back_populates="domain")

    def __repr__(self):
        return self.id


@db.event.listens_for(Domain, 'before_update')
@db.event.listens_for(Domain, 'before_insert')
def my_before_insert_listener(mapper, connection, domain):
    __update_id__(domain)


def __update_id__(domain):
    domain.id = domain.environment_id + ':' + domain.name
