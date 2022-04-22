from os import path as opath

PLUGIN_NAME = 'extended_api_plugin'
PLUGIN_FULL_NAME = "Airflow Extended API Plugin"

PLUGIN_AUTHOR = "Eric Cao"
AUTHOR_EMAIL = "itsericsmail@gmail.com"

ROUTE = "/api/extended"
DOCS_ROUTE = "/api/extended/docs"
OPENAPI_ROUTE = "/api/extended/openapi"

DOCS = "Docs"
DOCS_ITEM = "Extended API OpenAPI"
INFO_ITEM = "about Extended API"
GITHUB_REPO_URL = "https://www.github.com/caoergou/airflow_extend_api_plugin"

PLUGIN_DIR_PATH = opath.dirname(opath.abspath(__file__))
PLUGIN_STATIC_DIR_PATH = opath.join(PLUGIN_DIR_PATH, 'static')
