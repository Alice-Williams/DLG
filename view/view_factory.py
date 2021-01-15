from __future__ import annotations

from typing import TYPE_CHECKING
from view.total_view import TotalView

if TYPE_CHECKING:
    from service.service_factory import ServiceFactory


class ViewFactory:
    def __init__(self, service_factory: ServiceFactory):
        self._total_view = TotalView(service_factory.get_total_service())

    def get_total_view(self) -> TotalView:
        return self._total_view
