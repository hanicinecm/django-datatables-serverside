from abc import ABC, abstractmethod

from django.views import View

from ._data_server import DataTablesServer


class ServerSideDataTableView(View, ABC):

    custom_value_getters = {}
    surrogate_columns_search = {}
    surrogate_columns_sort = {}

    @property
    @abstractmethod
    def queryset(self):
        """Docstring for the abstract method"""

    def get(self, request, *_, **__):
        dt_server = DataTablesServer(
            request=request,
            queryset=self.queryset,
            custom_value_getters=self.custom_value_getters,
            surrogate_columns_search=self.surrogate_columns_search,
            surrogate_columns_sort=self.surrogate_columns_sort,
        )
        data_served = dt_server.serve_data()
        return data_served
