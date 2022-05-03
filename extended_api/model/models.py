from typing import Tuple, List

from flask import Response, jsonify
from marshmallow import Schema, fields, post_load


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
        return jsonify(data)


class RunTaskRequestSchema(Schema):
    """Run Task Request Schema"""
    dag_name = fields.String(data_key="dagName", required=True)
    job_name = fields.String(data_key="jobName", required=True)
    start_date = fields.DateTime(data_key="startDate", required=True)
    username = fields.String(data_key="username", required=False, default="Extended API")

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
    username = fields.String(data_key="username", required=False, default="Extended API")

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


class BackfillDAGRunRequestSchema(Schema):
    """Backfill DAG Run Request Schema"""
    dag_name = fields.String(data_key="dagName", required=True)
    start_date = fields.DateTime(data_key="startDate", required=True)
    end_date = fields.DateTime(data_key="endDate", required=True)
    job_name = fields.String(data_key="jobName", required=True)
    pool = fields.String(data_key="pool", required=False)
    rerun_failed_tasks = fields.Boolean(data_key="rerunFailedTasks", required=False)
    ignore_dependencies = fields.Boolean(data_key="ignoreDependencies", required=False)
    username = fields.String(data_key="username", required=False, default="Extended API")

    @post_load
    def gen_command_list(self, data, **kwargs) -> Tuple[List[str], str]:
        start_date_str_UTC: str = data['start_date'].isoformat()
        end_date_str_UTC: str = data['end_date'].isoformat()
        command_list = ['airflow', 'dags', 'backfill', data['dag_name'],
                        "-e", end_date_str_UTC,
                        "-s", start_date_str_UTC,
                        "-t", data['job_name'],
                        "-y"]

        if data.get("pool"):
            command_list += ['--pool', data['pool']]

        if data.get("rerun_failed_tasks"):
            command_list.append('--ignore-first-depends-on-past')
        if data.get("ignore_dependencies"):
            command_list.append('--ignore-dependencies')

        return command_list, data['username']


commandExecutionResult = CommandExecutionResult()
runTaskSchema = RunTaskRequestSchema()
clearTaskSchema = ClearTaskRequestSchema()
backfillDAGRunSchema = BackfillDAGRunRequestSchema()
