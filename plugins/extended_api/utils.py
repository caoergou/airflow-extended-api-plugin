import logging
import os
import subprocess
from typing import List, Tuple

from flask import Response, jsonify
from marshmallow import Schema, fields, post_load
from werkzeug.exceptions import InternalServerError

log = logging.getLogger(__name__)


class CommandExecutionResult(Schema):
    """Command Execution Result Schema"""
    executed_command = fields.String()
    exit_code = fields.Integer()
    output_info = fields.String(default="")
    error_info = fields.String(default="")

    @post_load
    def gen_response(self, data, **kwargs) -> Response:
        output_str: str = data['output_info']
        data['output_info'] = output_str.split("\n")

        error_str: str = data['error_info']
        data['error_info'] = error_str.split("\n")
        if data['exit_code'] != 0:
            raise InternalServerError(
                description=f"There is a not-zero result of the CLI command: {data}")
        return jsonify(data)


class RunTaskRequestSchema(Schema):
    """Run Task Request Schema"""
    dag_name = fields.String(data_key="dagName", required=True)
    job_name = fields.String(data_key="jobName", required=True)
    start_date = fields.DateTime(data_key="startDate", required=True)
    username = fields.String(data_key="username", required=False, default="Knowhere API")

    @post_load
    def gen_command_list(self, data, **kwargs) -> Tuple[List[str], str]:
        start_date_str_UTC: str = data['start_date'].isoformat()
        command_list = ['airflow', 'tasks', 'run',
                        data['dag_name'], data['job_name'], start_date_str_UTC]

        return command_list, data['username']


class ClearTaskRequestSchema(Schema):
    """Clear Task Request Schema"""
    dag_name = fields.String(data_key="dagName", required=True)
    job_name = fields.String(data_key="jobName", required=True)
    start_date = fields.DateTime(data_key="startDate", required=True)
    end_date = fields.DateTime(data_key="endDate", required=True)
    downstream = fields.Boolean(data_key="downstream", default=False)
    username = fields.String(data_key="username", required=False, default="Knowhere API")

    @post_load
    def gen_command_list(self, data, **kwargs) -> Tuple[List[str], str]:
        start_date_str_UTC: str = data['start_date'].isoformat()
        end_date_str_UTC: str = data['end_date'].isoformat()
        command_list = ['airflow', 'tasks', 'clear', data['dag_name'],
                        "-e", end_date_str_UTC,
                        "-s", start_date_str_UTC,
                        "-t", data['job_name'],
                        "-y"]

        if data.get("downstream"):
            command_list.append("-d")

        return command_list, data['username']


runTaskSchema = RunTaskRequestSchema()
clearTaskSchema = ClearTaskRequestSchema()
commandExecutionResult = CommandExecutionResult()


def execute_cli_command(cmd_list: List[str], username: str = "Knowhere API") -> dict:
    cmd_str: str = ' '.join(cmd_list)
    log.warning(f"Executing CLI Command {cmd_str}")
    os.environ.setdefault("LOGNAME", username)
    try:
        process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        exit_code = process.returncode
    except Exception as e:
        log.error("An error occurred while trying to executing run cli command")
        raise InternalServerError(original_exception=e)

    original_result = {
        "executed_command": cmd_str,
        "output_info": out.decode('utf-8'),
        "error_info": err.decode('utf-8'),
        "exit_code": exit_code
    }
    return original_result
