from models import Service, Stack

from views import DefaultView


class ServiceView(DefaultView):
    column_searchable_list = [Service.id]
    column_filters = [Service.id, Stack.id, ]
    column_sortable_list = ['name', 'stack']
    can_export = True
    column_exclude_list = ['id']
