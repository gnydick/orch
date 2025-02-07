from sqlalchemy import *
from sqlalchemy.orm import relationship, validates

from db import db


class Application(db.Model):
    __tablename__ = "application"

    id = Column(String, primary_key=True)
    defaults = Column(Text, default='{}', server_default='{}')

    stacks = relationship('Stack', back_populates='application')

    def __repr__(self):
        return self.id


    @validates('id')
    def validate_name(self, key, value):
        assert value != ''
        return value
