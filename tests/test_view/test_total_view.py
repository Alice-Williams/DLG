from unittest import mock
from view.total_view import TotalView
from service.total_service import TotalService


class TestTotalView:
    def test_total_view_get(self):
        mock_service = mock.MagicMock(TotalService, autospec=True)
        mock_service.get_total.return_value = 10
        total_view = TotalView(mock_service)
        assert total_view.get() == {'total': 10}
