# Airflow 插件 - Airflow 拓展 API

<p align="center">
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/license/caoergou/airflow-extended-api-plugin"/>
    </a>
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/languages/code-size/caoergou/airflow-extended-api-plugin"/>
    </a>
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/stars/caoergou/airflow-extended-api-plugin"/>
    </a>
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/forks/caoergou/airflow-extended-api-plugin"/>
    </a>
   <a href="https://github.com/caoergou/airflow-extended-api-plugin/">
      <img src="https://img.shields.io/github/watchers/caoergou/airflow-extended-api-plugin"/>
    </a>
</p>
Airflow 扩展 API, 可将 airflow 的命令行包装成 RESTful 风格的 API，以扩展 Airflow 官方 API 的能力。

## 安装插件

1. 从以下地址下载插件的 zip 包:

```url
https://github.com/caoergou/airflow-extended-api/archive/master.zip
```

2. 检查 Airflow 配置文件 `airflow.cfg` 中定义的 `Plugins floder`。

   如果没有设置 airflow 默认插件地址，可以考虑使用默认插件地址 `{AIRFLOW_HOME}/plugins`

3. 解压 ZIP 包, 将解压得到的所有文件移动至插件目录.

```bash
unzip airflow-extended-api-plugin.zip

cp -r airflow-rest-api-plugin/* {AIRFLOW_PLUGINS_FOLDER}
```

4. 启动 airflow webserver 与 airflow scheduler.

```bash
airflow webserver -p 8080
airflow scheduler
```

## 目录结构

- **/plugins**
  - **/extended_api**
    - **/extended_api.py** - Airflow Extended API 接口目录.
    - **/utils.py** - API 的 DTO 类与执行命令的功能函数.
    - **/index.html** - Airflow Extended API 说明的静态界面.
    - **/openapi.yaml** - 以 OpenAPI 规范定义的 API 说明.

## ⚠️鉴权与安全警告

**为了插件的易用性，插件目前没有任何鉴权！**

因此如果将此 API 直接暴露于公网环境，相当于将命令行权限直接暴露于公网权限，这相当危险。

从安全角度出发，请仔细思考是否需要保留接口定义函数上的 `@csrf.exempt` 注解。

## 使用 API

- [clear_task](#clear_task)

### ***<span id="clear_task">clear_task</span>***

##### Description:

- 使用命令行清理任务的执行记录，以便让该任务重跑。

##### Endpoint:

```text
https://{AIRFLOW_HOST}:{AIRFLOW_PORT}/api/extended/clear
```

##### Method:

- POST

##### POST request body:

Args for Airflow CLI command `airflow tasks clear`.

| 参数       | 类型               | 说明                                               | Required |
| ---------- | ------------------ | -------------------------------------------------- | -------- |
| dagName    | String             | 要清理运行记录的 DAG 名                            | True     |
| startDate  | <date-time> String | 要清理的任务范围的开始时间                         | True     |
| endDate    | <date-time> String | 要清理的任务范围的结束时间                         | True     |
| jobName    | String             | 需要清理的任务的正则表达式                         | True     |
| downstream | boolean            | 是否需要递归的清理下游任务的执行记录，默认为 False | False    |
| username   | String             | 调用 API 的用户名                                  | False    |



##### CURL 调用示例:

```bash
curl -X POST https://localhost:8080/api/extended/clear -H "Content-Type: application/json" -d '{"dagName": "string","downstream": true,"endDate": "2019-08-24T14:15:22Z","jobName": "string","startDate": "2019-08-24T14:15:22Z","username": "Knowhere API"}'
```

##### 返回结果示例:

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

## 相关链接

- [Airflow 配置文档](https://airflow.apache.org/docs/stable/configurations-ref.html)
- 联系邮箱
  - Eric CAO - `caofuguo@iftech.io`

