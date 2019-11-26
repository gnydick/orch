class OrchSchema:
    CREATE_FIELDS = dict(
        application=[
            'id',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        artifact_repository=[
            'name',
            'url',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        build=[
          'service_id',
          'git_tag',
          'created_at'
        ],
        docker_registry=[
            'name',
            'url',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        nexus=[
            'name',
            'url',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        config=[
            {'config_type_id': {'dotters': {'completer': '_config_type_completer_'}}},
            {'deployment_id': {'dotters': {'completer': '_deployment_completer_'}}},
            'name',
            {'-c': {'args': {'dest': 'config', 'default': '{}'}}},
            {'-t': {'args': {'dest': 'tag', 'help': 'tag', 'default': 'default'}}},

        ],
        config_type=[
            'id'
        ],
        deployment=[
            {'service_id': {'dotters': {'completer': '_service_completer_'}}},
            {'deployment_target_id': {'dotters': {'completer': '_deployment_target_completer_'}}},
            {'-v': {'args': {'dest': 'version', 'default': 'latest'}}},
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}},
            {'-t': {'args': {'dest': 'tag', 'help': 'tag', 'default': 'default'}}}
        ],
        deployment_process=[
            {'deployment_id': {'dotters': {'completer': '_deployment_completer_'}}},
            {'process_id': {'dotters': {'completer': '_proc_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        deployment_target=[
            {'environment_id': {'dotters': {'completer': '_environment_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
            cloudformation=[
            {'environment_id': {'dotters': {'completer': '_environment_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
            k8s_cluster=[
            {'environment_id': {'dotters': {'completer': '_environment_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        domain=[
            {'environment_id': {'dotters': {'completer': '_environment_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        environment=[
            'id',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        network=[
            {'domain_id': {'dotters': {'completer': '_domain_completer_'}}},
            'name',
            'cidr',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        nodegroup=[
            'name',
            'cpu_total',
            'memory_total',
            {'deployment_target_id': {'dotters': {'completer': '_deployment_target_completer_'}}},
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        process=[
            'name',
            {'service_id': {'dotters': {'completer': '_service_completer_'}}},
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        provider=[
            'id',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        region=[
            {'provider_id': {'dotters': {'completer': '_provider_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        release=[
            'build_id',
            'deployment_id',
            'created_at'
        ],
        resource_allocation=[

            {'deployment_process_id': {'dotters': {'completer': '_deployment_process_completer_'}}},
            'value',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
            cpu_allocation=[

            {'deployment_process_id': {'dotters': {'completer': '_deployment_process_completer_'}}},
            'value',
            'watermark',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
            memory_allocation=[

            {'deployment_process_id': {'dotters': {'completer': '_deployment_process_completer_'}}},
            'value',
            'watermark',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ],
        service=[
            {'stack_id': {'dotters': {'completer': '_stack_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}},
            {'-s': {'args': {'dest': 'scm_url', 'help': 'source control URL'}}},
            {'-a': {'args': {'dest': 'artifact_repository_id', 'help': 'artifact repository'}}},
        ],
        service_config=[
            'name',
            'service_id',
            {'-c': {'args': {'dest': 'service_config', 'default': '{}'}}}
        ],
        stack=[
            {'application_id': {'dotters': {'completer': '_application_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}},
        ],
        subnet=[
            'network_id',
            'name',
            'cidr'
        ],
        zone=[
            {'region_id': {'dotters': {'completer': '_region_completer_'}}},
            'name',
            {'-d': {'args': {'dest': 'defaults', 'default': '{}'}}}
        ]
    )
