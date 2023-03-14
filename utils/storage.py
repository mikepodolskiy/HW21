from abc import ABC, abstractmethod


class StorageAbstract(ABC):
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name: str, quantity: int):
        pass

    @abstractmethod
    def remove(self, name: str, quantity: int):
        pass

    @abstractmethod
    def _get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def _get_unique_items_count(self):
        pass
