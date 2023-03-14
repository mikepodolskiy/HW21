# import required classes
from utils.store import Store
from utils.shop import Shop
from utils.file import File

# set constants - path to data files
store_source = "data/store.json"
shop_source = "data/shop.json"

# create File class object
store_file = File(store_source)
shop_file = File(shop_source)

# load data from json file
store_items = store_file.load_data()
shop_items = shop_file.load_data()
# create shop and store classes objects from data
store = Store(store_items)
shop = Shop(shop_items)

# create dict of possible storages to use
storages = {"shop": shop, "store": store}
