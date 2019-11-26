from flask_admin.contrib.sqla import ModelView


class DeploymentProcessView(ModelView):
    can_view_details = True
    # column_searchable_list = [Environment.id, Deployment.tag]
    # column_filters = [Environment.id]
    can_export = True
