from stores_data import storages
from request import Request


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

        # creating request dict for using in printouts
        req_data = request.return_object()

        # check possibility of removing item from source point, otherwise return False to break the cycle
        if storages[request.from_].remove(request.product, request.amount):
            print('Source point contains required amount of goods')
        else:
            return False

        # print output message as required
        print(f'Courier gets {req_data["amount"]} {req_data["product"]} from {req_data["from"]}')

        # check possibility of adding items to destination point

        try:
            storages[request.to].add(request.product, request.amount)
            print(
                f'Courier delivered {req_data["amount"]} {req_data["product"]} from {req_data["from"]} to'
                f' {req_data["to"]}')



        except:
            print(f'Courier returns undelivered {req_data["amount"]} {req_data["product"]} back to '
                  f' {req_data["to"]}')
            raise Exception('Product could not be delivered to destination storage')

        for store in storages:
            print(f'\n{store} contents {storages[store].get_items()}')

        exit()


if __name__ == '__main__':
    main()
