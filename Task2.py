# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "get_user_average_age" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "get_user_names" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

# 1. funkcija "get_user_average_age" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.

def get_user_average_age(x):
    sumAge = 0
    for user in x:
        sumAge = sumAge + user['age']

    avg = sumAge / len(x)
    print(avg)

get_user_average_age(users)

# ats: 30.77777777777778

# 2. funkcija "get_user_names" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

def get_user_names(x):
    name_list = []
    for user in x:
        name_list.append(user['name'])
    print(name_list)

get_user_names(users)

# ats: ['John Smith', 'Ann Smith', 'Tom Jones', 'Rose Peterson', 'Alex John', 'Ronald Jones', 'Elton Smith', 'Simon Peterson', 'Daniel Cane']