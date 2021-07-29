book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 read street, NY',
    'phone':4654365
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone':6454146
}

import json
s = json.dumps(book)
# print(s)

with open("/home/cavid/Desktop/Alienide/All_project/python/data/book.txt", "w") as f:
    f.write(s)


### Read json

f = open("/home/cavid/Desktop/Alienide/All_project/python/data/book.txt", "r")
s = f.read()
# print("read data from json", s)
print(type(s))

book = json.loads(s)
# print("load data from json", book)
print(type(book))
print(book["bob"])
print(book["bob"]["phone"])

for person in book:
    print(book[person])
    print(type(person))