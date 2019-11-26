from flask_admin.contrib.sqla import ModelView
from wtforms import StringField


class ResourceAllocationView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    form_excluded_columns = ['unit', 'type']
    column_exclude_list = ['type']
