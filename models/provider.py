from sqlalchemy import *
from sqlalchemy.orm import relationship, validates

from db import db


class Provider(db.Model):
    __tablename__ = "provider"
    id = Column(String, primary_key=True)
    defaults = Column(Text, default='{}', server_default='{}')

    regions = relationship("Region", back_populates="provider")

    def __repr__(self):
        return self.id

    @validates('id')
    def validate_name(self, key, value):
        assert value != ''
        return value