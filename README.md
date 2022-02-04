# Airflow Plugin - Airflow Extended API

<p align="center">
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/license/caoergou/airflow-extended-api-plugin?logo=apache"/>
    </a>
    <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/badge/Airflow Version-2.X-00c7d4?logo=Apache Airflow"/>
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
