import re
from datetime import datetime

from controllers import RestController, functions as ufunc

rest = RestController()


class RancherController:

    def rancher_op(self, command, deployment_id, dry=False):
        deployment = rest.get_instance('deployment', deployment_id)
        results = getattr(self, command)(deployment, dry=dry)
        if dry:
            print(results)

    def deploy(self, deployment, force=False, pull=False, dry=False):
        return self.__rancher_up__(deployment, style=None, force=force, pull=pull, dry=dry)

    def upgrade(self, deployment, force=False, pull=False, dry=False):
        return self.__rancher_up__(deployment, style="upgrade", force=force, pull=pull, dry=dry)

    def rollback(self, deployment, force=False, pull=False, dry=False):
        return self.__rancher_up__(deployment, style="rollback", force=force, pull=pull, dry=dry)

    def pull(self, deployment, force=False, pull=False, dry=False):
        return self.__rancher_up__(deployment, style="pull", force=force, pull=pull, dry=dry)

    def confirm(self, deployment, force=False, pull=False, dry=False):
        return self.__rancher_up__(deployment, style="confirm-upgrade", force=force, pull=pull, dry=dry)

    def __rancher_up__(self, deployment, style=None, force=False, pull=False, dry=False):
        config = ufunc.__parse_deployment__(deployment)
        stack_name = config['stack_name']
        service_name = config['service_name']
        docker_file = config['docker_compose_file']
        env_file = config['env_file']
        rancher_file = config['rancher_compose_file']
        force_flag = "--force-upgrade" if force else ""
        pull_flag = "--pull" if pull else ""
        style_flag = "--%s" % style if style is not None else ""
        command_line = "rancher up %s -s %s %s %s -f %s -e %s --rancher-file %s -d %s" % (
            service_name, stack_name, force_flag, pull_flag,
            docker_file, env_file,
            rancher_file, style_flag)
        command_line = re.sub(' +', ' ', command_line)

        vars = {
            'VERSION': config['version'],
            'DEPLOY_TIMESTAMP': datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%SUTC')
        }

        return ufunc.__call_command__(ufunc.clean_command_line(command_line), config, vars, dry)

    def restart(self, deployment, dry=False):
        config = ufunc.__parse_deployment__(deployment)
        command_line = "rancher restart %s" % config['rancher_service']
        return ufunc.__call_command__(ufunc.clean_command_line(command_line), config, {}, dry)

    def logs(self, deployment, follow=False, dry=False):
        config = ufunc.__parse_deployment__(deployment)
        if follow:
            follow = "-f"
        else:
            follow = ""
        command_line = "rancher logs %s %s" % (config['rancher_service'], follow)

        return ufunc.__call_command__(ufunc.clean_command_line(command_line), config, {}, dry)

    def install_catalog(self, deployment, catalog_name, dry=False):
        config = ufunc.__parse_deployment__(deployment)
        command_line = "rancher catalog install %s -a %s" % (catalog_name, config['rancher_catalog_file'])
        return ufunc.__call_command__(ufunc.clean_command_line(command_line), config, {}, dry)
