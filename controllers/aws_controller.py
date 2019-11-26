import re

from controllers import RestController, functions as ufunc

rest = RestController()


class AWSController:

    def lambda_publish(self, deployment_id, zipfile):
        config = ufunc.__parse_deployment__(deployment_id)

    def aws_op(self, command, deployment_id, dry=False):
        deployment = rest.get_instance('deployment', deployment_id)
        getattr(self, '_' + command + '_')(deployment, dry=dry)

    def _example_wrapped_(self, deployment, force=False, pull=False, dry=False):
        self.__rancher_op__(deployment, style=None, force=force, pull=pull, dry=dry)

    def __example_wrapper__(self, deployment, style=None, upgrade=False, force=False, pull=False,
                            dry=False):
        config = ufunc.__parse_deployment__(deployment)
        stack_name = config['stack_name']
        service_name = config['service_name']
        docker_file = config['docker_compose_file']
        env_file = config['env_file']
        rancher_file = config['rancher_compose_file']
        upgrade_flag = "--upgrade" if upgrade else ""
        force_flag = "--force-upgrade" if force else ""
        pull_flag = "--pull" if pull else ""
        style_flag = "--%s" % style if style is not None else ""
        command_line = "rancher up %s -s %s %s %s %s -f %s -e %s --rancher-file %s -d %s" % (
            service_name, stack_name, upgrade_flag, force_flag, pull_flag,
            docker_file, env_file,
            rancher_file, style_flag)
        command_line = re.sub(' +', ' ', command_line)
        ufunc.__call_command__(command_line, config, dry)
