import argparse

import argcomplete
from .schema import OrchSchema
from .rest_controller import RestController


class CLIArgs:

    def __init__(self, restcontroller):
        self.rest = restcontroller
        self.__gen_completers__(restcontroller)

    def __add_list_parser__(self, parsers):
        list_parser = parsers.add_parser('list')
        list_parser.required = False
        list_parser.add_argument('-p', help='page', dest='page')
        list_parser.add_argument('-r', help='results per page', dest='resperpage')
        list_parser.add_argument('-o', help='output fields', dest='output_fields', action='append')

        query_parser = parsers.add_parser('query')
        query_parser.required = False
        query_parser.add_argument('search_field')
        query_parser.add_argument('op')
        query_parser.add_argument('value')
        query_parser.add_argument('-p', help='page', dest='page')
        query_parser.add_argument('-r', help='results per page', dest='resperpage')
        query_parser.add_argument('-o', help='output fields', dest='output_fields', action='append')

    def __add_set_field_parser__(self, rest, parsers, resource):
        field_update_parser = parsers.add_parser('setfield')
        field_update_parser.add_argument('id').completer = getattr(rest, '_%s_completer_' % resource)
        field_update_parser.add_argument('field')
        field_update_parser.add_argument('value')

    def assign_args(self, rest):
        schema = OrchSchema()
        parser = argparse.ArgumentParser(description='orchRegistry CLI')
        parser.add_argument('-q', help='Quiet', required=False, action='store_true')
        context_parsers = parser.add_subparsers(help='context to operate in', dest='resource')

        network_parser = context_parsers.add_parser('network')
        ntw_com_parsers = network_parser.add_subparsers(help='command', dest='command')
        ntw_com_parsers.required = True
        self.__add_list_parser__(ntw_com_parsers)
        self.__add_set_field_parser__(rest, ntw_com_parsers, 'network')
        _ntw_com_get_parser = ntw_com_parsers.add_parser('get')
        _ntw_com_get_parser.add_argument('id').completer = rest._network_completer_
        _ntw_com_create_parser = ntw_com_parsers.add_parser('create')
        self.__populate_args__(rest, _ntw_com_create_parser, schema.CREATE_FIELDS['network'])
        _ntw_com_delete_parser = ntw_com_parsers.add_parser('delete')
        _ntw_com_delete_parser.add_argument('id').completer = rest._network_completer_
        _ntw_com_clone_parser = ntw_com_parsers.add_parser('clone')
        _ntw_com_clone_parser.add_argument('id', help='network_id').completer = rest._network_completer_
        _ntw_com_clone_parser.add_argument('name',
                                           help='NOT IMPLEMENTED')

        subnet_parser = context_parsers.add_parser('subnet')
        sbnt_com_parsers = subnet_parser.add_subparsers(help='command', dest='command')
        sbnt_com_parsers.required = True
        self.__add_list_parser__(sbnt_com_parsers)
        self.__add_set_field_parser__(rest, sbnt_com_parsers, 'subnet')
        _sbnt_com_get_parser = sbnt_com_parsers.add_parser('get')
        _sbnt_com_get_parser.add_argument('id').completer = rest._subnet_completer_

        _sbnt_com_delete_parser = sbnt_com_parsers.add_parser('delete')
        _sbnt_com_delete_parser.add_argument('id').completer = rest._subnet_completer_
        _sbnt_com_clone_parser = sbnt_com_parsers.add_parser('clone')
        _sbnt_com_clone_parser.add_argument('id', help='subnet_id').completer = rest._subnet_completer_
        _sbnt_com_clone_parser.add_argument('name',
                                            help='NOT IMPLEMENTED')
        _sbnt_com_allocate_parser = sbnt_com_parsers.add_parser('allocate')
        _sbnt_com_allocate_parser.add_argument('network_id').completer = rest._network_completer_
        _sbnt_com_allocate_parser.add_argument('additional_mask_bits', help='if CIDR=/16 and you want /24, specify "8"')
        _sbnt_com_allocate_parser.add_argument('name', help='name of subnet')

        nodegroup_parser = context_parsers.add_parser('nodegroup')
        ngr_com_parsers = nodegroup_parser.add_subparsers(help='command', dest='command')
        ngr_com_parsers.required = True
        self.__add_list_parser__(ngr_com_parsers)
        self.__add_set_field_parser__(rest, ngr_com_parsers, 'nodegroup')
        _ngr_com_get_parser = ngr_com_parsers.add_parser('get')
        _ngr_com_get_parser.add_argument('id').completer = rest._nodegroup_completer_
        _ngr_com_create_parser = ngr_com_parsers.add_parser('create')
        self.__populate_args__(rest, _ngr_com_create_parser, schema.CREATE_FIELDS['nodegroup'])
        _ngr_com_delete_parser = ngr_com_parsers.add_parser('delete')
        _ngr_com_delete_parser.add_argument('id').completer = rest._nodegroup_completer_
        _ngr_com_clone_parser = ngr_com_parsers.add_parser('clone')
        _ngr_com_clone_parser.add_argument('id', help='nodegroup_id').completer = rest._nodegroup_completer_
        _ngr_com_clone_parser.add_argument('name',
                                           help='destination nodegroup name')

        provider_parser = context_parsers.add_parser('provider')
        prv_com_parsers = provider_parser.add_subparsers(help='command', dest='command')
        prv_com_parsers.required = True
        self.__add_list_parser__(prv_com_parsers)
        self.__add_set_field_parser__(rest, prv_com_parsers, 'provider')
        _prv_com_get_parser = prv_com_parsers.add_parser('get')
        _prv_com_get_parser.add_argument('id').completer = rest._provider_completer_
        _prv_com_create_parser = prv_com_parsers.add_parser('create')
        self.__populate_args__(rest, _prv_com_create_parser, schema.CREATE_FIELDS['provider'])
        _prv_com_delete_parser = prv_com_parsers.add_parser('delete')
        _prv_com_delete_parser.add_argument('id').completer = rest._provider_completer_

        region_parser = context_parsers.add_parser('region')
        rgn_com_parsers = region_parser.add_subparsers(help='command', dest='command')
        rgn_com_parsers.required = True
        self.__add_list_parser__(rgn_com_parsers)
        self.__add_set_field_parser__(rest, rgn_com_parsers, 'region')
        _rgn_com_get_parser = rgn_com_parsers.add_parser('get')
        _rgn_com_get_parser.add_argument('id').completer = rest._region_completer_
        _rgn_com_create_parser = rgn_com_parsers.add_parser('create')
        self.__populate_args__(rest, _rgn_com_create_parser, schema.CREATE_FIELDS['region'])
        _rgn_com_delete_parser = rgn_com_parsers.add_parser('delete')
        _rgn_com_delete_parser.add_argument('id').completer = rest._region_completer_

        zone_parser = context_parsers.add_parser('zone')
        zn_com_parsers = zone_parser.add_subparsers(help='command', dest='command')
        zn_com_parsers.required = True
        self.__add_list_parser__(zn_com_parsers)
        self.__add_set_field_parser__(rest, zn_com_parsers, 'zone')
        _zn_com_get_parser = zn_com_parsers.add_parser('get')
        _zn_com_get_parser.add_argument('id').completer = rest._zone_completer_
        _zn_com_create_parser = zn_com_parsers.add_parser('create')
        self.__populate_args__(rest, _zn_com_create_parser, schema.CREATE_FIELDS['zone'])
        _zn_com_delete_parser = zn_com_parsers.add_parser('delete')
        _zn_com_delete_parser.add_argument('id').completer = rest._zone_completer_

        environment_parser = context_parsers.add_parser('environment')
        env_com_parsers = environment_parser.add_subparsers(help='command', dest='command')
        env_com_parsers.required = True
        self.__add_list_parser__(env_com_parsers)
        self.__add_set_field_parser__(rest, env_com_parsers, 'environment')
        _env_com_get_parser = env_com_parsers.add_parser('get')
        _env_com_get_parser.add_argument('id').completer = rest._environment_completer_
        _env_com_create_parser = env_com_parsers.add_parser('create')
        self.__populate_args__(rest, _env_com_create_parser, schema.CREATE_FIELDS['environment'])
        _env_com_delete_parser = env_com_parsers.add_parser('delete')
        _env_com_delete_parser.add_argument('id').completer = rest._environment_completer_

        k8s_cluster_parser = context_parsers.add_parser('k8s_cluster')
        k8sc_com_parsers = k8s_cluster_parser.add_subparsers(help='command', dest='command')
        k8sc_com_parsers.required = True
        self.__add_list_parser__(k8sc_com_parsers)
        self.__add_set_field_parser__(rest, k8sc_com_parsers, 'k8s_cluster')
        _k8sc_com_get_parser = k8sc_com_parsers.add_parser('get')
        _k8sc_com_get_parser.add_argument('id').completer = rest._k8s_cluster_completer_
        _k8sc_com_create_parser = k8sc_com_parsers.add_parser('create')
        self.__populate_args__(rest, _k8sc_com_create_parser, schema.CREATE_FIELDS['k8s_cluster'])
        _k8sc_com_delete_parser = k8sc_com_parsers.add_parser('delete')
        _k8sc_com_delete_parser.add_argument('id').completer = rest._k8s_cluster_completer_

        cloudformation_parser = context_parsers.add_parser('cloudformation')
        cldfrm_com_parsers = cloudformation_parser.add_subparsers(help='command', dest='command')
        cldfrm_com_parsers.required = True
        self.__add_list_parser__(cldfrm_com_parsers)
        self.__add_set_field_parser__(rest, cldfrm_com_parsers, 'cloudformation')
        _cldfrm_com_get_parser = cldfrm_com_parsers.add_parser('get')
        _cldfrm_com_get_parser.add_argument('id').completer = rest._cloudformation_completer_
        _cldfrm_com_create_parser = cldfrm_com_parsers.add_parser('create')
        self.__populate_args__(rest, _cldfrm_com_create_parser, schema.CREATE_FIELDS['cloudformation'])
        _cldfrm_com_delete_parser = cldfrm_com_parsers.add_parser('delete')
        _cldfrm_com_delete_parser.add_argument('id').completer = rest._cloudformation_completer_

        deployment_parser = context_parsers.add_parser('deployment')
        dep_com_parsers = deployment_parser.add_subparsers(help='command', dest='command')
        dep_com_parsers.required = True
        self.__add_list_parser__(dep_com_parsers)
        self.__add_set_field_parser__(rest, dep_com_parsers, 'deployment')
        _dep_com_get_parser = dep_com_parsers.add_parser('get')
        _dep_com_get_parser.add_argument('id').completer = rest._deployment_completer_
        _dep_com_getver_parser = dep_com_parsers.add_parser('getver')
        _dep_com_getver_parser.add_argument('id').completer = rest._deployment_completer_
        _dep_com_setver_parser = dep_com_parsers.add_parser('setver')
        _dep_com_setver_parser.add_argument('id').completer = rest._deployment_completer_
        _dep_com_setver_parser.add_argument('version')

        _dep_com_promote_parser = dep_com_parsers.add_parser('promote')
        _dep_com_promote_parser.add_argument('srcid').completer = rest._deployment_completer_
        _dep_com_promote_parser.add_argument('dstid').completer = rest._deployment_completer_
        _dep_com_create_parser = dep_com_parsers.add_parser('create')
        self.__populate_args__(rest, _dep_com_create_parser, schema.CREATE_FIELDS['deployment'])
        _dep_com_delete_parser = dep_com_parsers.add_parser('delete')
        _dep_com_delete_parser.add_argument('id').completer = rest._deployment_completer_
        _dep_com_clone_parser = dep_com_parsers.add_parser('clone')
        _dep_com_clone_parser.add_argument('id', help='deployment_id').completer = rest._deployment_completer_
        _dep_com_clone_parser.add_argument('deployment_target_id',
                                           help='destination deployment target').completer = rest._deployment_target_completer_

        _dep_com_clone_parser.add_argument('-v', '--version', dest='version')
        _dep_com_add_service_config_parser = dep_com_parsers.add_parser('addzone')
        _dep_com_add_service_config_parser.add_argument('owner_id').completer = rest._deployment_completer_
        _dep_com_add_service_config_parser.add_argument('item_id',
                                                        help='zone_id').completer = rest.add_zone_for_deployment_completer
        _dep_com_del_service_config_parser = dep_com_parsers.add_parser('delzone')
        _dep_com_del_service_config_parser.add_argument('owner_id').completer = rest._deployment_completer_
        _dep_com_del_service_config_parser.add_argument('item_id',
                                                        help='zone_id').completer = rest.del_zone_for_deployment_completer

        application_parser = context_parsers.add_parser('application')
        app_com_parsers = application_parser.add_subparsers(help='command', dest='command')
        app_com_parsers.required = True
        self.__add_list_parser__(app_com_parsers)
        self.__add_set_field_parser__(rest, app_com_parsers, 'application')
        _app_com_get_parser = app_com_parsers.add_parser('get')
        _app_com_get_parser.add_argument('id').completer = rest._application_completer_
        _app_com_create_parser = app_com_parsers.add_parser('create')
        self.__populate_args__(rest, _app_com_create_parser, schema.CREATE_FIELDS['application'])
        _app_com_delete_parser = app_com_parsers.add_parser('delete')
        _app_com_delete_parser.add_argument('id').completer = rest._application_completer_

        stack_parser = context_parsers.add_parser('stack')
        stk_com_parsers = stack_parser.add_subparsers(help='command', dest='command')
        stk_com_parsers.required = True
        self.__add_list_parser__(stk_com_parsers)
        self.__add_set_field_parser__(rest, stk_com_parsers, 'stack')
        _stk_com_get_parser = stk_com_parsers.add_parser('get')
        _stk_com_get_parser.add_argument('id').completer = rest._stack_completer_
        _stk_com_create_parser = stk_com_parsers.add_parser('create')
        self.__populate_args__(rest, _stk_com_create_parser, schema.CREATE_FIELDS['stack'])
        _stk_com_delete_parser = stk_com_parsers.add_parser('delete')
        _stk_com_delete_parser.add_argument('id').completer = rest._stack_completer_

        service_parser = context_parsers.add_parser('service')
        svc_com_parsers = service_parser.add_subparsers(help='command', dest='command')
        svc_com_parsers.required = True
        self.__add_list_parser__(svc_com_parsers)
        self.__add_set_field_parser__(rest, svc_com_parsers, 'service')
        _svc_com_get_parser = svc_com_parsers.add_parser('get')
        _svc_com_get_parser.add_argument('id').completer = rest._service_completer_
        _svc_com_create_parser = svc_com_parsers.add_parser('create')
        self.__populate_args__(rest, _svc_com_create_parser, schema.CREATE_FIELDS['service'])
        _svc_com_delete_parser = svc_com_parsers.add_parser('delete')
        _svc_com_delete_parser.add_argument('id').completer = rest._service_completer_
        _svc_com_add_service_config_parser = svc_com_parsers.add_parser('add_svc_config')
        _svc_com_add_service_config_parser.add_argument('owner_id').completer = rest._service_completer_
        _svc_com_add_service_config_parser.add_argument('item_id',
                                                        help='service_config_id').completer = rest.add_service_config_for_service_completer
        _svc_com_del_service_config_parser = svc_com_parsers.add_parser('del_svc_config')
        _svc_com_del_service_config_parser.add_argument('owner_id').completer = rest._service_completer_
        _svc_com_del_service_config_parser.add_argument('item_id',
                                                        help='service_config_id').completer = rest.del_service_config_for_service_completer

        config_parser = context_parsers.add_parser('config')
        cfg_com_parsers = config_parser.add_subparsers(help='command', dest='command')
        cfg_com_parsers.required = True
        self.__add_list_parser__(cfg_com_parsers)
        self.__add_set_field_parser__(rest, cfg_com_parsers, 'config')
        _cfg_com_get_parser = cfg_com_parsers.add_parser('get')
        _cfg_com_get_parser.add_argument('id').completer = rest._config_completer_
        _cfg_com_create_parser = cfg_com_parsers.add_parser('create')
        self.__populate_args__(rest, _cfg_com_create_parser, schema.CREATE_FIELDS['config'])
        _cfg_com_delete_parser = cfg_com_parsers.add_parser('delete')
        _cfg_com_delete_parser.add_argument('id').completer = rest._config_completer_

        _cfg_com_clone_parser = cfg_com_parsers.add_parser('clone')
        _cfg_com_clone_parser.add_argument('id', help='config_id').completer = rest._config_completer_
        _cfg_com_clone_parser.add_argument('deployment_id',
                                           help='destination deployment').completer = rest._deployment_completer_

        config_type_parser = context_parsers.add_parser('config_type')
        ctp_com_parsers = config_type_parser.add_subparsers(help='command', dest='command')
        ctp_com_parsers.required = True
        self.__add_list_parser__(ctp_com_parsers)
        self.__add_set_field_parser__(rest, ctp_com_parsers, 'config_type')
        _ctp_com_get_parser = ctp_com_parsers.add_parser('get')
        _ctp_com_get_parser.add_argument('id').completer = rest._config_type_completer_
        _ctp_com_create_parser = ctp_com_parsers.add_parser('create')
        self.__populate_args__(rest, _ctp_com_create_parser, schema.CREATE_FIELDS['config_type'])
        _ctp_com_delete_parser = ctp_com_parsers.add_parser('delete')
        _ctp_com_delete_parser.add_argument('id').completer = rest._config_type_completer_

        service_config_parser = context_parsers.add_parser('service_config')
        svc_cfg_com_parsers = service_config_parser.add_subparsers(help='command', dest='command')
        svc_cfg_com_parsers.required = True
        self.__add_list_parser__(svc_cfg_com_parsers)
        self.__add_set_field_parser__(rest, svc_cfg_com_parsers, 'service_config')
        _svc_cfg_com_get_parser = svc_cfg_com_parsers.add_parser('get')
        _svc_cfg_com_get_parser.add_argument('id').completer = rest._service_config_completer_
        _svc_cfg_com_create_parser = svc_cfg_com_parsers.add_parser('create')
        self.__populate_args__(rest, _svc_cfg_com_create_parser, schema.CREATE_FIELDS['service_config'])
        _svc_cfg_com_delete_parser = svc_cfg_com_parsers.add_parser('delete')
        _svc_cfg_com_delete_parser.add_argument('id').completer = rest._service_config_completer_

        orch_confirm_parser = context_parsers.add_parser('confirm')
        orch_confirm_parser.add_argument('deployment_ids',
                                         help='deployment id',
                                         nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_confirm_parser.add_argument('--dry', dest='dry', action='store_true')

        orch_deploy_parser = context_parsers.add_parser('deploy')
        orch_deploy_parser.add_argument('deployment_ids',
                                        help='deployment id',
                                        nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_deploy_parser.add_argument('--dry', dest='dry', action='store_true')

        orch_jenkins_parser = context_parsers.add_parser('jenkins')
        orch_jenkins_parser.add_argument('-r', action='store_true', dest='recursive', help='recursive')
        orch_jenkins_parser.add_argument('dir', help='directory to search')
        orch_jenkins_parser.add_argument('git_url',
                                         help='git url')

        orch_logs_parser = context_parsers.add_parser('logs')
        orch_logs_parser.add_argument('deployment_ids',
                                      help='deployment id',
                                      nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_logs_parser.add_argument('--dry', dest='dry', action='store_true')

        orch_rollback_parser = context_parsers.add_parser('rollback')
        orch_rollback_parser.add_argument('deployment_ids',
                                          help='deployment id',
                                          nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_rollback_parser.add_argument('--dry', dest='dry', action='store_true')

        orch_upgrade_parser = context_parsers.add_parser('upgrade')
        orch_upgrade_parser.add_argument('deployment_ids',
                                         help='deployment id',
                                         nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_upgrade_parser.add_argument('--dry', dest='dry', action='store_true')

        orch_restart_parser = context_parsers.add_parser('restart')
        orch_restart_parser.add_argument('deployment_ids',
                                         help='deployment id',
                                         nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_restart_parser.add_argument('--dry', action='store_true')

        orch_pull_parser = context_parsers.add_parser('pull')
        orch_pull_parser.add_argument('deployment_ids',
                                      help='deployment id',
                                      nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_pull_parser.add_argument('--dry', dest='dry', action='store_true')

        orch_logs_parser = context_parsers.add_parser('logs')
        orch_logs_parser.add_argument('deployment_ids',
                                      help='deployment id',
                                      nargs='*').completer = rest.orch_wrapped_deployment_search
        orch_logs_parser.add_argument('--dry', dest='dry', action='store_true')

        test_parser = context_parsers.add_parser('test')
        test_parser.add_argument('command', nargs='*')
        return parser

    def __gen_completers__(self, rest):
        resources = OrchSchema.CREATE_FIELDS.keys()
        for res in resources:
            def completer(self, prefix, parsed_args, resource=res, **kwargs):
                return rest.resource_get_search(prefix, resource, **kwargs)

            completer.__name__ = "%s_completer" % res

            setattr(RestController, ("_%s_completer_" % res), completer)

    def parse_args(self, rest):
        self.__gen_completers__(rest)
        parser = self.assign_args(rest)
        argcomplete.autocomplete(parser)

        return parser.parse_known_args()

    def __populate_args__(self, rest, parser, fields):
        for field in fields:
            if type(field) == str:
                parser.add_argument(field)
            elif type(field) == dict:
                for key in field.keys():
                    for k, v in field[key].items():
                        if k == 'args':
                            parser.add_argument(key, **v)
                        elif k == 'dotters':
                            for d, m in v.items():
                                arg = parser.add_argument(key)
                                setattr(arg, d, getattr(rest, m))
