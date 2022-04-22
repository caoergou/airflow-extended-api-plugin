from airflow.plugins_manager import AirflowPlugin
from flask_swagger_ui import get_swaggerui_blueprint

from extended_api.constants import DOCS, INFO_ITEM, GITHUB_REPO_URL, PLUGIN_FULL_NAME, PLUGIN_AUTHOR, AUTHOR_EMAIL, \
    PLUGIN_NAME, DOCS_ROUTE, OPENAPI_ROUTE

__author__ = f'{PLUGIN_AUTHOR} <{AUTHOR_EMAIL}>'

from extended_api.view.plugin_view import appbuilder_view

bp = get_swaggerui_blueprint(
    DOCS_ROUTE,
    OPENAPI_ROUTE,
    config={'app_name': PLUGIN_FULL_NAME}
)

api_info = {
    "category": DOCS,
    "name": INFO_ITEM,
    "href": GITHUB_REPO_URL
}


class ExtendedAPIPlugin(AirflowPlugin):
    name = PLUGIN_NAME
    appbuilder_views = [appbuilder_view]
    flask_blueprints = [bp]
    appbuilder_menu_items = [api_info]
