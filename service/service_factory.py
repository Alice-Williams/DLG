from __future__ import annotations

from service.total_service import TotalService
from service import numbers_service


class ServiceFactory:
    def __init__(self):
        self._total_service = TotalService(numbers_service.get_numbers_to_add)

    def get_total_service(self) -> TotalService:
        return self._total_service
