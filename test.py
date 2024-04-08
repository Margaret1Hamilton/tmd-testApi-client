import pydash

my_dict = {
    "name": "Alice",
    "age": 25,
    "location": "New York"
}

a = pydash.pick(my_dict, ['name'])
print('a', a);


print('name' in my_dict)

# 获取所有键
keys = my_dict.keys()
print(keys)


data1 = {
    "body": {
        "name": "Alice",
        "age": '3'
    }
}

data2 = {
    "body": {
        "name": "Alice",
        "age": 25,
        "location": "New York",
        "address": "s点击熬时间佛山店"
    }
}

restBoyData = pydash.pick(data2['body'], ['age', 'address'])

print('-----', restBoyData)
