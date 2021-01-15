from __future__ import annotations

from typing import TYPE_CHECKING
from flask.views import MethodView

if TYPE_CHECKING:
    from service.total_service import TotalService


class TotalView(MethodView):
    URL = '/total'

    def __init__(self, total_service: TotalService):
        self._total_service = total_service

    def get(self) -> dict:
        total = self._total_service.get_total()
        return {'total': total}
