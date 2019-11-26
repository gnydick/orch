from wtforms import Form, SelectField


class ProcessForDeploymentIterable(object):

    def __iter__(self):
        for proc in self.deployment.service.procs:
            choice = (proc.id, proc.name)
            yield choice


class ProcessForDeploymentForm(Form):
    proc = SelectField(choices=ProcessForDeploymentIterable(),
                       label="Proc")


from models import Deployment


def edit_dep_proc(request, id):
    deployment = Deployment.service.get(pk=id)
