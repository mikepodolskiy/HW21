# import reuired libraries
import json


# creating file class
class File:
    def __init__(self, source):
        self.source = source

    def load_data(self):
        if ".json" in self.source:
            with open(self.source, mode='r', encoding='utf-8') as file:
                return json.load(file)
        else:
            raise Exception("Wrong file format")

    def save_file(self, data):
        with open(self.source, mode='w', encoding='utf-8') as file:
            return json.dump(data, file)
