import logging

from airflow.api_connexion.exceptions import BadRequest
from flask import request, redirect, url_for, send_file
from marshmallow import ValidationError

from extended_api.constants import PLUGIN_STATIC_DIR_PATH
from extended_api.model.models import commandExecutionResult, clearTaskSchema, runTaskSchema, backfillDAGRunSchema
from extended_api.service.executor import execute_cli_command

log = logging.getLogger(__name__)


class APIService(object):
    default_view = "index"

    def _index(self):
        return redirect(url_for("swagger_ui.show"))

    def _openapi(self):
        from os import path as opath
        return send_file(opath.join(PLUGIN_STATIC_DIR_PATH, 'openapi.json'), mimetype='application/json')

    def _clear(self):
        log.info("Extended API clear called")

        body = request.get_json()
        try:
            command_list, username = clearTaskSchema.load(body)
        except ValidationError as err:
            raise BadRequest(detail=str(err.messages))

        output = execute_cli_command(command_list, username)
        return commandExecutionResult.load(output)

    def _backfill(self):
        log.info("Extended API backfill called")

        body = request.get_json()
        try:
            command_list, username = backfillDAGRunSchema.load(body)
        except ValidationError as err:
            raise BadRequest(detail=str(err.messages))

        output = execute_cli_command(command_list, username)
        return commandExecutionResult.load(output)

    def _run(self):
        log.info("Extended API run called")

        body = request.get_json()
        try:
            command_list, username = runTaskSchema.load(body)
        except ValidationError as err:
            raise BadRequest(detail=str(err.messages))

        output = execute_cli_command(command_list, username)
        return commandExecutionResult.load(output)
