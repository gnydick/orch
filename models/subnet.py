import sqlalchemy
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import CIDR
from sqlalchemy.orm import relationship

from db import db

import ipaddress as ip


class Subnet(db.Model):
    __tablename__ = "subnet"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    cidr = Column(CIDR, nullable=False, )
    network_id = Column(String, ForeignKey('network.id'), nullable=False)
    defaults = Column(Text, default='{}', server_default='{}')

    network = relationship("Network", back_populates="subnets")
    nodegroups = relationship("Nodegroup", secondary='subnets_nodegroups', back_populates="subnets")

    def __repr__(self):
        return self.id

    def net(self):
        return ip.IPv4Network(address=self.cidr)


class SubnetUnavailableError(RuntimeError):

    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


@db.event.listens_for(Subnet, 'before_update')
@db.event.listens_for(Subnet, 'before_insert')
def my_before_insert_listener(mapper, connection, subnet):
    newsubnet = ip.IPv4Network(address=subnet.cidr)
    from controllers import RestController
    rest = RestController()
    network = rest.get_instance('network', subnet.network_id)

    if newsubnet in [ip.IPv4Network(net.cidr) for net in network['subnets']]:
        error = SubnetUnavailableError("Already Used", null)
    __update_id__(subnet)


def __update_id__(subnet):
    subnet.id = subnet.network_id + ':' + subnet.name
