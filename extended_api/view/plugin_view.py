import logging

from airflow.api_connexion import security
from airflow.www.app import csrf
from flask_appbuilder import expose, BaseView

from extended_api.constants import DOCS, ROUTE, DOCS_ITEM
from extended_api.service.plugin_service import APIService

log = logging.getLogger(__name__)
__all__ = ["appbuilder_view"]

try:
    from airflow.api_connexion.exceptions import BadRequest

    from airflow.www import auth
    from airflow.security import permissions

    PERMISSIONS = [
        (permissions.ACTION_CAN_READ, permissions.RESOURCE_AIRFLOW),
    ]


    class PluginExtendedAPIView(BaseView, APIService):
        # AppBuilder (Airflow >= 2.0)

        default_view = "index"
        route_base = ROUTE

        @expose("/index")
        def index(self):
            return self._index()

        @expose("/openapi")
        def openapi(self):
            return self._openapi()

        @expose("/clear", methods=["POST"])
        @csrf.exempt
        @security.requires_access(PERMISSIONS)
        def clear(self):
            return self._clear()

        @expose("/run", methods=["POST"])
        @csrf.exempt
        @security.requires_access(PERMISSIONS)
        def run(self):
            return self._run()

        @expose("/backfill", methods=["POST"])
        @csrf.exempt
        @security.requires_access(PERMISSIONS)
        def backfill(self):
            return self._backfill()

except (ImportError, ModuleNotFoundError):
    # AppBuilder (Airflow >= 1.10 < 2.0)
    from airflow.www_rbac.decorators import has_dag_access


    class PluginExtendedAPIView(BaseView, APIService):

        default_view = "index"
        route_base = ROUTE

        @expose("/index")
        def index(self):
            return self._index()

        @expose("/openapi")
        def openapi(self):
            return self._openapi()

        @expose("/clear", methods=["POST"])
        @csrf.exempt
        @has_dag_access
        def clear(self):
            return self._clear()

        @expose("/run", methods=["POST"])
        @csrf.exempt
        @has_dag_access
        def run(self):
            return self._run()

        @expose("/backfill", methods=["POST"])
        @csrf.exempt
        @has_dag_access
        def backfill(self):
            return self._backfill()

extended_api_view = PluginExtendedAPIView()

appbuilder_view = {
    "category": DOCS,
    "name": DOCS_ITEM,
    "view": extended_api_view
}
