stores_list = ['shop', 'store']


class Request:
    def __init__(self, substring):
        self.from_ = substring.split(' ')[4]
        self.to = substring.split(' ')[6]
        self.amount = substring.split(' ')[1]
        self.product = substring.split(' ')[2]

    def return_object(self):
        return {
            'from': self.from_,
            'to': self.to,
            'amount': int(self.amount),
            'product': self.product
            }

request = Request('Pass 3 cookies from strore to shop')

print(request.give_object())