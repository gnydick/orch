import flask_restless
from flask_admin import Admin
from flask_migrate import Migrate
from werkzeug.debug import DebuggedApplication

from base import app
from controllers.subnets import SubnetController
from db import db

# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=12321, stdoutToServer=True, stderrToServer=True)

from models import *
from views import *

if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

migrate = Migrate(app, db)

admin = Admin(app, name='orch', template_mode='bootstrap3')

admin.add_view(WithIdView(Provider, db.session))
admin.add_view(DefaultView(Region, db.session))
admin.add_view(DefaultView(Zone, db.session))

admin.add_view(DefaultView(Domain, db.session))
admin.add_view(NetworkView(Network, db.session))
admin.add_view(NetworkView(Subnet, db.session))

admin.add_view(WithIdView(Environment, db.session))
admin.add_view(WithIdView(Application, db.session))
admin.add_view(DefaultView(Stack, db.session))
admin.add_view(ServiceView(Service, db.session))
admin.add_view(DefaultView(Build, db.session))
admin.add_view(DefaultView(Release, db.session))
admin.add_view(DefaultView(Deployment, db.session))
admin.add_view(ServiceConfigView(ServiceConfig, db.session))
admin.add_view(WithIdView(ConfigType, db.session))
admin.add_view(ConfigView(Config, db.session))
admin.add_view(StiView(DockerRegistry, db.session))
admin.add_view(StiView(Nexus, db.session))
admin.add_view(DeploymentTargetView(K8sCluster, db.session))
admin.add_view(DeploymentTargetView(CloudFormation, db.session))
admin.add_view(ResourceAllocationView(CpuAllocation, db.session))
admin.add_view(ResourceAllocationView(MemoryAllocation, db.session))
admin.add_view(DefaultView(Proc, db.session))
admin.add_view(DeploymentProcessView(DeploymentProcess, db.session))
admin.add_view(DefaultView(Nodegroup, db.session))

restmanager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
restmanager.create_api(ServiceConfig, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(Stack, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(DeploymentTarget, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(K8sCluster, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1, collection_name='k8s_cluster')
restmanager.create_api(CloudFormation, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1, collection_name='cloudformation')
restmanager.create_api(ArtifactRepository, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(DockerRegistry, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1, collection_name='docker_registry')
restmanager.create_api(Nexus, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1, collection_name='nexus')
restmanager.create_api(Environment, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Region, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(Deployment, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Service, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(Provider, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(Zone, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(Config, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1',
                       max_results_per_page=-1)
restmanager.create_api(ConfigType, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Application, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Network, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Domain, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Network, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Subnet, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(CpuAllocation, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1, collection_name='cpu_allocation')
restmanager.create_api(MemoryAllocation, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1, collection_name='memoryf_allocation')
restmanager.create_api(ServiceConfig, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Proc, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(DeploymentProcess, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Nodegroup, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Build, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)
restmanager.create_api(Release, primary_key='id', methods=['GET', 'POST', 'DELETE', 'PUT'],
                       url_prefix='/api/rest/v1', max_results_per_page=-1)



from socket import gethostname

from flask import Response

from controllers import HelmController
from models import Network, Subnet, Config, Deployment, Environment, Provider, Region




@app.route('/api/health')
def health():
    return "I'm Alive!! " + gethostname()


@app.route('/api/rest/v1/network/<network_id>/allocate_subnet/<mask>/<name>', methods=['POST'])
def allocate_subnet(network_id, mask, name):
    subnet_controller = SubnetController(network_id)
    return subnet_controller.allocate_subnet(mask, name) + "\n"


@app.route('/api/tf/v1/deployment/gen/<dep_id>')
@app.route('/api/tf/v1/deployment/gen/<dep_id>/<config_tag>')
def gen_config(dep_id, config_tag=None):
    from db import db
    s = db.session
    config_tag = 'default' if config_tag == None else config_tag
    tfs = s.query(Config).filter(Config.deployment_id == dep_id, Config.config_type_id == 'tf',
                                 Config.tag == config_tag).all()
    tf_files = list(map(lambda x: x.name, tfs))

    result = ''

    for file in tf_files:
        res = _gen_tf(dep_id, 'tf', file, config_tag)
        result += res + '\n'
    return Response(result, mimetype='text/plain')


@app.route('/api/helm/v1/chart/<dep_id>')
def gen_helm(dep_id):
    hc = HelmController()
    return hc.genChart(dep_id)


@app.route('/api/tf/v1/deployment/gen/<dep_id>/<config_type>/<name>')
@app.route('/api/tf/v1/deployment/gen/<dep_id>/<config_type>/<name>/<config_tag>')
def gen_tf(dep_id, config_type, name, config_tag=None):
    return Response(_gen_tf(dep_id, config_type, name, config_tag), mimetype='text/plain')


def __clean_config_reader__(query):
    import ast
    if query is not None:
        config = query.config
    else:
        config = '{}'
    return ast.literal_eval(config)


def __clean_outputs_reader__(query):
    import ast
    if query is not None:
        config = query.config
    else:
        config = '{}'
    return ast.literal_eval(config)


def _gen_tf(dep_id, config_type, name, tag=None):
    import ast
    from string import Template
    from db import db
    s = db.session
    app_result = s.query(Config).filter(Config.deployment_id == dep_id, Config.config_type_id == 'vars').first()
    appvars = __clean_config_reader__(app_result)
    dep = s.query(Deployment).get(dep_id)
    env = s.query(Environment).get(dep.environment.id)
    # inheritance order
    # provider
    # region
    # zone
    # appvars

    provvars = ast.literal_eval(s.query(Provider).get('aws').defaults)
    regvars = __clean_outputs_reader__(s.query(Region).get('us-east-1'))

    depcfg = ast.literal_eval(
        dep.defaults)
    envvars = ast.literal_eval(env.defaults)
    servicevars = ast.literal_eval(dep.service.defaults)

    config_type_tmpl = s.query(Config).get(dep_id + ':tf:' + name + ':default').config

    config_type_cfg = Template(config_type_tmpl)

    post_prov_cfg = config_type_cfg.safe_substitute(provvars)
    post_prov_tmpl = Template(post_prov_cfg)
    post_env_cfg = post_prov_tmpl.safe_substitute(envvars)
    post_env_tmpl = Template(post_env_cfg)
    post_dep_cfg = post_env_tmpl.safe_substitute(depcfg)
    post_dep_tmpl = Template(post_dep_cfg)
    svc_cfg = post_dep_tmpl.safe_substitute(servicevars)
    post_svc_cfg = Template(svc_cfg)
    app_cfg = post_svc_cfg.safe_substitute(appvars)
    return app_cfg


if __name__ == '__main__':
    app.run(host='0.0.0.0')
