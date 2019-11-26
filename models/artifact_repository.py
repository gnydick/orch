from sqlalchemy import *
from sqlalchemy.orm import relationship

from db import db


class ArtifactRepository(db.Model):
    __tablename__ = "artifact_repository"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, default='artifact-repo', server_default='artifact-repo')
    type = Column(String(64))
    url = Column(String(253))
    defaults = Column(Text, default='{}', server_default='{}')

    services = relationship("Service", back_populates="artifact_repository")

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'artifact_repository'
    }

    def __repr__(self):
        return self.id


class DockerRegistry(ArtifactRepository):
    __sti_type__ = 'dckr'
    __mapper_args__ = {
        'polymorphic_identity': __sti_type__
    }

    def __repr__(self):
        return self.id


class Nexus(ArtifactRepository):
    __sti_type__ = 'nexus'
    __mapper_args__ = {
        'polymorphic_identity': __sti_type__
    }

    def __repr__(self):
        return self.id


@db.event.listens_for(DockerRegistry, 'before_update')
@db.event.listens_for(DockerRegistry, 'before_insert')
@db.event.listens_for(Nexus, 'before_update')
@db.event.listens_for(Nexus, 'before_insert')
def my_before_insert_listener(mapper, connection, repo):
    __update_id__(repo)


def __update_id__(repo):
    repo.id = repo.name + ':' + repo.__sti_type__
