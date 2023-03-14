class Request:
    def __init__(self, storages: dict, substring: str):
        request_list = substring.split(' ')
        if len(request_list) != 7:
            raise Exception('Wrong input')
        self.from_ = request_list[4]
        self.to = request_list[6]
        self.amount = int(request_list[1])
        self.product = request_list[2]
        if self.from_ not in storages:
            raise Exception('Wrong goods source data')
        if self.to not in storages:
            raise Exception('Wrong goods destination data')

    def return_object(self):
        return {
            'from': self.from_,
            'to': self.to,
            'amount': int(self.amount),
            'product': self.product
        }



