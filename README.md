# Airflow Plugin - Airflow Extended API

<p align="center">
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/license/caoergou/airflow-extended-api-plugin?logo=apache"/>
    </a>
    <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/badge/Airflow Version-2.X-00c7d4?logo=data:image/png;base64,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"/>
    </a>
    <a href="https://github.com/caoergou/airflow-extended-api-plugin/blob/main/README_CN.md">
      <img src="https://img.shields.io/badge/Chinese-中文文档-informational?logo=Markdown"/>
    </a>
</p>

Airflow Extended API, which export [airflow CLI command](https://airflow.apache.org/docs/apache-airflow/2.0.2/cli-and-env-variables-ref.html) as RESTful API to extend the ability of airflow official API.

## Features

- 👏**Available**: Probably the only available CLI command plugin on Github that **supports the Airflow 2.x version**.
- 🎉**Extensible**: Easily define your own API to execute any Airflow CLI command so that it fits your demand.

## Deploy plugin

1. Download plugins zip from:

```url
https://github.com/caoergou/airflow-extended-api/archive/master.zip
```

2. Check the [plugins_floder](http://airflow.apache.org/docs/2.0.2/configurations-ref.html#plugins-folder)
   configuration in airflow.cfg.
   If not, consider use airflow default plugin dir path `{AIRFLOW_HOME}/plugins` as plugin floder.
3. Unzip the plugins zip, move folder `/plugins/extended_api/`
   to [plugins_floder](http://airflow.apache.org/docs/2.0.2/configurations-ref.html#plugins-folder) directory.

```bash
unzip airflow-extended-api-plugin.zip

cp -r airflow-rest-api-plugin/plugins/extended_api/* {AIRFLOW_PLUGINS_FOLDER}
```

4. Start services of the airflow webserver and the airflow scheduler.

```bash
airflow webserver -p 8080
airflow scheduler
```

## Directory structure

- **/plugins**
  - **/extended_api**
    - **/extended_api.py** - Airflow plugins, expose functions as RESTful API.
    - **/utils.py** - API DTO class and function to execute CLI command.
    - **/index.html** - Airflow Extended API specification static front-end page.
    - **/openapi.yaml** - Airflow Extended API specification `yaml` file in OpenAPI Specification style.

## ⚠️Authentication And Security Warning

**For convenience, these APIs does NOT require any authentication!**

Therefore, if these APIs is directly exposed to the public network environment, it is equivalent to exposing the command
line execution authority to public, which is a huge security risk.

So it For safety reasons, please think carefully about whether you need to keep this `@csrf.exempt` annotation.

## Using the REST API

- [clear_task](#clear_task)

### ***<span id="clear_task">clear_task</span>***

##### Description

- use CLI command to clear a task for rerun.

##### Endpoint

```text
https://{AIRFLOW_HOST}:{AIRFLOW_PORT}/api/extended/clear
```

##### Method

- POST

##### POST request Arguments

Args for Airflow CLI command `airflow tasks clear`.

| Parameter  | Type               | Description                                                           | Required |
| ---------- | ------------------ | --------------------------------------------------------------------- | -------- |
| dagName    | String             | Name of DAG to clear                                                  | True     |
| downstream | boolean            | Whether to recursively clear downstream tasks. default value is false | False    |
| startDate  | <date-time> String | Start of the time range for task instance to clear                    | True     |
| endDate    | <date-time> String | End of the time range for task instance to clear                      | True     |
| jobName    | String             | Regex of operator to clear                                            | True     |
| username   | String             | Username who call this api                                            | False    |

##### Examples

```bash
curl -X POST https://localhost:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Knowhere API"}'
```

##### response

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

## Project Status

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

**TODO**

- [ ] Add API authentication for security.
- [ ] Add the ability to automatically generate API documentation.
- [ ] Commit the code to the PyPI repository.

## links

- [Airflow configuration documentation](https://airflow.apache.org/docs/stable/configurations-ref.html)
- [Airflow CLI command documentation](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html)
- Contact email: Eric Cao `caofuguo@iftech.io`
