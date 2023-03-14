from store import Store
from shop import Shop

store = Store(
    items={
        "cookies": 10,
        "dogs": 8,
        "boxes": 6,
        "candies": 10,
        "cats": 8,
        "bags": 6
    })

shop = Shop(
    items={
        "cookies": 3,
        "dogs": 8,
        "boxes": 6
    })

storages = {"shop": shop, "store": store}
