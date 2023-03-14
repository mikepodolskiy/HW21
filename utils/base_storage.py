# import required modules
from utils.storage import StorageAbstract


# creating class for requests
class StorageBase(StorageAbstract):
    def __init__(self, items: dict, capacity: int):
        super().__init__(items, capacity)

    def _add(self, name: str, quantity: int):
        if self._get_free_space() < quantity:
            raise Exception("Not enough space in storage")

        if name in self._items:
            self._items[name] += quantity
        else:
            self._items[name] = quantity

    @property
    def add(self, **kwargs):
        return self._add

    def remove(self, name: str, quantity: int):
        if name not in self._items.keys():
            raise Exception("No such item in storage")

        if self._items[name] < quantity:
            raise Exception("Not enough items in storage")

        self._items[name] -= quantity

        if self._items[name] == 0:
            del self._items[name]

    def _get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def _get_unique_items_count(self):
        return len(self._items)
