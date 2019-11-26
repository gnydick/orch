from behave import *
import os


## TODO
# all of these should be rancher up tservice. This is triggering the no yml files found routine
# will take a lot more work to fix that all up
#
# as well as the ../../apps/tstack rather than the correct ../../apps/tapp

# def before_tag(context, )


@given('deploy mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.deploy(deployment_id, dry=True)
    assert command_line == 'rancher up tservice -s tstack -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d'


@given('upgrade mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.upgrade(deployment_id, dry=True)
    assert command_line == 'rancher up tservice -s tstack -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d --upgrade'


@given('rollback mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.rollback(deployment_id, dry=True)
    assert command_line == 'rancher up tservice -s tstack -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d --rollback'


@given('pull mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.pull(deployment_id, dry=True)
    assert command_line == 'rancher up tservice -s tstack -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d --pull'


@given('confirm mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.confirm(deployment_id, dry=True)
    assert command_line == 'rancher up tservice -s tstack -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d --confirm-upgrade'


@given('restart mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.restart(deployment_id, dry=True)
    assert command_line == 'rancher restart tstack/tservice'


@given('logs mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.logs(deployment_id, dry=True)
    assert command_line == 'rancher logs tstack/tservice'


@given('forced deploy mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.deploy(deployment_id, force=True, dry=True)
    assert command_line == 'rancher up tservice -s tstack --force-upgrade -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d'


@given('pull deploy mock is "{deployment_id}"')
def step_impl(context, deployment_id):
    command_line = context.rancher.deploy(deployment_id, pull=True, dry=True)
    assert command_line == 'rancher up tservice -s tstack --pull -f ../../apps/tstack/stacks/tstack/tservice/docker-compose.yml -e orch.conf --rancher-file ../../apps/tstack/stacks/tstack/tservice/rancher-compose.yml -d'
