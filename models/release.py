import datetime

from sqlalchemy import *
from sqlalchemy.orm import relationship, validates
from db import db


class Release(db.Model):
    __tablename__ = "release"

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    build_id = Column(String, ForeignKey('build.id'), nullable=False)
    deployment_id = Column(String, ForeignKey('deployment.id'), nullable=False)
    iteration = Column(String, nullable=False)

    build = relationship('Build', back_populates='releases')
    deployment = relationship('Deployment', back_populates='releases')

    def __repr__(self):
        return self.id


@db.event.listens_for(Release, 'before_insert')
@db.event.listens_for(Release, 'before_update')
def my_before_update_listener(mapper, connection, release):
    from models import Deployment, Build
    dep = db.session.query(Deployment).filter_by(id=release.deployment_id).first()
    bld = db.session.query(Build).filter_by(id=release.build_id).first()

    if dep.service_id != bld.service_id:
        raise ValueError("Service must be common to the build and deployment.")

    __update_id__(release)


def __update_id__(release):
    release.id = release.deployment_id + ':' + release.build_id + ':' + release.iteration
