from flask_admin.contrib.sqla import ModelView
from wtforms import StringField


class StiView(ModelView):
    column_display_pk = True
    column_searchable_list = ['id']
    column_sortable_list = ['id']
    can_view_details = True
    can_export = True
    column_exclude_list = ['type']
    form_excluded_columns = ['type']

    form_extra_fields = {
        'id': StringField('Id')
    }
