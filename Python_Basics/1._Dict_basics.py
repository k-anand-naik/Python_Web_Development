dic = {
    'name':'Anand',
    'age' : 19,
    'eligible' : True
}

print(dic)
print(dic['name'])
print(dic.get('name'))
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(f"{key} : {dic[key]}")
    
for key, value in dic.items():
    print(f"{key} : {value}")

