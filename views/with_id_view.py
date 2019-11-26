from flask_admin.contrib.sqla import ModelView
from wtforms import StringField


class WithIdView(ModelView):
    can_view_details = True
    column_searchable_list = ['id']
    column_sortable_list = ['id']
    list_display_pk = True
    column_display_pk = True
    can_export = True

    form_extra_fields = {
        'id': StringField('Id')
    }
