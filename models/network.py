from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db

from sqlalchemy.dialects.postgresql.base import CIDR

import ipaddress as ip

class Network(db.Model):
    __tablename__ = "network"

    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = Column(String, primary_key=True)
    domain_id = Column(String, ForeignKey('domain.id'), nullable=False)
    name = Column(String, nullable=False)
    cidr = Column(CIDR, nullable=False, )
    defaults = Column(Text, default='{}', server_default='{}')

    domain = relationship("Domain", back_populates="networks")
    subnets = relationship("Subnet", back_populates='network')

    def __repr__(self):
        return self.id

    def ipv4network(self):
        return ip.IPv4Network(address=self.cidr)


@db.event.listens_for(Network, 'before_update')
@db.event.listens_for(Network, 'before_insert')
def my_before_insert_listener(mapper, connection, network):
    __update_id__(network)


def __update_id__(network):
    network.id = network.domain_id + ':' + network.name
