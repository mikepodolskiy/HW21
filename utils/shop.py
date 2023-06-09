from utils.base_storage import StorageBase


class Shop(StorageBase):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def _add(self, name: str, quantity: int):
        if self._get_unique_items_count() >= 5 and name not in self._items:
            raise Exception("Not enough space in storage")
        super().add(name, quantity)

    @property
    def add(self, **kwargs):
        return self._add
