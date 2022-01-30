import logging

from airflow.api_connexion.exceptions import BadRequest
from airflow.plugins_manager import AirflowPlugin
from airflow.www.app import csrf
from flask import Blueprint, request, send_from_directory
from flask_appbuilder import expose, BaseView
from marshmallow import ValidationError

from utils import clearTaskSchema, runTaskSchema, execute_cli_command, commandExecutionResult

log = logging.getLogger(__name__)

bp = Blueprint(
    "extended_API",
    __name__,
    template_folder='templates',
    static_folder='')


class AppView(BaseView):
    default_view = "index"

    @expose("/")
    @expose("/index")
    def index(self):
        return send_from_directory(bp.static_folder, 'index.html')

    route_base = "/api/extended"

    # IMPORTANT!
    # For safety reasons, please think carefully about whether you need to keep this `@csrf.exempt` annotation.
    @csrf.exempt
    @expose("/clear", methods=["POST"])
    def clear(self):
        log.info("Extended API clear called")

        body = request.get_json()
        try:
            command_list, username = clearTaskSchema.load(body)
        except ValidationError as err:
            raise BadRequest(detail=str(err.messages))

        output = execute_cli_command(command_list, username)
        return commandExecutionResult.load(output)

    # IMPORTANT!
    # For safety reasons, please think carefully about whether you need to keep this `@csrf.exempt` annotation.
    @csrf.exempt
    @expose("/run", methods=["POST"])
    def run(self):
        log.info("Extended API run called")

        body = request.get_json()
        try:
            command_list, username = runTaskSchema.load(body)
        except ValidationError as err:
            raise BadRequest(detail=str(err.messages))

        output = execute_cli_command(command_list, username)
        return commandExecutionResult.load(output)


api_view = AppView()
api_doc = {
    "category": "Docs",
    "name": "Extended API OpenAPI",
    "view": api_view
}

api_info = {
    "category": "Docs",
    "name": "about Extended API",
    "href": "https://www.github.com/caoergou/airflow_extend_api_plugin"
}


# Defining the plugin class
class ExtendedAPIPlugin(AirflowPlugin):
    name = "api_extended_api_plugin"
    flask_blueprints = [bp]
    appbuilder_views = [api_doc]
    appbuilder_menu_items = [api_info]
