[中文版文档](https://github.com/caoergou/airflow-extended-api-plugin/blob/main/README_CN.md)

# Airflow Extended API Plugin

<p align="center">
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/stars/caoergou/airflow-extended-api-plugin"/>
    </a>
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/forks/caoergou/airflow-extended-api-plugin"/>
    </a>
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/watchers/caoergou/airflow-extended-api-plugin"/>
    </a>
    <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/languages/code-size/caoergou/airflow-extended-api-plugin"/>
    </a>
</p>

Airflow Extended API, which
export [airflow CLI command](https://airflow.apache.org/docs/apache-airflow/2.0.2/cli-and-env-variables-ref.html) as
REST-ful API to extend the ability of airflow official API.

## Features

- 👏**Available**: Probably the only available CLI command plugin on Github that **supports the Airflow 2.x version**.
- 🎉**Extensible**: Easily define your own API to execute any Airflow CLI command so that it fits your demand.

## Plugin Install

1. Install the plugin via `pip`

  ```bash
    pip install airflow-extended-api
  ```

2. Restart the Airflow Web Server

3. Open Airflow UI in  `Docs - Extended API OpenAPI` or `http://localhost:8080/` to view extended API details in swagger
   UI.
   ![img.png](https://github.com/caoergou/airflow-extended-api-plugin/raw/main/pics/img.png)

## Usage

### Examples

#### curl request example:

```bash
curl -X POST --user "airflow:airflow" https://localhost:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Extended API"}'
```

#### Response Schema:

```json
{
  "executed_command": "string",
  "exit_code": 0,
  "output_info": [
    "string"
  ],
  "error_info": [
    "string"
  ]
}
```

#### curl without Credentials data

Note that you will need to pass credentials' data in `--user "{username}:{password}"` format, or you will get an
Unauthorized error.

```bash
curl -X POST http://127.0.0.1:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Extended API"}'
```

### response

```json
{
  "detail": null,
  "status": 401,
  "title": "Unauthorized",
  "type": "https://airflow.apache.org/docs/apache-airflow/2.2.5/stable-rest-api-ref.html#section/Errors/Unauthenticated"
}
```

#### curl with wrong CLI Command

```bash
curl -X POST --user "airflow:airflow"  http://127.0.0.1:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Extended API"}'
```

### response

```json
{
  "error_info": [
    "Traceback (most recent call last):",
    "  File \"/home/airflow/.local/bin/airflow\", line 8, in <module>",
    "    sys.exit(main())",
    "  File \"/home/airflow/.local/lib/python3.7/site-packages/airflow/__main__.py\", line 48, in main",
    "    args.func(args)",
    "  File \"/home/airflow/.local/lib/python3.7/site-packages/airflow/cli/cli_parser.py\", line 48, in command",
    "    return func(*args, **kwargs)",
    "  File \"/home/airflow/.local/lib/python3.7/site-packages/airflow/utils/cli.py\", line 92, in wrapper",
    "    return f(*args, **kwargs)",
    "  File \"/home/airflow/.local/lib/python3.7/site-packages/airflow/cli/commands/task_command.py\", line 506, in task_clear",
    "    dags = get_dags(args.subdir, args.dag_id, use_regex=args.dag_regex)",
    "  File \"/home/airflow/.local/lib/python3.7/site-packages/airflow/utils/cli.py\", line 203, in get_dags",
    "    return [get_dag(subdir, dag_id)]",
    "  File \"/home/airflow/.local/lib/python3.7/site-packages/airflow/utils/cli.py\", line 193, in get_dag",
    "    f\"Dag {dag_id!r} could not be found; either it does not exist or it failed to parse.\"",
    "airflow.exceptions.AirflowException: Dag 'string' could not be found; either it does not exist or it failed to parse.",
    ""
  ],
  "executed_command": "airflow tasks clear string -e 2019-08-24T14:15:22+00:00 -s 2019-08-24T14:15:22+00:00 -t string -y -d",
  "exit_code": 1,
  "output_info": [
    "[\u001b[34m2022-04-22 10:05:50,538\u001b[0m] {\u001b[34mdagbag.py:\u001b[0m500} INFO\u001b[0m - Filling up the DagBag from /opt/airflow/dags\u001b[0m",
    ""
  ]
}
```

## Project Plan

- [ ] support `dags backfill` cli command
- [ ] support custom configuration

## Links and References

- [Airflow configuration documentation](https://airflow.apache.org/docs/stable/configurations-ref.html)
- [Airflow CLI command documentation](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)
- This project was inspired by the following projects:
    - [andreax79/airflow-code-editor](https://github.com/andreax79/airflow-code-editor)
    - [airflow-plugins/airflow_api_plugin](https://github.com/airflow-plugins/airflow_api_plugin)
- Contact email: Eric Cao `itsericsmail@gmail.com`

<p align="center">
  <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
  <img src="https://img.shields.io/github/license/caoergou/airflow-extended-api-plugin?logo=apache"/>
  </a>
</p>