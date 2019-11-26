from flask_admin.contrib.sqla import ModelView
from models import Domain, Network
from converters import NetworkModelConverter


class NetworkView(ModelView):
    model_form_converter = NetworkModelConverter
    can_view_details = True
    column_searchable_list = [Domain.id, Network.name]
    column_filters = [Domain.id]
    can_export = True
    # list_template = 'network_list.html'
    # column_editable_list = [Network.name, "cid, Network.defaults]
