[English Document](https://github.com/caoergou/airflow-extended-api-plugin/blob/main/README.md)

# Airflow 拓展 API 插件

<p align="center">
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/license/caoergou/airflow-extended-api-plugin?logo=apache"/>
    </a>
    <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/badge/Airflow Version-2.X-00c7d4?logo=Apache Airflow"/>
    </a>
    <a href="https://github.com/caoergou/airflow-extended-api-plugin/blob/main/README.md">
      <img src="https://img.shields.io/badge/English-英文文档-informational?logo=Markdown"/>
    </a>
</p>

可将 airflow 的命令行包装成 REST-ful 风格 API 的插件，以扩展 Airflow 官方 API 的能力。

该插件可用于 Airflow 2.0 以上版本，且易于扩展，你可以根据需要修改代码，将任意 CLI 命令封装成 API。

## 当前支持的命令

当前支持使用以下命令：

- `airflow dags backfill`
- `airflow tasks run`
- `airflow tasks clear`

## 安装插件

1. 通过 Pip 安装

  ```bash
    pip install airflow-extended-api
  ```

2. 重启 Airflow WebServer

3. 打开 Airflow 界面中的 `Docs - Extended API OpenAPI` 或 `http://localhost:8080/` 来查看 API 细节。

   ![img.png](https://github.com/caoergou/airflow-extended-api-plugin/raw/main/pics/img.png)

## 使用 API

### 一般调用示例

#### curl 请求:

```bash
curl -X POST --user "airflow:airflow" https://localhost:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Extended API"}'
```

#### 返回结果格式:

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

### 身份验证

#### 不带身份信息的 curl 请求

请以`--user "{username}:{password}"`的样式提供 airflow 账户信息，否则将鉴权失败。

```bash
curl -X POST http://127.0.0.1:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Extended API"}'
```

### 返回结果

```json
{
  "detail": null,
  "status": 401,
  "title": "Unauthorized",
  "type": "https://airflow.apache.org/docs/apache-airflow/2.2.5/stable-rest-api-ref.html#section/Errors/Unauthenticated"
}
```

### 错误的命令行

#### curl 请求

```bash
curl -X POST --user "airflow:airflow"  http://127.0.0.1:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Extended API"}'
```

### 返回结果

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

## 项目计划

- [ ] 支持 `backfill` 命令
- [ ] support custom configuration

## 相关链接

- [Airflow 配置文档](https://airflow.apache.org/docs/stable/configurations-ref.html)
- [Airflow 命令行工具](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)
- 开发过程中参考了以下项目，在此表示感谢
    - [andreax79/airflow-code-editor](https://github.com/andreax79/airflow-code-editor)
    - [airflow-plugins/airflow_api_plugin](https://github.com/airflow-plugins/airflow_api_plugin)
- 联系邮箱 Eric Cao `itsericsmail@gmail.com`

<p align="center">
  <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
  <img src="https://img.shields.io/github/license/caoergou/airflow-extended-api-plugin?logo=apache"/>
  </a>
</p>