import json


class Iter_country:
    def __init__(self, path_file):
        self.file = json.load(open(path_file))
        self.url = 'https://en.wikipedia.org/wiki/'
        self.start = 0
        self.stop = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        write_file = open('countries.txt', 'at', encoding='utf-8')
        self.stop = len(self.file)
        item = self.file[self.start]
        country = item['name']['official']
        write_file.write(f'{country} - {self.url}{country}' + '\n')
        self.start += 1
        if self.start >= self.stop+1:
            raise StopIteration
        return country
