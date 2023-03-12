from storage import StorageAbstract

class Shop(StorageAbstract):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int):
        if self.get_unique_items_count() >= 5 and name not in self._items:
            return "Shop overflowed"
        super().add(name, quantity)

