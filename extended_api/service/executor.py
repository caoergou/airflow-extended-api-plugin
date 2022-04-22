import logging
import os
import subprocess
from typing import List

from airflow.api_connexion.exceptions import BadRequest

log = logging.getLogger(__name__)


def execute_cli_command(cmd_list: List[str], username: str = "Airflow Extended API") -> dict:
    cmd_str: str = ' '.join(cmd_list)
    log.warning(f"Executing CLI Command {cmd_str}")
    os.environ.setdefault("LOGNAME", username)
    try:
        process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        exit_code = process.returncode
    except Exception as e:
        log.error("An error occurred while trying to executing run cli command")
        raise BadRequest(detail=str(e))

    original_result = {
        "executed_command": cmd_str,
        "output_info": out.decode('utf-8'),
        "error_info": err.decode('utf-8'),
        "exit_code": exit_code
    }
    return original_result
