from utils.stores_data import storages, store_items, shop_items, store_source, shop_source
from utils.request import Request
from utils.file import File


def main():
    print("\nHello!")

    while True:

        for store in storages:
            print(f'\n{store} contents {storages[store].get_items()}')

        print('\nWhat delivery is required?')

        user_input = input(
            "\nPlease enter route below (format: Pass 'goods amount' 'goods name' from 'first point name' "
            "to "
            "'second "
            "point "
            "name'\n")

        # creating request object from user input data
        request = Request(storages, user_input)

        # check possibility of removing item from source point
        try:
            storages[request.from_].remove(request.product, request.amount)
            print('Source point contains required amount of goods')


        except:
            raise Exception('Product could not be received from source storage')

        print(f'Courier gets {request.amount} {request.product} from {request.from_}')

        # check possibility of adding items to destination point

        try:
            storages[request.to].add(request.product, request.amount)
            print(
                f'Courier delivered {request.amount} {request.product} from {request.from_} to'
                f' {request.to}')

        except:
            print(f'Courier returns undelivered {request.amount} {request.product} back to '
                  f' {request.to}')
            raise Exception('Product could not be delivered to destination storage')

        # update storages data

        # create File class object
        new_store_file = File(store_source)
        new_shop_file = File(shop_source)

        # update data in json files
        new_store_file.save_file(store_items)
        new_shop_file.save_file(shop_items)

        for store in storages:
            print(f'\n{store} contents {storages[store].get_items()}')

        exit()


if __name__ == '__main__':
    main()
