from unittest import mock
from service.total_service import TotalService


class TestTotalService:
    def test_get_total_when_there_are_numbers(self):
        mock_get_numbers = mock.Mock(return_value=[1, 2, 3])
        total_service = TotalService(mock_get_numbers)
        assert total_service.get_total() == 6

    def test_get_total_when_there_is_nothing_to_sum(self):
        mock_get_numbers = mock.Mock(return_value=[])
        total_service = TotalService(mock_get_numbers)
        assert total_service.get_total() == 0
