from db import db
from models import *
from forms import *

dep = db.session.query(Deployment).first()

form = ProcessForDeploymentForm(dep)

for field in form:
    print(field)