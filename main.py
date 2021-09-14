from iter_class import Iter_country
import hashlib


def create_md5(file_name):
    with open(file_name, 'r', encoding='utf-8') as read_file:
        for line in read_file:
            hash_md5 = hashlib.md5(line.encode()).hexdigest()
            yield hash_md5


if __name__ == '__main__':
    with Iter_country('countries.json') as file:
        for country in file:
            continue
    for md5 in create_md5('countries.txt'):
        print(md5)
