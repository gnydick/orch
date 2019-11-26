from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class Environment(db.Model):
    __tablename__ = "environment"
    id = Column(String, primary_key=True)

    deployment_url = Column(String)
    defaults = Column(Text, default='{}', server_default='{}')
    deployment_targets = relationship("DeploymentTarget", back_populates="environment")
    domains = relationship("Domain", back_populates="environment")

    def __repr__(self):
        return self.id
