from typing import Callable


class TotalService:
    def __init__(self, get_numbers_to_add: Callable):
        self._get_numbers_to_add = get_numbers_to_add

    def get_total(self) -> int:
        numbers = self._get_numbers_to_add()
        return sum(numbers)
