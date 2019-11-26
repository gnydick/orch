from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class ConfigType(db.Model):
    __tablename__ = "config_type"

    id = Column(String, primary_key=True)

    configs = relationship("Config", back_populates="config_type")

    def __repr__(self):
        return self.id
