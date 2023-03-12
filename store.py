from base_storage import StorageBase


class Store(StorageBase):
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)
