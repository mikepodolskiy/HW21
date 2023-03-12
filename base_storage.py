from storage import StorageAbstract


class StorageBase(StorageAbstract):
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity


    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            return "Not enough space in storage"

        if name in self._items:
            self._items[name] += quantity
        self._items[name] = quantity


    def remove(self,name: str, quantity:int):
        if name not in self._items.keys():
            return "No such item in storage"

        if self._items[name] < quantity:
            return "Not enough items in storage"

        self._items[name] -= quantity

        if self._items[name] == 0:
            del self._items[name]

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())


    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self._items)
