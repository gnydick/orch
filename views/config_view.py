from flask_admin.contrib.sqla import ModelView
from models import Deployment

from db import db


class ConfigView(ModelView):
    edit_template = 'config_edit.html'
    create_template = 'config_create.html'
    column_searchable_list = [Deployment.id]
    can_view_details = True
    can_export = True
    form_excluded_columns = ['id']

