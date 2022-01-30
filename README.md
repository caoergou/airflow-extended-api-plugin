# Airflow Plugin - Airflow Extended API

Airflow Extended API, which
export [airflow CLI command](https://airflow.apache.org/docs/apache-airflow/2.0.2/cli-and-env-variables-ref.html) as
RESTful API to extend the ability of airflow official API.

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

## Authentication And Security Warning

**For convenience, these APIs does NOT require any authentication!**

Therefore, if these APIs is directly exposed to the public network environment, it is equivalent to exposing the command
line execution authority to public, which is a greater security risk.

So it For safety reasons, please think carefully about whether you need to keep this `@csrf.exempt` annotation.

## Using the REST API

- [clear_task](#clear_task)
- [run_task](#run_task)

### ***<span id="clear_task">clear_task</span>***

##### Description:

- use CLI command to clear a task for rerun.

##### Endpoint:

```text
https://{AIRFLOW_HOST}:{AIRFLOW_PORT}/api/extended/clear
```

##### Method:

- POST

##### POST request Arguments:

Args for Airflow CLI command `airflow tasks clear`.

| Parameter  | Type               | Description                                                           | Required |
|------------|--------------------|-----------------------------------------------------------------------|----------|
| dagName    | String             | Name of DAG to clear                                                  | True     |
| downstream | boolean            | Whether to recursively clear downstream tasks. default value is false | False    |
| startDate  | <date-time> String | Start of the time range for task instance to clear                    | True     |
| endDate    | <date-time> String | End of the time range for task instance to clear                      | True     |
| jobName    | String             | Regex of operator to clear                                            | True     |
| username   | String             | Username who call this api                                            | False    |

##### Examples:

```bash
curl -X POST https://localhost:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Knowhere API"}'
```

##### response:

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

## links

- [Airflow configuration documentation](https://airflow.apache.org/docs/stable/configurations-ref.html)
- Contact email
    - Eric CAO - `caofuguo@iftech.io`